# Towards a Standard Upper Ontology (SUMO)

> **Local reference identifier:** `xwkont:ref:sumo-niles-pease-2001`
> **Slug:** `sumo-niles-pease-2001`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-05`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Towards a Standard Upper Ontology | Foundational paper introducing SUMO (Suggested Upper Merged Ontology). |
| Creator | Ian Niles, Adam Pease | |
| Contributor | unknown | |
| Publisher | ACM (Proceedings of the 2nd International Conference on Formal Ontology in Information Systems, FOIS 2001) | |
| Source type | conference paper | |
| Version or edition | FOIS 2001, pp. 2-9 | SUMO has been substantially expanded since 2001 with a mid-level ontology and domain ontologies; this reference covers the original top-level structure only. |
| Identifier or URL | DOI: `10.1145/505168.505170` (<https://doi.org/10.1145/505168.505170>) | Per `ADR-0012`, DOI preferred over the ResearchGate mirror. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | DOI given above serves as the stable identifier; no separate archival snapshot needed per `ADR-0012`. | |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

SUMO has grown considerably since this 2001 paper (mid-level ontology, domain ontologies, ongoing maintenance at ontologyportal.org). This reference is cited specifically for the original top-level `Entity` → `Physical`/`Abstract` → `Object`/`Process` structure; a claim about current SUMO content beyond that top-level split should cite the current SUMO source files directly, not this paper alone.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Niles, I., & Pease, A. (2001). Towards a Standard Upper Ontology. In *Proceedings of the 2nd International Conference on Formal Ontology in Information Systems (FOIS 2001)*. Cited in `docs/crosswalks/concepts/continuant-occurrent.md` for SUMO's `Physical`/`Abstract` and `Object`/`Process` top-level distinctions, which this crosswalk treats as a lower-confidence structural analog to Continuant/Occurrent rather than a confirmed equivalent — SUMO's split is defined by physicality, not by temporal-persistence semantics, and this paper does not by itself confirm `Process`'s exact temporal semantics relative to BFO/DOLCE/UFO's Occurrent/Perdurant.

**Direct primary-source verification (2026-07-01):** current SUMO source (`Merge.kif`, `ontologyportal/sumo` GitHub repository, master branch — not this 2001 paper, which predates the current source structure) was fetched and read directly to verify `Object`, `Process`, `Attribute`, `Relation`, `SocialRole`, `ContentBearingPhysical`, and `ContentBearingObject` for `object.md`, `event.md`, `process.md`, `quality.md`, `role.md`, `relation.md`, and `information-artifact.md`. This corrected one claim (`information-artifact.md`: `ContentBearingPhysical` is a direct subclass of `Physical`, not nested under `Object` as originally drafted) and confirmed several others with exact quotations. One example ("Plumber" as a `SocialRole` subclass) was not found in `Merge.kif` and was removed from `role.md` as unverified rather than left uncorrected.

**Reused for `time.md` (2026-07-04):** the same `Merge.kif` was searched again, deeper into the `Abstract`/`Quantity` branch than any prior crosswalk pass had gone. Found `TimeMeasure` ("The class of temporal durations... and positions of TimePoints and TimeIntervals along the universal timeline"), subclass chain `Entity` → `Abstract` → `Quantity` → `PhysicalQuantity` → `ConstantQuantity` → `TimeMeasure` → `{TimeDuration, TimePosition}`, with `TimePosition` further `(partition TimePosition TimeInterval TimePoint)`. This corrects `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s SUMO ASCII tree and Observation 2, both of which stopped short of this branch and concluded SUMO had no Time category — a depth-of-search miss, not a real absence. Separately, `TemporalRelation` (`subclass TemporalRelation Relation`, `subclass TemporalRelation InheritableRelation`) reifies temporal *relations* (`before`, `BeginFn`, `EndFn`, `temporalPart`), a distinct piece of content already correctly filed under Relation in [`candidate-concepts.md`](../crosswalks/candidate-concepts.md). SUMO's Time content sits entirely on the **Abstract** side of its `Physical`/`Abstract` split, alongside mass/length quantities, not classified as an occurrent the way BFO/DOLCE/GFO's Time content is. See `time.md`'s Source Definitions and correspondence row 003, and its Uncertainty section for the matrix-correction note.

**Reused for `docs/methodology/source-ontology-module-conventions.md` (2026-07-05, resolving `ADR-0021`'s SUMO gap):** `Merge.kif` was fetched again and its header comment read directly: "The SUMO is a modular ontology. That is, the ontology is divided into self-contained subontologies." The GitHub repository (`ontologyportal/sumo`) confirms this structurally — dozens of separate domain `.kif` files (`Anatomy.kif`, `Cars.kif`, `Economy.kif`, `Food.kif`, etc.) alongside `Merge.kif` and `Mid-level-ontology.kif`. A direct text search of `Merge.kif` for "core" found no self-description of `Merge.kif` as SUMO's own "core" — only unrelated domain content (`AtomicNucleus`, `Virus`) and, in `CONTRIBUTING.md`, "core team" in a governance sense. SUMO's own terminology for its base tier is **"upper"/"meta-level,"** not "core" (per web-search-mediated secondary description, not independently re-verified against a primary SUMO-authored passage in this pass). SUMO therefore confirms the structural base/extension pattern (`Merge.kif` vs. domain `.kif` files) without confirming the specific word "core."
