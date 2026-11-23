# Portal session cookie weak attributes

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `lib/portal-session.ts:26`

## Cvss Assessment

Cookie secure flag tied to NODE_ENV production; sameSite lax; no __Host prefix.

**Impact:** MitM in dev, limited CSRF exposure.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.3

**Local PoC (localhost only):**
```
curl -I http://localhost:3000/api/portal/login
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.
