# CVSS Assessment — Finding 010

## Vector (CVSS 4.0)

```
AV:N/AC:H/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N
```

## Base score

Approximately **3.1 (Low)**.

## Metric justification

| Metric | Value | Rationale |
| --- | --- | --- |
| Attack Vector (AV) | Network (N) | The affected code is reachable over the network in a deployed CMS; exploitation path is network-based. |
| Attack Complexity (AC) | High (H) | Requires attacker influence over deployment configuration (`serverURL`); no reliable pre-auth remote primitive. |
| Attack Requirements (AT) | None (N) | No special race or configuration state beyond the misconfiguration itself is required at exploit time. |
| Privileges Required (PR) | None (N) | The weakness itself grants no privileges; configuration influence is treated as an external precondition. |
| User Interaction (UI) | None (N) | No victim interaction is required by the code path once CORS is widened; a victim session may be leveraged but is not an attack prerequisite at the code level. |
| Confidentiality (VC) | Low (L) | Possible read of authenticated CMS data for a victim session. |
| Integrity (VI) | None (N) | No direct integrity primitive in the reviewed code. |
| Availability (VA) | None (N) | No availability impact. |
| Subsequent Confidentiality (SC) | None (N) | No confirmed pivot beyond the CMS. |
| Subsequent Integrity (SI) | None (N) | No downstream integrity impact confirmed. |
| Subsequent Availability (SA) | None (N) | No downstream availability impact confirmed. |

## Notes on scoring

- The High complexity and None-privilege combination reflects that exploitation hinges
  on an external configuration precondition rather than a direct code flaw.
- The Low confidentiality reflects the potential to read authenticated CMS responses
  under a misconfiguration; integrity and availability remain unaffected.
- This score describes the weakness in isolation. A deployed environment with weaker
  configuration hygiene could rate higher, but that is an environmental, not a code,
  property.

## Severity label

Low (consistent with the informational/low classification of this finding).
