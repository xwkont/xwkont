# XwkOnt URI/IRI Publication Policy

> **Status:** Publication baseline  
> **Date:** 2026-07-01  
> **Scope:** Current core ontology artifacts and illustrative validation examples

## Purpose

This policy defines the publication posture for XwkOnt ontology identifiers. It supports the first publication-oriented core ontology package while preserving XwkOnt's repository-first, source-first, traceability, and neutrality principles.

XwkOnt is not a new foundational ontology. The identifiers below identify XwkOnt comparison scaffolding, documentation artifacts, and illustrative examples. They do not assert that source ontologies share the same categories, commitments, or correspondences.

## Policy Summary

| Identifier area | Policy |
|---|---|
| Public project base | `https://w3id.org/xwkont/` |
| Current core ontology namespace | `https://w3id.org/xwkont/core#` |
| Current illustrative example namespace | `https://w3id.org/xwkont/examples/core-validation#` |
| Versioned ontology document path | Deferred until the first externally tagged release requires immutable distribution files. |
| Repository-local identifiers | Continue to use `xwkont:*` local identifiers as defined by the information architecture. |

## Namespace Rules

The current core ontology namespace is:

```text
https://w3id.org/xwkont/core#
```

Terms in `data/ontology/core.ttl` use hash IRIs in that namespace, for example:

```text
https://w3id.org/xwkont/core#Entity
https://w3id.org/xwkont/core#mapsTo
```

The current example namespace is:

```text
https://w3id.org/xwkont/examples/core-validation#
```

Example IRIs are explicitly non-authoritative. They are allowed only for validation examples, tutorials, tests, and explanatory documentation.

## Versioning Posture

This policy defines stable current namespaces but defers immutable versioned ontology documents. The deferral is intentional because:

1. The current core ontology remains a conservative comparison scaffold, not a finalized public standard.
2. No repository release tag exists yet for the core ontology milestone.
3. Governance and semantic-versioning policy are addressed separately (`docs/governance/release-versioning-policy.md`).
4. Creating versioned distribution IRIs before redirect and release-tag procedures exist would introduce a false stability signal.

Until a later release policy supersedes this document:

- The current namespace identifies the latest accepted repository version of the core ontology scaffold.
- Release notes identify the exact repository artifacts included in the milestone.
- Future governance work should define immutable version paths, redirect behavior, content negotiation expectations, and deprecation rules.

## Persistence and Dereferenceability

`https://w3id.org/xwkont/` is the target persistent public base for XwkOnt. Before external publication that advertises dereferenceable IRIs, maintainers should configure redirects from the persistent base to the repository's published documentation and Turtle artifacts.

Until redirects are configured, these IRIs are publication targets and stable identifiers, not guaranteed dereferenceable web resources.

## Local Identifier Relationship

Repository-local identifiers such as `xwkont:concept:continuant` remain local project identifiers, not web IRIs. They may later be mapped to public IRIs, but local identifier semantics do not change under this policy.

## Mapping Identifier Guidance

This policy does not introduce a new mapping-record identifier scheme. Detailed crosswalk mapping records remain governed by the existing information architecture patterns until a later mapping-record policy is created.

## Non-Commitments

This policy does not:

- Adopt OWL as the default modeling layer.
- Introduce source-ontology correspondences.
- Make examples authoritative evidence.
- Finalize semantic versioning.
- Define source ontology term IRIs.
- Resolve Process/Event, dependency, inverse-property, disjointness, cardinality, or transitivity questions.
