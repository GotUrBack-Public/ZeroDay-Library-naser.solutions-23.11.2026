# Impact Assessment — Finding 011

## Summary

The application serves responses without global defensive HTTP security headers. This
is a confirmed configuration gap whose direct impact is reduced defense-in-depth. Its
material impact is as an **amplifier** of other weaknesses (XSS, clickjacking,
MIME confusion, protocol downgrade).

## CIA impact

| Property | Rating | Rationale |
| --- | --- | --- |
| Confidentiality | Low | No direct disclosure; amplifies XSS/exfiltration if a sink exists. |
| Integrity | None | No direct integrity impact from header absence alone. |
| Availability | None | No availability impact. |

## Why Low rather than None

The headers are a real, measurable security control. Their absence is a confirmed
weakness with a plausible exploitation path whenever a secondary weakness exists.
This justifies a Low rating rather than dismissing it as purely informational.

## Defense-in-depth loss

Each missing header removes a layer that would otherwise:

- contain XSS blast radius (CSP),
- prevent clickjacking of state-changing actions (frame-ancestors),
- prevent MIME confusion (`nosniff`),
- prevent transport downgrade (HSTS).

## Aggravating / mitigating factors

- **Aggravating:** any content-injection finding becomes more severe.
- **Mitigating:** if the hosting platform (e.g. a CDN/reverse proxy) injects these
  headers at the edge, real-world exposure may be lower than the code suggests. This
  should be confirmed against the actual deployment.
