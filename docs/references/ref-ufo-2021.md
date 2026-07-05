# UFO: Unified Foundational Ontology

> **Local reference identifier:** `xwkont:ref:ufo-2021`
> **Slug:** `ufo-2021`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | UFO: Unified Foundational Ontology | |
| Creator | Giancarlo Guizzardi, Alessander Botti Benevides, Claudenir M. Fonseca, Daniele Porello, João Paulo A. Almeida, Tiago Prince Sales | Author order confirmed via DOI resolver metadata (ACM/SagePub listing). Corrects an earlier draft's uncertain ordering. |
| Contributor | unknown | |
| Publisher | Applied Ontology (IOS Press) | |
| Source type | journal article | |
| Version or edition | Applied Ontology, vol. 17, 2021, pp. 167-210 | An earlier companion paper, Guizzardi, Wagner, Almeida & Guizzardi (2015), "Towards ontological foundations for conceptual modeling: The unified foundational ontology (UFO) story," Applied Ontology 10, pp. 259-271, is related — see Source Relation Notes. |
| Identifier or URL | DOI: `10.3233/AO-210256` (<https://doi.org/10.3233/AO-210256>) | Per `ADR-0012`, DOI preferred over the personal-page PDF mirror. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | DOI given above serves as the stable identifier; no separate archival snapshot needed per `ADR-0012`. | |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This 2021 Applied Ontology paper is the comprehensive UFO reference. The 2015 "UFO story" paper (Guizzardi, Wagner, Almeida, Guizzardi) is an earlier, narrower account of the same project; cite the 2021 paper as primary unless a claim specifically traces to the 2015 account. gUFO (a lightweight OWL implementation of UFO) is a derived, non-primary artifact — cite this reference for UFO's own theoretical claims, not gUFO's implementation choices, unless the crosswalk is specifically discussing gUFO.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Guizzardi, G., Sales, T.P., Almeida, J.P.A., Porello, D., Fonseca, C.M., & Benevides, A.B. (2021). UFO: Unified Foundational Ontology. *Applied Ontology*, IOS Press. Endurant/Perdurant (event) definitions used in `docs/crosswalks/concepts/continuant-occurrent.md` are cited to this document.

**Direct primary-source verification (2026-07-01):** the PDF was fetched directly from the author's personal page and its text extracted manually using the same `zlib`-stream-decompression technique used for the DOLCE D18 and 2022 papers (no PDF-text-extraction tool otherwise available in this environment). This found and corrected a significant error in `docs/crosswalks/concepts/object.md`: UFO *does* have a formal `Object` class ("Objects (aka functional complexes) are entities whose parts play differentiated functional roles with respect to the whole"), a leaf species of `Substantial` alongside `Quantity` and `Collective` — the crosswalk's original claim that UFO had no such term was wrong. Also confirmed the formal `Moment` partition (`Relator`/`IntrinsicMoment`, the latter further split into `Mode`/`Quality`) and the `Kind` sortal-pairing mechanism (`ObjectKind`, `QuantityKind`, etc.) used in `object.md`, `quality.md`, and `role.md`.

In the same extraction pass, `docs/crosswalks/concepts/process.md`'s claim that "UFO has no distinct formal `Process` class" was checked and found **correct** (contrast with the `Object` correction above). The paper explicitly flags "process" as an informal label — "there is a special perdurant (which we may call a process, in a very particular sense) that is the life of an endurant" — and its own worked "Jogging Process" example is formally typed as `EventType(JoggingProcess)`, under `EventType` rather than any separate `ProcessType`. No axiom or definition in the paper introduces a class literally named `Process`.

The same extracted text was reused later (2026-07-01) to verify `docs/crosswalks/concepts/role.md`'s Role and Relator content directly, confirming the crosswalk's existing paraphrase: "In UFO, roles are anti-rigid types whose instantiation occur in virtue of relational conditions"; "a relator is a moment (i.e., an existentially dependent entity) that is an aggregation of qua individuals... Externally dependent modes as well as relators serve as truthmakers of material relations."

Reused again for `docs/crosswalks/concepts/relation.md`: confirmed the paper's material-relation/Relator-truthmaker content directly (same quotation as above). Also searched the full extracted text for "formal relation" and "internal relation" specifically — **neither term appears in this paper.** `relation.md`'s citation of this reference for "formal (internal) relation" terminology should be read as consistent-with, not sourced-from, this specific 2021 paper; that half of the formal/material split traces to earlier UFO-adjacent literature not yet fetched in this repository.

Reused again (2026-07-01) for `docs/crosswalks/concepts/continuant-occurrent.md`: confirmed the paper's endurant/perdurant definitions directly ("Endurants are individuals that exist in time with all their parts. Perdurants are individuals that unfold in time accumulating temporal parts...") and resolved that crosswalk's `uncertainty-001` (UFO's philosophical grounding) using the paper's own account of its origin: an initial evaluation of conceptual-modeling languages against Bunge-Wand-Weber ontology, later merging DOLCE with the General Formal Ontology (GFO) on the shared basis of a four-category ontology ("the Aristotelian Square," per Lowe 2006).

Reused again (2026-07-01) for `docs/crosswalks/concepts/quality.md`, fully resolving `uncertainty-002`: confirmed the paper's own Moment/Quality/value-space definitions directly, and found that UFO independently cites Gärdenfors — "quality structures... can be either one-dimensional... or composed of multiple co-dependent dimensions (see also integral dimensions, Gärdenfors, 2004)" — confirming a shared theoretical origin with DOLCE's own Gärdenfors (2000) citation for the same quality-space/value-space apparatus, cited independently by each source rather than one copying the other.

**Reused for `time.md` (2026-07-04):** the already-extracted paper text has no class or term named "Time," "TemporalRegion," "Instant," or "Interval." UFO's only temporal content is indirect, through Perdurant's own definition (already on file above): "Perdurants are individuals that unfold in time accumulating temporal parts." No reified Time category is asserted; this absence is recorded honestly in `time.md` rather than inferred from the Perdurant definition. See also `xwkont:ref:ontouml-vocabulary` for the OntoUML metamodel fallback check (no Time-related class found there either — only `begin`/`end` property stereotypes, not a temporal-region class).
