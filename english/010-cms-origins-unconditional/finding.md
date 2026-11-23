# Finding 010 — Unconditional CMS Origin Allowlist

## Statement

`cmsOrigins()` in `lib/cms-origins.ts` returns a set containing the four hard-coded
production origins plus the origin parsed from the caller-supplied `serverURL`
(`lib/cms-origins.ts:14`). The function only validates that the configured URL uses
the `http:` or `https:` scheme (`lib/cms-origins.ts:11-13`). It performs **no**
validation of the host, subdomain, port, or suffix of the configured URL against a
trusted allowlist before adding it to the CORS/CSRF origin set.

## Root cause

```ts
// lib/cms-origins.ts:9-15
export function cmsOrigins(serverURL: string): string[] {
  const configuredURL = new URL(serverURL)                              // :10
  if (!['https:', 'http:'].includes(configuredURL.protocol)) {          // :11
    throw new Error('The CMS server URL must use HTTP or HTTPS.')        // :12
  }
  return [...new Set([...productionOrigins, configuredURL.origin])]      // :14
}
```

Only `configuredURL.protocol` is checked. `configuredURL.origin` is trusted and
appended verbatim. There is no comparison against `productionOrigins`, no host
allowlist, and no rejection of lookalike or user-influenced hosts.

## Consumers

`payload.config.ts` feeds the result directly into both Payload security controls:

```ts
// payload.config.ts:100-101
cors: cmsOrigins(serverURL),
csrf: cmsOrigins(serverURL),
```

`serverURL` itself is derived from environment configuration:

```ts
// payload.config.ts:29-35
const serverURL =
  process.env.NEXT_PUBLIC_SERVER_URL ||
  (process.env.VERCEL_PROJECT_PRODUCTION_URL
    ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
    : process.env.VERCEL_URL
      ? `https://${process.env.VERCEL_URL}`
      : 'http://localhost:3000')
```

## Classification

Informational / Low. The behaviour is a defense-in-depth gap that becomes a
vulnerability only under a deployment misconfiguration (attacker-influenced
`serverURL`). It is not remotely exploitable on a correctly configured deployment.

## Prerequisites

An attacker must be able to influence `NEXT_PUBLIC_SERVER_URL` (or the Vercel
fallback variables) so that the derived origin resolves to a domain the attacker
controls, or the operator must otherwise introduce a hostile origin into the config.
