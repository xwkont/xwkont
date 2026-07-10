# Changelog

<!-- updated at: 2026-07-10 13:17 Z   (2026-07-10 09:17 EDT) -->

All notable changes to XwkOnt are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

> **Retracted: `ontology-core-v0.3.1` (tagged 2026-07-08, retracted the same day).** It was cut before `core.ttl` placement work already in flight (Symbol/Sign/Representation, Situation/State of Affairs) completed `0.3.0`'s own scope — those two concepts were the last ones left unplaced from the `0.2.0`/`0.3.0` batches. Rather than let a `0.3.1` exist that undersold what `0.3.0` was actually finishing, the tag was deleted (both the private repo and the public `xwkont/xwkont` repo) and `ontology-core-v0.3.0` was force-moved to the consolidated commit covering everything through `v0.3.1` plus the completed placements. **If anything pins `ontology-core-v0.3.1` by tag name, that tag no longer exists — re-pin to `ontology-core-v0.3.0`,** which is a superset (everything `v0.3.1` had, plus both placements). This is the first and only accepted historical exception to tag immutability; [docs/governance/release-versioning-policy.md](docs/governance/release-versioning-policy.md) now forbids repeating it — future incomplete cuts must ship as a new tag with CHANGELOG supersession, not a retag. The version number `0.3.1` is permanently retired as a live tag; the next patch after `0.3.0` is **`ontology-core-v0.3.2`**.

## [Unreleased]

## [0.3.2] - 2026-07-10

Tagged `ontology-core-v0.3.2`. Post-`0.3.0` stabilize and public-site milestone: no new reviewed crosswalks and no `core.ttl` class changes. Skips `0.3.1` as a live tag number because that name was retracted (see note above). The `0.4.0` concept batch is **selected only** here — drafting remains future work.

### Changed

- Release/versioning policy now commits to **published-tag immutability** after the `v0.3.1` retraction, with an explicit exception record for that one event ([docs/governance/release-versioning-policy.md](docs/governance/release-versioning-policy.md)).
- Public contribution backlog (`docs/crosswalks/candidate-concepts.md`) refreshed: intro no longer claims `0.3.0` `core.ttl` placement is pending; bucket labels for all 26 reviewed concepts drop the stale `(candidate)` suffix; public roadmap pointers prefer this file over unpublished `TODO.md`.
- Core ontology specification, glossary, and axiom notes advanced from `draft` to `reviewed`, matching the completed `0.3.0` placement and glossary-closure work (known limitations such as Process/Event remain documented, not erased).
- Stale open follow-ups in early crosswalk YAML (claims that Process/Event/Role/ADR-0015 buildouts were still pending) marked resolved and regenerated.

### Added

- `0.4.0` concept batch **selected** (not drafted): Dependence/Dependent Entity, Material/Immaterial, Set/Class, and History — see [docs/crosswalks/batch-0.4.0-selection.md](docs/crosswalks/batch-0.4.0-selection.md).
- Public documentation site via **Material for MkDocs** on GitHub Pages ([mkdocs.yml](mkdocs.yml), [.github/workflows/pages.yml](.github/workflows/pages.yml), [docs/publication/site-hosting.md](docs/publication/site-hosting.md)). Target URL: `https://xwkont.github.io/xwkont/`.
- w3id HTML retarget submitted as [`perma-id/w3id.org#6343`](https://github.com/perma-id/w3id.org/pull/6343): `/xwkont/` and HTML `/core` → Pages; Turtle `/core` unchanged.
- Interactive **Explore** views on the docs site: coverage matrix, mapping network, and interactive core hierarchy ([docs/explore/](docs/explore/)).

## [0.3.0] - 2026-07-08

Tagged `ontology-core-v0.3.0`. All 9 candidates from the `0.3.0` batch have now been through a crosswalk pass — 9 reviewed, 1 (Quality Space/Quale) off-ramped as not-distinct — bringing the total to 26 reviewed concepts, all of which now have `core.ttl` placement, completing every concept from both the `0.2.0` and `0.3.0` batches. (Originally split across `0.3.0`/`0.3.1` tags; consolidated into a single `0.3.0` release, since the placement work below completes rather than extends that batch's own scope.)

### Added

- 9 new concept crosswalks — Disposition/Capacity, Symbol/Sign/Representation, Mind/Conscious Being/Agent, Ontological Level/Stratum, Change, List/Sequence, Continuous vs. Discrete, Modality, and Non-physical/Social Object ([docs/crosswalks/concepts/](docs/crosswalks/concepts/)) — bringing the total to 26 reviewed concepts.
- `data/ontology/core.ttl` expanded from 21 to 32 classes: `Change`, `Continuous`, `Discrete`, `OntologicalLevelStratum`, and `ListSequence` as direct `Entity` subclasses; `MindConsciousBeingAgent`, `NonPhysicalObject`, and `Disposition` under `Continuant`; `Modality` under `Quality`; `SymbolSignRepresentation` under `Universal`, plus a new `symbolizes`/`symbolizedBy` relation pair, resolving that concept's own single-class-vs-class-plus-relation-family question; and `SituationStateOfAffairs` under `Continuant`, resolving `0.2.0`'s last remaining placement gap once its flagged three-way sense split was found to already be disentangled within the crosswalk's own reviewed content ([ADR-0021](docs/adr/ADR-0021-source-classified-core-placement-criterion.md)). No concept from either batch remains unplaced.
- `.tsv`/`.ttl` SSSOM/RDF exports for all 9 new concepts, generated from their YAML records ([ADR-0023](docs/adr/ADR-0023-machine-readable-crosswalk-export-sssom-tsv-generated-ttl.md)); all 26 reviewed concepts now have a machine-readable export.
- Closed glossary entries (`docs/ontology/core-glossary.md`) for all 20 `core.ttl` classes added across the `0.2.0` and `0.3.0` batches, deferred at both original placement passes.
- GUM `Name` added as new evidence to `information-artifact.md`, and GUM `NameEvent`'s `Configuration` branch added to `event.md`, resolving `symbol-sign-representation.md`'s two previously-unchecked Future Work items.
- Formal `xwkont:ref:*` reference records for ROMULUS and WFOL ([docs/references/](docs/references/)), the two closest historical predecessor projects `README.md`'s Related Prior Art section has cited since `0.1.0`.
- CI (`validate.yml`) now runs `linkml-validate` against every crosswalk YAML and `--check` mode for both export scripts, not just a manual local check.

### Fixed

- Regenerated `.tsv`/`.ttl` exports for 15 of the original 17 concepts, which had drifted out of sync with confidence-value corrections made in their own YAML during later review passes.
- Scrubbed dangling `_private/`-path/`SESSION-NNN` citations left in synced or sync-adjacent docs across several passes (`space.yaml`, `disposition-capacity.yaml`, `crosswalk-runbook.md`, `change.yaml`, `continuous-discrete.yaml`, and this repo's own review-notes working files).
- Independently re-verified four carried-over UFO/YAMATO absence-recheck claims (`change.md`, `continuous-discrete.md`, `list-sequence.md`, `non-physical-social-object.md`) against fresh or cached primary-source extractions.
- Fixed naming-drift bugs where mapping rows referenced `core.ttl` class names that were never actually placed, or a placeholder left over from before placement: `non-physical-social-object.md` (`NonPhysicalSocialObject` → `NonPhysicalObject`), `continuous-discrete.md` (`ContinuousDiscrete` → its real `Continuous`/`Discrete` split), and `situation-state-of-affairs.md` (`Situation (candidate)` → `SituationStateOfAffairs`).
- Corrected `docs/methodology/crosswalk-runbook.md`'s Step 4, which told contributors to hand-edit the generated `docs/crosswalks/concepts/` directory directly; now points to drafting in `_private/` first.
- Corrected stale `README.md`/`docs/crosswalks/concepts/README.md` claims about `core.ttl` placement completion that had outpaced the actual work at the time they were written.

## [0.2.0] - 2026-07-05

Tagged `ontology-core-v0.2.0`. All 17 planned concept crosswalks are now complete and reviewed.

### Added

- 9 new concept crosswalks — Time, Spatial Region/Space, Abstract/Concrete, Quantity/Amount of Matter, Situation/State of Affairs, Universal/Type, Mereology/Parthood/Aggregate, Boundary/Site, and Proposition/Content ([docs/crosswalks/concepts/](docs/crosswalks/concepts/)) — bringing the total to all 17 planned concepts, each reviewed against all 8 source ontologies.
- `data/ontology/core.ttl` expanded from 10 to 21 classes: `Abstract`, `Concrete`, `Universal`, `Time`, and `Space` as direct `Entity` subclasses; `Aggregate`, `Sum`, `Boundary`, and `Site` under `Continuant`; `Quantity` under `Concrete`; `Proposition` under `Abstract` ([ADR-0021](docs/adr/ADR-0021-source-classified-core-placement-criterion.md)).
- A LinkML-schema-validated YAML record per crosswalk concept ([data/crosswalks/schema/crosswalk-concept.yaml](data/crosswalks/schema/crosswalk-concept.yaml)) is now the source of truth; Markdown, SSSOM/TSV, and RDF/Turtle mapping exports are generated from it directly, nested under `data/crosswalks/<slug>/` ([ADR-0023](docs/adr/ADR-0023-machine-readable-crosswalk-export-sssom-tsv-generated-ttl.md), [ADR-0024](docs/adr/ADR-0024-linkml-structured-source-of-truth-for-crosswalk-concepts.md)).
- [docs/crosswalks/candidate-concepts.md](docs/crosswalks/candidate-concepts.md): a public backlog of 540 candidate crosswalk concepts across all 8 sources, for anyone wanting to pick up a future crosswalk ([docs/governance/contributing.md](docs/governance/contributing.md)).
- 8 new Architecture Decision Records ([ADR-0017](docs/adr/ADR-0017-exclude-reality-as-a-crosswalk-concept.md) through [ADR-0024](docs/adr/ADR-0024-linkml-structured-source-of-truth-for-crosswalk-concepts.md)).
- New reference records for DOLCE's `ExtendedDnS` module and the OntoUML vocabulary ([docs/references/](docs/references/)), and a foundational-ontology concept-terms matrix evaluation ([docs/evaluations/foundational-ontology-concept-terms-matrix.md](docs/evaluations/foundational-ontology-concept-terms-matrix.md)).

## [0.1.0] - 2026-07-03

First tagged milestone, `ontology-core-v0.1.0`. See [docs/publication/release-tagging-checklist.md](docs/publication/release-tagging-checklist.md) for the completed pre-tag checklist and [docs/releases/core-ontology-release-notes.md](docs/releases/core-ontology-release-notes.md) for full release notes.

### Added

- Core ontology scaffold: a conservative RDF/RDFS/SKOS vocabulary ([data/ontology/core.ttl](data/ontology/core.ttl)) with specification, glossary, axiom notes, competency questions, and validation documentation ([docs/ontology/](docs/ontology/)).
- Concept crosswalks for all 8 planned concepts — Continuant/Occurrent, Object, Event, Process, Quality, Role, Relation, and Information Artifact ([docs/crosswalks/concepts/](docs/crosswalks/concepts/)) — each comparing 8 source ontologies (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM) against directly-verified primary sources.
- Source-ontology scope expanded from 4 to 8 ontologies ([ADR-0015](docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md)).
- Governance framework: Founding Principles, Architectural Principles, Editorial Policy, Project Lifecycle, and a numbered Architecture Decision Record series.
- Dual-license structure: CC BY 4.0 for documentation/ontology/vocabulary content, MIT for code and tooling ([ADR-0008](docs/adr/ADR-0008-select-repository-license.md)).
- Publication materials: URI/IRI policy, redirect and content-negotiation specification, validation commands, and a pre-tag release checklist ([docs/publication/](docs/publication/)).
- `https://w3id.org/xwkont/` and `https://w3id.org/xwkont/core` namespace redirects submitted and merged upstream (`perma-id/w3id.org#6277`, `perma-id/w3id.org#6292`), both verified live.
- GitHub community-health files: [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), issue and pull request templates.

[0.3.2]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.3.2
[0.3.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.3.0
[0.2.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.2.0
[0.1.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.1.0
