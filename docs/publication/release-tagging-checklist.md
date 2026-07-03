# First Ontology Milestone Tagging Checklist

> **Status:** Complete — tag created  
> **Date:** 2026-07-01 (checklist opened); 2026-07-03 (tag created)  
> **Scope:** Pre-tag checklist for the first externally tagged XwkOnt core ontology milestone

## Decision

The first external ontology milestone tag was created 2026-07-03:

```text
ontology-core-v0.1.0
```

Public redirect and content-negotiation behavior were fully deployed and verified before the tag was created.

## Pre-Tag Checklist

Complete all items before creating `ontology-core-v0.1.0`.

### Repository and Governance

- [x] Working tree is clean before final release validation. Verified 2026-07-02: `git status --short` returns nothing.
- [x] No pending ADR is required for the release posture. Verified 2026-07-02: no open ADR gaps found for this release.
- [x] Release remains consistent with repository-first governance.
- [x] Release remains consistent with the URI/IRI policy.
- [x] Release remains consistent with the release-versioning policy.
- [x] Immutable versioned ontology document IRIs are still explicitly deferred (see `docs/releases/core-ontology-release-notes.md`, Namespace Posture).

### Publication Operations

- [x] `https://w3id.org/xwkont/` resolves to the project entry point or repository landing page. Verified 2026-07-02: `302` to `https://github.com/xwkont`.
- [x] `https://w3id.org/xwkont/core` supports Turtle retrieval for `data/ontology/core.ttl`. Verified 2026-07-03: `perma-id/w3id.org#6292` merged; `Accept: text/turtle` → `302` → `raw.githubusercontent.com/xwkont/xwkont/main/data/ontology/core.ttl`, final `200`.
- [x] `https://w3id.org/xwkont/core` supports HTML retrieval for human-readable core ontology documentation. Verified 2026-07-03: default `Accept` → `302` → `github.com/xwkont/xwkont/blob/main/docs/ontology/core-ontology.md`, final `200`.
- [x] Redirect and content-negotiation verification commands have been run and recorded. Both paths recorded in `docs/releases/core-ontology-release-notes.md`'s Content-Negotiation Verification section.
- [x] Documentation does not advertise dereferenceability beyond verified behavior.

### Artifact Bundle

- [x] `data/ontology/core.ttl` is included.
- [x] `docs/ontology/core-ontology.md` is included.
- [x] `docs/ontology/core-glossary.md` is included.
- [x] `docs/ontology/core-axioms.md` is included.
- [x] `docs/ontology/core-competency-questions.md` is included.
- [x] `docs/ontology/core-validation.md` is included.
- [x] `docs/publication/core-publication-guide.md` is included.
- [x] `docs/publication/uri-iri-policy.md` is included.
- [x] `docs/publication/redirects-content-negotiation.md` is included.
- [x] `docs/publication/validation-commands.md` is included.
- [x] `docs/releases/core-ontology-release-notes.md` identifies the tag, artifacts, validation results, and known limitations. Content-negotiation verification results and the created tag are both recorded 2026-07-03.

### Validation

- [x] `git status --short` returns no uncommitted files before release validation. Verified 2026-07-02.
- [x] Turtle artifacts parse with RDFLib, or the documented structural fallback is run and recorded. RDFLib unavailable in this environment; structural fallback run 2026-07-02, passed.
- [x] Navigation artifact checks pass. Verified 2026-07-02.
- [x] `xwkont-core:mapsTo` has no RDFS domain or range. Verified 2026-07-02 via structural fallback check.
- [x] Example data remains marked illustrative and non-authoritative. Verified 2026-07-02.

## Tag Command

The tag was created and pushed to both the private and public repositories 2026-07-03:

```bash
git tag ontology-core-v0.1.0
git push origin ontology-core-v0.1.0
```

A lightweight tag was used (no annotated release notes embedded in the tag object).

## Current Blockers

None remaining for this checklist — it is complete. `perma-id/w3id.org#6292` merged 2026-07-03T12:24:50Z; both Turtle and HTML retrieval for `https://w3id.org/xwkont/core` are verified live, and `ontology-core-v0.1.0` is tagged and pushed. Immutable versioned ontology document IRIs (`https://w3id.org/xwkont/ontology/core/0.1.0`) remain a separate, still-deferred decision — see `docs/governance/release-versioning-policy.md` and `TODO.md`; that path currently returns `404` and has no w3id redirect configured.
