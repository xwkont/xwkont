# XwkOnt Publication Operations Guide

> **Status:** Publication-operations guide  
> **Date:** 2026-07-01  
> **Scope:** Operational posture for public IRI publication, release artifacts, and first ontology milestone preparation

## Purpose

This guide defines the practical publication operations posture for the current XwkOnt core ontology package, following the repository-first governance baseline.

XwkOnt remains repository-first. Repository files, release tags, release notes, and validation results are authoritative until public redirects and content negotiation are implemented and verified.

## Current Publication State

| Area | Current posture |
|---|---|
| Current core namespace | Active identifier namespace: `https://w3id.org/xwkont/core#`. |
| Current Turtle artifact | Repository artifact: `data/ontology/core.ttl`. |
| Human-readable core documentation | Repository artifact: `docs/ontology/core-ontology.md`. |
| Public IRI redirects | External w3id implementation request documented; not verified as deployed. |
| Content negotiation | Minimal HTML/Turtle behavior documented for external w3id request; not verified as deployed. |
| First ontology milestone tag | Not ready to create until redirect and content-negotiation behavior is implemented and validated. |
| Immutable versioned ontology document IRIs | Deferred; governance prerequisites are not yet complete. |
| Release artifact packaging | Defined as a minimal repository release bundle for the first external ontology milestone. |

## Operating Principles

Publication operations must preserve the existing project posture:

- XwkOnt is not a foundational ontology.
- The Git repository remains the Single Source of Truth.
- Authoritative source ontologies remain authoritative.
- Public identifiers identify XwkOnt comparison scaffolding, not source-ontology commitments.
- Example data is illustrative and non-authoritative.
- RDF and SKOS remain adopted standards; RDFS remains adapted lightweight vocabulary semantics.
- OWL is not the default modeling layer.
- `xwkont-core:mapsTo` must not regain formal RDFS domain or range commitments.

## Publication Workflow

Before advertising public dereferenceability, maintainers should complete this sequence:

1. Confirm repository cleanliness.
2. Run publication validation commands.
3. Submit the external `w3id.org` redirect request documented in `docs/publication/w3id-redirect-request.md`.
4. Verify HTML and Turtle retrieval behavior using the policy in `docs/publication/redirects-content-negotiation.md`.
5. Record validation results in the release notes.
6. Prepare the first ontology milestone release bundle.
7. Create the ontology milestone tag only after the checked repository state is accepted.

## Current Namespace Relationship

The current namespace is:

```text
https://w3id.org/xwkont/core#
```

It is the stable current term namespace for core terms such as:

```text
https://w3id.org/xwkont/core#Entity
https://w3id.org/xwkont/core#mapsTo
```

Because this is a hash namespace, retrieval of the namespace document occurs at the fragmentless IRI:

```text
https://w3id.org/xwkont/core
```

The current namespace identifies current core terms. It is not an immutable version snapshot.

## Future Versioned Document IRI Relationship

The governance baseline reserved this future pattern:

```text
https://w3id.org/xwkont/ontology/core/MAJOR.MINOR.PATCH
```

That pattern remains inactive. It must not be advertised as dereferenceable or immutable until all prerequisites in `docs/governance/release-versioning-policy.md` are satisfied.

When activated, the versioned ontology document IRI should correspond exactly to a release tag and immutable release artifact bundle. The versioned document may identify versioned terms with fragment identifiers, for example:

```text
https://w3id.org/xwkont/ontology/core/0.1.0#Entity
```

This example is reserved pattern documentation only; it is not active publication.

## Release Tags and Release Notes

Repository release tags identify accepted repository states. Ontology release tags should follow:

```text
ontology-core-vMAJOR.MINOR.PATCH
```

The expected first external ontology milestone tag is:

```text
ontology-core-v0.1.0
```

The tag must not be created until the checklist in `docs/publication/release-tagging-checklist.md` is complete.

Release notes must identify:

- the tag;
- the included Turtle artifact;
- included human-readable documentation;
- validation commands and results;
- known limitations;
- redirect and content-negotiation status;
- whether immutable versioned ontology document IRIs are active or deferred.

## Minimal Release Bundle

The first external ontology milestone should include these repository artifacts at minimum:

| Artifact | Role |
|---|---|
| `data/ontology/core.ttl` | Machine-readable current core vocabulary companion. |
| `docs/ontology/core-ontology.md` | Human-readable core ontology specification. |
| `docs/ontology/core-glossary.md` | Closed glossary. |
| `docs/ontology/core-axioms.md` | Conservative axiom and non-axiom commitments. |
| `docs/ontology/core-competency-questions.md` | Competency-question documentation. |
| `docs/ontology/core-validation.md` | Validation report. |
| `docs/publication/core-publication-guide.md` | Publication guide. |
| `docs/publication/uri-iri-policy.md` | URI/IRI policy. |
| `docs/publication/redirects-content-negotiation.md` | Redirect and content-negotiation policy. |
| `docs/publication/w3id-redirect-request.md` | External w3id implementation request for the current namespace. |
| `docs/publication/validation-commands.md` | Publication validation commands. |
| `docs/publication/release-tagging-checklist.md` | Pre-tag checklist. |
| `docs/releases/core-ontology-release-notes.md` | Release notes. |

Illustrative examples may be included for validation context, but they must remain clearly non-authoritative.

## Deferred Activation Items

Immutable versioned ontology document IRIs remain deferred because the repository does not yet contain verified deployed redirects, verified content negotiation, an accepted ontology release tag, or validation results tied to that tag.

Redirect implementation must be submitted to external w3id infrastructure rather than implemented as an active configuration in this repository. The next operational step is to verify public redirects and content negotiation, then rerun final validation from a clean tree and prepare `ontology-core-v0.1.0`.
