# References — Finding 010

## Source code (reviewed revision)

- `lib/cms-origins.ts:2-15` — origin allowlist construction.
- `payload.config.ts:29-35` — `serverURL` derivation.
- `payload.config.ts:100-101` — `cors` and `csrf` consumers.
- `tests/cms-origins.test.ts:7-31` — existing origin tests.

## Standards and classifications

- CWE-942: Permissive Cross-domain Policy / Allowlist.
  <https://cwe.mitre.org/data/definitions/942.html>
- OWASP: Cross-Site Request Forgery Prevention Cheat Sheet (origin/referer validation).
  <https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html>
- OWASP: HTML5 Security Cheat Sheet — CORS.
  <https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html>
- CVSS 4.0 Specification.
  <https://www.first.org/cvss/v4-0/specification-document>

## Framework documentation

- Payload CMS — CSRF protection (uses the `csrf` config option consumed here).
  <https://payloadcms.com/docs/>
- Payload CMS — CORS configuration (`cors` option).
  <https://payloadcms.com/docs/>
- Next.js — environment variables (`NEXT_PUBLIC_*` exposure semantics).
  <https://nextjs.org/docs/app/building-your-application/configuring/environment-variables>
