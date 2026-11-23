# Affected Code — Finding 010

## Primary location

`lib/cms-origins.ts:14`

```ts
14  return [...new Set([...productionOrigins, configuredURL.origin])]
```

`configuredURL.origin` is appended without validation beyond the scheme check on
lines 11-13.

## Full function

`lib/cms-origins.ts:9-15`

```ts
export function cmsOrigins(serverURL: string): string[] {
  const configuredURL = new URL(serverURL)
  if (!['https:', 'http:'].includes(configuredURL.protocol)) {
    throw new Error('The CMS server URL must use HTTP or HTTPS.')
  }
  return [...new Set([...productionOrigins, configuredURL.origin])]
}
```

## Hard-coded baseline origins

`lib/cms-origins.ts:2-7`

```ts
const productionOrigins = [
  'https://www.naser.solutions',
  'https://naser.solutions',
  'https://www.naser-solutions.de',
  'https://naser-solutions.de',
]
```

These four are constant and safe. The weakness is exclusively the dynamic term
`configuredURL.origin` on line 14.

## Consumers (trust propagation)

`payload.config.ts:100-101`

```ts
cors: cmsOrigins(serverURL),
csrf: cmsOrigins(serverURL),
```

## Origin of `serverURL`

`payload.config.ts:29-35`

```ts
const serverURL =
  process.env.NEXT_PUBLIC_SERVER_URL ||
  (process.env.VERCEL_PROJECT_PRODUCTION_URL
    ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
    : process.env.VERCEL_URL
      ? `https://${process.env.VERCEL_URL}`
      : 'http://localhost:3000')
```

If `NEXT_PUBLIC_SERVER_URL` is set to an attacker-controlled value, or if a
preview/fork deployment exposes `VERCEL_URL` for a project the attacker can influence,
the derived origin flows unchecked into both the `cors` and `csrf` allowlists.

## Related tests (context, not mitigation)

`tests/cms-origins.test.ts:7-10` constructs a Payload-like config using
`cmsOrigins(serverURL)` and exercises `extractJWT` from Payload to confirm
cookie-auth behaviour. The tests assert rejection of origins that differ from the
configured one (`:19-21`, `:27`); they do not assert rejection of a hostile
`serverURL`, confirming the gap is untested rather than closed.
