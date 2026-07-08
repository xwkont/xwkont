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

**Reused for `time.md` (2026-07-04):** the same `bfo-core.ttl` was fetched again and read directly to verify the full temporal-region hierarchy: `BFO_0000008` (temporal region, "an occurrent over which processes can unfold"), splitting into `BFO_0000038` (one-dimensional temporal region) and `BFO_0000148` (zero-dimensional temporal region, mutually `owl:disjointWith`), each specialized further by `BFO_0000202` (temporal interval, "continuous, thus without gaps or breaks") and `BFO_0000203` (temporal instant, "has no proper temporal part") respectively. `temporal region` is explicitly enumerated as a subclass of occurrent (`BFO_0000003`) in the same elucidation that defines occurrent itself. No standalone philosophical-grounding essay for Time found in this file (BFO's elucidations are terse, non-argued glosses throughout, consistent with the rest of this record). See `time.md`'s Source Definitions and correspondence row 001.

**Reused for `list-sequence.md` (2026-07-07):** the same `21838-2/owl/bfo-core.ttl` was re-fetched and directly grepped for "list," "sequence," "tuple," and "ordered." Found only one informal use of "sequence," inside an Information Content Entity `skos:example` ("the sequence of this protein molecule"), not a dedicated ordered-collection class. Recorded as a scoped absence. See `list-sequence.md`'s Source Definitions.

**Reused for `continuous-discrete.md` (2026-07-07):** the same `21838-2/owl/bfo-core.ttl` was re-fetched and grepped for "continuous," "discrete," "gunky," and "granular." Found exactly two hits, both incidental wording inside unrelated elucidations: `fiat line` ("a one-dimensional continuant fiat boundary that is continuous") and `temporal interval` ("continuous, thus without gaps or breaks"). No dedicated continuous/discrete class or axis exists in this file. Confirms the crosswalk's draft finding exactly. See `continuous-discrete.md`'s Source Definitions.

**Reused for `modality.md` (2026-07-07):** the same `21838-2/owl/bfo-core.ttl` was re-fetched and grepped directly for "modal," "modality," "necessity," "possibility," "necessary," "possible," "deontic," and "alethic." Zero hits for any of the eight terms. Confirms the crosswalk's finding of a clean absence exactly. See `modality.md`'s Source Definitions.

**Reused for `non-physical-social-object.md` (2026-07-07, session-048):** the same `21838-2/owl/bfo-core.ttl` was re-fetched (note: `master`-branch `src/owl/bfo-core.ttl` 404s; the correct path is `21838-2/owl/bfo-core.ttl` at the repository root, as recorded in every prior reuse note above) and used to confirm `generically dependent continuant` (`BFO_0000031`) and `immaterial entity`. This corrected a citation-fidelity defect in the Codex draft: its correspondence table cited `BFO_0000142` for "immaterial entity," but that IRI is actually `bfo-core.ttl`'s "fiat line" class. The correct IRI for "immaterial entity" is `BFO_0000141` ("b is an immaterial entity =Def b is an independent continuant which is such that there is no time t when it has a material entity as continuant part"). See `non-physical-social-object.md`'s Source Definitions and correspondence row 002.

**Reused for `symbol-sign-representation.md` (2026-07-07, session-049):** the same `21838-2/owl/bfo-core.ttl` was re-fetched and grepped directly for "symbol," "sign," "signifier," "representation," "name," and "word." All hits were incidental uses inside unrelated `skos:scopeNote`/`skos:definition` text (e.g. "more sophisticated representations of time"), not a dedicated sign/symbol/representation class. Confirms the crosswalk's draft finding of a clean absence exactly. See `symbol-sign-representation.md`'s Source Definitions.
