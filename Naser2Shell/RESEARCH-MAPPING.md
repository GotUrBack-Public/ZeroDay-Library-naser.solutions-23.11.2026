# RESEARCH MAPPING

## 001-payload-secret-empty-default

# README.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Primary file: payload.config.ts:39
Root cause: secret: process.env.PAYLOAD_SECRET || ''

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# affected-code.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Primary file: payload.config.ts:39
Root cause: secret: process.env.PAYLOAD_SECRET || ''

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# attack-scenario.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Primary file: payload.config.ts:39
Root cause: secret: process.env.PAYLOAD_SECRET || ''

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# cvss-assessment.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Primary file: payload.config.ts:39
Root cause: secret: process.env.PAYLOAD_SECRET || ''

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# disclosure.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Primary file: payload.config.ts:39
Root cause: secret: process.env.PAYLOAD_SECRET || ''

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# exploit-walkthrough.md

Finding: 001-payload-secret-empty-default
Status: CONFIRMED
Severity: HIGH
Prima

## 002-portal-login-no-rate-limiting

# README.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# affected-code.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# attack-scenario.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# cvss-assessment.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# disclosure.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# exploit-walkthrough.md

Finding: 002-portal-login-no-rate-limiting
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/portal/login/route.ts
Root cause: No rate limiting



## 003-thumbnail-resource-exhaustion

# README.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root cause: Arbitrary url

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# affected-code.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root cause: Arbitrary url

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# attack-scenario.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root cause: Arbitrary url

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# cvss-assessment.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root cause: Arbitrary url

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# disclosure.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root cause: Arbitrary url

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# exploit-walkthrough.md

Finding: 003-thumbnail-resource-exhaustion
Status: CONFIRMED
Severity: HIGH
Primary file: app/api/generate-thumbnail/route.ts
Root caus

## 004-contact-form-no-rate-limiting

# README.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# affected-code.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# attack-scenario.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# cvss-assessment.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# disclosure.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disclaimer: Testing performed only on localhost; no production systems affected.

# exploit-walkthrough.md

Finding: 004-contact-form-no-rate-limiting
Status: CONFIRMED
Severity: MEDIUM
Primary file: app/api/contact/route.ts
Root cause: No rate limiting

Local testing disc

## 005-upload-no-per-user-quota

# Upload endpoint without per-user quota

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/api/portal/attachments/upload/route.ts`

## Readme

No global per-user quota; 20MB per file (MAX_ATTACHMENT_BYTES); filename controllable (addRandomSuffix:false); onUploadCompleted empty.

**Impact:** Resource exhaustion via unlimited uploads, blob storage abuse.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N` → 5.9

**Local PoC (localhost only):**
```
curl -X POST http://localhost:3000/api/portal/attachments/upload -H 'Content-Type: application/json' -d '{"type":"blob.generate-client-token"}'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# Upload endpoint without per-user quota

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/api/portal/attachments/upload/route.ts`

## Affected Code

No global per-user quota; 20MB per file (MAX_ATTACHMENT_BYTES); filename controllable (addRandomSuffix:false); onUploadCompleted empty.

**Impact:** Resource exhaustion via unlimited uploads, blob storage abuse.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N` → 5.9

**Local PoC (localhost only):**
```
curl -X POST http://localhost:3000/api/portal/attachments/upload -H 'Content-Type: application/json' -d '{"type":"blob.generate-client-token"}'
```

Local testing disclaimer: This documentation is for au

## 006-session-cookie-weak-attributes

# Portal session cookie weak attributes

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `lib/portal-session.ts:26`

## Readme

Cookie secure flag tied to NODE_ENV production; sameSite lax; no __Host prefix.

**Impact:** MitM in dev, limited CSRF exposure.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.3

**Local PoC (localhost only):**
```
curl -I http://localhost:3000/api/portal/login
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# Portal session cookie weak attributes

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `lib/portal-session.ts:26`

## Affected Code

Cookie secure flag tied to NODE_ENV production; sameSite lax; no __Host prefix.

**Impact:** MitM in dev, limited CSRF exposure.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.3

**Local PoC (localhost only):**
```
curl -I http://localhost:3000/api/portal/login
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# Portal session cookie weak attributes

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `lib/portal-session.ts:26`

## Attack Scenario

Cookie secure flag tied to NODE_ENV production; sameSite lax; no __Host prefix.

**Impact:** MitM in dev, limited CSRF exposure.

*

## 007-preview-csrf-get

# Preview draftMode activation via CSRF GET

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/preview/route.ts:6,15,28-29`

## Readme

State-changing GET activates draftMode().enable() without CSRF protection; no Origin/Referer check; no CSRF token.

**Impact:** Victim browser forced into draft mode, sees unpublished content.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:R/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.4

**Local PoC (localhost only):**
```
curl 'http://localhost:3000/preview?slug=home&collection=pages'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# Preview draftMode activation via CSRF GET

**Status:** CONFIRMED  
**Severity:** MEDIUM  
**File:** `app/preview/route.ts:6,15,28-29`

## Affected Code

State-changing GET activates draftMode().enable() without CSRF protection; no Origin/Referer check; no CSRF token.

**Impact:** Victim browser forced into draft mode, sees unpublished content.

**CVSS 4.0:** `AV:N/AC:L/AT:N/PR:N/UI:R/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` → 5.4

**Local PoC (localhost only):**
```
curl 'http://localhost:3000/preview?slug=home&collection=pages'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# Preview draftMode activation via CSRF GET

**Status:** CONFIRMED  
**Severity:** MEDIUM  
*

## 008-portal-jwt-no-client-binding

# Portal JWT not bound to client

**Status:** CONFIRMED (with restrictions)  
**Severity:** MEDIUM  
**File:** `app/api/portal/login/route.ts:19, lib/portal-session.ts:26`

## Readme

JWT not bound to IP/User-Agent; stateless; no server-side invalidation; secure=false in dev.

**Impact:** Stolen token works from any client until expiry (requires second theft vector).

**CVSS 4.0:** `AV:N/AC:M/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N` → 5.9

**Local PoC (localhost only):**
```
curl -X POST http://localhost:3000/api/portal/login -H 'Content-Type: application/json' -d '{"email":"x","password":"y"}'
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

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

Local testing disclaimer: This documentation is for authorized local security research only. D

## 009-saveclientfeedback-lost-update

# saveClientFeedback lost update

**Status:** INFORMATIONAL  
**Severity:** LOW  
**File:** `app/portal/actions.ts:42-62`

## Readme

Read-modify-write without atomicity; no locking; no version check; Last-Write-Wins overwrites concurrent submissions.

**Impact:** Attachment data loss on concurrent requests, no PII exposure.

**CVSS 4.0:** `AV:N/AC:H/AT:N/PR:L/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N` → 2.7

**Local PoC (localhost only):**
```
concurrent POSTs to saveClientFeedback
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# saveClientFeedback lost update

**Status:** INFORMATIONAL  
**Severity:** LOW  
**File:** `app/portal/actions.ts:42-62`

## Affected Code

Read-modify-write without atomicity; no locking; no version check; Last-Write-Wins overwrites concurrent submissions.

**Impact:** Attachment data loss on concurrent requests, no PII exposure.

**CVSS 4.0:** `AV:N/AC:H/AT:N/PR:L/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N` → 2.7

**Local PoC (localhost only):**
```
concurrent POSTs to saveClientFeedback
```

Local testing disclaimer: This documentation is for authorized local security research only. Do not test against systems you do not own or have written permission to assess.

# saveClientFeedback lost update

**Status:** INFORMATIONAL  
**Severity:** LOW  
**File:** `app/portal/actions.ts:42-62`

## Attack Scenario

Read-modify-write without at

## 010-cms-origins-unconditional

# Finding 010 — Unconditional CMS Origin Allowlist (`configuredURL.origin`)

| Field | Value |
| --- | --- |
| Finding ID | 010 |
| Title | Unconditional CMS Origin Allowlist |
| Classification | Informational / Low |
| CWE | CWE-942 (Permissive Cross-domain Policy / Allowlist) |
| Affected file | `lib/cms-origins.ts:14` |
| Consumers | `payload.config.ts:100` (`cors`), `payload.config.ts:101` (`csrf`) |
| CVSS 4.0 | `AV:N/AC:H/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N` (~3.1) |

## Summary

`cmsOrigins()` merges a fixed list of production origins with the origin derived
from the configured `serverURL`. The configured origin is appended **unconditionally**;
the function validates only the URL scheme (`http:` / `https:`) and never checks the
resulting host against an allowlist. If `NEXT_PUBLIC_SERVER_URL` (or its Vercel
fallback) is misconfigured to point at an attacker-controlled domain, that domain is
silently added to the Payload CMS CORS and CSRF allowlists.

## Document index

1. `finding.md` — executive finding statement
2. `technical-analysis.md` — root-cause analysis
3. `affected-code.md` — exact code excerpts and line references
4. `attack-scenario.md` — preconditions and realistic attack path
5. `poc.md` — local-only proof of concept
6. `exploit-walkthrough.md` — step-by-step reproduction
7. `impact-assessment.md` — security impact
8. `cvss-assessment.md` — CVSS 4.0 scoring and rationale
9. `remediation.md` — fix guidance
10. `verification.md` — how to verify pres

## 011-missing-security-headers

# Finding 011 — Missing Global Security Headers

| Field | Value |
| --- | --- |
| Finding ID | 011 |
| Title | Missing Global Security Headers |
| Classification | Confirmed / Informational (Low) |
| CWE | CWE-693 (Protection Mechanism Failure), CWE-1021 (Improper Restriction of Rendered UI Layers / Clickjacking) |
| Affected file | `next.config.mjs` (headers configuration) |
| CVSS 4.0 | `AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N` (~3.1) |

## Summary

`next.config.mjs` configures HTTP headers for exactly one route
(`/zertifikate/hexagon-cyber-security.pdf`, adding `X-Robots-Tag: noindex`). No
global security headers are configured. In particular the application does not set:

- `Content-Security-Policy` (CSP)
- `Strict-Transport-Security` (HSTS)
- `X-Frame-Options` / `frame-ancestors`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy`
- `Permissions-Policy`

This reduces defense-in-depth and leaves the application more exposed to clickjacking,
MIME-sniffing, protocol-downgrade, and content-injection classes of attack.

## Document index

1. `finding.md` — executive finding statement
2. `technical-analysis.md` — root-cause analysis
3. `affected-code.md` — exact code excerpts
4. `attack-scenario.md` — preconditions and realistic attack path
5. `poc.md` — local-only proof of concept
6. `exploit-walkthrough.md` — step-by-step reproduction
7. `impact-assessment.md` — security impact
8. `cvss-assessment.md` — CVSS 4.0 scoring and rationale
9. `remediation.md` —
