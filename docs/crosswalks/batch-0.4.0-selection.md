# Batch `0.4.0` — Concept Selection (No Drafting Yet)

<!-- updated at: 2026-07-10 12:30 Z   (2026-07-10 08:30 EDT) -->

> **Status:** Selected for admission; **not yet drafted or reviewed**  
> **Date:** 2026-07-10  
> **Governing rules:** [`ADR-0018`](../adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md), [`docs/methodology/crosswalk-runbook.md`](../methodology/crosswalk-runbook.md), [`docs/crosswalks/candidate-concepts.md`](candidate-concepts.md)

## Why a new selection pass

The original matrix-derived queue of 19 candidates is exhausted:

| Release | Concepts |
|---|---|
| `0.1.0` | 8 reviewed (original inventory) |
| `0.2.0` | +9 (≥3-source rung) |
| `0.3.0` | +9 reviewed, 1 off-ramped (Quality Space/Quale) |

`docs/crosswalks/candidate-concepts.md` still lists **540** source classes. Most remaining rows are either (a) already bucketed under one of the 26 reviewed concepts as sub-species, (b) Ungrouped linguistic/domain leaves flagged "likely NOT core", or (c) single-source Ungrouped terms. This pass does **not** draft crosswalks. It only admits the next batch by re-clustering evidence already visible in the public backlog.

## Admission method

Per `ADR-0018` and the `0.3.0` precedent:

1. Prefer multi-source themes whose classes are currently **scattered across existing reviewed buckets** (or left Ungrouped) rather than inventing labels with no source footprint.
2. Do **not** exclude a same-tier candidate on pre-verification "weakness" impressions (`crosswalk-runbook.md`).
3. Single- and two-source admissions remain allowed when the term is a source's own core/base concept (`ADR-0021` / runbook reviewed-eligibility), but this batch leads with ≥3-source clusters.
4. Off-ramp remains available later if Step 3 verification shows a source-side equivalence to an already-reviewed concept.

## Admitted batch (4 concepts)

| # | Working label | Provisional slug | Seed source count | Seed evidence (from `candidate-concepts.md` triage) | Why it is not already covered |
|---|---|---|---|---|---|
| 1 | Dependence / Dependent Entity | `dependence-dependent-entity` | ≥5 | BFO `independent` / `specifically dependent` / `generically dependent continuant`; GFO `Dependent` / `Independent`; YAMATO `dependent entity`, `specifically dependent`, `generically dependent`; UFO `externalDependence`; DOLCE `dependent-place` (adjacent) | Today these rows are split across Continuant-Occurrent, Quality, Information Artifact, and Boundary/Site. No dedicated crosswalk compares dependence as its own organizing distinction. |
| 2 | Material / Immaterial | `material-immaterial` | ≥4 | BFO `material entity` / `immaterial entity`; GFO `Material_*` family; TUpper `MaterialObject`; UFO `material`; GUM material-quality ascriptions (adjacent) | Materiality is currently folded into Object / Continuant-Occurrent / Boundary buckets. Several sources treat material/immaterial as a top-level partition, not merely an Object subtype. |
| 3 | Set / Class | `set-class` | ≥3 | SUMO `SetOrClass` / `Set` / `Class`; DOLCE `set`; GFO `Set`; GUM `UMSet` / `DisjunctiveSet` (OrderedSet already moved to List/Sequence) | Currently parked under Universal/Type, which focuses on type/kind/category. Extensional set/class collections are a recurring cross-source cluster that Universal/Type deliberately does not settle. |
| 4 | History | `history` | 2 | BFO `history`; GFO `History` | Both sit under Process today. A dedicated pass can test whether History is a distinct occurrent kind (BFO: history of a continuant) vs. ordinary Process — same two-source admission style used in `0.3.0`. |

## Explicitly not admitted this batch

| Cluster | Reason |
|---|---|
| Function | Already in scope of `disposition-capacity` (BFO `function` is an etiological disposition subtype there). |
| Feature | Three sources, but divergent senses (DOLCE feature → Boundary/Site; YAMATO feature → Quality; TUpper `ShapeFeature`). Needs a scoping spike before admission; not silently dropped — deferred. |
| Configuration | Largely covered by `situation-state-of-affairs` (GFO/GUM `Configuration*`). |
| Relator | Already treated inside `relation` (GFO/UFO relator evidence). |
| GUM Ungrouped linguistic leaves (~51) | Flagged "likely NOT core"; no cross-source counterpart pattern. |
| TUpper Ungrouped extrema (`Max`/`Min`/`ZEX`/…), SUMO `Graph`/`GraphElement`, GFO `Configuroid`/`Persistant`, YAMATO `substrate` | Single-source or not yet showing a multi-source cluster; remain Ungrouped for later triage. |
| Domain leaves (YAMATO living organism / chemical compound / morphological whole) | Explicitly "likely NOT core". |

## Provisional Feature spike (not in batch)

If a later session wants a fifth `0.4.0` slot, run a **scoping-only** check on Feature before drafting: confirm whether any source treats Feature as a first-class category independent of Boundary/Site and Quality. Until that check exists, Feature stays out of the admitted set.

## Next steps (when drafting begins)

For each admitted concept, follow `docs/methodology/crosswalk-runbook.md`:

1. Session branch from current `main`
2. Fetch/verify all 8 sources (do not trust this selection table as final source counts)
3. Off-ramp if a source-side equivalence to an existing reviewed concept appears
4. Draft in `_private/` → YAML SSOT → generate Markdown/TSV/TTL
5. Maintainer review → `core.ttl` placement per `ADR-0021` → glossary closure

No crosswalk YAML or Markdown for these four concepts is created by this document.

## References

- [`docs/crosswalks/candidate-concepts.md`](candidate-concepts.md)
- [`docs/adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md`](../adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md)
- [`docs/adr/ADR-0021-source-classified-core-placement-criterion.md`](../adr/ADR-0021-source-classified-core-placement-criterion.md)
- [`docs/methodology/crosswalk-runbook.md`](../methodology/crosswalk-runbook.md)
