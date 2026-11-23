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
10. `verification.md` — how to verify presence/absence
11. `references.md` — standards and documentation
12. `detection.md` — detection and monitoring guidance

## Testing disclaimer

All proof-of-concept material in this directory targets `http://localhost` only and
was authored for a local development instance. No external system, production host,
or third-party service is exercised. This document is descriptive of source code as
reviewed and is not evidence of a live exploit against any deployed environment.
