# XwkOnt

<!-- updated at: 2026-07-05 16:55 Z   (2026-07-05 12:55 EDT) -->

> **The Crosswalk of Foundational Ontologies**

XwkOnt is an open reference project whose sole purpose is to build a concept-centric crosswalk across a defined set of foundational (upper) ontologies (currently eight — see [ADR-0015](docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md)).

> **XwkOnt is not another foundational ontology.**
>
> It documents, compares, and connects existing foundational ontologies.

## Goal

Create a crosswalk that helps people understand how the same concept is represented across multiple foundational ontologies.

Users begin with a concept (for example, **Object**, **Event**, **Role**, **Process**, or **Quality**) and discover how each ontology defines, classifies, and relates that concept.

## Why "Concept"?

XwkOnt organizes its crosswalk around **Concepts** — neutral, cross-source comparison points (in the sense of ISO 1087 and SKOS: a unit of thought, not itself a real, instantiated class) — even though most of the 8 source ontologies use some form of "category" for their own top-level notion (DOLCE, SUMO, GFO, YAMATO, and GUM self-describe it directly; BFO and TUpper inherit "Category" from their governing standard, ISO/IEC 21838-1 §3.19; only UFO has no traceable term). That word names what a given source ontology calls *its own* general, domain-neutral class — BFO's `role`, DOLCE's `physical-object` — not XwkOnt's cross-source pivot. Reusing it for XwkOnt's own pivot would risk suggesting XwkOnt asserts its own top-level category system, which is exactly what it does not do (see above). "Concept," because no source ontology uses it for itself, signals the opposite: a neutral reference sitting alongside the 8 sources, not a 9th competitor among them — the same role `skos:Concept` already plays in library/information-science cross-referencing practice (e.g. Getty AAT, LCSH). See [ADR-0011](docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md) and [ADR-0019](docs/adr/ADR-0019-reinforce-concept-against-practitioner-usage.md) for the full investigation, including the ontology-alignment and meta-ontology literature this was checked against.

## Scope

XwkOnt focuses on:

- Crosswalking foundational ontologies.
- Comparing concepts across ontologies.
- Recording authoritative definitions.
- Documenting semantic correspondences.
- Citing authoritative references.
- Explaining similarities and differences.

XwkOnt does **not**:

- Create a new foundational ontology.
- Replace existing ontologies.
- Reconcile philosophical disagreements.
- Introduce new domain concepts.

## Related Prior Art

XwkOnt is not the first attempt at comparing foundational ontologies side by side. The closest historical predecessors are the **WonderWeb Foundational Ontologies Library (WFOL)** (DOLCE, OCHRE, BFO; produced under a fixed-term EU research grant, 2002–2004) and **ROMULUS** (BFO, DOLCE, GFO; a repository with comparison, alignment, and merging tooling, dormant since around 2014). Both are inactive; neither states an explicit license for its ontology files. See [docs/evaluations/comparable-projects-survey.md](docs/evaluations/comparable-projects-survey.md) for the full verification and comparison against XwkOnt's scope and non-goals.

## Guiding Principle

**Reuse Before Introduce**

Whenever practical, XwkOnt adopts existing standards, specifications, repository patterns, and accepted practices before introducing project-specific conventions.

Decision order:

1. Reuse
2. Reference
3. Adapt
4. Introduce (last resort)

## Project Status

The project has completed its first **core ontology publication package**, a public-IRI redirect implementation posture, and two full rounds of **concept crosswalk content**.

**All 17 planned concept crosswalks** — the original 8 (Continuant/Occurrent, Object, Event, Process, Quality, Role, Relation, Information Artifact) plus the `0.2.0` batch of 9 (Time, Spatial Region/Space, Abstract/Concrete, Quantity/Amount of Matter, Situation/State of Affairs, Universal/Type, Mereology/Parthood/Aggregate, Boundary/Site, Proposition/Content) — are complete and `reviewed`, each comparing all 8 source ontologies now in scope — BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, and GUM (see [ADR-0015](docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md)) — against directly-verified primary sources, not secondary summaries. Each of these 8 also classifies itself as a foundational/upper/top-level ontology — terms `ISO/IEC 21838-1:2021` §3.20 confirms are synonyms, not competing categories — either by third-party standardization (BFO, DOLCE, and TUpper are published as consecutive parts 2, 3, and 4 of the ISO/IEC 21838 "Top-Level Ontologies" family) or by their own chosen name (SUMO's "Upper," UFO's "Foundational," GFO's "Formal," YAMATO's "Top-level," GUM's "Upper"); see [ADR-0022](docs/adr/ADR-0022-reinforce-eight-source-scope-against-self-classification.md) for the full check. See [docs/crosswalks/concepts/](docs/crosswalks/concepts/) for the crosswalks themselves and [CHANGELOG.md](CHANGELOG.md) for release-level history. `core.ttl` placement (per [ADR-0021](docs/adr/ADR-0021-source-classified-core-placement-criterion.md)) is now done for 8 of the 9 newer concepts (Abstract/Concrete, Universal/Type, Time, Space, Mereology/Parthood/Aggregate, Boundary/Site, Quantity/Amount of Matter, Proposition/Content — 11 new classes, `core.ttl` now has 21); Situation/State of Affairs remains deliberately unplaced pending an unresolved sense-split concern (see `docs/ontology/core-ontology.md`'s Unresolved Modeling Questions).

Each `reviewed` crosswalk's Mapping Assertions are now also machine-readable: [`data/crosswalks/`](data/crosswalks/) holds an SSSOM-conformant TSV per concept, plus a generated RDF/Turtle mapping graph, both derived from the Markdown source (see [ADR-0023](docs/adr/ADR-0023-machine-readable-crosswalk-export-sssom-tsv-generated-ttl.md)). Looking ahead to a much larger candidate set (540 raw source-ontology classes triaged in [`docs/crosswalks/candidate-concepts.md`](docs/crosswalks/candidate-concepts.md)) and delegated, AI-agent-assisted authorship, [ADR-0024](docs/adr/ADR-0024-linkml-structured-source-of-truth-for-crosswalk-concepts.md) decided a further shift: a LinkML-schema-validated structured record becomes the source of truth for a crosswalk concept, with Markdown, TSV, and Turtle all generated from it. The schema ([`data/crosswalks/schema/crosswalk-concept.yaml`](data/crosswalks/schema/crosswalk-concept.yaml)) is now built and all 17 `reviewed` concepts have a validated YAML record (one per concept, under `data/crosswalks/<slug>/`, alongside its generated `.tsv`/`.ttl`). YAML is now the actual generation source: `docs/crosswalks/concepts/*.md` is a generated artifact (rendered from YAML, verified byte-for-byte against the prior hand-maintained Markdown), and the SSSOM/TSV and RDF/Turtle exports are generated directly from YAML rather than from Markdown (see [`docs/methodology/crosswalk-concept-linkml-schema.md`](docs/methodology/crosswalk-concept-linkml-schema.md)).

**Want to contribute a crosswalk?** [`docs/crosswalks/candidate-concepts.md`](docs/crosswalks/candidate-concepts.md) is the public backlog — pick a candidate and follow the process in [`docs/governance/contributing.md`](docs/governance/contributing.md).

Current infrastructure work provides a conservative RDF/RDFS/SKOS-compatible core ontology scaffold, publication guidance, URI/IRI policy, redirect/content-negotiation expectations, an external w3id implementation request, validation commands, release notes, and first milestone tagging checklist. XwkOnt remains a crosswalk project, not a new foundational ontology.

## Current Core Ontology Package

Publication-oriented core ontology materials are available at:

- [docs/publication/core-publication-guide.md](docs/publication/core-publication-guide.md)
- [docs/publication/uri-iri-policy.md](docs/publication/uri-iri-policy.md)
- [docs/publication/validation-commands.md](docs/publication/validation-commands.md)
- [docs/publication/publication-operations.md](docs/publication/publication-operations.md)
- [docs/publication/redirects-content-negotiation.md](docs/publication/redirects-content-negotiation.md)
- [docs/publication/release-tagging-checklist.md](docs/publication/release-tagging-checklist.md)
- [docs/publication/w3id-redirect-request.md](docs/publication/w3id-redirect-request.md)
- [docs/releases/core-ontology-release-notes.md](docs/releases/core-ontology-release-notes.md)
- [data/ontology/core.ttl](data/ontology/core.ttl)

## Governance and Maintenance

Project governance is documented in the `/docs` directory through:

- [Founding Principles](docs/FOUNDING_PRINCIPLES.md)
- [Architectural Principles](docs/ARCHITECTURAL_PRINCIPLES.md)
- [Editorial Policy](docs/EDITORIAL_POLICY.md)
- [Architecture Decision Records](docs/adr/) (ADR)
- [docs/governance/governance.md](docs/governance/governance.md)
- [docs/governance/contributing.md](docs/governance/contributing.md)
- [docs/governance/release-versioning-policy.md](docs/governance/release-versioning-policy.md)
- [docs/governance/change-management.md](docs/governance/change-management.md)

Current governance keeps XwkOnt repository-first and source-first. [docs/publication/w3id-redirect-request.md](docs/publication/w3id-redirect-request.md) documents the external w3id redirect request needed for minimal redirect and content-negotiation behavior, but public dereferenceability must not be advertised until deployed behavior is verified. Immutable versioned ontology document IRIs remain deferred until release tags, exact release artifacts, redirects, content-negotiation behavior, release notes, and validation results are ready.

### AI Assistance Disclosure

Consistent with this project's provenance principle (every artifact and claim is traceable — see [docs/EDITORIAL_POLICY.md](docs/EDITORIAL_POLICY.md)), XwkOnt discloses its use of AI tools:

- **Claude Code** (Anthropic) has been used throughout the project's history as an editorial and research assistant — drafting documentation, running primary-source verification passes, and performing self-reviews — always under the maintainer's direction and review, never as an unreviewed autonomous author. Crosswalk review-table entries individually disclose which review passes involved it.
- **OpenAI Codex** was used for a number of early-session implementation tasks (visible in this repository's git history as `codex/*`-named work).
- **ChatGPT** (OpenAI) produced one externally-sourced research document ([docs/evaluations/comparable-projects-survey.md](docs/evaluations/comparable-projects-survey.md)), pasted in by the maintainer and explicitly marked as unverified pending independent confirmation.

No claim about a source ontology is treated as final on an AI tool's output alone — all such claims are checked against primary sources per [docs/methodology/primary-source-verification.md](docs/methodology/primary-source-verification.md) before a crosswalk is marked `reviewed`.

## License

XwkOnt uses a dual license ([ADR-0008](docs/adr/ADR-0008-select-repository-license.md)):

- **Documentation, governance policy, ontology specification content, and RDF/Turtle vocabulary** (`docs/**`, `data/**`, root-level Markdown) — [CC BY 4.0](LICENSE) (`SPDX-License-Identifier: CC-BY-4.0`).
- **Code and tooling** (present or future, e.g. validation scripts) — [MIT](LICENSE-CODE) (`SPDX-License-Identifier: MIT`).

## Vision

Provide a useful reference for understanding concepts across the foundational ontologies in scope.

**One Concept. Multiple Ontologies. Clear Understanding.**