# Portal JWT not bound to client

**Status:** CONFIRMED (with restrictions)  
**Severity:** MEDIUM  
**File:** `app/api/portal/login/route.ts:19, lib/portal-session.ts:26`

## Affected Code

JWT not bound to IP/User-Agent; stateless; no server-side invalidation; secure=false in dev.

**Impact:** Stolen token works from any client until expiry (requires second theft vector).

**CVSS 4.0:** `AV:N/AC:M/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N` → 5.9

**Local PoC (localhost only):**
```
curl -X POST http://localhost:3000/api/portal/login -H 'Content-Type: application/json' -d '{"email":"x","password":"y"}'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.
