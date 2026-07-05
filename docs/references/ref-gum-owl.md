# GUM: The Generalized Upper Model (OWL, GUM-3.1)

> **Local reference identifier:** `xwkont:ref:gum-owl`
> **Slug:** `gum-owl`
> **Editorial status:** `candidate`
> **Created:** `2026-07-02`
> **Modified:** `2026-07-05`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | GUM (Generalized Upper Model), version 3.1, OWL rendering | A linguistically-motivated ontology mediating between natural-language form and domain knowledge. |
| Creator | John A. Bateman | University of Bremen. |
| Contributor | unknown | Full contributor list not verified in this pass. |
| Publisher | University of Bremen, Faculty 10 (Linguistics/Language Processing group) | Originally self-hosted at `fb10.uni-bremen.de`; that host no longer resolves the ontology page (confirmed 404/dead redirect chain 2026-07-02 — see Source Relation Notes) and the canonical `purl.org/net/gum2` PURL now redirects to a dead link. Retrieved via the Internet Archive Wayback Machine instead. |
| Source type | ontology specification (OWL) | |
| Version or edition | GUM 3.1 (`GUM-31.owl`, part of the `GUM-3.owl` namespace) | An earlier `GUM-3-space.owl` module and a CASL rendering (`GUM.casl`) also exist at the same archived location but were not fetched in this pass. |
| Identifier or URL | Canonical PURL: `https://purl.org/net/gum2` (currently redirects to a dead host chain, confirmed 2026-07-02); archived source: `http://www.fb10.uni-bremen.de/anglistik/langpro/webspace/jb/gum/gum-files/GUM-31.owl.txt` | No DOI for the OWL file itself. |
| Access date | 2026-07-02 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/2021/http://www.fb10.uni-bremen.de/anglistik/langpro/webspace/jb/gum/gum-files/GUM-31.owl.txt> (Wayback Machine, resolved to a 2021-dated capture at fetch time), verified retrievable at time of writing, per `ADR-0012`. The file was fetched *through* this archival URL directly (the canonical host no longer serves it live), so the snapshot and the fetched artifact are the same access, not a separate archival step. | |
| Rights/license | unknown | Not stated in the fetched OWL file's header; not guessed. |

## Source Relation Notes

**GUM's canonical hosting has decayed.** The `purl.org/net/gum2` PURL (cited in `ADR-0015` and `TODO.md` as GUM's "stable OWL DL identifier") now 307-redirects to `purl.archive.org/net/gum2`, which 302-redirects to the original `fb10.uni-bremen.de` page, which 404s (confirmed 2026-07-02) — the live chain is fully dead, not merely slow or paywalled. The Internet Archive Wayback Machine has a working capture of the original index page and its linked `GUM-31.owl.txt` file, which is what this record and `continuant-occurrent.md` cite. If GUM is later republished at a new stable location (e.g., a GitHub mirror), prefer that as the canonical source and retain this record as the historical/archival citation.

**The dedicated 2022 Applied Ontology paper was not accessed.** Bateman, J. A. (2022), "GUM: The generalized upper model," `10.3233/AO-210258`, is hosted on the same platform that blocked `xwkont:ref:borgo-galton-kutz-2022`, the YAMATO 2022 paper, and the TUpper 2022 paper — not independently re-checked in this pass, but assumed blocked by the same pattern given three-for-three prior results.

## Rights and License Notes

Not stated in the fetched file; do not assert a license. The original page (per its archived index) references academic/research use context typical of a university-hosted linguistics ontology, but this is not a substitute for an explicit license statement.

## Citation and Locator Notes

Recommended citation: Bateman, J. A. *GUM: The Generalized Upper Model*, version 3.1 (OWL). University of Bremen. Archived at `http://web.archive.org/web/20211231000000*/fb10.uni-bremen.de/anglistik/langpro/webspace/jb/gum/`.

**Direct primary-source verification (2026-07-02):** `GUM-31.owl` was fetched directly (via the Wayback Machine, per the dead-canonical-host note above) and read directly to verify `continuant-occurrent.md`'s GUM correspondence. GUM does **not** use continuant/occurrent, endurant/perdurant, or any comparable philosophical top-level label — its top-level split is a linguistic one, `SimpleThing` (nominal-group-realized participants) vs. `Process` (verb-realized "goings-on"), both subclasses of `Element`, explicitly `owl:disjointWith` each other. Exact `rdfs:comment` text:

- `SimpleThing` (`http://www.ontospace.uni-bremen.de/ontology/stable/GUM-3.owl#SimpleThing`): "An entity which may participate in a configuration." Subclass of `Element`.
- `Process` (`http://www.ontospace.uni-bremen.de/ontology/stable/GUM-3.owl#Process`): "A Process is the linguistic construal of 'goings-on' or events. Processes are similar to Configurations, but factor out Participants, Circumstances, and other elements. As such, entities classified under Process can be expressed as verbs and are frequently the main verb in a clause." Subclass of `Element`; `owl:disjointWith` `SimpleThing` and `SimpleQuality`.
- `GUMThing` (`http://www.ontospace.uni-bremen.de/ontology/stable/GUM-3.owl#GUMThing`), the ontology's actual top node: "The most general experiential category that can be expressed through the resources of the lexicogrammar of a language. UMThing corresponds to 'phenomena' in Halliday and Mathiessen (1999: 48)." [`sic` — "UMThing" in the source text, likely a typo for "GUMThing" carried over from an earlier "UM" (Upper Model) naming.]

GUM's SimpleThing/Process split is grounded in systemic-functional linguistics (Halliday & Matthiessen), not in a metaphysical persistence criterion — the closest structural analog to BFO's continuant/occurrent in this crosswalk's existing SUMO precedent (`note-003`), not a terminological match. See `continuant-occurrent.md`'s Uncertainty section.

**Reused for `object.md` (2026-07-02):** `DecomposableObject` ("An object that is being viewed as being made up of parts that may be taken apart and are often given explicit linguistic recognition.") and `NonDecomposableObject` ("An object that is being regarded as not possessing significant parts, or which is not to be considered decomposable for present purposes."), both direct subclasses of `SimpleThing` and mutually `owl:disjointWith`, are GUM's closest analog to a single "Object" category. See `object.md`'s correspondence rows 009-010.

**Reused for `event.md` (2026-07-02):** GUM's `Process` class definition (quoted above: "the linguistic construal of 'goings-on' or events") is the only one of the four ADR-0015 sources besides BFO's `skos:altLabel` usage to use the literal word "events" directly in a class definition — but, like BFO, as an informal gloss on a general occurrent-side class, not a separate named Event category. See `event.md`'s Source Definitions and correspondence row 010.

**Reused for `process.md` (2026-07-02):** the same `Process` class (quoted above) is also the only one of the four ADR-0015 sources with a class literally named "Process" — the strongest terminological match to this crosswalk's subject of any new source, though its criterion (verb-realizability) is linguistic rather than temporal/metaphysical. See `process.md`'s Source Definitions and correspondence row 008.

**Reused for `information-artifact.md` (2026-07-02):** `GUM-31.owl` was searched for an Information-Object-equivalent entity class; none was found. The only relevant hooks, `Symbolization` (no `rdfs:comment`) and its subclass `Signification` ("linguistically realized by verbs like 'represent', 'mean', 'express', e.g., 'green means go'"), are relation types (subclasses of `Intensive`), not object/entity types — considered and rejected as a correspondence. See `information-artifact.md`'s Source Definitions.

**Reused for `quality.md` (2026-07-02):** `GUM-31.owl` also supplies `SimpleQuality` ("Qualities are properties of SimpleThings and Processes... anything that can be expressed as an English adjective"), subclass of `Element`, `owl:disjointWith` `SimpleThing`. The only one of the four new sources with a class literally named "Quality" (via subclasses like `MaterialWorldQuality`/`ModalQuality`/`LogicalQuality`), though grounded in adjectival/linguistic realization rather than metaphysical inherence. See `quality.md`'s Source Definitions and correspondence row 007.

**Reused for `relation.md` (2026-07-02):** `GUM-31.owl` also supplies `Relating` ("A configuration indicating a relation holding between two entities. A relating must contain at least a domain and an attribute"), `rdfs:subClassOf` `BeingAndHaving`, itself `rdfs:subClassOf` `Configuration` (a clause-level situation construct containing a `Process`, Participants, and Circumstances). A fourth distinct relation-modeling style — reified, but as a situation/state-of-affairs, not a trope, abstracta, or bare predicate. See `relation.md`'s Source Definitions and correspondence row 007.

**Reused for `role.md` (2026-07-02):** `GUM-31.owl` also supplies `RolePlaying` ("A circumstantial relationship that expresses a restriction in which a facet of one of the participants in a process is relevant for the actualization of the process... frequently realized in English by a prepositional phrase with the preposition 'as'; For example: 'As a president, he was terrible, although as a golfer he was not too bad.'"), `rdfs:subClassOf` `Symbolization`. A relation type, not an object/entity type — the third concept in this repository (after Information Artifact's `Signification`/`Symbolization` and Relation's `Relating`) where GUM reifies this kind of content as a relation rather than an entity. See `role.md`'s Source Definitions and correspondence row 007.

**Reused for `time.md` (2026-07-04):** `GUM-31.owl` was fetched fresh (via `curl` through the same Wayback Machine snapshot — WebFetch itself cannot reach `web.archive.org` in this environment, confirmed again this pass) and found to have by far the richest temporal treatment of any of the 8 sources: 18 distinct classes under a `TemporalObject`/`Time`/`TimeInterval`/`TimePoint` hierarchy (full tree in `time.md`'s Source Definitions), including `Past`/`Present`/`Future`, `TemporallyBounded`/`TemporallyUnbounded`, `DurationInTime`/`InstantaneousInTime`, `OneOrTwoDTime`/`ThreeDTime`, and `ProfilesAndStages`/`TemporalProfile`. Unlike every other source checked, GUM's temporal apparatus is explicitly grounded in Halliday & Matthiessen's (1999) systemic-functional-linguistics theory of the clause, cited by page number directly inside multiple class definitions (e.g. `DurationInTime`: "A Configuration may be take time to unfold or be instantaneous (HM 1999: 471)") — modeling how a clause's temporal profile is grammatically realized (tense, aspect, boundedness), not time as a mind-independent feature of reality. `Time` itself has a dual parent, `rdfs:subClassOf` both `Substance` and `TemporalObject` — neither of GUM's occurrent-like (`Process`) or continuant-like (`SimpleThing`/`DecomposableObject`) classes are ancestors of any temporal class. This corrects `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s Observation 2, which omitted GUM from its list of sources with an explicit Time category entirely. See `time.md`'s Source Definitions and correspondence row 008.

**Reused for `docs/methodology/source-ontology-module-conventions.md` (2026-07-05, checking `ADR-0021`'s GUM gap):** this record's own Descriptive Metadata already notes an unfetched `GUM-3-space.owl` module existing alongside `GUM-31.owl` at the same archived location — suggestive of some modular structure, but a secondary-literature search of Bateman's own GUM papers found no "core" terminology or explicit base/extension description for GUM's own architecture. Recorded as inconclusive, not a confirmed absence — GUM's canonical host is dead (see Source Relation Notes above) and a full site fetch was not attempted in this pass.
