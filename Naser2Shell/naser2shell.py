#!/usr/bin/env python3
import argparse, json, os, sys, re

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

@reg("001")
def m001(target,verify=False):
    hits=check_pattern(target,r"PAYLOAD_SECRET\s*\|\|\s*['\"]['\"]")
    if hits:
        return module_result("001","CONFIRMED","Empty default secret in: "+", ".join(hits))
    hits2=check_pattern(target,r"process\.env\.PAYLOAD_SECRET")
    if hits2:
        return module_result("001","POTENTIAL","PAYLOAD_SECRET referenced but default not empty: "+", ".join(hits2))
    return module_result("001","NOT TESTABLE","No payload.config.ts found in target")

@reg("002")
def m002(target,verify=False):
    hits=check_pattern(target,r"api/portal/login")
    rl=check_pattern(target,r"rate.?limit|ratelimit|throttle")
    if hits and not rl:
        return module_result("002","CONFIRMED","Portal login route found without rate limiting: "+", ".join(hits))
    if hits and rl:
        return module_result("002","FIXED","Rate limiting present: "+", ".join(rl))
    return module_result("002","NOT TESTABLE","Portal login route not found")

@reg("003")
def m003(target,verify=False):
    hits=check_pattern(target,r"thumbnail")
    if hits:
        # check for size limits
        lim=check_pattern(target,r"maxSize|max_size|limit.*thumb|thumb.*limit")
        if not lim:
            return module_result("003","CONFIRMED","Thumbnail route without size limits: "+", ".join(hits))
        return module_result("003","FIXED","Thumbnail limits present: "+", ".join(lim))
    return module_result("003","NOT TESTABLE","No thumbnail code found")

@reg("004")
def m004(target,verify=False):
    hits=check_pattern(target,r"contact")
    rl=check_pattern(target,r"rate.?limit|ratelimit|throttle")
    if hits and not rl:
        return module_result("004","POTENTIAL","Contact route found; verify rate limiting: "+", ".join(hits[:3]))
    if hits and rl:
        return module_result("004","FIXED","Rate limiting present")
    return module_result("004","NOT TESTABLE","No contact code found")

@reg("005")
def m005(target,verify=False):
    hits=check_pattern(target,r"upload")
    quota=check_pattern(target,r"quota|per.?user.*limit|userQuota")
    if hits and not quota:
        return module_result("005","POTENTIAL","Upload code without per-user quota: "+", ".join(hits[:3]))
    if hits and quota:
        return module_result("005","FIXED","Quota present: "+", ".join(quota[:3]))
    return module_result("005","NOT TESTABLE","No upload code found")

@reg("006")
def m006(target,verify=False):
    hits=check_pattern(target,r"cookie|session.*cookie|Set-Cookie")
    secure=check_pattern(target,r"secure:\s*true|httpOnly:\s*true|sameSite")
    if hits and not secure:
        return module_result("006","CONFIRMED","Session cookie without strong attributes: "+", ".join(hits[:3]))
    if hits and secure:
        return module_result("006","FIXED","Cookie attributes present: "+", ".join(secure[:3]))
    return module_result("006","NOT TESTABLE","No cookie code found")

@reg("007")
def m007(target,verify=False):
    hits=check_pattern(target,r"preview")
    if hits:
        # check if GET mutates state
        getmut=check_pattern(target,r"export\s+async\s+function\s+GET.*(?:update|delete|create|save)")
        if getmut:
            return module_result("007","CONFIRMED","Preview GET mutates state: "+", ".join(getmut))
        return module_result("007","POTENTIAL","Preview code found; manual review needed: "+", ".join(hits[:3]))
    return module_result("007","NOT TESTABLE","No preview code found")

@reg("008")
def m008(target,verify=False):
    hits=check_pattern(target,r"portal-session|portal.*jwt|jwt.*portal")
    bind=check_pattern(target,r"ip.*binding|userAgent.*bind|client.*bind")
    if hits and not bind:
        return module_result("008","CONFIRMED","Portal JWT without client binding: "+", ".join(hits[:3]))
    if hits and bind:
        return module_result("008","FIXED","Client binding present")
    return module_result("008","NOT TESTABLE","No portal session code found")

@reg("009")
def m009(target,verify=False):
    hits=check_pattern(target,r"saveClientFeedback|save.*feedback")
    if hits:
        # check for transaction/locking
        lock=check_pattern(target,r"transaction|lock|atomic|compareAndSwap")
        if not lock:
            return module_result("009","POTENTIAL","Save feedback without concurrency control: "+", ".join(hits[:3]))
        return module_result("009","FIXED","Concurrency control present")
    return module_result("009","NOT TESTABLE","No saveClientFeedback found")

@reg("010")
def m010(target,verify=False):
    hits=check_pattern(target,r"cms.*origin|origin.*cms|allowedOrigins")
    if hits:
        unconditional=check_pattern(target,r"origin.*\|\|.*true|if\s*\(\s*true\s*\)")
        if unconditional:
            return module_result("010","CONFIRMED","Unconditional CMS origin check: "+", ".join(unconditional[:3]))
        return module_result("010","POTENTIAL","CMS origin code found: "+", ".join(hits[:3]))
    return module_result("010","NOT TESTABLE","No CMS origin code found")

@reg("011")
def m011(target,verify=False):
    hits=check_pattern(target,r"security.*header|helmet|X-Frame-Options|Content-Security-Policy")
    if not hits:
        return module_result("011","CONFIRMED","No security headers found in target")
    return module_result("011","FIXED","Security headers present: "+", ".join(hits[:3]))

def run_finding(fid, target, verify=False):
    fid=fid.strip().zfill(3)
    if fid not in MODULES:
        print(f"Unknown finding {fid}")
        return
    res=MODULES[fid](target, verify)
    print(json.dumps(res,indent=2))

def run_all(target, verify=False):
    print(ASCII)
    results=[]
    for fid in sorted(MODULES):
        r=MODULES[fid](target, verify)
        results.append(r)
        print(f"{fid}: {r['status']}")
    # write report
    out=os.path.join(ROOT,"results.json")
    with open(out,"w") as f: json.dump(results,f,indent=2)
    print("Results written to",out)

def main():
    ap=argparse.ArgumentParser(prog="naser2shell")
    ap.add_argument("--list",action="store_true")
    ap.add_argument("--finding")
    ap.add_argument("--verify",action="store_true")
    ap.add_argument("--all",action="store_true")
    ap.add_argument("--target",default=".")
    args=ap.parse_args()
    if args.list:
        list_findings(); return
    target=os.path.abspath(args.target)
    if args.finding:
        run_finding(args.finding,target,args.verify); return
    if args.all:
        run_all(target,args.verify); return
    print(ASCII)
    print("Use --list, --finding, or --all")

if __name__=="__main__":
    main()
