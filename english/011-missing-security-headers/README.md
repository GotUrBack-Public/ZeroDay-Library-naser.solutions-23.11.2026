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
9. `remediation.md` — fix guidance
10. `verification.md` — how to verify presence/absence
11. `references.md` — standards and documentation
12. `detection.md` — detection and monitoring guidance

## Testing disclaimer

All proof-of-concept material in this directory targets `http://localhost` only and
was authored for a local development instance. No external system, production host,
or third-party service is exercised. Header inspection is non-destructive and does not
modify application state. This document is descriptive of source code and configuration
as reviewed and is not evidence of a live compromise of any deployed environment.
