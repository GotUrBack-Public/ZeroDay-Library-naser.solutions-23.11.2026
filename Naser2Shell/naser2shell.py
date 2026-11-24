#!/usr/bin/env python3
import argparse, json, os, sys, re, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT, "findings_db.json")

ASCII = r"""
 _   _    _    ____  _____ ____   ____  _   _ ___ _     _     
| \ | |  / \  / ___|| ____|  _ \ / ___|| | | |_ _| |   | |    
|  \| | / _ \ \___ \|  _| | |_) | |  _ | |_| || || |   | |    
| |\  |/ ___ \ ___) | |___|  _ <| |_| ||  _  || || |___| |___ 
|_| \_/_/   \_\____/|_____|_| \_\\____||_| |_|___|_____|_____|
                                                                
               Naser2Shell - Finding-Driven Exploit Tool
"""

TARGET = {"mode": "LOCAL", "url": "", "host": "", "confirmed": False}

def load_db():
    with open(DB_PATH) as f:
        return json.load(f)

def list_findings():
    db = load_db()
    print(ASCII)
    print("Available findings:")
    for fid in sorted(db):
        print(f"  {fid}  {db[fid]['slug']}")

def scan_target(target):
    files = []
    for root,_,fs in os.walk(target):
        for fn in fs:
            files.append(os.path.join(root,fn))
    return files

def read_file(path):
    try:
        with open(path,errors='ignore') as f:
            return f.read()
    except Exception:
        return ""

def check_pattern(target, pattern):
    hits=[]
    for fp in scan_target(target):
        c=read_file(fp)
        if re.search(pattern,c):
            hits.append(fp)
    return hits

def http_get(url):
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Naser2Shell"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, dict(r.headers), r.read(2000).decode('utf-8','ignore')
    except Exception as e:
        return None, {}, str(e)

def module_result(fid, status, evidence, fallback=None):
    r={"finding":fid,"status":status,"evidence":evidence}
    if fallback: r["fallback"]=fallback
    return r

MODULES = {}
def reg(fid):
    def deco(fn):
        MODULES[fid]=fn
        return fn
    return deco

def target_str():
    return TARGET["url"]

# Local static modules
@reg("001")
def m001(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        code,_=http_get(t)
        return module_result("001","NOT TESTABLE","Domain mode: static secret check requires source tree")
    hits=check_pattern(t,r"PAYLOAD_SECRET\s*\|\|\s*['\"]['\"]")
    if hits: return module_result("001","CONFIRMED","Empty default secret in: "+", ".join(hits))
    if check_pattern(t,r"process\.env\.PAYLOAD_SECRET"): return module_result("001","POTENTIAL","PAYLOAD_SECRET referenced")
    return module_result("001","NOT TESTABLE","No payload.config.ts found")

@reg("002")
def m002(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,headers,body=http_get(t.rstrip("/")+"/api/portal/login")
        if status in (403,429): return module_result("002","NOT TESTABLE","Blocked by protection: "+str(status))
        return module_result("002","POTENTIAL","Portal login endpoint reachable: "+str(status))
    hits=check_pattern(t,r"api/portal/login")
    rl=check_pattern(t,r"rate.?limit|ratelimit|throttle")
    if hits and not rl: return module_result("002","CONFIRMED","Portal login without rate limiting: "+", ".join(hits))
    if hits and rl: return module_result("002","FIXED","Rate limiting present")
    return module_result("002","NOT TESTABLE","Portal login route not found")

@reg("003")
def m003(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,headers,body=http_get(t.rstrip("/")+"/api/thumbnail")
        if status in (403,429): return module_result("003","NOT TESTABLE","Blocked: "+str(status))
        return module_result("003","POTENTIAL","Thumbnail endpoint reachable: "+str(status))
    hits=check_pattern(t,r"thumbnail")
    if hits:
        lim=check_pattern(t,r"maxSize|max_size|limit.*thumb|thumb.*limit")
        if not lim: return module_result("003","CONFIRMED","Thumbnail without size limits: "+", ".join(hits))
        return module_result("003","FIXED","Thumbnail limits present")
    return module_result("003","NOT TESTABLE","No thumbnail code found")

@reg("004")
def m004(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,_,_=http_get(t.rstrip("/")+"/api/contact")
        if status in (403,429): return module_result("004","NOT TESTABLE","Blocked: "+str(status))
        return module_result("004","POTENTIAL","Contact endpoint reachable: "+str(status))
    hits=check_pattern(t,r"contact")
    rl=check_pattern(t,r"rate.?limit|ratelimit|throttle")
    if hits and not rl: return module_result("004","POTENTIAL","Contact route without rate limiting")
    if hits and rl: return module_result("004","FIXED","Rate limiting present")
    return module_result("004","NOT TESTABLE","No contact code found")

@reg("005")
def m005(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        return module_result("005","NOT TESTABLE","Domain mode: static quota check requires source")
    hits=check_pattern(t,r"upload")
    quota=check_pattern(t,r"quota|per.?user.*limit|userQuota")
    if hits and not quota: return module_result("005","POTENTIAL","Upload without per-user quota")
    if hits and quota: return module_result("005","FIXED","Quota present")
    return module_result("005","NOT TESTABLE","No upload code found")

@reg("006")
def m006(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,headers,_=http_get(t)
        cookie=headers.get("Set-Cookie","")
        if not cookie: return module_result("006","POTENTIAL","No Set-Cookie on root response")
        if "HttpOnly" not in cookie or "Secure" not in cookie: return module_result("006","CONFIRMED","Weak cookie attrs: "+cookie)
        return module_result("006","FIXED","Cookie attrs present")
    hits=check_pattern(t,r"cookie|session.*cookie|Set-Cookie")
    secure=check_pattern(t,r"secure:\s*true|httpOnly:\s*true|sameSite")
    if hits and not secure: return module_result("006","CONFIRMED","Weak cookie attrs")
    if hits and secure: return module_result("006","FIXED","Cookie attrs present")
    return module_result("006","NOT TESTABLE","No cookie code found")

@reg("007")
def m007(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,_,_=http_get(t.rstrip("/")+"/preview")
        if status in (403,429): return module_result("007","NOT TESTABLE","Blocked: "+str(status))
        return module_result("007","POTENTIAL","Preview endpoint reachable: "+str(status))
    hits=check_pattern(t,r"preview")
    if hits:
        getmut=check_pattern(t,r"export\s+async\s+function\s+GET.*(?:update|delete|create|save)")
        if getmut: return module_result("007","CONFIRMED","Preview GET mutates state")
        return module_result("007","POTENTIAL","Preview code found")
    return module_result("007","NOT TESTABLE","No preview code found")

@reg("008")
def m008(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,_,_=http_get(t.rstrip("/")+"/api/portal/login")
        if status in (403,429): return module_result("008","NOT TESTABLE","Blocked: "+str(status))
        return module_result("008","POTENTIAL","Portal login reachable: "+str(status))
    hits=check_pattern(t,r"portal-session|portal.*jwt|jwt.*portal")
    bind=check_pattern(t,r"ip.*binding|userAgent.*bind|client.*bind")
    if hits and not bind: return module_result("008","CONFIRMED","Portal JWT without client binding")
    if hits and bind: return module_result("008","FIXED","Client binding present")
    return module_result("008","NOT TESTABLE","No portal session code found")

@reg("009")
def m009(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"): return module_result("009","NOT TESTABLE","Domain mode: static check requires source")
    hits=check_pattern(t,r"saveClientFeedback|save.*feedback")
    if hits:
        lock=check_pattern(t,r"transaction|lock|atomic|compareAndSwap")
        if not lock: return module_result("009","POTENTIAL","Save feedback without concurrency control")
        return module_result("009","FIXED","Concurrency control present")
    return module_result("009","NOT TESTABLE","No saveClientFeedback found")

@reg("010")
def m010(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"): return module_result("010","NOT TESTABLE","Domain mode: static check requires source")
    hits=check_pattern(t,r"cms.*origin|origin.*cms|allowedOrigins")
    if hits:
        unconditional=check_pattern(t,r"origin.*\|\|.*true|if\s*\(\s*true\s*\)")
        if unconditional: return module_result("010","CONFIRMED","Unconditional CMS origin check")
        return module_result("010","POTENTIAL","CMS origin code found")
    return module_result("010","NOT TESTABLE","No CMS origin code found")

@reg("011")
def m011(cfg,verify=False):
    t=cfg["url"]
    if t.startswith("http"):
        status,headers,_=http_get(t)
        required=["X-Frame-Options","Content-Security-Policy","Strict-Transport-Security"]
        missing=[h for h in required if h not in headers]
        if missing: return module_result("011","CONFIRMED","Missing headers: "+", ".join(missing))
        return module_result("011","FIXED","Security headers present")
    hits=check_pattern(t,r"security.*header|helmet|X-Frame-Options|Content-Security-Policy")
    if not hits: return module_result("011","CONFIRMED","No security headers found")
    return module_result("011","FIXED","Security headers present")

def run_finding(fid, cfg, verify=False):
    fid=fid.strip().zfill(3)
    if fid not in MODULES:
        print(f"Unknown finding {fid}"); return
    res=MODULES[fid](cfg, verify)
    print(json.dumps(res,indent=2))

def run_all(cfg, verify=False):
    print(ASCII)
    results=[]
    for fid in sorted(MODULES):
        r=MODULES[fid](cfg, verify)
        results.append(r)
        print(f"{fid}: {r['status']}")
    out=os.path.join(ROOT,"results.json")
    with open(out,"w") as f: json.dump(results,f,indent=2)
    print("Results written to",out)

def configure_local():
    url=input("Local target URL (e.g. http://localhost:3000): ").strip()
    if not url: url="http://localhost:3000"
    TARGET.update(mode="LOCAL", url=url, host=urllib.parse.urlparse(url).hostname or "", confirmed=True)
    print("Target set:", url)

def configure_domain():
    print("\n[ DOMAIN TARGET CONFIGURATION ]\n")
    url=input("Enter target domain: ").strip()
    if not url.startswith("http"):
        url="https://"+url
    parsed=urllib.parse.urlparse(url)
    if not parsed.hostname:
        print("Invalid URL"); return
    print("Hostname:",parsed.hostname,"Protocol:",parsed.scheme)
    if input("Confirm target? (y/n): ").strip().lower()!="y":
        print("Aborted"); return
    TARGET.update(mode="DOMAIN", url=url, host=parsed.hostname, confirmed=True)
    print("Target set:", url)

def interactive():
    while True:
        print(ASCII)
        print("\n[ TARGET CONFIGURATION ]\n")
        print("  [1] LOCAL TARGET")
        print("  [2] DOMAIN TARGET")
        print("  [3] EXIT\n")
        c=input("Select target: ").strip()
        if c=="1": configure_local()
        elif c=="2": configure_domain()
        elif c=="3": sys.exit(0)
        else: continue
        if not TARGET["confirmed"]: continue
        while True:
            print("\n[ SELECT MODULE ]\n")
            print("  [1] Execute single finding")
            print("  [2] Execute all findings")
            print("  [3] View findings")
            print("  [4] Change target")
            print("  [5] Exit\n")
            m=input("Select: ").strip()
            if m=="1":
                fid=input("Finding ID: ").strip()
                run_finding(fid,TARGET)
            elif m=="2":
                run_all(TARGET)
            elif m=="3":
                list_findings()
            elif m=="4":
                break
            elif m=="5":
                sys.exit(0)

def main():
    ap=argparse.ArgumentParser(prog="naser2shell")
    ap.add_argument("--list",action="store_true")
    ap.add_argument("--finding")
    ap.add_argument("--verify",action="store_true")
    ap.add_argument("--all",action="store_true")
    ap.add_argument("--target",default=None)
    args=ap.parse_args()
    if args.list:
        list_findings(); return
    if args.target:
        TARGET.update(mode="LOCAL", url=args.target, host="", confirmed=True)
    if args.finding:
        run_finding(args.finding,TARGET,args.verify); return
    if args.all:
        run_all(TARGET,args.verify); return
    interactive()

if __name__=="__main__":
    main()
