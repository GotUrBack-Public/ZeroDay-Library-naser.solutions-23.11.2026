# Affected Code — Finding 011

## Configuration file

`next.config.mjs` (full file, 30 lines):

```js
1  import { withPayload } from '@payloadcms/next/withPayload'
2
3  /** @type {import('next').NextConfig} */
4  const nextConfig = {
5    async headers() {
6      return [{ source: '/zertifikate/hexagon-cyber-security.pdf', headers: [{ key: 'X-Robots-Tag', value: 'noindex' }] }]
7    },
8    async rewrites() {
9      return [{ source: '/favicon.ico', destination: '/favicon.png' }]
10   },
...
28 }
29
30 export default withPayload(nextConfig)
```

## Key observation

- `next.config.mjs:5-7` — the only `headers()` rule, scoped to one PDF route.
- No rule uses `source: '/(.*)'` or `/:path*` to apply headers globally.
- `X-Robots-Tag: noindex` is an SEO directive, not a browser security control.

## What is absent

There is no occurrence of the following keys anywhere in `next.config.mjs`:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`

## Consumer

`withPayload(nextConfig)` (line 30) wraps the config for the Payload/Next.js
integration; it does not add security headers on its own. The absence therefore
propagates to the served application.
