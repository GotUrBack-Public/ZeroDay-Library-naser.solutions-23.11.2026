# Attack Scenario — Finding 010

## Nature

This is **not** a remotely exploitable vulnerability on a correctly configured
deployment. It is a defense-in-depth weakness that becomes exploitable only when the
trusted configuration input (`serverURL`) is attacker-influenced or misconfigured.
The scenario below documents the conditions under which impact materializes.

## Prerequisites

1. **Configuration influence.** The attacker can set or influence one of:
   - `NEXT_PUBLIC_SERVER_URL`, or
   - `VERCEL_PROJECT_PRODUCTION_URL` / `VERCEL_URL` (e.g. via a forked or
     attacker-controlled Vercel project that the victim deployment reads).
2. **A reachable CMS mutation endpoint** that relies on the CORS/CSRF allowlist for
   browser-origin enforcement (Payload admin API / auth cookie flows).
3. **A victim with an authenticated CMS session** (admin/editor) who can be induced
   to load attacker content, or a browser context where the session cookie is sent
   cross-origin under the misconfigured CORS policy.

If any of these is absent, no security impact follows.

## Attack path (conditional)

1. Attacker arranges for `serverURL` to resolve to `https://attacker.example`
   (configuration poisoning, fork/preview leakage, or supply-chain of env vars).
2. `cmsOrigins('https://attacker.example')` returns
   `[...productionOrigins, 'https://attacker.example']` (`lib/cms-origins.ts:14`).
3. Payload now treats `https://attacker.example` as an allowed CORS and CSRF origin
   (`payload.config.ts:100-101`).
4. A browser at `https://attacker.example` issues credentialed cross-origin requests
   to the CMS. Because the origin is allowlisted, CORS does not block reading the
   responses and the CSRF check does not reject the mutation.
5. If the victim's session cookie is attached, the attacker script can read
   authenticated CMS data and/or perform state-changing actions within the victim's
   privileges.

## Why "High" complexity

The attacker cannot reach step 4 without first controlling deployment configuration.
On a correctly configured deployment, `serverURL` is one of the four trusted
production origins or a trusted Vercel production URL, and no hostile origin enters
the allowlist. The realistic likelihood is therefore low, but the consequence of the
misconfiguration is a genuine cross-origin trust failure.

## Out of scope / not claimed

- No claim that the four hard-coded `productionOrigins` are weak.
- No claim that Payload's CORS/CSRF implementation is bypassable in general.
- No claim of exploitability without configuration influence.
