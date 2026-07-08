# Changelog

<!-- updated at: 2026-07-08 02:15 Z   (2026-07-07 22:15 EDT) -->

All notable changes to XwkOnt are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.3.0] - 2026-07-07

Tagged `ontology-core-v0.3.0`. All 9 candidates from the `0.3.0` batch have now been through a crosswalk pass — 9 reviewed, 1 (Quality Space/Quale) off-ramped as not-distinct — bringing the total to 26 reviewed concepts.

### Added

- 9 new concept crosswalks — Disposition/Capacity, Symbol/Sign/Representation, Mind/Conscious Being/Agent, Ontological Level/Stratum, Change, List/Sequence, Continuous vs. Discrete, Modality, and Non-physical/Social Object ([docs/crosswalks/concepts/](docs/crosswalks/concepts/)) — bringing the total to 26 reviewed concepts.
- `data/ontology/core.ttl` expanded from 21 to 29 classes: `Change`, `Continuous`, `Discrete`, `OntologicalLevelStratum`, and `ListSequence` as direct `Entity` subclasses; `MindConsciousBeingAgent`, `NonPhysicalObject`, and `Disposition` under `Continuant`; `Modality` under `Quality` ([ADR-0021](docs/adr/ADR-0021-source-classified-core-placement-criterion.md)). Symbol/Sign/Representation was deliberately left unplaced pending an unresolved single-class-vs-class-plus-relation-family question, alongside `0.2.0`'s already-unplaced Situation/State of Affairs.
- `.tsv`/`.ttl` SSSOM/RDF exports for all 9 new concepts, generated from their YAML records ([ADR-0023](docs/adr/ADR-0023-machine-readable-crosswalk-export-sssom-tsv-generated-ttl.md)); all 26 reviewed concepts now have a machine-readable export.

### Fixed

- Regenerated `.tsv`/`.ttl` exports for 15 of the original 17 concepts, which had drifted out of sync with confidence-value corrections made in their own YAML during later review passes.

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

[0.2.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.2.0
[0.1.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.1.0
