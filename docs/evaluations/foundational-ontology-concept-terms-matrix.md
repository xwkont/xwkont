# Foundational Ontology Concept-Term Matrix

> **Status:** Verified directly against each source ontology's own primary artifact (OWL file or spec paper) — not summarized from secondary literature or filled from training-data memory
> **Produced:** 2026-07-03, by Claude working in this repository, using the same fetch-and-parse rigor as `docs/methodology/primary-source-verification.md`. Terminology Cross-Reference section added 2026-07-04, same rigor. SUMO's ASCII tree and Cross-Cutting Observation 2 corrected 2026-07-04 during `docs/crosswalks/concepts/time.md`'s research (SUMO's `TimeMeasure`/`TimeInterval`/`TimePoint` branch and GUM's Time apparatus were both missed/omitted in the original pass). Renamed three times: from `foundational-ontology-primitives-matrix.md` (2026-07-04 — "primitive" is not an XwkOnt term, `ADR-0011` considered and rejected it) to `foundational-ontology-class-hierarchy-matrix.md`, then briefly to `foundational-ontology-category-matrix.md` (2026-07-04, same session — later found to overstate "Category" as an XwkOnt-adopted term when it is only a finding, per `ADR-0019`), then to its current name. **Concept-Term** reuses only vocabulary `ADR-0011` already established: each source's own word (or absence of one) for its internal analog of a Concept is that source's own **Term** — reflexively applying the existing Concept/Term relationship, not introducing new vocabulary or privileging any one source's word (e.g. "Category") as if XwkOnt had adopted it. 7 of the 8 sources trace to some form of "category" for this Term (5 self-declare it; BFO and TUpper inherit it from their governing standard, ISO/IEC 21838-1 §3.19); UFO has none found. Per-source values below and in the Terminology Cross-Reference section are each cited to that source's own primary material, not to ISO 21838, except where BFO/TUpper's own inheritance is the explicit point being made.
> **Provenance classification:** Referenced (each ontology's own top-level classes, directly cited to its primary source; XwkOnt does not assert any of these hierarchies as correct or adopt them as its own — Source First, `docs/ARCHITECTURAL_PRINCIPLES.md` Principle 4)

## Why this matters

External review (2026-07-03) asked how XwkOnt's own concept set relates to what each source ontology treats as its own top-level categories. `ADR-0011` and `ADR-0017` already established that XwkOnt's crosswalk concepts are not the same thing as any one source's own classes — but no artifact had actually laid out, side by side and verified, what each of the eight source ontologies' own top-level category tree looks like. This document does that.

Each source was fetched directly from the same primary-source locator already on file in the corresponding `docs/references/ref-*.md` record (BFO: `ref-bfo-2020.md`; DOLCE: `ref-dolce-lite-owl.md`; SUMO: `ref-sumo-niles-pease-2001.md`; UFO: `ref-ufo-2021.md`, plus the OntoUML vocabulary as a fallback; GFO: `ref-gfo.md`; YAMATO: `ref-yamato-mizoguchi-2010.md`; TUpper: `ref-tupper-colore.md`; GUM: `ref-gum-owl.md`), parsed for actual `subClassOf`/`subclass`/`partition` axioms (not AI-summarized secondary description), with honest gap-flagging where a source's file didn't support a claim.

## Summary Table

| Ontology | Root class | Immediate top-level split | Concept Term | Notes on split |
|---|---|---|---|---|
| **BFO 2020** | `entity` | `continuant` / `occurrent` | **"Category"** (ISO/IEC 21838-1 §3.19) — BFO is ISO/IEC 21838-**2**, so it inherits Part 1's normative vocabulary rather than defining its own; no separate self-description found in BFO's own site/README. | Genuinely minimal — 36 classes total in the whole core file. |
| **DOLCE** (Lite mirror) | `particular` | `abstract` (direct `subClassOf`) plus `endurant` / `perdurant` / `quality` (via an `equivalentClass` construction, `spatio-temporal-particular`, not a literal `subClassOf` chain) | **"basic categories" / "categories"** — WonderWeb D18 §3.2/§5.2, quote-verified. | This file is a reduced "Lite" module; several richer full-DOLCE categories (agentive/non-agentive objects, social objects, DnS constructs) are absent from it. |
| **SUMO** | `Entity` | `Physical` / `Abstract` (`(partition Entity Physical Abstract)`) | **"category" / "categorial"** — Niles & Pease FOIS paper, quote-verified ("a basic, categorial distinction between objects and processes"). | Then `Abstract` further divides via `(disjointDecomposition Abstract Quantity Attribute Relation Proposition List)`. |
| **UFO** | *(no single canonical machine-readable root found)* | `OntologicalNature` enum: `eventNature` vs. several endurant-related natures (`functionalComplexNature`, `collectiveNature`, `quantityNature`, `relatorNature`, `intrinsicModeNature`, `extrinsicModeNature`, `qualityNature`), plus `situationNature`, `typeNature`, `abstractNature` | **None found.** Not ISO-governed (unlike BFO/TUpper); the 2021 paper's own extraction notes show no explicit metalevel term; paywalled beyond that. | The commonly-cited "Endurant/Event" labeled split is **not literally present** in any fetched machine-readable source; the primary UFO 2021 paper is paywalled (403), same block already logged for `xwkont:ref:borgo-galton-kutz-2022` in `ADR-0015`. |
| **GFO** (base module) | `Entity` | `Item` / `Individual` | **"Category"** and **"Universal"** — both literal, separately-defined classes in the source file, quote-verified. | `Item` further splits into `Category` / `Individual`'s siblings; `Individual` further splits into `Occurrent`/`Presential`/`Continuous`/`Dependent`/`Discrete`/`Independent`/`Space_time`/`Abstract`/`Concrete`, with multiple inheritance in several places. |
| **YAMATO** | `Particular` | `entity` (→ `physical`/`abstract`/`semi-abstract`) as one branch, `dependent entity` (→ `generically dependent`/`specifically dependent`) as a second branch | **"top-level categories"** — Section 2.2 heading, quote-verified. | Root parentage of `dependent entity` relative to `Particular`/`entity` is visually ambiguous in the source figure — not confirmed by prose. |
| **TUpper** | `owl:Thing` | `activity` / `activity_occurrence` / `timepoint` / `object` (explicit `owl:Thing ⊑ activity ⊔ activity_occurrence ⊔ timepoint ⊔ object`) | **"Category"** (ISO/IEC 21838-1 §3.19) — TUpper is ISO/IEC 21838-**4**, same inheritance logic as BFO; TUpper's own CLIF/OWL files use only generic "class," no distinct metalevel word. | Spatial/mereotopology classes (`MaterialObject`, `ShapedObject`, etc.) exist in the same file but have no asserted `subClassOf` link to any of the four roots — only property-restriction connections. |
| **GUM** | `GUMThing` | `Configuration` / `Element` / `MultiConfiguration` | **"category"** (applied to the root node's own class comment) — quote-verified, reused from a prior on-file verification. | Linguistically motivated (Halliday & Matthiessen systemic-functional-linguistics framing, per the file's own `rdfs:comment`). A separate, unused class literally named `Thing` exists in the file with no relations — not the real root. |

**Pattern, updated:** 7 of 8 sources now have a traceable "category"-family term once ISO/IEC 21838's inheritance is accounted for (BFO and TUpper inherit it from Part 1 rather than self-defining it) — only UFO has none found. This changes the earlier reading (5 of 8, treating BFO/TUpper as "not found") — BFO/TUpper aren't silent on this, they defer to their governing standard's own vocabulary rather than repeating it in their own module.

## Verified Hierarchies (as fetched)

### BFO 2020
Source: `https://raw.githubusercontent.com/BFO-ontology/BFO-2020/master/21838-2/owl/bfo-core.owl` — all 36 classes traced, no gaps.

```
entity
├── continuant
│   ├── independent continuant
│   │   ├── material entity
│   │   │   ├── object
│   │   │   ├── fiat object part
│   │   │   └── object aggregate
│   │   └── immaterial entity
│   │       ├── continuant fiat boundary → fiat point / fiat line / fiat surface
│   │       ├── site
│   │       └── spatial region → zero/one/two/three-dimensional spatial region
│   ├── specifically dependent continuant
│   │   ├── quality → relational quality
│   │   └── realizable entity → role / disposition → function
│   └── generically dependent continuant
└── occurrent
    ├── process → history
    ├── process boundary
    ├── temporal region → zero-dimensional (→ temporal instant) / one-dimensional (→ temporal interval)
    └── spatiotemporal region
```

### DOLCE (Lite mirror)
Source: `https://raw.githubusercontent.com/iddi/sofia/master/eu.sofia.adk.common/ontologies/foundational/DOLCE-Lite.owl` — 37 classes in this module; full DOLCE's richer categories not present here.

```
particular
├── abstract → proposition / set / region (→ abstract-region / physical-region → space-region → spatio-temporal-region / temporal-region → time-interval)
└── [endurant / perdurant / quality connect only via the equivalentClass "spatio-temporal-particular", not a plain subClassOf chain]
    endurant → arbitrary-sum / non-physical-endurant (→ non-physical-object) / physical-endurant (→ amount-of-matter / feature / physical-object)
    perdurant → event (→ accomplishment / achievement) / stative (→ process / state)
    quality → abstract-quality / physical-quality (→ spatial-location_q) / temporal-quality (→ temporal-location_q)
```

### SUMO
Source: `https://raw.githubusercontent.com/ontologyportal/sumo/master/Merge.kif`.

```
Entity
├── Physical
│   ├── Object → Region, CorpuscularObject
│   ├── Process
│   ├── Collection
│   └── ContentBearingPhysical
└── Abstract
    ├── Quantity → Number / PhysicalQuantity (→ ConstantQuantity → TimeMeasure → TimeDuration / TimePosition (→ TimeInterval / TimePoint))
    ├── Attribute → InternalAttribute (→ PhysicalAttribute) / RelationalAttribute
    ├── Relation → Predicate / Function / TemporalRelation
    ├── Proposition
    └── List
```

**Correction (2026-07-04):** an earlier pass of this tree stopped short of the `Quantity` branch's `TimeMeasure`/`TimeInterval`/`TimePoint` classes, a depth-of-search miss (not a real absence) corrected during `docs/crosswalks/concepts/time.md`'s research — see that document and `docs/references/ref-sumo-niles-pease-2001.md`'s "Reused for `time.md`" note for the full verification.

### UFO / OntoUML
Sources: OntoUML vocabulary TTL (`https://raw.githubusercontent.com/OntoUML/ontouml-vocabulary/master/ontouml.ttl`) as primary; the UFO 2021 journal paper (DOI `10.3233/AO-210256`) was attempted and returned 403 Forbidden.

```
Stereotype (disjoint union)
├── ClassStereotype: abstract, category, collective, datatype, enumeration, event, historicalRole,
│   historicalRoleMixin, kind, mixin, mode, phase, phaseMixin, quality, quantity, relator, role,
│   roleMixin, situation, subkind, type
├── PropertyStereotype: begin, end
└── RelationStereotype: bringsAbout, characterization, comparative, componentOf, creation,
    derivation, externalDependence, historicalDependence, instantiation, manifestation, material,
    mediation, memberOf, participation, participational, subCollectionOf, subQuantityOf,
    termination, triggers

OntologicalNature (separate enum, explicitly credited to UFO theory):
abstractNature, collectiveNature, eventNature, extrinsicModeNature, functionalComplexNature,
intrinsicModeNature, qualityNature, quantityNature, relatorNature, situationNature, typeNature
```

Not found in this source: rigid/anti-rigid/semi-rigid or sortal/non-sortal grouping classes, or an explicit labeled Endurant/Event split.

### GFO (base module)
Source: `https://raw.githubusercontent.com/Onto-Med/GFO/master/modules/gfo-base.owl`.

```
Entity
├── Item
│   ├── Category → Concept / Ontological_layer / Symbol_structure / Universal (→ Persistant / Value_space)
│   └── Individual
│       ├── Abstract
│       ├── Continuous
│       ├── Discrete → Discrete_presential / Discrete_process
│       ├── Independent → Social_role
│       ├── Dependent → Material_boundary / Property / Property_value / Relational_role
│       ├── Concrete
│       │   ├── Occurrent → Action / Change (→ Continuous_change) / History / Process (→ Configuroid / Continuous_process / Discrete_process)
│       │   └── Presential → Amount_of_substrate / Configuration / Discrete_presential / Mass_entity / Material_boundary
│       └── Space_time → Space / Time
└── Set (no subclasses found in this module)
```

Several classes carry multiple `rdfs:subClassOf` assertions (multiple inheritance). Deeper GFO strata sometimes cited in secondary literature (`Material_stratum`, `Mental_stratum`, `Social_stratum`, `Chronoid`, `Topoid`) were **not** confirmed in this specific base module — they may live in an unexplored `situation/` submodule.

### YAMATO
Source: `https://www.hozo.jp/onto_library/YAMATO101216.pdf`, Section 2.2, Fig. 1/Fig. 2 (verified by rendering the PDF pages and cross-checking against body-text labels (a)–(o)).

```
Particular
├── substrate
└── entity
    ├── physical
    │   ├── occurrent → stative (→ process) / event (→ ordinary event / instant event)
    │   └── continuant → object (→ functional (→ living organism / artifact → non-representing thing / representing thing) / Chemical compound / morphological whole / weak agent) / non-unitary
    ├── abstract
    └── semi-abstract → mind / content (→ proposition / content_2) / representation (→ representation form)
dependent entity  [root parentage relative to Particular/entity not confirmed from source]
├── generically dependent → quality value (→ categorical / quantity) / role_3
└── specifically dependent → quality_1 (→ property / generic quality) / role (→ function / role_2) / feature
```

### TUpper
Source: `https://raw.githubusercontent.com/gruninger/colore/master/ontologies/tupper/owl/tupper.all.owl`.

```
owl:Thing ⊑ (activity ∪ activity_occurrence ∪ timepoint ∪ object)
├── activity → atomic (→ primitive, generator) 
├── activity_occurrence → arboreal (→ initial, legal, generator)
├── timepoint (no subclasses found)
└── object → state
```

Spatial classes (`MaterialObject`, `ShapedObject`, `VoluminalRegion`, `ArealRegion`, `Curve`, etc.) exist in the same file but connect to the above only through property-restriction axioms (`bounds`, `constitutes`, `occupies`), not asserted `subClassOf` — not claimed as verified children of `object`.

### GUM
Source: `http://web.archive.org/web/2021/http://www.fb10.uni-bremen.de/anglistik/langpro/webspace/jb/gum/gum-files/GUM-31.owl.txt` (canonical live host is dead; fetched via the same Wayback snapshot already on file in `ref-gum-owl.md`).

```
GUMThing
├── Configuration → BeingAndHaving (→ Existence, Relating) / DoingAndHappening (→ AffectingAction, NonAffectingAction) / SayingAndSensing (→ External, Internal)
├── Element → Circumstance (→ SubjectMatter) / Process (leaf) / SimpleQuality (→ LogicalQuality, MaterialWorldQuality, ModalQuality) / SimpleThing (→ ConsciousBeing, DecomposableObject, NamedObject, NonConsciousThing, NonDecomposableObject)
└── MultiConfiguration → Expansion (→ Elaboration, Enhancement, Extension) / Projection (→ IdeaProjection, LocutionProjection, Quoting, Reporting)
```

No class named `Entity` exists in this file — the real root token is `GUMThing`, distinct from a separate vestigial `Thing` class with no relations.

## Cross-Cutting Observations

1. **No two sources split their root the same way**, confirming the earlier in-conversation finding: BFO uses a two-way Continuant/Occurrent split; DOLCE (in this Lite module) connects endurant/perdurant/quality via an equivalence-class trick rather than plain subclassing; SUMO partitions Entity into exactly two (`Physical`/`Abstract`); GFO splits into `Item`/`Individual` first, occurrent/continuant-like categories only appearing a level lower; YAMATO has *two* root-level branches (`entity` and `dependent entity`) rather than one; TUpper's root divides into four, not two; GUM's split (`Configuration`/`Element`/`MultiConfiguration`) is organized around linguistic function, not metaphysical category at all.
2. **Time is an explicit, nameable category in 6 of the 8 sources — corrected 2026-07-04, was previously undercounted at 5.** `docs/crosswalks/concepts/time.md`'s direct primary-source research found: BFO's `temporal region` (→ `temporal instant`/`temporal interval`), DOLCE's `temporal-region`/`time-interval`, **SUMO's `TimeMeasure`/`TimeInterval`/`TimePoint`** (missed by this document's earlier, shallower pass into the `Quantity` branch — see the corrected SUMO tree above), GFO's `Time` (under `Space_time`), TUpper's `timepoint`, and **GUM's 18-class `Time`/`TemporalObject` apparatus** (omitted from this observation entirely in the earlier pass, despite already being verified elsewhere in `xwkont:ref:gum-owl`) all give Time (or its instant/interval subdivisions) a real class. UFO and YAMATO have neither, for different reasons: UFO has no reified Time class in the fetched 2021 paper or the OntoUML vocabulary fallback (only a "Perdurants... unfold in time" property); YAMATO has none found, but only in the one YAMATO document that is actually fetchable, not confirmed as a settled fact about YAMATO overall (see `time.md`'s Uncertainty section for both scoped caveats).
3. **UFO's primary paper being paywalled is now a recurring, not isolated, finding** — the same block already logged in `ADR-0015` for `xwkont:ref:borgo-galton-kutz-2022` recurred here for the UFO 2021 paper itself. The OntoUML vocabulary TTL was usable as a fallback but does not carry the same theoretical framing (Endurant/Event, rigidity) the paper is normally cited for.
4. **"Lite"/module-scoped files understate their full ontologies.** DOLCE-Lite and GFO-base both visibly omit categories that secondary literature attributes to the fuller systems (DOLCE's agentive/social/DnS constructs; GFO's strata and situation module). Anyone citing this matrix for DOLCE or GFO specifically should treat it as "verified for this module," not "the complete DOLCE/GFO."

## Terminology Cross-Reference: What Each Source Calls Its Own Top-Level Categories

This section addresses a distinct question from the hierarchies above: not *what* each source's top-level classes are, but what metalevel word (if any) that source's own material uses for the general notion of "a top-level organizing category." XwkOnt's own organizing unit is **Concept** (`ADR-0011`, which considered and rejected "primitive" as XwkOnt's own term). Each source's own word documented here (e.g. DOLCE's "category," GFO's "Category"/"Universal") is that source's own **Term** for its internal analog of a Concept — reusing `ADR-0011`'s existing Concept/Term relationship rather than introducing a separate name for this role; `ADR-0019` considered and explicitly walked back naming it "Category" as a second formal term. This table is purely descriptive of the eight *sources'* own self-description, not a proposal to rename anything XwkOnt uses. Per Source First / Neutrality (`docs/ARCHITECTURAL_PRINCIPLES.md`), this is reported as found, with gaps flagged honestly rather than filled in.

| Source | Concept Term(s) Found | Quotation | Locator | Confidence |
|---|---|---|---|---|
| **BFO 2020** | "category" (via ISO/IEC 21838-1 §3.19, inherited — BFO is published as ISO/IEC 21838-**2**) | BFO's own site/README describe what BFO contains (object, process, etc.) with no self-standing metalevel term — but BFO does not need one: ISO/IEC 21838-1 §3.19 defines "category" as "a general class or type... shared across many different domains, represented by a domain-neutral term," and §3.20 defines "top-level ontology" as one "created to represent the categories... shared across a maximally broad range of domains" — the normative vocabulary BFO inherits by being Part 2 of the same standard. | `http://bfo-ontology.github.io/BFO-2020/`; `https://github.com/BFO-ontology/BFO-2020` README; ISO/IEC 21838-1:2021 §3.19–3.20 | quote-verified (via governing standard, not BFO's own module text) |
| **DOLCE** | "basic categories" / "categories" | Section 3.2 heading "Basic categories"; "The taxonomy of the most basic categories of particulars assumed in DOLCE is depicted in Figure 2. They are considered as rigid properties, according to the OntoClean methodology..."; also §5.2 "Basic Categories," Fig. 2 caption "Taxonomy of DOLCE basic categories." | `https://www.loa.istc.cnr.it/old/Papers/D18.pdf` (WonderWeb D18, `xwkont:ref:dolce-wonderweb-d18`) | quote-verified |
| **SUMO** | "category" / "categorial" | "The former category includes everything that has a position in space/time, and the latter category includes everything else" (re: Physical/Abstract); "there is a basic, categorial distinction between objects and processes" (re: Object/Process). | `Merge.kif` (existing `xwkont:ref:sumo-niles-pease-2001` locator) and `https://www.adampease.com/FOIS.pdf` (fallback mirror of the Niles & Pease FOIS paper) | quote-verified |
| **UFO** | not found | The 2021 Applied Ontology paper's already-fetched extraction notes (`xwkont:ref:ufo-2021`) discuss Endurant/Perdurant, Moment, Kind, but contain no authorial metalevel term for "top-level organizing category" itself; the paper's DOI remains paywalled, consistent with the block already logged in `ADR-0015` and this matrix's Cross-Cutting Observation 3. | `xwkont:ref:ufo-2021` (existing extraction notes; no new fetch this pass) | not-found |
| **GFO** | "Category" / "Universal" (as literal, defined class names, not just labels) | Class `Category`: "Categories satisfy the following conditions: (1) Categories can be instantiated; (2) Categories can be predicated of other entities. Categories are defined intensional-with-an-s. They are, therefore, closely related to language." Class `Universal`: "Universals are immanent universals. They exist in re." | `https://onto-med.github.io/GFO/release/latest/index-en.html` (redirected from `https://w3id.org/gfo/base`) | quote-verified |
| **YAMATO** | "top-level categories" | Section 2.2 heading "Top-level categories"; "Fig. 1 shows the top-level categories of YAMATO... A more finer-grained view of YAMATO is shown in Fig. 2 that reveals its features," captioned "Fig. 2 Detail version of top-level categories." | `https://www.hozo.jp/onto_library/YAMATO101216.pdf` | quote-verified |
| **TUpper** | "category" (via ISO/IEC 21838-1 §3.19, inherited — TUpper is published as ISO/IEC 21838-**4**) | `tupper.clif` has no descriptive prose beyond a license header and imports; `TUpper-Terms.html` defines `object`/`activity`/`activity_occurrence`/`timepoint` via "is a member of the class of..." — using "class," a generic OWL/CLIF term, not a distinct metalevel word. Same inheritance logic as BFO applies: TUpper doesn't need its own term because ISO/IEC 21838-1 §3.19 already supplies "category" as the standard's normative vocabulary for exactly this notion. | `https://raw.githubusercontent.com/gruninger/colore/master/ontologies/tupper/tupper.clif`; `.../tupper/TUpper-Terms.html`; ISO/IEC 21838-1:2021 §3.19 | quote-verified (via governing standard, not TUpper's own module text) |
| **GUM** | "category" (applied to the single root node, not the whole scheme) | `GUMThing`'s class comment: "The most general experiential category that can be expressed through the resources of the lexicogrammar of a language." | `ref-gum-owl.md`'s existing verified Wayback-snapshot quotation (2026-07-02); live `web.archive.org` re-fetch was blocked in this research pass, so this row reuses the prior on-file verification rather than a fresh read this session. | quote-verified (via prior repo record) |

**Pattern (updated 2026-07-04):** 7 of 8 sources trace to some form of "category" for this metalevel notion once governing-standard inheritance is accounted for — DOLCE, SUMO, GFO, YAMATO, GUM self-describe it directly; BFO and TUpper inherit it from ISO/IEC 21838-1 §3.19 rather than repeating it in their own module text, since they are published as Parts 2 and 4 of that same standard. GFO alone additionally has "Universal" as a second, separately-defined literal class. Only UFO (not ISO-governed, and its own paper paywalled) has no traceable metalevel term at all in the material checked.

## Deferred Questions

1. Should the UFO 2021 paper's Endurant/Event/rigidity taxonomy be pursued via an alternate non-paywalled mirror (author's page, preprint), given it's now blocked twice across two different reference records?
2. Should GFO's `situation/` submodule and DOLCE's full (non-Lite) module be fetched and added to this matrix, given both were flagged as incomplete here?
3. Does this matrix change anything about the `TODO.md` Time candidate-concept item, or the closed `ADR-0017` Reality decision? (Initial read: reinforces Time's candidacy per Observation 2; does not disturb `ADR-0017`, since none of these top-level trees contain a class comparably named/scoped to "Reality" itself.)
4. Should BFO, UFO, and TUpper be re-checked against a broader set of each project's own secondary material (e.g. BFO's own tutorial/user-guide documents, if any exist beyond the spec and README) before concluding they have no metalevel term at all, or is the current fetched material sufficient to report "not-found" as a stable finding?

## References

- `docs/references/ref-bfo-2020.md`, `ref-dolce-lite-owl.md`, `ref-dolce-wonderweb-d18.md`, `ref-sumo-niles-pease-2001.md`, `ref-ufo-2021.md`, `ref-gfo.md`, `ref-yamato-mizoguchi-2010.md`, `ref-tupper-colore.md`, `ref-gum-owl.md`
- `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md`
- `docs/adr/ADR-0017-exclude-reality-as-a-crosswalk-concept.md`
- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md`
- `docs/methodology/primary-source-verification.md`
