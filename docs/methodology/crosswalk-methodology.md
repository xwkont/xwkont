# Crosswalk Methodology

> **Status:** Accepted, in active use; mapping-record fields amended by `ADR-0009`; confidence vocabulary extended by `ADR-0013`; numeric export projection defined by `ADR-0014`  
> **Date:** 2026-06-30 (mapping fields amended 2026-07-01; confidence vocabulary extended 2026-07-01; numeric export projection defined 2026-07-01)  
> **Related specification:** `docs/INFORMATION_ARCHITECTURE.md`

## Purpose

This method guides human review of concept crosswalks. It favors conservative, evidence-linked mapping assertions over unsupported equivalence claims.

## Mapping Categories

Per `ADR-0009`, each mapping assertion records both its XwkOnt category and, where one exists, an explicit SSSOM-compatible `predicate_id`.

| Category | SKOS candidate | `predicate_id` (ADR-0009) | Use |
|---|---|---|---|
| `exact-equivalence-candidate` | `skos:exactMatch` | `skos:exactMatch` | Use only when the compared concepts appear interchangeable in the stated scope and source evidence does not reveal material differences. |
| `close-match` | `skos:closeMatch` | `skos:closeMatch` | Use when concepts are similar enough to align for many purposes but differ in scope, axioms, usage, or context. |
| `broader-than` | `skos:broadMatch` or inverse note | `skos:broadMatch` | Use when the subject is narrower than the object, or document direction explicitly. |
| `narrower-than` | `skos:narrowMatch` or inverse note | `skos:narrowMatch` | Use when the subject is broader than the object, or document direction explicitly. |
| `related` | `skos:relatedMatch` | `skos:relatedMatch` | Use for non-hierarchical semantic association. |
| `overlap` | none | none (XwkOnt extension) | Use when concepts partially intersect but neither subsumes the other. |
| `incompatible` | none | none (XwkOnt extension) | Use when source modeling commitments conflict in the scoped comparison. |
| `unknown` | none | none (XwkOnt extension) | Use when evidence is insufficient. |
| `explicit-non-equivalence` | none | none (XwkOnt extension) | Use to prevent accidental equivalence claims. |

## Evidence, Confidence, and Justification

Confidence values are `high`, `medium-high`, `medium`, `low-medium`, `low`, and `unknown` (retained as categorical per `ADR-0009`, not SSSOM's numeric 0.0-1.0 scale; extended with the two intermediate values by `ADR-0013`). Each confidence value should be accompanied by rationale and references. A high-confidence assertion can still be scoped, provisional, or later superseded.

`medium-high` and `low-medium` are reserved for a specific case, per `ADR-0013`: a confidence shift driven by a *sourcing* change (e.g., a claim moved from secondary-sourced to independently primary-source-verified) without the underlying substantive/metaphysical judgment moving a full category. They are not a general-purpose hedge between two values — every use must state, in the mapping's `rationale`, why the full adjacent category was not reached.

For machine-readable (SSSOM/TSV) export, `ADR-0014` defines a **fixed** numeric projection of these categories — contributors never pick a number by hand, and no crosswalk content records one:

| Category | Numeric projection |
|---|---|
| `high` | `1.0` |
| `medium-high` | `0.8` |
| `medium` | `0.6` |
| `low-medium` | `0.4` |
| `low` | `0.2` |
| `unknown` | omitted from export (not `0.0` — see `ADR-0014`) |

Per `ADR-0009`, each mapping assertion also records a `mapping_justification` value from the SEMAPV vocabulary (e.g., `semapv:ManualMappingCuration`, `semapv:LexicalMatching`, `semapv:LogicalReasoning`, `semapv:MappingReview`), recording *how* the mapping was derived. This is distinct from `rationale`, which records *why* it's believed correct, in prose. XwkOnt's mapping assertions are expected to be manually curated from cited source evidence, so `semapv:ManualMappingCuration` will be the common case.

## Claim Typing

Crosswalk prose distinguishes direct quotation, paraphrase, editorial observation, and inference. Inferences should explain the evidence chain and identify uncertainty.

## Neutrality Rules

XwkOnt compares source concepts and records mapping candidates. It does not resolve foundational-ontology disagreements by creating a new preferred ontology, and it does not assert equivalence merely because labels resemble each other.
