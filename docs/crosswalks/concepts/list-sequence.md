# List / Sequence

> **Local identifier:** `xwkont:concept:list-sequence`
> **Slug:** `list-sequence`
> **Editorial status:** `reviewed`
> **Created:** `2026-07-07`
> **Modified:** `2026-07-07`

## Scope Note

This candidate is about a source ontology's own reified ordered-collection apparatus, centered on SUMO's `List`/`UniqueList` and GUM's `OrderedObject`/`OrderedSet`, not about:

- the unrelated `sequence` wording used inside other SUMO classes such as `Procedure`, `Plan`, `BinaryNumber`, `SymbolicString`, or `successorClass`;
- GFO's `Symbol_sequence` and YAMATO's "symbol sequence" language, both symbol-vehicle sequence material already claimed by `symbol-sign-representation.md` (still `draft`, not yet `reviewed`) -- a sequence of symbols/signs is a different kind of thing from a general ordered collection of arbitrary items, and this crosswalk does not re-litigate that claim;
- GUM's `ElementList` relation, a part-whole relation type (subclass of `Part`) between a list and its elements, not an entity class -- `mereology-parthood-aggregate.md`'s territory, not this candidate's;
- the broader `Abstract` split already noted in `abstract-concrete.md`, which already records `List` as one of SUMO's abstract-side branches.

Independent re-verification this session found this is a two-source candidate, not the single-source (SUMO-only) framing the Codex draft recorded: GUM's `OrderedObject` ("a type of decomposable object whose parts have an intrinsic ordering of their own; for example, the elements of a list, the carriages of a train, etc.") and its subtype `OrderedSet` ("a set whose elements are ordered") were missed by the drafting pass entirely -- it checked only SUMO's `Merge.kif` and recorded no attempt to check the other 7 sources, contrary to this repository's standing requirement that every crosswalk check all 8. This is now the fourth session in a row (after `time.md`, `space.md`, and `abstract-concrete.md`, per that crosswalk's own `uncertainty-004`) where a candidate's seed or drafting pass undercounted GUM content that direct verification of `GUM-31.owl` found.

BFO, DOLCE, YAMATO, and TUpper were independently checked this session and confirmed absent (informal "sequence" usage only, no dedicated ordered-collection class). UFO was not independently re-checked this session -- the DOI-linked primary source returned HTTP 403 and no other accessible mirror was found; see Future Work.

## Labels, Alternate Labels, and Source Terminology

| Role | Label or term | Source | Language | Notes |
|---|---|---|---|---|
| XwkOnt working label | List / Sequence | XwkOnt | `en` | Working label for the source-side ordered-collection family. |
| Alternate label | Sequence | XwkOnt | `en` | Candidate shorthand only; no source ontology checked in this pass reifies a separate `Sequence` class for arbitrary ordered collections. |
| Source term | List | SUMO | `en` | Dedicated ordered-collection class under `Abstract`. |
| Source term | UniqueList | SUMO | `en` | Narrower subtype of `List` that forbids repeated items. |
| Source term | OrderedObject | GUM | `en` | Dedicated ordered-collection class, subclass of `DecomposableObject`. Missed by the Codex draft; found during this session's independent re-verification. |
| Source term | OrderedSet | GUM | `en` | Narrower subtype of `OrderedObject` (also subclass of `UMSet`). |
| Source term | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | GFO | `en` | `Symbol_sequence` exists but denotes a sequence of symbols/signs (subclass of `Symbol_structure`, GFO's `Category`/type side), not a general ordered collection of arbitrary items -- already claimed by `symbol-sign-representation.md`. |
| Source term | *(no dedicated ordered-collection class found)* | BFO | `en` | Only informal "sequence" usage found (an Information Content Entity example about a protein sequence). |
| Source term | *(no dedicated ordered-collection class found)* | DOLCE | `en` | Only the informal verb "sequenced" found, in prose about events/situations. |
| Source term | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | YAMATO | `en` | All "sequence" occurrences are "symbol sequence" -- the same representation/symbol territory as GFO's `Symbol_sequence`, not a general ordered-collection class. |
| Source term | *(no dedicated ordered-collection class found)* | TUpper | `en` | Only informal "sequences of activity occurrences" prose found, describing Occurrence Trees. |
| Source term | *(not independently re-checked this session)* | UFO | `en` | The DOI-linked primary source (`https://doi.org/10.3233/AO-210256`) returned HTTP 403 during this session's verification pass; no other accessible mirror was found. The Codex draft did not check this source either. See Future Work. |

## Source Definitions and Contextual Notes

| Source | Term or identifier | Dimension | Claim type | Definition, quotation, or paraphrase | Reference | Locator | Notes |
|---|---|---|---|---|---|---|---|
| SUMO | List | technical | direct quotation | "Every List is a particular ordered n-tuple of items." `subclass List Abstract`. | `xwkont:ref:sumo-niles-pease-2001` | `Merge.kif`, class `List`, fetched and read directly 2026-07-07 | The ordered-collection anchor for this candidate. SUMO places it on the `Abstract` side of the Physical/Abstract split already documented in `abstract-concrete.md`. |
| SUMO | UniqueList | technical | direct quotation | "A List in which no item appears more than once." `subclass UniqueList List`. | `xwkont:ref:sumo-niles-pease-2001` | `Merge.kif`, class `UniqueList`, fetched and read directly 2026-07-07 | A stricter source-side subtype, useful as family evidence but not a separate target concept. |
| GUM | OrderedObject | technical | direct quotation | A type of decomposable object whose parts have an intrinsic ordering of their own; for example, the elements of a list, the carriages of a train, etc. (Used to be "Element".) | `xwkont:ref:gum-owl` | `GUM-31.owl.txt`, class `OrderedObject`, fetched and read directly 2026-07-07 | Subclass of `DecomposableObject`. GUM's own comment names "the elements of a list" as its own worked example -- a direct terminological hook to this candidate's scope, missed by the Codex draft, which checked only SUMO. |
| GUM | OrderedSet | technical | direct quotation | A set whose elements are ordered. | `xwkont:ref:gum-owl` | `GUM-31.owl.txt`, class `OrderedSet`, fetched and read directly 2026-07-07 | Subclass of `OrderedObject` and `UMSet`; `owl:disjointWith` `SpaceInterval` and `TimeInterval` (GUM's domain-specific ordered subclasses for spatial/temporal intervals). |
| GFO | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | technical | non-equivalence | `Symbol_sequence` is `rdfs:subClassOf Symbol_structure`, itself `rdfs:subClassOf Category` (GFO's type/universal side) -- a sequence of symbols/signs, not a general ordered collection of arbitrary items. | `xwkont:ref:gfo` | `modules/gfo-base.owl`, class `Symbol_sequence`, fetched and read directly 2026-07-07 | Already claimed by `symbol-sign-representation.md`'s GFO `Symbol`/`Symbol_sequence`/`Symbol_structure` correspondence (still `draft`); not re-litigated here. |
| BFO | *(no dedicated ordered-collection class found)* | technical | non-equivalence | Direct grep of the fetched core artifact found only one informal use of "sequence" (an Information Content Entity example, "the sequence of this protein molecule"), no dedicated ordered-collection class. | `xwkont:ref:bfo-2020` | `21838-2/owl/bfo-core.ttl`, fetched and read directly 2026-07-07 | Scoped absence. |
| DOLCE | *(no dedicated ordered-collection class found)* | technical | non-equivalence | Direct grep of the fetched artifact found only the informal verb "sequenced," used in prose about events/situations having no unifying description ("they can be sequenced by some course"), no dedicated ordered-collection class. | `xwkont:ref:dolce-lite-owl` | `DOLCE-Lite.owl`, fetched and read directly 2026-07-07 | Scoped absence. |
| YAMATO | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | technical | non-equivalence | Every "sequence" occurrence in the fetched report is "symbol sequence," in the same representation/symbol-vehicle discussion as GFO's `Symbol_sequence` -- no general ordered-collection class or apparatus found. | `xwkont:ref:yamato-mizoguchi-2010` | `YAMATO101216.pdf`, `pdftotext`-extracted directly 2026-07-07 | Same territory already claimed by `symbol-sign-representation.md`/`information-artifact.md`; not re-litigated here. |
| TUpper | *(no dedicated ordered-collection class found)* | technical | non-equivalence | The only "sequence" occurrence in the fetched artifact is informal prose describing Occurrence Trees ("the set of all sequences of activity occurrences forms a tree"), not a dedicated ordered-collection class. | `xwkont:ref:tupper-colore` | `TUpper-Terms.html`, fetched and read directly 2026-07-07 (zero occurrences in `tupper.all.owl`/`tupper.clif`) | Scoped absence. |
| UFO | *(not independently re-checked this session)* | technical | editorial observation | This source was not independently re-checked this session. The DOI-linked primary source (`https://doi.org/10.3233/AO-210256`) returned HTTP 403; no other accessible mirror was found. The Codex draft also did not check this source. | `xwkont:ref:ufo-2021` | not fetched this session | Flagged as an open verification gap, not treated as a confirmed absence. See Future Work. |

## Source Ontology Correspondences

| Correspondence ID | Source ontology | Source term | Source identifier or IRI | Source version | Reference | Inclusion rationale |
|---|---|---|---|---|---|---|
| `xwkont:correspondence:list-sequence:001` | SUMO | List / UniqueList | `List`, `UniqueList` | Current `Merge.kif` (directly verified 2026-07-07) | `xwkont:ref:sumo-niles-pease-2001` | SUMO's source-side ordered-collection family: `List` is the anchor class, and `UniqueList` is its narrower subtype. |
| `xwkont:correspondence:list-sequence:002` | GUM | OrderedObject / OrderedSet | `http://www.ontospace.uni-bremen.de/ontology/stable/GUM-3.owl#OrderedObject`, `#OrderedSet` | GUM 3.1 OWL (directly verified 2026-07-07) | `xwkont:ref:gum-owl` | GUM's source-side ordered-collection family: `OrderedObject` is the anchor class (its own comment cites "the elements of a list" as a worked example), and `OrderedSet` is its narrower subtype. Missed by the Codex draft, which checked only SUMO. |
| `xwkont:correspondence:list-sequence:003` | GFO | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | `none` | GFO base module (directly verified 2026-07-07) | `xwkont:ref:gfo` | `Symbol_sequence` exists but denotes a symbol/sign sequence, already claimed by `symbol-sign-representation.md`, not a general ordered collection. |
| `xwkont:correspondence:list-sequence:004` | BFO | *(no dedicated ordered-collection class found)* | `none` | BFO 2020 | `xwkont:ref:bfo-2020` | Scoped absence in the checked core artifact. |
| `xwkont:correspondence:list-sequence:005` | DOLCE | *(no dedicated ordered-collection class found)* | `none` | DOLCE-Lite OWL | `xwkont:ref:dolce-lite-owl` | Scoped absence in the checked artifact. |
| `xwkont:correspondence:list-sequence:006` | YAMATO | *(no dedicated ordered-collection class found; symbol-vehicle sequence only)* | `none` | YAMATO 2010 report | `xwkont:ref:yamato-mizoguchi-2010` | Symbol-sequence territory only, already claimed elsewhere; no general ordered-collection apparatus found. |
| `xwkont:correspondence:list-sequence:007` | TUpper | *(no dedicated ordered-collection class found)* | `none` | TUpper COLORE formalization | `xwkont:ref:tupper-colore` | Scoped absence in the checked artifacts. |
| `xwkont:correspondence:list-sequence:008` | UFO | *(not independently re-checked this session)* | `none` | UFO 2021 paper (not fetched this session) | `xwkont:ref:ufo-2021` | Open verification gap, not a confirmed absence -- primary source returned HTTP 403 this session. |

## Semantic Comparison Notes

| Note ID | Dimension | Claim type | Note | Supporting references | Confidence |
|---|---|---|---|---|---|
| `note-001` | technical | editorial observation | SUMO's `List` is not a prose-only sequence idea; it is a reified abstract class with an explicit ordered-n-tuple definition. `UniqueList` is not a separate peer concept but a stricter subtype. That makes the source-side family clear enough to stand on its own, even though the candidate label uses "Sequence" as project shorthand. | `xwkont:ref:sumo-niles-pease-2001` | high |
| `note-002` | technical | editorial observation | The candidate label's `Sequence` half does not correspond to a separate SUMO class in the checked artifact. The word appears elsewhere in SUMO's prose and documentation (`Procedure`, `Plan`, `BinaryNumber`, `SymbolicString`, `successorClass`), but those are different notions of sequence, not the ordered-list apparatus under `Abstract`. | `xwkont:ref:sumo-niles-pease-2001` | high |
| `note-003` | technical | editorial observation | `abstract-concrete.md` already records SUMO `List` under `Abstract` and notes that `List` had no XwkOnt counterpart yet. This crosswalk is the dedicated home for that residual branch, not a duplicate of the broader abstract/concrete split. | docs/crosswalks/concepts/abstract-concrete.md | high |
| `note-004` | technical | editorial observation | GUM's `OrderedObject` ("a type of decomposable object whose parts have an intrinsic ordering of their own; for example, the elements of a list, the carriages of a train, etc.") and `OrderedSet` ("a set whose elements are ordered") are a genuine second source, missed by the Codex draft entirely -- its Provenance section names only SUMO, with no record of checking the other 7 sources. GUM's own comment uses "the elements of a list" as its worked example, a direct terminological hook to this candidate's scope. | `xwkont:ref:gum-owl` | high |
| `note-005` | technical | editorial observation | This is the fourth session in a row where a candidate's seed or drafting pass undercounted GUM content that direct verification of `GUM-31.owl` found -- `time.md`, `space.md`, and `abstract-concrete.md` (whose own `uncertainty-004` first named this as a possible pattern) each found the same thing. `abstract-concrete.md`'s suggestion that "GUM's OWL file may be systematically under-surveyed relative to the other 7 sources" is now supported by a fourth independent data point. | docs/crosswalks/concepts/abstract-concrete.md, `xwkont:ref:gum-owl` | high |

## Mapping Assertions or Candidate Relations

Per `ADR-0009`, each mapping records a `predicate_id` (SSSOM/SKOS predicate, or none for XwkOnt-only categories) and a `mapping_justification` (SEMAPV term, e.g. `semapv:ManualMappingCuration`) in addition to the free-text rationale.

| Mapping ID | Subject | Relation category | Object | `predicate_id` | `mapping_justification` | Status | Confidence | Rationale | Provenance |
|---|---|---|---|---|---|---|---|---|---|
| `xwkont:mapping:list-sequence:001` | SUMO:List / UniqueList | `close-match` | GUM:OrderedObject / OrderedSet | `skos:closeMatch` | `semapv:ManualMappingCuration` | candidate | high | Both are direct, reified ordered-collection apparatuses (SUMO's `List` under `Abstract`; GUM's `OrderedObject` under `DecomposableObject`), each with a narrower subtype forbidding/imposing an additional constraint (`UniqueList` forbids repeats; `OrderedSet` is a `UMSet` whose elements are ordered). `close-match`, not a stronger exact-equivalence claim, because the two sit in structurally different type hierarchies (SUMO's abstract/physical split vs. GUM's decomposable-object apparatus) and no source itself asserts an equivalence between them. | `xwkont:ref:sumo-niles-pease-2001`, `xwkont:ref:gum-owl` |

## Uncertainty, Non-Equivalence, and Open Questions

| Item ID | Type | Description | Impact | Follow-up |
|---|---|---|---|---|
| `uncertainty-001` | open-question | Where should `xwkont-core:ListSequence` be placed once this candidate is reviewed: directly under `Abstract` (matching SUMO's source hierarchy), under GUM's `DecomposableObject` lineage, or under a more specific ordered-collection branch if the repository later introduces one? | Blocks final core.ttl placement; does not block the crosswalk research itself. | Confirm at review time; for now, note that SUMO places `List` under `Abstract` and GUM places `OrderedObject` under `DecomposableObject` -- two different type-hierarchy lineages for the same descriptive idea. |
| `uncertainty-002` | non-equivalence | The candidate label's `Sequence` half is not a reified class in any source checked this session. It is project shorthand only, and should not be treated as an additional source-side correspondence. | Prevents over-counting the source-side family or fabricating an additional source term. | None needed; recorded here for traceability. |
| `uncertainty-003` | uncertainty | UFO was not independently re-checked this session -- the DOI-linked primary source (`https://doi.org/10.3233/AO-210256`) returned HTTP 403, and no other accessible mirror was found. The Codex draft did not check this source either. | This crosswalk's absence claim for UFO is unverified, not confirmed, unlike the other 6 non-positive sources (BFO, DOLCE, GFO, YAMATO, TUpper independently re-checked this session). | Fetch the UFO 2021 paper via an accessible mirror (or ask the maintainer for one) and full-text search for "list," "sequence," "tuple," and "ordered" before treating this source as a confirmed absence. |

## Provenance and References

- `xwkont:ref:sumo-niles-pease-2001` — SUMO `Merge.kif` / Niles and Pease 2001 record — **verified** directly against `Merge.kif`, 2026-07-07; confirmed `List`, `UniqueList`, and the absence of a dedicated `Sequence` class
- `xwkont:ref:gum-owl` — GUM 3.1 OWL — **verified** directly against `GUM-31.owl.txt`, 2026-07-07; confirmed `OrderedObject` and `OrderedSet` -- missed by the Codex draft
- `xwkont:ref:gfo` — General Formal Ontology (GFO) base module — **verified absence** of a general ordered-collection class directly against `modules/gfo-base.owl`, 2026-07-07; `Symbol_sequence` confirmed as symbol-vehicle-specific, already claimed by `symbol-sign-representation.md`
- `xwkont:ref:bfo-2020` — BFO 2020 — **verified absence** of a dedicated ordered-collection class directly against `21838-2/owl/bfo-core.ttl`, 2026-07-07
- `xwkont:ref:dolce-lite-owl` — DOLCE-Lite OWL translation — **verified absence** of a dedicated ordered-collection class directly against `DOLCE-Lite.owl`, 2026-07-07
- `xwkont:ref:yamato-mizoguchi-2010` — YAMATO technical report — **verified absence** of a general ordered-collection class directly against `YAMATO101216.pdf` (`pdftotext`-extracted), 2026-07-07; all "sequence" hits are symbol-vehicle usage
- `xwkont:ref:tupper-colore` — TUpper COLORE formalization — **verified absence** of a dedicated ordered-collection class directly against `TUpper-Terms.html`/`tupper.all.owl`/`tupper.clif`, 2026-07-07
- `xwkont:ref:ufo-2021` — UFO: Unified Foundational Ontology — **not independently re-checked this session** -- DOI-linked primary source returned HTTP 403; no accessible mirror found. Not a confirmed absence.

## Review History

| Review ID | Date | Outcome | Notes |
|---|---|---|---|
| — | 2026-07-07 | Draft created | Created after direct verification of SUMO `Merge.kif` only. The draft records the ordered `List` / `UniqueList` family, keeps `Sequence` scoped as project shorthand, and leaves core.ttl placement open for review. Provenance section names only SUMO -- no record of checking the other 7 sources. |
| — | 2026-07-07 | Independently re-verified; one source-count correction | Independently re-fetched and re-read `modules/gfo-base.owl`, `21838-2/owl/bfo-core.ttl`, `DOLCE-Lite.owl`, `GUM-31.owl.txt`, `YAMATO101216.pdf` (`pdftotext`-extracted), and TUpper's `TUpper-Terms.html`/`tupper.all.owl`/`tupper.clif` directly. Found a genuine second source the Codex draft missed entirely -- GUM's `OrderedObject`/`OrderedSet`. Confirmed GFO's `Symbol_sequence` and YAMATO's "symbol sequence" language are a different, already-claimed concept (symbol-vehicle sequences, `symbol-sign-representation.md`'s territory), not this candidate's ordered-collection apparatus. UFO was not independently re-checked (DOI returned HTTP 403, no accessible mirror found) -- recorded as an open verification gap (`uncertainty-003`), not a confirmed absence. |
| — | 2026-07-07 | Passed — advanced `draft` → `reviewed` | Meets the reviewed-eligibility criterion (`docs/methodology/crosswalk-runbook.md`) on SUMO alone: `List`/`UniqueList` are declared directly in `Merge.kif`, SUMO's own upper/meta-level module (not a domain-specific `.kif` file), which `docs/methodology/source-ontology-module-conventions.md` already confirms satisfies `ADR-0021`'s placement rule via SUMO's own upper/meta-level-vs-domain split -- the rule requires a source's own core/base-vs-extension classification, not literally the word "core." GUM's `OrderedObject`/`OrderedSet` is additional confirmed content, not a requirement for this advancement; GUM's own module status remains "Inconclusive" per that same conventions doc, unresolved either way. UFO's unverified status (`uncertainty-003`) does not block advancement, consistent with `Ontological Level/Stratum`'s and `Change`'s precedent of advancing once the eligibility bar is met on confirmed sources, with open gaps recorded rather than blocking. |

## Future Work

- Decide whether `xwkont-core:ListSequence` should sit under SUMO's `Abstract` lineage, GUM's `DecomposableObject` lineage, or both/neither, once reviewed.
- Keep `abstract-concrete.md` as the broader abstract/concrete split record; do not duplicate its scope here.
- Fetch UFO's 2021 paper via an accessible mirror and full-text search for "list"/"sequence"/"tuple"/"ordered" before treating UFO as a confirmed absence (`uncertainty-003`).
- Consider whether `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s GUM tree needs a dedicated re-survey pass against the full `GUM-31.owl` class list -- this is the fourth crosswalk in a row to find GUM content the seed/drafting pass missed (`note-005`).
