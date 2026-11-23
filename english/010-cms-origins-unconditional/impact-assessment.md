# Impact Assessment — Finding 010

## Summary

Unconditional inclusion of `configuredURL.origin` in the Payload CORS and CSRF
allowlists converts an operational configuration value into a security trust input.
On a correctly configured deployment the impact is nil; under a configuration
misconfiguration it enables cross-origin access to authenticated CMS functionality.

## CIA impact (conditional on misconfiguration)

| Property | Rating | Rationale |
| --- | --- | --- |
| Confidentiality | Low | An allowed hostile origin could read authenticated CMS responses for a victim session. |
| Integrity | None | No direct write primitive is introduced by this code; state changes depend on other endpoints. |
| Availability | None | No availability impact in the reviewed paths. |

## Scope

The weakness is confined to the CORS/CSRF configuration derived in
`payload.config.ts:100-101`. It does not affect the four hard-coded production
origins and does not weaken Payload's CSRF token validation for non-allowlisted
origins.

## Defense-in-depth loss

Security controls should fail closed on unexpected input. Here, unexpected input
(an unrecognized host) is silently accepted and promoted to a trusted origin. This
removes a layer of defense that would otherwise contain a configuration error.

## Likelihood

Low. Requires control over deployment configuration. No pre-authentication remote
primitive exists in the reviewed code.

## Business impact

- No direct financial or data-breach impact under correct operation.
- Material impact only if a deployment pipeline, fork, or environment variable
  injection allows an attacker to influence `serverURL`.
- Worth remediating as hardening to guarantee the allowlist cannot be widened by a
  configuration mistake.
