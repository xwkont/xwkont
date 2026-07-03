# Basic Formal Ontology (BFO) 2020

> **Local reference identifier:** `xwkont:ref:bfo-2020`
> **Slug:** `bfo-2020`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Basic Formal Ontology (BFO) 2020 | Also standardized as ISO/IEC 21838-2:2021. |
| Creator | Barry Smith (lead); BFO Technical Committee | Multiple contributors; do not treat as a complete author list. |
| Contributor | unknown | Full ISO 21838-2 contributor list not verified in this pass. |
| Publisher | International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC); artifacts also hosted at basic-formal-ontology.org | Two distinct publication channels — see Source Relation Notes. |
| Source type | ontology specification / international standard | |
| Version or edition | BFO 2020; ISO/IEC 21838-2:2021 | |
| Identifier or URL | <https://www.iso.org/standard/74572.html>; <https://github.com/BFO-ontology/BFO-2020> | No DOI; ISO standards and GitHub repositories are not DOI-bearing. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | `https://basic-formal-ontology.org/BFO-2020/` → <http://web.archive.org/web/20240710202903/https://basic-formal-ontology.org/bfo-2020> (2024-07-10); `https://github.com/BFO-ontology/BFO-2020` → <http://web.archive.org/web/20260607064906/https://github.com/BFO-ontology/BFO-2020> (2026-06-07) | Both verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. |
| Rights/license | unknown (mixed) | The BFO-2020 GitHub repository states its OWL artifacts are available under a Creative Commons license per repository documentation, but this was not independently verified against the repository's LICENSE file in this pass. ISO/IEC 21838-2 itself is a purchasable ISO standard text with its own separate rights terms. Do not conflate the two. |

## Source Relation Notes

The GitHub repository `BFO-ontology/BFO-2020` publishes the same content standardized as ISO/IEC 21838-2:2021. The ISO standard text and the GitHub artifacts are related but distinct publications (different rights terms, potentially different formatting); cite the specific one actually consulted for a given claim.

## Rights and License Notes

Not fully verified in this pass — see Descriptive Metadata. Do not assert a specific SPDX license for either publication channel until the repository's LICENSE file or the ISO standard's rights terms are directly checked.

## Citation and Locator Notes

Recommended citation for the standard: ISO/IEC 21838-2:2021, *Information technology — Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)*. For the open artifacts: BFO-ontology/BFO-2020 GitHub repository, `http://basic-formal-ontology.org/BFO-2020/`. Cite the Continuant/Occurrent definitions used in `docs/crosswalks/concepts/continuant-occurrent.md` to the BFO 2020 specification's top-level class definitions.

**Direct primary-source verification (2026-07-01):** the actual OWL/TTL source (`21838-2/owl/bfo-core.ttl` in the `BFO-ontology/BFO-2020` GitHub repository, master branch) was fetched and read directly to verify exact definitions for `continuant-occurrent.md`, `object.md`, `event.md`, `process.md`, `quality.md`, `role.md`, and `relation.md`. This corrected one crosswalk claim (`event.md`: BFO_0000015 "process" carries `skos:altLabel "event"@en`, contradicting the earlier claim that BFO has no "Event" term at all) and confirmed several others with exact quotations, replacing secondary-source paraphrases. See each crosswalk's own Source Definitions table for the specific quotations and BFO class IRIs (e.g., BFO_0000015 process, BFO_0000019 quality, BFO_0000023 role, BFO_0000030 object, BFO_0000035 process boundary, BFO_0000145 relational quality).
