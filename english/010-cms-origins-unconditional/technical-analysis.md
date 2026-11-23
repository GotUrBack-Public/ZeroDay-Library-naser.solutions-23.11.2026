# Technical Analysis — Finding 010

## Function under review

`lib/cms-origins.ts` (15 lines total):

```ts
1  // Both public domains serve this CMS; browser mutations send their current origin.
2  const productionOrigins = [
3    'https://www.naser.solutions',
4    'https://naser.solutions',
5    'https://www.naser-solutions.de',
6    'https://naser-solutions.de',
7  ]
8
9  export function cmsOrigins(serverURL: string): string[] {
10   const configuredURL = new URL(serverURL)
11   if (!['https:', 'http:'].includes(configuredURL.protocol)) {
12     throw new Error('The CMS server URL must use HTTP or HTTPS.')
13   }
14   return [...new Set([...productionOrigins, configuredURL.origin])]
15 }
```

## Data flow

1. `payload.config.ts:29-35` computes `serverURL` from `NEXT_PUBLIC_SERVER_URL` with
   Vercel-provided fallbacks and a `http://localhost:3000` default.
2. `payload.config.ts:100` assigns `cors: cmsOrigins(serverURL)`.
3. `payload.config.ts:101` assigns `csrf: cmsOrigins(serverURL)`.
4. Payload uses these arrays to decide which `Origin` values are accepted for
   cross-origin requests (CORS) and which origins may receive authenticated,
   cookie-bearing mutations (CSRF defense).

## Root cause

The trust boundary is crossed without validation. `configuredURL.origin` is the
serialized `scheme://host[:port]` of whatever `serverURL` contains. The only guard
(`lib/cms-origins.ts:11-13`) rejects non-HTTP(S) schemes. Consequently:

- A hostile host such as `https://attacker.example` is accepted verbatim.
- A lookalike such as `https://www.naser-solutions.de.attacker.example` is accepted.
- Any port on an otherwise legitimate host is folded into the origin.

The `new Set(...)` on line 14 deduplicates but does not filter; it provides no
security property.

## Why the existing tests do not cover the gap

`tests/cms-origins.test.ts` validates the intended behaviour for *known good* inputs
and for *unrelated* origins while the config stays at a trusted value:

- `tests/cms-origins.test.ts:25-27` confirm that a mismatched preview host is
  rejected when the server URL is the trusted `this-project.vercel.app`.
- `tests/cms-origins.test.ts:19-21` confirm lookalike/attacker origins are rejected
  **because they are not the configured origin**.

These tests pass because the attacker origins are not equal to `serverURL`. They do
**not** assert that a hostile `serverURL` is rejected — and the code does not reject
it. The guarantee therefore rests entirely on the operator keeping `serverURL`
trustworthy, which the function does not enforce.

## Security-relevant boundary

The CORS/CSRF allowlist is a *security control*. Accepting an unvalidated,
configuration-derived origin turns an operational input into a security input. This
is the classic "configuration is code / configuration is a trust boundary" weakness
(CWE-942 family).

## Severity drivers

- **Confidentiality: Low** — a hostile allowed origin could read authenticated CMS
  responses if the browser sends the session cookie cross-origin and CORS permits it.
- **Attack complexity: High** — requires control over deployment configuration; no
  pre-auth remote primitive exists.
- **No integrity/availability impact** in the reviewed code paths.
