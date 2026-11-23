# Upload endpoint without per-user quota

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/api/portal/attachments/upload/route.ts`

## Attack Scenario

No global per-user quota; 20MB per file (MAX_ATTACHMENT_BYTES); filename controllable (addRandomSuffix:false); onUploadCompleted empty.

**Impact:** Resource exhaustion via unlimited uploads, blob storage abuse.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N` → 5.9

**Local PoC (localhost only):**
```
curl -X POST http://localhost:3000/api/portal/attachments/upload -H 'Content-Type: application/json' -d '{"type":"blob.generate-client-token"}'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.
