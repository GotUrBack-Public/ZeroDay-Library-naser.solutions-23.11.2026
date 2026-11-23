# Remediation — Finding 010

## Recommended fix

Validate the configured URL's **origin** against an explicit allowlist before merging
it into the returned set. Do not append `configuredURL.origin` unconditionally.

### Option A — Strict allowlist check (recommended)

```ts
// lib/cms-origins.ts
const productionOrigins = [
  'https://www.naser.solutions',
  'https://naser.solutions',
  'https://www.naser-solutions.de',
  'https://naser-solutions.de',
]

const allowedConfiguredHosts = new Set([
  'www.naser.solutions',
  'naser.solutions',
  'www.naser-solutions.de',
  'naser-solutions.de',
  'localhost',
])

export function cmsOrigins(serverURL: string): string[] {
  const configuredURL = new URL(serverURL)
  if (!['https:', 'http:'].includes(configuredURL.protocol)) {
    throw new Error('The CMS server URL must use HTTP or HTTPS.')
  }
  if (!allowedConfiguredHosts.has(configuredURL.hostname)) {
    throw new Error('The CMS server URL host is not allowed.')
  }
  return [...new Set([...productionOrigins, configuredURL.origin])]
}
```

This preserves local/preview support (`localhost`) while rejecting arbitrary hosts.

### Option B — Allowlist-only for production, append only for local

Append `configuredURL.origin` only when the host is `localhost`, `127.0.0.1`, or a
`.vercel.app` preview you explicitly trust; otherwise ignore it in production.

## Defense-in-depth additions

- **Fail closed:** throw on unknown hosts rather than silently returning them.
- **Environment guard:** in production, assert `serverURL` resolves to one of the
  four production origins and fail startup otherwise.
- **Log and alert:** emit a warning when a non-production origin is added to the
  allowlist.

## Tests to add

Extend `tests/cms-origins.test.ts` to assert that a hostile `serverURL` is rejected:

```ts
assert.throws(() => cmsOrigins('https://attacker.example'))
assert.throws(() => cmsOrigins('https://www.naser-solutions.de.attacker.example'))
```

## Risk of change

Low. The four production origins remain supported, and legitimate local/preview usage
(`localhost`, Vercel preview URLs) is retained by the host allowlist. Confirm which
preview hosts are legitimately used before narrowing the list.
