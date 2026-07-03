# XwkOnt Core Ontology Release Notes

> **Milestone:** First core ontology publication package — `ontology-core-v0.1.0`  
> **Date:** 2026-07-01 (package assembled); 2026-07-03 (tagged)  
> **Status:** Tagged and live; immutable versioned ontology document IRIs remain deferred

## Summary

This milestone packages the current XwkOnt core ontology scaffold for first publication-oriented review. It consolidates the core ontology, glossary, axiom, validation, governance, and publication-operations work into a navigable release package and operational pre-tag posture.

XwkOnt remains a crosswalk project, not a new foundational ontology.

## Included Artifacts

- Core ontology specification: `docs/ontology/core-ontology.md`
- Closed glossary: `docs/ontology/core-glossary.md`
- Conservative axiom notes: `docs/ontology/core-axioms.md`
- Competency questions: `docs/ontology/core-competency-questions.md`
- Validation report: `docs/ontology/core-validation.md`
- Diagram sources: `docs/ontology/core-ontology.mmd`, `docs/ontology/core-glossary-dependencies.mmd`
- Turtle vocabulary companion: `data/ontology/core.ttl`
- Illustrative validation examples: `data/ontology/examples/core-validation-example.ttl`
- Publication guide: `docs/publication/core-publication-guide.md`
- URI/IRI policy: `docs/publication/uri-iri-policy.md`
- Publication validation commands: `docs/publication/validation-commands.md`
- Publication operations guide: `docs/publication/publication-operations.md`
- Redirect/content-negotiation policy: `docs/publication/redirects-content-negotiation.md`
- Release tagging checklist: `docs/publication/release-tagging-checklist.md`

## Namespace Posture

The milestone adopts the target public namespace:

```text
https://w3id.org/xwkont/core#
```

Illustrative examples use:

```text
https://w3id.org/xwkont/examples/core-validation#
```

`ontology-core-v0.1.0` satisfies most of the immutable-versioned-IRI prerequisites in `docs/governance/release-versioning-policy.md` (release tag, matching artifact bundle, current-namespace redirect and content-negotiation, validation results). It does not yet satisfy the prerequisite that a `w3id.org` redirect exist for the versioned document path itself: `https://w3id.org/xwkont/ontology/core/0.1.0` currently returns `404` (checked 2026-07-03), since only the current-namespace redirects (`perma-id/w3id.org#6277`, `#6292`) have been submitted so far. Activating immutable versioned IRIs therefore remains deferred — filing and waiting on a third w3id PR is explicitly not planned for this session, immediately after `#6292` merged.


## External w3id Submission Status

Two external w3id change requests were submitted and merged:

- `perma-id/w3id.org#6277` ("Add xwkont namespace"), merged 2026-07-02, adding `xwkont/.htaccess` with a temporary (302) redirect from `https://w3id.org/xwkont` to `https://github.com/xwkont`. Verified live 2026-07-02 with a real `curl` (`302` to `https://github.com/xwkont`).
- `perma-id/w3id.org#6292` ("Add xwkont /core content-negotiation redirect"), merged 2026-07-03, adding content-negotiation rules for `https://w3id.org/xwkont/core`.

The public `xwkont/xwkont` repository is live and populated as a curated export of this repository (see `docs/publication/public-repository-curation-plan.md`). Both redirect paths are now verified deployed — see Content-Negotiation Verification below.

## Content-Negotiation Verification

Verified 2026-07-03 with live `curl` checks against the deployed w3id redirect (`perma-id/w3id.org#6292`, merged 2026-07-03T12:24:50Z):

- `curl -sI -L "https://w3id.org/xwkont/core"` (default `Accept`) → `302` → `https://github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.md` (human-readable documentation), final response `200`.
- `curl -sI -L -H "Accept: text/turtle" "https://w3id.org/xwkont/core"` → `302` → `https://raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl` (Turtle vocabulary), final response `200`.

Both retrieval paths behave as specified in `docs/publication/redirects-content-negotiation.md`.

## Validation Posture

Publication-time validation is intentionally minimal:

- Check repository cleanliness before final publication.
- Parse Turtle files with RDFLib when available.
- Run a dependency-free structural fallback check when RDFLib is unavailable.
- Confirm required publication artifacts exist.

No OWL reasoner is required for this milestone.

## Known Limitations

- No source-ontology correspondences are introduced.
- Example data is illustrative and non-authoritative.
- `xwkont-core:mapsTo` remains transitional and has no RDFS domain or range.
- Full mapping-record guidance and SKOS mapping-property usage guidance are deferred.
- Process/Event boundaries remain unresolved.
- Dependency subtypes remain unresolved.
- Inverse-property, disjointness, cardinality, transitivity, and other property-characteristic axioms remain deferred.
- Versioned release distribution files are not created as part of this milestone.
- Immutable versioned ontology document IRIs (`https://w3id.org/xwkont/ontology/core/0.1.0`) are not yet active — no w3id redirect exists for that path.

## Compatibility Notes

The Turtle namespace changed from the earlier placeholder `https://example.org/xwkont/` base to the target public `https://w3id.org/xwkont/` base. This is a publication preparation change, not a source-ontology semantic change.

## Follow-Up

`ontology-core-v0.1.0` is tagged and pushed to both the private and public repositories. All release-tagging-checklist items are complete — see `docs/publication/release-tagging-checklist.md`.

Remaining, deferred (not scheduled for this session):

1. Decide whether to submit a third w3id PR adding a redirect for the versioned document path (`https://w3id.org/xwkont/ontology/core/0.1.0`) — the last unmet prerequisite for activating immutable versioned ontology document IRIs per `docs/governance/release-versioning-policy.md`.
