# CVSS Assessment — Finding 011

## Vector (CVSS 4.0)

```
AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N
```

## Base score

Approximately **3.1 (Low)**.

## Metric justification

| Metric | Value | Rationale |
| --- | --- | --- |
| Attack Vector (AV) | Network (N) | The weakness is exposed over the network on served responses. |
| Attack Complexity (AC) | Low (L) | Observing/omitting headers is deterministic; no special conditions. |
| Attack Requirements (AT) | None (N) | No race or special configuration state required. |
| Privileges Required (PR) | None (N) | No privileges required; the weakness is in the response surface. |
| User Interaction (UI) | None (N) | No direct user interaction is required by the weakness itself. |
| Confidentiality (VC) | Low (L) | Potential amplification of data exposure (e.g. via XSS) under a secondary weakness. |
| Integrity (VI) | None (N) | No direct integrity impact from header absence alone. |
| Availability (VA) | None (N) | No availability impact. |
| Subsequent Confidentiality (SC) | None (N) | No confirmed downstream impact. |
| Subsequent Integrity (SI) | None (N) | No confirmed downstream integrity impact. |
| Subsequent Availability (SA) | None (N) | No confirmed downstream availability impact. |

## Notes on scoring

- **AC:L** because header absence is deterministic and trivially observable.
- **VC:L** reflects the amplifying effect on confidentiality when a secondary weakness
  exists; it is not a direct disclosure.
- VI/VA are None because header absence alone does not alter or deny service.
- The score intentionally remains Low to reflect that this is a defense-in-depth gap,
  not a standalone compromise.

## Severity label

Low (consistent with the Informational/Low classification).
