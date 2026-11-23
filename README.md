<div align="center">

# ZeroDay Library — naser.solutions

**Security Research · Vulnerability Analysis · Local Proofs of Concept**

[![Repository](https://img.shields.io/badge/repository-public-blue?logo=github)](https://github.com/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026)
[![Research](https://img.shields.io/badge/focus-security%20research-7c3aed)](#project-scope)
[![Testing](https://img.shields.io/badge/testing-local%20only-success)](#testing-scope)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20DE%20%7C%20RU-informational)](#documentation-languages)
[![Status](https://img.shields.io/badge/status-research%20documentation-orange)](#research-status)
[![GitHub stars](https://img.shields.io/github/stars/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026?style=flat)](https://github.com/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026?style=flat)](https://github.com/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026/network/members)
[![GitHub issues](https://img.shields.io/github/issues/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026)](https://github.com/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026/issues)

*An organized collection of security findings, technical analysis, risk assessments and controlled proof-of-concept research.*

</div>

---

## About this project

ZeroDay Library is a security research repository documenting the analysis of the **naser.solutions** application.

The project is intended to make security findings understandable, reviewable and reproducible by other developers and security researchers. Documentation focuses on:

- Vulnerability descriptions and root-cause analysis
- Affected components and source-code references
- Attack prerequisites and realistic impact
- Proofs of Concept (PoCs) for controlled local environments
- Severity and CVSS assessments, including their assumptions
- Mitigation guidance and verification notes
- False positives, limitations and unresolved questions

This repository is a **research and documentation project**. It is not an authorization to test, scan, access or interfere with any system.

## Documentation languages

The research documentation is intended to be maintained in three languages:

| Language | Description |
|---|---|
| English (EN) | Canonical technical documentation |
| Deutsch (DE) | Vollständige deutschsprachige Dokumentation |
| Русский (RU) | Полная техническая документация на русском языке |

Language-specific documents should preserve the same finding IDs, technical details, evidence status, source references and risk ratings. Where a translation is incomplete, that limitation must be stated rather than silently omitting material.

## Research status and evidence standard

Security labels in this repository describe the evidence available for the corresponding finding. They must not be interpreted as a guarantee that a vulnerability is exploitable in every deployment.

| Classification | Meaning |
|---|---|
| **CONFIRMED** | The stated behavior or weakness was reproduced or directly established in the documented test scope. The demonstrated impact must be described separately. |
| **POTENTIAL** | A plausible weakness exists, but exploitability or impact has not been sufficiently demonstrated. |
| **INFORMATIONAL** | A hardening, reliability or configuration observation without a demonstrated security impact. |
| **FALSE POSITIVE** | The original concern was not supported after validation or was mitigated by an existing control. |

A confirmed code-level weakness does not automatically mean that a complete attack chain, production exposure or data compromise has been demonstrated.

Risk ratings and CVSS scores must include their assumptions, scope and rationale. Provisional scores must be marked as provisional.

## Testing scope

The reported proof-of-concept work is described as having been performed in controlled local environments, such as:

- `localhost` application instances
- Isolated development or test instances
- Local mocks and test fixtures

**No production testing is authorized or implied by this repository.** Readers must not run the PoCs against public hosts, third-party services, customer environments or systems they do not own or have explicit written permission to test.

Each finding should state its actual test environment and evidence. If a test was not independently reproduced or its logs are unavailable, the documentation must say so clearly.

## Responsible use

This repository is published for defensive security research, education, remediation and coordinated vulnerability handling.

You may use the material to understand the documented behavior and to improve systems you own or are explicitly authorized to assess. You are responsible for obtaining permission before performing any security test and for complying with applicable laws, contracts and policies.

Do not use this material to:

- Access accounts, data or systems without authorization
- Disrupt services or exhaust resources on systems outside a controlled test environment
- Exfiltrate, modify or destroy data
- Bypass access controls on systems you do not own or have permission to assess
- Deploy or adapt PoCs for attacks against third parties

If you believe you have identified an issue in a live system, stop testing, preserve only the minimum evidence necessary, and report it through an authorized disclosure channel.

## Legal disclaimer

**Use at your own risk. For authorized defensive research and educational purposes only.**

The materials in this repository are provided **“AS IS” and “AS AVAILABLE”**, without warranties or guarantees of any kind, whether express or implied, to the maximum extent permitted by applicable law. This includes, without limitation, warranties of accuracy, completeness, fitness for a particular purpose and non-infringement.

The authors and contributors make no representation that the documented findings are exhaustive, current, independently verified, exploitable in a particular deployment or applicable to every version or configuration of the referenced software.

The authors and contributors are not responsible for misuse of the information, unauthorized testing, damage to systems, loss of data, service interruption, legal consequences or other direct or indirect losses arising from use of this repository, to the extent permitted by applicable law.

**No permission or license to access, test, attack or interfere with naser.solutions or any other third-party system is granted by publication of this repository.** Any testing requires explicit authorization from the relevant system owner.

Nothing in this disclaimer excludes or limits liability where such exclusion or limitation is prohibited by law. This statement is not legal advice and does not replace applicable laws, contractual obligations or a formal authorization to test.

## Disclosure and remediation

If you are responsible for an affected system, use the technical details to assess exposure and prioritize remediation. Coordinate sensitive details privately with the relevant system owner before broad public disclosure whenever appropriate.

Do not submit secrets, personal data, customer information or exploitable details of a live third-party system in public issues.

For corrections to this repository, open a GitHub issue or submit a pull request. Please include the relevant finding ID and supporting, non-sensitive evidence.

## Repository integrity

- Findings should retain stable IDs across revisions and translations.
- Evidence must be distinguished from assumptions and researcher interpretation.
- PoCs must remain safe-by-default and local-only.
- False positives and limitations must remain documented.
- No credentials, tokens, private keys, personal data or production secrets should be committed.
- Severity changes should include a written rationale.

## Contributing

Contributions that improve technical accuracy, reproducibility, translation quality or remediation guidance are welcome.

Before submitting a contribution:

1. Do not include secrets or personal data.
2. Reproduce tests only in an environment you own or are authorized to use.
3. Include exact versions, prerequisites and expected versus observed results.
4. Separate verified evidence from assumptions.
5. Explain changes to severity or CVSS scoring.
6. Keep EN, DE and RU versions technically consistent.

## Contact and reporting

For repository corrections, use [GitHub Issues](https://github.com/GotUrBack-Public/ZeroDay-Library-naser.solutions-23.11.2026/issues).

Do not use public issues to disclose credentials, private data or details that would enable attacks against a live system.

---

<div align="center">

**Security research should be reproducible, evidence-based and responsible.**

<sub>ZeroDay Library · naser.solutions · Research documentation</sub>

</div>
