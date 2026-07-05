# Changelog

<!-- updated at: 2026-07-05 17:35 Z   (2026-07-05 13:35 EDT) -->

All notable changes to XwkOnt are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
