# Raw-Class Inventory — Candidate Triage Toward Concepts

<!-- updated at: 2026-07-07 21:45 Z   (2026-07-07 17:45 EDT) -->

> **This is XwkOnt's public contribution backlog.** It enumerates every class in all 8 source ontologies, each tagged with its nearest existing XwkOnt bucket — a **candidate** for a future crosswalk concept. If you want to contribute a crosswalk, this is where to find one: pick a bucket below that isn't yet one of the 26 `reviewed` concepts in [`docs/crosswalks/concepts/`](concepts/), and follow the selection/sourcing/scoping/review process in [`docs/governance/contributing.md`](../governance/contributing.md). "Ungrouped" rows are not yet triaged into any bucket at all — flagging one you think deserves its own concept, with source-count evidence per `ADR-0018`, is itself a useful contribution.
>
> "Core" was dropped from this file's original name (`core-concepts.md`, 2026-07-04) pending a future pass that actually defines what would qualify a candidate as "core." **That pass is now done, in two ADRs: `docs/adr/ADR-0020-define-core-as-base-module-not-domain-tier.md` (2026-07-05) defines "core" as XwkOnt's base module (distinct from optional extension modules), not a domain-tier "core ontology" in the Scherp-et-al. sense; `docs/adr/ADR-0021-source-classified-core-placement-criterion.md` (2026-07-05) then sets the actual placement rule — a concept qualifies as XwkOnt-core if *any one* contributing source ontology classifies it as part of that source's own core/base module, no cross-source majority or popularity filter on top.** Applying `ADR-0021`'s rule to the 26 reviewed concepts is now mechanical, not judgment-based, but is still a separate, not-yet-started pass for the `0.3.0` batch's 9 newer concepts (it's already done for the original 17). Until it happens, this file continues to use only already-grounded vocabulary: a row is either a source's own **Concept Term** (`ADR-0011`/`ADR-0019`, e.g. BFO's `role`), a **candidate** if `ADR-0018`'s source-count threshold is met, or a real **Concept** once actually selected/sourced/scoped/reviewed (26 exist today, across `docs/crosswalks/concepts/` — the original 8, all 9 of the `0.2.0` batch (reviewed 2026-07-05), and all 10 of the `0.3.0` batch: Disposition/Capacity, Symbol/Sign/Representation, Mind/Conscious Being/Agent, Ontological Level/Stratum, Change, List/Sequence, Continuous vs. Discrete, Modality, and Non-physical/Social Object). Nothing here is placed into `core.ttl`'s base module or an extension module yet for the `0.3.0` batch's concepts.
>
> Enumerates every class exactly once verified against each of the 8 source ontologies' own primary artifact (re-fetched and parsed directly for this pass — the earlier draft relied on `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s simplified ASCII trees, which undercounted several sources badly). Every row is numbered `<ONTOLOGY>.<n>` and tagged with its nearest existing XwkOnt bucket (one of the 8 `reviewed` crosswalks, one of `TODO.md`'s 19 candidates, or **Ungrouped** if no existing bucket fits). **Ungrouped does not mean "will become its own concept"** — it means "not yet triaged," per `ADR-0018`'s process: every future concept still needs its own selection/sourcing/scoping/review pass, no matter how it's listed here.
>
> **Exact total: 540 classes** (36 + 37 + 60 + 56 + 77 + 44 + 37 + 193). No approximation — every count below was independently verified by direct fetch and parse of the source file, not estimated from a summary sketch. UFO's figure (56) includes its `AggregationKind` group (3 classes, `UFO.54`–`UFO.56`) — outside the original class-hierarchy matrix's stated scope for UFO (53), but enumerated below for completeness, so it's counted in this file's total. See "Corrections from the prior draft" below for what changed and why.

## Summary (exact)

| Source | Exact class count | Verification method |
|---|---|---|
| BFO 2020 | **36** | Direct OWL parse (rdflib + raw-tag grep, cross-checked, agree exactly) |
| DOLCE (Lite) | **37** | Direct OWL parse (rdflib + raw-tag grep, cross-checked, agree exactly) |
| SUMO | **60** | Direct `Merge.kif` parse, capped at 3 levels below `Entity` for comparability (SUMO's full taxonomy continues far deeper) |
| UFO / OntoUML | **56** (53 per the class-hierarchy matrix's original 4-group scope, +3 `AggregationKind` not previously scoped) | Direct Turtle parse, cross-checked against two independent sections of the file (declarative enum + individuals section), agree exactly |
| GFO | **77** | Direct OWL parse (regex over every `owl:Class` tag) |
| YAMATO | **44** | Direct visual inspection of rendered PDF Fig. 2 at up to 600 DPI (not OCR — diagram is a rasterized image) |
| TUpper | **37** | Direct OWL2-functional-in-XML parse (exact `Declaration`/`Class` block match) |
| GUM | **193** | Direct fetch (via `curl`, since WebFetch itself was blocked for this archive.org URL) and full RDF/XML parse |
| **Total** | **540** | — |

## Corrections from the prior draft

The prior draft used the class-hierarchy matrix's simplified ASCII trees, which are **illustrative sketches, not guaranteed-exhaustive flat lists**. Re-verification found:

- **BFO (34→36):** the tree's compressed notation `temporal region → zero-dimensional (→ temporal instant)` reads as one item but is actually 3 separate classes (`temporal region`, `zero-dimensional temporal region`, `temporal instant`); same for the one-dimensional/interval branch. Fixed by treating each arrow-target as its own row.
- **DOLCE (32→37):** found 5 previously-missing classes — `dependent-place`, `relevant-part` (children of `feature`, itself already listed), and `quale`/`quality-space`/`spatio-temporal-particular` (all three connected only via `owl:equivalentClass`, not `subClassOf`, so a subclass-chain-only tree misses them entirely).
- **SUMO (21→60):** the original sketch only went 1-2 levels deep and missed an entire top-level sibling (`PhysicalSystem`) and a whole branch (`SetOrClass` → `Class`/`Set`); re-verified to a consistent 3-level depth from `Entity`, matching the depth used for other sources.
- **UFO (53→53, +3 optional):** confirmed exact; found one additional group, `AggregationKind` (`composite`/`none`/`shared`), present in the file but outside the original matrix's stated 4-group scope — included here for completeness.
- **GFO (37→77):** the original tree only traced a subset of the base module; direct parse found 77 named classes, including 12 with genuine multiple inheritance.
- **YAMATO (43→44):** the tree's `stative → (process)` compressed notation dropped a sibling leaf, `stative_2`, confirmed present as its own distinct node in the rendered figure.
- **TUpper (16→37):** the original list only covered the core 4-way partition and its immediate children; missed 21 further classes in the file's mereotopology/measurement branches (`Max`, `MaxDim`, `Min`, `MinDim`, `ZEX`, `PointRegion`, `box`, `edge`, `mat`, `point`, `poly`, `ridge`, `surface`, `vertex`, `border`, `outer`, `amount`, `spatial_area`, `spatial_length`, `spatial_volume`).
- **GUM (35→193):** by far the largest correction — the original matrix only sketched GUM's top 3 branches (`Configuration`/`Element`/`MultiConfiguration`) near the root; the full model has 193 classes. GUM is the single biggest contributor to the total, and the large majority of its classes are fine-grained linguistic clause-type/quality distinctions, most already flagged "likely NOT core" in `TODO.md`.

---

## BFO 2020 (36 classes — `BFO.1`–`BFO.36`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| BFO.1 | entity | Continuant-Occurrent (root) |
| BFO.2 | continuant | Continuant-Occurrent |
| BFO.3 | occurrent | Continuant-Occurrent |
| BFO.4 | independent continuant | Continuant-Occurrent |
| BFO.5 | spatial region | Spatial Region / Space (candidate) |
| BFO.6 | temporal region | Time (candidate) |
| BFO.7 | two-dimensional spatial region | Spatial Region / Space (candidate) |
| BFO.8 | spatiotemporal region | Time / Spatial Region (candidate) |
| BFO.9 | process | Process |
| BFO.10 | disposition | Disposition / Capacity |
| BFO.11 | realizable entity | Role / Disposition |
| BFO.12 | zero-dimensional spatial region | Spatial Region / Space (candidate) |
| BFO.13 | quality | Quality |
| BFO.14 | specifically dependent continuant | Quality |
| BFO.15 | role | Role |
| BFO.16 | fiat object part | Mereology / Parthood / Aggregate (candidate) |
| BFO.17 | one-dimensional spatial region | Spatial Region / Space (candidate) |
| BFO.18 | object aggregate | Mereology / Parthood / Aggregate (candidate) |
| BFO.19 | three-dimensional spatial region | Spatial Region / Space (candidate) |
| BFO.20 | site | Boundary / Site (candidate) |
| BFO.21 | object | Object |
| BFO.22 | generically dependent continuant | Information Artifact / Abstract vs. Concrete (candidate) |
| BFO.23 | function | Disposition / Capacity |
| BFO.24 | process boundary | Boundary / Site (candidate) |
| BFO.25 | one-dimensional temporal region | Time (candidate) |
| BFO.26 | material entity | Object |
| BFO.27 | continuant fiat boundary | Boundary / Site (candidate) |
| BFO.28 | immaterial entity | Continuant-Occurrent |
| BFO.29 | fiat line | Boundary / Site (candidate) |
| BFO.30 | relational quality | Quality |
| BFO.31 | fiat surface | Boundary / Site (candidate) |
| BFO.32 | fiat point | Boundary / Site (candidate) |
| BFO.33 | zero-dimensional temporal region | Time (candidate) |
| BFO.34 | history | Process |
| BFO.35 | temporal interval | Time (candidate) |
| BFO.36 | temporal instant | Time (candidate) |

---

## DOLCE — Lite mirror (37 classes — `DOLCE.1`–`DOLCE.37`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| DOLCE.1 | abstract | Abstract vs. Concrete (candidate) |
| DOLCE.2 | abstract-quality | Quality |
| DOLCE.3 | abstract-region | Spatial Region / Space (candidate) |
| DOLCE.4 | accomplishment | Event |
| DOLCE.5 | achievement | Event |
| DOLCE.6 | amount-of-matter | Quantity / Amount of Matter (candidate) |
| DOLCE.7 | arbitrary-sum | Mereology / Parthood / Aggregate (candidate) |
| DOLCE.8 | dependent-place | Boundary / Site (candidate) |
| DOLCE.9 | endurant | Continuant-Occurrent |
| DOLCE.10 | event | Event |
| DOLCE.11 | feature | Boundary / Site (candidate) |
| DOLCE.12 | non-physical-endurant | Non-physical / Social Object (candidate) |
| DOLCE.13 | non-physical-object | Non-physical / Social Object (candidate) |
| DOLCE.14 | particular | Continuant-Occurrent (root) |
| DOLCE.15 | perdurant | Continuant-Occurrent |
| DOLCE.16 | physical-endurant | Object |
| DOLCE.17 | physical-object | Object |
| DOLCE.18 | physical-quality | Quality |
| DOLCE.19 | physical-region | Spatial Region / Space (candidate) |
| DOLCE.20 | process | Process |
| DOLCE.21 | proposition | Proposition / Content (candidate) |
| DOLCE.22 | quale | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: covered by `quality.md`, not a separate concept) |
| DOLCE.23 | quality | Quality |
| DOLCE.24 | quality-space | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: covered by `quality.md`, not a separate concept) |
| DOLCE.25 | region | Spatial Region / Space (candidate) |
| DOLCE.26 | relevant-part | Mereology / Parthood / Aggregate (candidate) |
| DOLCE.27 | set | Universal / Type (candidate) |
| DOLCE.28 | space-region | Spatial Region / Space (candidate) |
| DOLCE.29 | spatio-temporal-particular | Continuant-Occurrent (root-adjacent — `equivalentClass` union, not `subClassOf`) |
| DOLCE.30 | spatio-temporal-region | Time / Spatial Region (candidate) |
| DOLCE.31 | state | Situation / State of Affairs (candidate) |
| DOLCE.32 | stative | Process |
| DOLCE.33 | temporal-location_q | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06 as a genuine Quality subtype, not a separate "quality space" category) |
| DOLCE.34 | temporal-quality | Quality |
| DOLCE.35 | temporal-region | Time (candidate) |
| DOLCE.36 | time-interval | Time (candidate) |
| DOLCE.37 | spatial-location_q | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06 as a genuine Quality subtype, not a separate "quality space" category) |

---

## SUMO (60 classes — `SUMO.1`–`SUMO.60`, capped 3 levels below `Entity` for comparability)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| SUMO.1 | Physical | Continuant-Occurrent |
| SUMO.2 | Abstract | Abstract vs. Concrete (candidate) |
| SUMO.3 | Object | Object |
| SUMO.4 | Collection | Mereology / Parthood / Aggregate (candidate) |
| SUMO.5 | ContentBearingPhysical | Information Artifact |
| SUMO.6 | Process | Process |
| SUMO.7 | PhysicalSystem | Object |
| SUMO.8 | Quantity | Quantity / Amount of Matter (candidate) |
| SUMO.9 | Attribute | Quality |
| SUMO.10 | SetOrClass | Universal / Type (candidate) |
| SUMO.11 | Relation | Relation |
| SUMO.12 | List | List / Sequence |
| SUMO.13 | Proposition | Proposition / Content (candidate) |
| SUMO.14 | SelfConnectedObject | Object |
| SUMO.15 | Region | Spatial Region / Space (candidate) |
| SUMO.16 | AutonomousAgent | Mind / Conscious Being / Agent |
| SUMO.17 | AstronomicalBody | Object |
| SUMO.18 | Artifact | Information Artifact |
| SUMO.19 | ContactSite | Boundary / Site (candidate) |
| SUMO.20 | CollectionOfObjects | Mereology / Parthood / Aggregate (candidate) |
| SUMO.21 | CollectionOfProcesses | Mereology / Parthood / Aggregate (candidate) |
| SUMO.22 | ContentBearingProcess | Information Artifact / Process (multiple inheritance: also child of Process) |
| SUMO.23 | ContentBearingObject | Information Artifact |
| SUMO.24 | SymbolicString | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: SymbolicString confirmed rdfs:subClassOf ContentBearingPhysical, already crosswalked) |
| SUMO.25 | Icon | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: Icon confirmed rdfs:subClassOf ContentBearingPhysical, already crosswalked) |
| SUMO.26 | LinguisticExpression | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: LinguisticExpression confirmed rdfs:subClassOf ContentBearingPhysical, already crosswalked) |
| SUMO.27 | VisualContentBearingPhysical | Information Artifact |
| SUMO.28 | DualObjectProcess | Process |
| SUMO.29 | SingleAgentProcess | Process |
| SUMO.30 | NaturalProcess | Process |
| SUMO.31 | IntentionalProcess | Process |
| SUMO.32 | Motion | Process |
| SUMO.33 | InternalChange | Change |
| SUMO.34 | Number | Quantity / Amount of Matter (candidate) |
| SUMO.35 | PhysicalQuantity | Quantity / Amount of Matter (candidate) |
| SUMO.36 | InternalAttribute | Quality |
| SUMO.37 | RelationalAttribute | Quality / Relation |
| SUMO.38 | Class | Universal / Type (candidate) |
| SUMO.39 | Set | Universal / Type (candidate) |
| SUMO.40 | SingleValuedRelation | Relation |
| SUMO.41 | TotalValuedRelation | Relation |
| SUMO.42 | PartialValuedRelation | Relation |
| SUMO.43 | BinaryRelation | Relation |
| SUMO.44 | InheritableRelation | Relation |
| SUMO.45 | ProbabilityRelation | Relation |
| SUMO.46 | SpatialRelation | Relation |
| SUMO.47 | TemporalRelation | Relation |
| SUMO.48 | IntentionalRelation | Relation |
| SUMO.49 | TernaryRelation | Relation |
| SUMO.50 | QuaternaryRelation | Relation |
| SUMO.51 | QuintaryRelation | Relation |
| SUMO.52 | Predicate | Relation |
| SUMO.53 | VariableArityRelation | Relation |
| SUMO.54 | RelationExtendedToQuantities | Relation |
| SUMO.55 | UniqueList | List / Sequence |
| SUMO.56 | Graph | Ungrouped |
| SUMO.57 | GraphElement | Ungrouped |
| SUMO.58 | FieldOfStudy | Ungrouped |
| SUMO.59 | Procedure | Disposition / Capacity |
| SUMO.60 | Argument | Proposition / Content (candidate) |

---

## UFO / OntoUML (56 classes — `UFO.1`–`UFO.56`, includes `AggregationKind`)

### ClassStereotype (`UFO.1`–`UFO.21`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| UFO.1 | abstract | Abstract vs. Concrete (candidate) |
| UFO.2 | category | Universal / Type (candidate) |
| UFO.3 | collective | Mereology / Parthood / Aggregate (candidate) |
| UFO.4 | datatype | Ungrouped |
| UFO.5 | enumeration | Ungrouped |
| UFO.6 | event | Event |
| UFO.7 | historicalRole | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.8 | historicalRoleMixin | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.9 | kind | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.10 | mixin | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.11 | mode | Disposition / Capacity |
| UFO.12 | phase | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.13 | phaseMixin | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.14 | quality | Quality |
| UFO.15 | quantity | Quantity / Amount of Matter (candidate) |
| UFO.16 | relator | Relation |
| UFO.17 | role | Role |
| UFO.18 | roleMixin | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.19 | situation | Situation / State of Affairs (candidate) |
| UFO.20 | subkind | Universal / Type (candidate) — rigidity-taxonomy detail |
| UFO.21 | type | Universal / Type (candidate) |

### PropertyStereotype (`UFO.22`–`UFO.23`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| UFO.22 | begin | Ungrouped — temporal-boundary property, not a class |
| UFO.23 | end | Ungrouped — temporal-boundary property, not a class |

### RelationStereotype (`UFO.24`–`UFO.42`)

All 19 → **Relation** (already-crosswalked concept; UFO's own named sub-kinds of relation, not separate candidate concepts):

| # | Class |
|---|---|
| UFO.24 | bringsAbout |
| UFO.25 | characterization |
| UFO.26 | comparative |
| UFO.27 | componentOf |
| UFO.28 | creation |
| UFO.29 | derivation |
| UFO.30 | externalDependence |
| UFO.31 | historicalDependence |
| UFO.32 | instantiation |
| UFO.33 | manifestation |
| UFO.34 | material |
| UFO.35 | mediation |
| UFO.36 | memberOf |
| UFO.37 | participation |
| UFO.38 | participational |
| UFO.39 | subCollectionOf |
| UFO.40 | subQuantityOf |
| UFO.41 | termination |
| UFO.42 | triggers |

### OntologicalNature (`UFO.43`–`UFO.53`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| UFO.43 | abstractNature | Abstract vs. Concrete (candidate) |
| UFO.44 | collectiveNature | Mereology / Parthood / Aggregate (candidate) |
| UFO.45 | eventNature | Event |
| UFO.46 | extrinsicModeNature | Disposition / Capacity |
| UFO.47 | functionalComplexNature | Object |
| UFO.48 | intrinsicModeNature | Disposition / Capacity |
| UFO.49 | qualityNature | Quality |
| UFO.50 | quantityNature | Quantity / Amount of Matter (candidate) |
| UFO.51 | relatorNature | Relation |
| UFO.52 | situationNature | Situation / State of Affairs (candidate) |
| UFO.53 | typeNature | Universal / Type (candidate) |

### AggregationKind (`UFO.54`–`UFO.56`) — not in the original matrix's scope, included here for completeness

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| UFO.54 | composite | Mereology / Parthood / Aggregate (candidate) |
| UFO.55 | none | Ungrouped |
| UFO.56 | shared | Mereology / Parthood / Aggregate (candidate) |

---

## GFO (77 classes — `GFO.1`–`GFO.77`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| GFO.1 | Abstract | Abstract vs. Concrete (candidate) |
| GFO.2 | Action | Event / Process |
| GFO.3 | Amount_of_substrate | Quantity / Amount of Matter (candidate) |
| GFO.4 | Awareness_level | Ontological Level / Stratum |
| GFO.5 | Biological_level | Ontological Level / Stratum |
| GFO.6 | Category | Universal / Type (candidate) |
| GFO.7 | Change | Change |
| GFO.8 | Chemical_level | Ontological Level / Stratum |
| GFO.9 | Chronoid | Time (candidate) |
| GFO.10 | Concept | Universal / Type (candidate) |
| GFO.11 | Concrete | Abstract vs. Concrete (candidate) |
| GFO.12 | Configuration | Situation / State of Affairs (candidate) |
| GFO.13 | Configuroid | Ungrouped — flagged single-source, source-unique |
| GFO.14 | Continuous | Continuous vs. Discrete |
| GFO.15 | Continuous_change | Change |
| GFO.16 | Continuous_process | Process |
| GFO.17 | Dependent | Quality |
| GFO.18 | Discrete | Continuous vs. Discrete |
| GFO.19 | Discrete_presential | Continuous vs. Discrete |
| GFO.20 | Discrete_process | Process |
| GFO.21 | Entity | Continuant-Occurrent (root) |
| GFO.22 | Extrinsic_change | Change — deprecated in source |
| GFO.23 | Function | Disposition / Capacity |
| GFO.24 | History | Process |
| GFO.25 | Independent | Continuant-Occurrent |
| GFO.26 | Individual | Continuant-Occurrent |
| GFO.27 | Instantaneous_change | Change |
| GFO.28 | Intrinsic_change | Change — deprecated in source |
| GFO.29 | Item | Universal / Type (candidate) |
| GFO.30 | Level | Ontological Level / Stratum |
| GFO.31 | Line | Boundary / Site (candidate) |
| GFO.32 | Mass_entity | Quantity / Amount of Matter (candidate) |
| GFO.33 | Material_boundary | Boundary / Site (candidate) |
| GFO.34 | Material_line | Boundary / Site (candidate) |
| GFO.35 | Material_object | Object |
| GFO.36 | Material_persistant | Object |
| GFO.37 | Material_point | Boundary / Site (candidate) |
| GFO.38 | Material_stratum | Ontological Level / Stratum |
| GFO.39 | Material_structure | Object |
| GFO.40 | Material_surface | Boundary / Site (candidate) |
| GFO.41 | Mental_stratum | Ontological Level / Stratum |
| GFO.42 | Occurrent | Continuant-Occurrent |
| GFO.43 | Ontological_layer | Ontological Level / Stratum |
| GFO.44 | Persistant | Ungrouped |
| GFO.45 | Personality_level | Ontological Level / Stratum |
| GFO.46 | Physical_level | Ontological Level / Stratum |
| GFO.47 | Point | Boundary / Site (candidate) |
| GFO.48 | Presential | Continuant-Occurrent |
| GFO.49 | Process | Process |
| GFO.50 | Processual_role | Role |
| GFO.51 | Property | Quality |
| GFO.52 | Property_value | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: covered by `quality.md`, not a separate concept) |
| GFO.53 | Relational_role | Role |
| GFO.54 | Relator | Relation |
| GFO.55 | Role | Role |
| GFO.56 | Set | Universal / Type (candidate) |
| GFO.57 | Situation | Situation / State of Affairs (candidate) |
| GFO.58 | Situoid | Situation / State of Affairs (candidate) |
| GFO.59 | Social_role | Role |
| GFO.60 | Social_stratum | Ontological Level / Stratum |
| GFO.61 | Space | Spatial Region / Space (candidate) |
| GFO.62 | Space_time | Time / Spatial Region (candidate) |
| GFO.63 | Spatial_boundary | Boundary / Site (candidate) |
| GFO.64 | Spatial_region | Spatial Region / Space (candidate) |
| GFO.65 | State | Situation / State of Affairs (candidate) |
| GFO.66 | Stratum | Ontological Level / Stratum |
| GFO.67 | Surface | Boundary / Site (candidate) |
| GFO.68 | Symbol | Symbol / Sign / Representation (candidate) |
| GFO.69 | Symbol_sequence | Symbol / Sign / Representation (candidate) |
| GFO.70 | Symbol_structure | Symbol / Sign / Representation (candidate) |
| GFO.71 | Temporal_region | Time (candidate) |
| GFO.72 | Time | Time (candidate) |
| GFO.73 | Time_boundary | Boundary / Site (candidate) |
| GFO.74 | Token | Object |
| GFO.75 | Topoid | Spatial Region / Space (candidate) |
| GFO.76 | Universal | Universal / Type (candidate) |
| GFO.77 | Value_space | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: covered by `quality.md`, not a separate concept) |

---

## YAMATO (44 classes — `YAMATO.1`–`YAMATO.44`, Fig. 2 "Detail version")

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| YAMATO.1 | Particular | Continuant-Occurrent (root) |
| YAMATO.2 | substrate | Ungrouped |
| YAMATO.3 | entity | Continuant-Occurrent |
| YAMATO.4 | physical | Continuant-Occurrent |
| YAMATO.5 | occurrent | Continuant-Occurrent |
| YAMATO.6 | stative | Process |
| YAMATO.7 | stative_2 | Process — previously-missed sibling of `process` |
| YAMATO.8 | process | Process |
| YAMATO.9 | event | Event |
| YAMATO.10 | ordinary event | Event |
| YAMATO.11 | instant event | Event |
| YAMATO.12 | continuant | Continuant-Occurrent |
| YAMATO.13 | object | Object |
| YAMATO.14 | functional | Object |
| YAMATO.15 | living organism | Ungrouped — domain-specific leaf, `TODO.md` "likely NOT core" |
| YAMATO.16 | artifact | Information Artifact |
| YAMATO.17 | non-representing thing | Object |
| YAMATO.18 | representing thing | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: representing thing quotes the identical passage already used as information-artifact.md's own flagship YAMATO correspondence) |
| YAMATO.19 | Chemical compound | Ungrouped — domain-specific leaf, `TODO.md` "likely NOT core" |
| YAMATO.20 | morphological whole | Ungrouped — domain-specific leaf, `TODO.md` "likely NOT core" |
| YAMATO.21 | weak agent | Mind / Conscious Being / Agent |
| YAMATO.22 | non-unitary | Mereology / Parthood / Aggregate (candidate) |
| YAMATO.23 | abstract | Abstract vs. Concrete (candidate) |
| YAMATO.24 | semi-abstract | Abstract vs. Concrete (candidate) |
| YAMATO.25 | mind | Mind / Conscious Being / Agent |
| YAMATO.26 | content | Proposition / Content (candidate) |
| YAMATO.27 | proposition | Proposition / Content (candidate) |
| YAMATO.28 | content_2 | Proposition / Content (candidate) |
| YAMATO.29 | representation | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: quotes the identical passage already used as information-artifact.md's own flagship YAMATO correspondence, including the form-and-content line) |
| YAMATO.30 | representation form | Information Artifact (was tagged "Symbol / Sign / Representation"; narrowed by maintainer 2026-07-06: quotes the identical passage already used as information-artifact.md's own flagship YAMATO correspondence, including the form-and-content line) |
| YAMATO.31 | dependent entity | Quality |
| YAMATO.32 | generically dependent | Information Artifact / Abstract vs. Concrete (candidate) |
| YAMATO.33 | quality value | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: internal subdivision of YAMATO's quality apparatus, not a separate concept) |
| YAMATO.34 | categorical | Quality (was tagged "Quality Space / Quale"; confirmed by maintainer 2026-07-06: internal subdivision of YAMATO's quality apparatus, not a separate concept) |
| YAMATO.35 | quantity | Quantity / Amount of Matter (candidate) |
| YAMATO.36 | role_3 | Role |
| YAMATO.37 | specifically dependent | Quality |
| YAMATO.38 | quality_1 | Quality |
| YAMATO.39 | property | Quality |
| YAMATO.40 | generic quality | Quality |
| YAMATO.41 | role | Role |
| YAMATO.42 | function | Disposition / Capacity |
| YAMATO.43 | role_2 | Role |
| YAMATO.44 | feature | Quality |

---

## TUpper (37 classes — `TUPPER.1`–`TUPPER.37`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| TUPPER.1 | activity | Process |
| TUPPER.2 | activity_occurrence | Event |
| TUPPER.3 | timepoint | Time (candidate) |
| TUPPER.4 | object | Object |
| TUPPER.5 | atomic | Ungrouped |
| TUPPER.6 | primitive | Ungrouped — TUpper's own literal class name, unrelated to the "primitive"-as-XwkOnt-term question (`ADR-0011`) |
| TUPPER.7 | generator | Ungrouped |
| TUPPER.8 | arboreal | Ungrouped |
| TUPPER.9 | initial | Ungrouped |
| TUPPER.10 | legal | Ungrouped |
| TUPPER.11 | state | Situation / State of Affairs (candidate) |
| TUPPER.12 | VoluminalRegion | Spatial Region / Space (candidate) |
| TUPPER.13 | ArealRegion | Spatial Region / Space (candidate) |
| TUPPER.14 | Curve | Boundary / Site (candidate) |
| TUPPER.15 | MaterialObject | Spatial Region / Space (candidate) |
| TUPPER.16 | ShapedObject | Spatial Region / Space (candidate) |
| TUPPER.17 | ShapeFeature | Boundary / Site (candidate) |
| TUPPER.18 | Max | Ungrouped |
| TUPPER.19 | MaxDim | Ungrouped |
| TUPPER.20 | Min | Ungrouped |
| TUPPER.21 | MinDim | Ungrouped |
| TUPPER.22 | PointRegion | Boundary / Site (candidate) |
| TUPPER.23 | ZEX | Ungrouped |
| TUPPER.24 | box | Spatial Region / Space (candidate) |
| TUPPER.25 | point | Boundary / Site (candidate) |
| TUPPER.26 | poly | Spatial Region / Space (candidate) |
| TUPPER.27 | surface | Boundary / Site (candidate) |
| TUPPER.28 | edge | Boundary / Site (candidate) |
| TUPPER.29 | ridge | Boundary / Site (candidate) |
| TUPPER.30 | border | Boundary / Site (candidate) |
| TUPPER.31 | outer | Boundary / Site (candidate) |
| TUPPER.32 | vertex | Boundary / Site (candidate) |
| TUPPER.33 | mat | Quantity / Amount of Matter (candidate) |
| TUPPER.34 | amount | Quantity / Amount of Matter (candidate) |
| TUPPER.35 | spatial_area | Spatial Region / Space (candidate) |
| TUPPER.36 | spatial_length | Spatial Region / Space (candidate) |
| TUPPER.37 | spatial_volume | Spatial Region / Space (candidate) |

---

## GUM (193 classes — `GUM.1`–`GUM.193`)

| # | Class | Nearest XwkOnt bucket |
|---|---|---|
| GUM.1 | Ability | Disposition / Capacity |
| GUM.2 | Abstraction | Abstract vs. Concrete (candidate) |
| GUM.3 | AddresseeOriented | Ungrouped — linguistic clause type, `TODO.md` "likely NOT core" |
| GUM.4 | Addressing | Ungrouped — linguistic |
| GUM.5 | AddressingVerbal | Ungrouped — linguistic |
| GUM.6 | AffectingAction | Ungrouped — linguistic |
| GUM.7 | Age | Quality |
| GUM.8 | AgePropertyAscription | Quality |
| GUM.9 | Ambience | Ungrouped — linguistic |
| GUM.10 | Ascription | Ungrouped — linguistic |
| GUM.11 | AscriptionInverse | Ungrouped — linguistic |
| GUM.12 | AtLeast | Ungrouped — linguistic |
| GUM.13 | AtMost | Ungrouped — linguistic |
| GUM.14 | BehavioralQuality | Quality |
| GUM.15 | BehavioralVerbal | Ungrouped — linguistic |
| GUM.16 | BeingAndHaving | Situation / State of Affairs (candidate) |
| GUM.17 | Believe | Mind / Conscious Being / Agent |
| GUM.18 | Causal | Ungrouped — linguistic |
| GUM.19 | Circumstance | Ungrouped — linguistic |
| GUM.20 | Circumstantial | Ungrouped — linguistic |
| GUM.21 | CircumstantialOther | Ungrouped — linguistic |
| GUM.22 | ClassAscription | Universal / Type (candidate) |
| GUM.23 | ClassQuality | Quality |
| GUM.24 | Cognition | Mind / Conscious Being / Agent |
| GUM.25 | Color | Quality |
| GUM.26 | ColorPropertyAscription | Quality |
| GUM.27 | CommunicativeAttitude | Ungrouped — linguistic |
| GUM.28 | Conditional | Modality |
| GUM.29 | Configuration | Situation / State of Affairs (candidate) |
| GUM.30 | ConfigurationBeginning | Situation / State of Affairs (candidate) |
| GUM.31 | ConfigurationBoundary | Boundary / Site (candidate) |
| GUM.32 | ConfigurationContinuity | Situation / State of Affairs (candidate) |
| GUM.33 | ConfigurationEnding | Situation / State of Affairs (candidate) |
| GUM.34 | ConfigurationInitializing | Situation / State of Affairs (candidate) |
| GUM.35 | ConfigurationResuming | Situation / State of Affairs (candidate) |
| GUM.36 | ConfigurationStaging | Situation / State of Affairs (candidate) |
| GUM.37 | Conjunction | Ungrouped — linguistic |
| GUM.38 | ConsciousBeing | Mind / Conscious Being / Agent |
| GUM.39 | CreativeMaterialAction | Ungrouped — linguistic |
| GUM.40 | DecomposableObject | Mereology / Parthood / Aggregate (candidate) |
| GUM.41 | DiffuseMatter | Quantity / Amount of Matter (candidate) |
| GUM.42 | Disjunction | Ungrouped — linguistic |
| GUM.43 | DisjunctiveSet | Universal / Type (candidate) |
| GUM.44 | Disliking | Mind / Conscious Being / Agent |
| GUM.45 | DispositiveMaterialAction | Ungrouped — linguistic |
| GUM.46 | DoingAndHappening | Situation / State of Affairs (candidate) |
| GUM.47 | DurationInTime | Time (candidate) |
| GUM.48 | DynamicQuality | Quality |
| GUM.49 | Elaboration | Ungrouped — linguistic |
| GUM.50 | Element | Continuant-Occurrent |
| GUM.51 | ElementList | Mereology / Parthood / Aggregate (candidate) |
| GUM.52 | ElementOf | Mereology / Parthood / Aggregate (candidate) |
| GUM.53 | Enhancement | Ungrouped — linguistic |
| GUM.54 | EvaluativeQuality | Quality |
| GUM.55 | Exactly | Ungrouped — linguistic |
| GUM.56 | Existence | Situation / State of Affairs (candidate) |
| GUM.57 | Expansion | Ungrouped — linguistic |
| GUM.58 | Extension | Ungrouped — linguistic |
| GUM.59 | External | Ungrouped — linguistic |
| GUM.60 | Fearing | Mind / Conscious Being / Agent |
| GUM.61 | Female | Mind / Conscious Being / Agent |
| GUM.62 | Future | Time (candidate) |
| GUM.63 | GUMThing | Continuant-Occurrent (root) |
| GUM.64 | GeneralPossibility | Disposition / Capacity |
| GUM.65 | GeneralizedLocating | Spatial Region / Space (candidate) |
| GUM.66 | GeneralizedPossession | Relation |
| GUM.67 | GeneralizedPossessionInverse | Relation |
| GUM.68 | GeneralizedRoleRelation | Role |
| GUM.69 | GreaterThan | Quantity / Amount of Matter (candidate) |
| GUM.70 | GreaterThanComparison | Quantity / Amount of Matter (candidate) |
| GUM.71 | Hailing | Ungrouped — linguistic |
| GUM.72 | IdeaProjection | Ungrouped — linguistic |
| GUM.73 | IdeaQuoting | Ungrouped — linguistic |
| GUM.74 | IdeaReporting | Ungrouped — linguistic |
| GUM.75 | Identity | Ungrouped — linguistic |
| GUM.76 | InstantaneousInTime | Time (candidate) |
| GUM.77 | Intensive | Relation |
| GUM.78 | Intention | Disposition / Capacity |
| GUM.79 | Internal | Ungrouped — linguistic |
| GUM.80 | Know | Mind / Conscious Being / Agent |
| GUM.81 | LessThan | Quantity / Amount of Matter (candidate) |
| GUM.82 | LessThanComparison | Quantity / Amount of Matter (candidate) |
| GUM.83 | Liking | Mind / Conscious Being / Agent |
| GUM.84 | LocutionProjection | Ungrouped — linguistic |
| GUM.85 | LocutionQuoting | Ungrouped — linguistic |
| GUM.86 | LocutionReporting | Ungrouped — linguistic |
| GUM.87 | LogicalPropertyAscription | Quality |
| GUM.88 | LogicalQuality | Quality |
| GUM.89 | LogicalUniqueness | Quality |
| GUM.90 | Male | Mind / Conscious Being / Agent |
| GUM.91 | MaterialClassQuality | Quality |
| GUM.92 | MaterialPropertyAscription | Quality |
| GUM.93 | MaterialWorldQuality | Quality |
| GUM.94 | MentalActive | Mind / Conscious Being / Agent |
| GUM.95 | MentalInactive | Mind / Conscious Being / Agent |
| GUM.96 | MessageOriented | Ungrouped — linguistic |
| GUM.97 | MessageTransfer | Ungrouped — linguistic |
| GUM.98 | ModalPropertyAscription | Modality |
| GUM.99 | ModalQuality | Modality |
| GUM.100 | MultiConfiguration | Situation / State of Affairs (candidate) |
| GUM.101 | Name | Symbol / Sign / Representation (candidate; excluded from that crosswalk's evidence 2026-07-06 — its definition is comparable in form to information-artifact.md's own BFO(IAO) Information Content Entity definition; not added there by this pass, open question, see symbol-sign-representation.yaml's Future Work) |
| GUM.102 | NameEvent | Event |
| GUM.103 | NameOf | Symbol / Sign / Representation (candidate) |
| GUM.104 | NameRelation | Symbol / Sign / Representation (candidate) |
| GUM.105 | NamedObject | Object |
| GUM.106 | NaturalNumber | Quantity / Amount of Matter (candidate) |
| GUM.107 | Necessity | Modality |
| GUM.108 | NonAddresseeOriented | Ungrouped — linguistic |
| GUM.109 | NonAddressing | Ungrouped — linguistic |
| GUM.110 | NonAffectingAction | Situation / State of Affairs (candidate) |
| GUM.111 | NonAffectingDoing | Ungrouped — linguistic |
| GUM.112 | NonAffectingHappening | Ungrouped — linguistic |
| GUM.113 | NonConditional | Modality |
| GUM.114 | NonConsciousThing | Object |
| GUM.115 | NonDecomposableObject | Object |
| GUM.116 | NonMessageOriented | Ungrouped — linguistic |
| GUM.117 | NonScalableQuality | Quality |
| GUM.118 | NonVolitional | Modality |
| GUM.119 | NumberFocusing | Quantity / Amount of Matter (candidate) |
| GUM.120 | OneOrTwoDLocation | Spatial Region / Space (candidate) |
| GUM.121 | OneOrTwoDTime | Time (candidate) |
| GUM.122 | OrderedObject | List / Sequence (was tagged "Mereology / Parthood / Aggregate (candidate)"; retagged 2026-07-07, session verification: reifies the same ordered-collection apparatus as SUMO's `List`, not a part-whole aggregate) |
| GUM.123 | OrderedSet | List / Sequence (was tagged "Universal / Type (candidate)"; retagged 2026-07-07, session verification: subclass of `OrderedObject`, the ordered-collection apparatus, not a type/universal-side class) |
| GUM.124 | OwnedBy | Relation |
| GUM.125 | Ownership | Relation |
| GUM.126 | Part | Mereology / Parthood / Aggregate (candidate) |
| GUM.127 | PartOf | Mereology / Parthood / Aggregate (candidate) |
| GUM.128 | PartWhole | Mereology / Parthood / Aggregate (candidate) |
| GUM.129 | Past | Time (candidate) |
| GUM.130 | Perception | Mind / Conscious Being / Agent |
| GUM.131 | Person | Mind / Conscious Being / Agent |
| GUM.132 | PolarQuality | Quality |
| GUM.133 | Possibility | Modality |
| GUM.134 | Present | Time (candidate) |
| GUM.135 | Process | Process |
| GUM.136 | ProfilesAndStages | Time (candidate) |
| GUM.137 | Projection | Ungrouped — linguistic |
| GUM.138 | ProperVerbal | Ungrouped — linguistic |
| GUM.139 | PropertyAscription | Quality |
| GUM.140 | PropertyOf | Quality |
| GUM.141 | ProvenanceClassQuality | Quality |
| GUM.142 | ProvenancePropertyAscription | Quality |
| GUM.143 | Quantity | Quantity / Amount of Matter (candidate) |
| GUM.144 | QuantityAscription | Quantity / Amount of Matter (candidate) |
| GUM.145 | Quoting | Ungrouped — linguistic |
| GUM.146 | Raining | Ungrouped — linguistic |
| GUM.147 | ReactionAndEmotion | Mind / Conscious Being / Agent |
| GUM.148 | Relating | Relation |
| GUM.149 | Reporting | Ungrouped — linguistic |
| GUM.150 | RoleOrOffice | Role |
| GUM.151 | RolePlaying | Role |
| GUM.152 | SayingAndSensing | Ungrouped — linguistic |
| GUM.153 | ScalableQuality | Quality |
| GUM.154 | ScaledComparison | Quantity / Amount of Matter (candidate) |
| GUM.155 | SenseANDMeasureQuality | Quality |
| GUM.156 | Signification | Symbol / Sign / Representation (candidate) |
| GUM.157 | SimpleQuality | Quality |
| GUM.158 | SimpleThing | Object |
| GUM.159 | Size | Quality |
| GUM.160 | SizePropertyAscription | Quality |
| GUM.161 | Snowing | Ungrouped — linguistic |
| GUM.162 | Space | Spatial Region / Space (candidate) |
| GUM.163 | SpaceInterval | Spatial Region / Space (candidate) |
| GUM.164 | SpacePoint | Spatial Region / Space (candidate) |
| GUM.165 | SpatialObject | Spatial Region / Space (candidate) |
| GUM.166 | SpatialTemporal | Spatial Region / Space (candidate) |
| GUM.167 | SpecificMatter | Quantity / Amount of Matter (candidate) |
| GUM.168 | StativeQuality | Quality |
| GUM.169 | StatusQuality | Quality |
| GUM.170 | Striving | Mind / Conscious Being / Agent |
| GUM.171 | SubjectMatter | Ungrouped — linguistic |
| GUM.172 | Substance | Quantity / Amount of Matter (candidate) |
| GUM.173 | Sunning | Ungrouped — linguistic |
| GUM.174 | Symbolization | Symbol / Sign / Representation (candidate) |
| GUM.175 | TaxonomicQuality | Quality |
| GUM.176 | TemporalObject | Time (candidate) |
| GUM.177 | TemporalProfile | Time (candidate) |
| GUM.178 | TemporallyBounded | Time (candidate) |
| GUM.179 | TemporallyUnbounded | Time (candidate) |
| GUM.180 | Think | Mind / Conscious Being / Agent |
| GUM.181 | ThreeDLocation | Spatial Region / Space (candidate) |
| GUM.182 | ThreeDTime | Time (candidate) |
| GUM.183 | Time | Time (candidate) |
| GUM.184 | TimeInterval | Time (candidate) |
| GUM.185 | TimePoint | Time (candidate) |
| GUM.186 | UMSet | Universal / Type (candidate) |
| GUM.187 | UsePropertyAscription | Quality |
| GUM.188 | Volitional | Modality |
| GUM.189 | Wanting | Mind / Conscious Being / Agent |
| GUM.190 | Winding | Ungrouped — linguistic |
| GUM.191 | Word | Symbol / Sign / Representation (candidate) |
| GUM.192 | ZeroDLocation | Spatial Region / Space (candidate) |
| GUM.193 | ZeroDTime | Time (candidate) |

---

## Notes on method

- Every count above was independently re-verified by direct fetch and parse of the primary source (not the earlier ASCII-tree sketches). BFO/DOLCE/GFO/TUpper were parsed programmatically from their OWL files; SUMO from `Merge.kif` capped at a stated depth; UFO from its Turtle vocabulary, cross-checked two ways; YAMATO from direct high-resolution visual inspection of the rendered PDF figure (the diagram is a rasterized image, not machine-readable text); GUM from a direct `curl` fetch of the same archive.org snapshot already on file.
- SUMO's 60 is a **depth-capped** count (3 levels below `Entity`), not SUMO's full taxonomy, which continues far deeper (hundreds more classes) — capped for comparability with the other 7 sources' matrix entries, which are similarly shallow.
- "Nearest XwkOnt bucket" is a judgment call made by re-reading each class in context of the existing 8 `reviewed` crosswalks and `TODO.md`'s 19-candidate queue — it is not independently re-verified against each class's own primary-source definition beyond the exhaustive-count pass above. Treat this as a triage pass, not a new round of definitional/semantic primary-source verification.
- **GUM accounts for over a third of the total (193 of 540)**, but only 51 of its 193 classes are tagged `Ungrouped — linguistic` (fine-grained clause-type/quality distinctions with no cross-source counterpart pattern, consistent with `TODO.md`'s existing "likely NOT core" flag) — the other ~142 map to ordinary candidate buckets (Quality, Time, Mind/Conscious Being/Agent, Object, etc.), same as any other source's raw classes. GUM's linguistically-motivated design (Halliday & Matthiessen systemic-functional-linguistics framing, a genuinely different orientation from the other 7 sources' general-purpose top-level framing, already noted elsewhere in this project's source-ontology survey notes) explains the *Ungrouped* minority, not the file's overall size.
- Similarly, most of SUMO's and TUpper's newly-found classes at deeper levels are fine-grained domain leaves (SUMO's `Relation` sub-taxonomy, TUpper's mereotopology primitives) rather than new candidate concepts — they map to existing buckets (mostly Relation, Spatial Region/Space, Boundary/Site) rather than expanding the candidate count.

## References

- `docs/evaluations/foundational-ontology-concept-terms-matrix.md`
- `TODO.md`
- `docs/adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md`
- `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md`
- `docs/adr/ADR-0019-reinforce-concept-against-practitioner-usage.md`
