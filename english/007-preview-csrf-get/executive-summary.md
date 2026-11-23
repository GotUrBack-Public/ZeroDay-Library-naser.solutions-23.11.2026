# Preview draftMode activation via CSRF GET

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/preview/route.ts:6,15,28-29`

## Executive Summary

State-changing GET activates draftMode().enable() without CSRF protection; no Origin/Referer check; no CSRF token.

**Impact:** Victim browser forced into draft mode, sees unpublished content.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:R/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.4

**Local PoC (localhost only):**
```
curl 'http://localhost:3000/preview?slug=home&collection=pages'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.
