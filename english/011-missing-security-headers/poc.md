# Proof of Concept — Finding 011

> Scope: this proof of concept runs entirely against `http://localhost`. It inspects
> HTTP response headers of a local development server. It does not target any
> production host or third-party service.

## Objective

Demonstrate that the local Next.js server does not emit the expected global security
headers, confirming the configuration gap.

## Steps

1. Start the local development server (only if not already running):

   ```bash
   cd /home/schaden637/naser-audit-clean
   npm run dev   # serves on http://localhost:3000 (per payload.config.ts default)
   ```

2. Inspect response headers for a representative page:

   ```bash
   curl -sD - -o /dev/null http://localhost:3000/ | sort
   ```

3. Repeat for the PDF route to confirm only `X-Robots-Tag` is present there:

   ```bash
   curl -sD - -o /dev/null http://localhost:3000/zertifikate/hexagon-cyber-security.pdf | sort
   ```

## Expected output

For `/`, the response headers will **not** include any of:

- `content-security-policy`
- `strict-transport-security`
- `x-frame-options`
- `x-content-type-options`
- `referrer-policy`
- `permissions-policy`

For the PDF route, only `x-robots-tag: noindex` is added (per
`next.config.mjs:6`); no security headers are present.

## Interpretation

The absence of these headers on responses confirms the root cause: no global header
rule exists in `next.config.mjs`. This is a defense-in-depth gap, not a direct exploit.

## Cleanup

Stop the development server after inspection.
