# Remediation — Finding 011

## Recommended fix

Add a global header rule to `next.config.mjs` that applies defensive headers to all
routes. Keep the existing PDF-specific `X-Robots-Tag` rule and add a catch-all rule.

```js
// next.config.mjs
const securityHeaders = [
  { key: 'Content-Security-Policy', value: "default-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'" },
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Frame-Options', value: 'DENY' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
]

const nextConfig = {
  async headers() {
    return [
      { source: '/:path*', headers: securityHeaders },
      { source: '/zertifikate/hexagon-cyber-security.pdf', headers: [{ key: 'X-Robots-Tag', value: 'noindex' }] },
    ]
  },
  // ... rest unchanged
}
```

## Notes on each header

- **CSP:** start in `Content-Security-Policy-Report-Only` to avoid breaking inline
  scripts/styles, then enforce. Tailor `script-src`/`style-src` to the app's real
  usage (Next.js may require `'unsafe-inline'` for some bundles; prefer nonces where
  possible).
- **HSTS:** only enable `preload` after confirming all subdomains are HTTPS-only.
- **X-Frame-Options vs frame-ancestors:** `frame-ancestors` (CSP) supersedes
  `X-Frame-Options`; include both for legacy browsers.
- **Permissions-Policy:** disable only features the app does not need.

## Verification

See `verification.md` for commands that confirm the headers appear after the change.

## Risk of change

Low to moderate. An overly strict CSP can break legitimate functionality; roll out CSP
in report-only mode first and monitor violations before enforcing. HSTS is
hard to reverse once clients cache it; enable with a modest `max-age` initially.
