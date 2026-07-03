# Changelog

<!-- updated at: 2026-07-03 12:57 Z   (2026-07-03 08:57 EDT) -->

All notable changes to XwkOnt are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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

[0.1.0]: https://github.com/xwkont/xwkont/releases/tag/ontology-core-v0.1.0
