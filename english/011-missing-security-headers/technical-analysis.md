# Technical Analysis — Finding 011

## Configuration under review

`next.config.mjs` (30 lines total). The relevant section:

```js
4  const nextConfig = {
5    async headers() {
6      return [{ source: '/zertifikate/hexagon-cyber-security.pdf', headers: [{ key: 'X-Robots-Tag', value: 'noindex' }] }]
7    },
```

The `headers()` hook returns a single-element array scoped to one PDF route. Next.js
applies these headers only to that route. No additional rules are present elsewhere in
the file (verified across lines 1-30).

## Why this matters

Next.js does not inject security headers by default. When `headers()` is present but
scoped narrowly, the rest of the application is served with Next.js defaults plus
whatever the hosting platform adds. On a minimal Node/self-hosted deployment, that
means the browser receives responses with none of the defensive headers listed below.

### Content-Security-Policy

Without CSP, any injected script executes with full origin privileges. CSP is the
primary defense-in-depth against XSS and data exfiltration; its absence means a single
XSS sink escalates directly to session compromise.

### Strict-Transport-Security

Without HSTS, a network attacker can attempt SSL stripping / protocol downgrade on a
victim's first (or any) HTTP request, since browsers are free to accept `http://`
links.

### X-Frame-Options / frame-ancestors

Without framing restrictions, the site can be embedded in an attacker-controlled
iframe, enabling clickjacking / UI-redress attacks against authenticated actions.

### X-Content-Type-Options: nosniff

Without `nosniff`, browsers may MIME-sniff responses and execute content in a
different type than declared, enabling certain content-confusion attacks.

### Referrer-Policy and Permissions-Policy

Absent these, referrer URLs may leak to third parties, and powerful browser features
(camera, geolocation, etc.) are not explicitly disabled.

## Trust boundary

Security headers are a browser-enforced control. Their absence shifts more
responsibility onto application-layer output encoding and onto the hosting platform.
Any deployment that does not add them at the edge therefore loses a defense layer.

## Interaction with other findings

The lack of CSP and `nosniff` increases the impact of any content-injection finding.
The lack of framing protection increases the impact of any state-changing action.
This finding is best read as an amplifier of other weaknesses rather than a standalone
compromise.
