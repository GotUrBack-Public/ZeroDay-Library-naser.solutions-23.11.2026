# Finding 011 — Missing Global Security Headers

## Statement

The Next.js configuration in `next.config.mjs` defines an HTTP header rule for a single
route only:

```js
// next.config.mjs:5-7
async headers() {
  return [{ source: '/zertifikate/hexagon-cyber-security.pdf', headers: [{ key: 'X-Robots-Tag', value: 'noindex' }] }]
},
```

No global (catch-all `source: '/(.*)'` or `/:path*`) header rules are defined. As a
result, responses across the application are served without the standard defensive
HTTP security headers.

## Missing headers

| Header | Purpose | Status |
| --- | --- | --- |
| `Content-Security-Policy` | Mitigate XSS, injection, and unauthorized resource loads | Missing |
| `Strict-Transport-Security` | Enforce HTTPS, prevent protocol downgrade | Missing |
| `X-Frame-Options` / CSP `frame-ancestors` | Prevent clickjacking | Missing |
| `X-Content-Type-Options: nosniff` | Prevent MIME sniffing | Missing |
| `Referrer-Policy` | Limit referrer leakage | Missing |
| `Permissions-Policy` | Restrict powerful browser features | Missing |

## Root cause

No global security-header configuration exists in `next.config.mjs`. The only `headers()`
entry targets a single PDF route for an SEO directive (`X-Robots-Tag: noindex`),
unrelated to browser security hardening.

## Classification

Confirmed / Informational (Low). The absence of security headers is a confirmed
configuration state. Its direct exploitability is limited (defense-in-depth), hence the
Low rating; it raises the severity of other weaknesses (e.g. XSS, clickjacking) that
would otherwise be contained by these headers.

## Prerequisites

For concrete impact, a secondary weakness must exist that these headers would mitigate
(for example an XSS sink for CSP, a framing surface for clickjacking, or a MIME
confusion vector for `nosniff`). Absent such a weakness, the impact is reduced
defense-in-depth only.
