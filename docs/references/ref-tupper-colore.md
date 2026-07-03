# TUpper (COLORE CLIF/OWL formalization)

> **Local reference identifier:** `xwkont:ref:tupper-colore`
> **Slug:** `tupper-colore`
> **Editorial status:** `candidate`
> **Created:** `2026-07-02`
> **Modified:** `2026-07-03`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | TUpper | A top-level ontology built on PSL (Process Specification Language); this record covers its open CLIF/OWL formalization in COLORE, not the ISO/IEC 21838-4:2023 standard text itself (not accessed in this pass — see Source Relation Notes). |
| Creator | Michael Grüninger | Per the CLIF file's own header comment ("Contributors: Michael Gruninger - initial implementation"), University of Toronto. |
| Contributor | unknown | Full contributor list not verified in this pass; the associated 2022 Applied Ontology paper adds Yi Ru and Jona Thai as co-authors, but that paper was not accessed (see Source Relation Notes). |
| Publisher | University of Toronto; hosted in the COLORE (Common Logic Ontology Repository and Evaluation) GitHub repository, `github.com/gruninger/colore` | |
| Source type | ontology specification (Common Logic / CLIF, with an OWL rendering) | `tupper.clif` is a thin import wrapper over PSL modules (`disc_state`, `psl_actocc`, `occupy_root`, `fount`); term-level informal semantics are documented separately in `TUpper-Terms.html`. |
| Version or edition | unknown — no version metadata in the fetched files | |
| Identifier or URL | <https://github.com/gruninger/colore/blob/master/ontologies/tupper/> (directory); <https://raw.githubusercontent.com/gruninger/colore/master/ontologies/tupper/owl/tupper.all.owl> (OWL); <https://raw.githubusercontent.com/gruninger/colore/master/ontologies/tupper/tupper.clif> (CLIF) | No DOI. |
| Access date | 2026-07-02 | |
| Snapshot / Stable identifier | `https://github.com/gruninger/colore/blob/master/ontologies/tupper/owl/tupper.all.owl` → <http://web.archive.org/web/20221024070550/https://github.com/gruninger/colore/blob/master/ontologies/tupper/owl/tupper.all.owl> (2022-10-24), verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. | |
| Rights/license | CC-BY-SA-4.0 | Per `tupper.clif`'s own header comment ("licensed under the Creative Commons Attribution-ShareAlike 4.0 Unported license"). |
| Archive mirror status | eligible — license permits redistribution, not yet mirrored | Per `ADR-0016`. CC-BY-SA-4.0 is verified from `tupper.clif`'s own header comment (see Rights/license), which is sufficient to make this record eligible; actual mirroring (hosting location, fetch, publish) is separate future work not yet started. |

## Source Relation Notes

**This record covers TUpper's open COLORE formalization, not ISO/IEC 21838-4:2023 itself.** `ADR-0015` and `TODO.md` both flagged TUpper's ISO standardization as its strongest inclusion rationale, but the ISO standard text is a purchasable document not fetched in this pass. Nor was the dedicated 2022 Applied Ontology paper (Grüninger, Ru & Thai, "TUpper: A top level ontology within standards," `10.3233/AO-220263`) accessed — a direct HTTP fetch of its IOS Press content-download URL returned HTTP 403 (Cloudflare block), the same pattern that blocked `xwkont:ref:borgo-galton-kutz-2022` and the YAMATO 2022 paper.

TUpper's own CLIF/OWL files, maintained by the same author (Grüninger) in the public COLORE repository, are directly fetchable and are the authoritative machine-readable formalization TUpper's ISO standardization and paper both describe — Grüninger's COLORE work substantially predates and underlies both. This record treats the COLORE artifacts as a legitimate primary source for TUpper's own vocabulary and definitions, while explicitly not claiming to have verified the ISO standard text's exact wording, which may differ in presentation (though not, per COLORE's stated role as the working formalization, in substance).

TUpper builds on PSL (Process Specification Language, also a Grüninger project); its base vocabulary (`object`, `activity`, `activity_occurrence`, `timepoint`) is inherited from PSL's ontology of activities and objects, not authored fresh for TUpper.

## Rights and License Notes

CC-BY-SA-4.0, per `tupper.clif`'s own header. Not independently cross-checked against a separate repository-level LICENSE file.

## Citation and Locator Notes

Recommended citation: Grüninger, M. *TUpper* (COLORE formalization). University of Toronto. `https://github.com/gruninger/colore/tree/master/ontologies/tupper`.

**Direct primary-source verification (2026-07-02):** `tupper.all.owl`, `tupper.clif`, and `TUpper-Terms.html` were fetched directly from the `gruninger/colore` GitHub repository (`master` branch, confirmed via the GitHub Contents API before fetching, so as not to trust an unverified WebSearch-reported URL) and read directly. TUpper does **not** use continuant/occurrent (or endurant/perdurant) terminology at all; its top-level vocabulary, inherited from PSL, is `object` / `activity` / `activity_occurrence` / `timepoint`. Exact informal-semantics text from `TUpper-Terms.html`:

- `object`: "(object x) is TRUE in an interpretation of TUpper if and only if x is a member of the class of objects in the universe of discourse of the interpretation. An object is anything that is not a timepoint, nor an activity nor an activity-occurrence. Intuitively, an object is a concrete or abstract thing that can participate in an activity. Objects can come into existence (be created) and go out of existence (be 'used up' as a resource) at certain points in time."
- `activity_occurrence`: "(activity_occurrence occ) is TRUE in an interpretation of TUpper if and only if occ is a member of the class of activity occurrences in the universe of discourse of the interpretation. An activity occurrence is associated with a unique activity" via the `occurrence_of` relation.
- `timepoint`: "(timepoint t) is TRUE in an interpretation of TUpper if and only if t is a member of the class of timepoints in the universe of discourse of the interpretation. Timepoints form a linear ordering."

`object` is defined negatively (anything that is not a timepoint, activity, or activity-occurrence) rather than by a positive temporal-persistence criterion — a different definitional style from BFO/DOLCE/UFO's "wholly present at a time" framing, GFO's Presential/Occurrent split, or YAMATO's continuant/occurrent labels. See `continuant-occurrent.md`'s Uncertainty section for how this is handled in the crosswalk's mapping confidence.

**Reused for `object.md` (2026-07-02):** the same `object` term (quoted above) is TUpper's only Object-equivalent — no more specific sub-term exists in the fetched files. See `object.md`'s correspondence row 008.

**Reused for `event.md` (2026-07-02):** `TUpper-Terms.html`'s full `activity_occurrence` entry was read directly, including its NOTE: "An activity occurrence is not an instance of an activity." This is TUpper's closest structural analog to Event, but it is a type/token (occurrence-of) relation, not a Process/Event category split — treated as `unknown` confidence, consistent with `object.md`'s TUpper precedent. See `event.md`'s Source Definitions and correspondence row 009.

**Reused for `process.md` (2026-07-02):** `TUpper-Terms.html`'s `activity` entry (the repeatable type, distinct from the token `activity_occurrence` already used in `event.md`) was read directly: "(activity a) is TRUE in an interpretation of TUpper if and only if a is a member of the class of activities in the universe of discourse of the interpretation." A minimal, circular-looking gloss typical of PSL's axiomatic style — treated as `unknown` confidence against BFO's particular-denoting Process, since `activity` is a type. See `process.md`'s Source Definitions and correspondence row 007.

**Reused for `information-artifact.md` (2026-07-02):** both `tupper.all.owl` and `TUpper-Terms.html` were searched directly for "information," "content," and "represent" — zero occurrences of any of the three. No Information-Artifact correspondence recorded; the most clear-cut absence of any source in that crosswalk. See `information-artifact.md`'s Source Definitions.

**Reused for `quality.md` (2026-07-02):** `tupper.all.owl` was searched for a reified Quality/Attribute/Property class; none was found. Instead, physical measurements (`mass`, `volume`, `physical_length`, `physical_area`, `physical_density`) are declared as `FunctionalObjectProperty` relations directly from an object to a value — a third modeling style, distinct from both the trope-theoretic (BFO/DOLCE/UFO/GFO/YAMATO) and abstract-entity (SUMO) camps. See `quality.md`'s Source Definitions.

**Reused for `relation.md` (2026-07-02):** both `tupper.all.owl` and `TUpper-Terms.html` were searched for a reified Relation class; none was found. Relations are exclusively bare OWL/CLIF binary predicates (`occurrence_of`, `subactivity`, `precedes`, `earlier`, etc.), each documented in prose but never reified as an instance of a "Relation" class — the same non-reification pattern already found for Quality. See `relation.md`'s Source Definitions.

**Reused for `role.md` (2026-07-02):** `TUpper-Terms.html` was searched for a reified Role class; none was found. The word "role" appears only once, informally, inside `participates_in`'s prose gloss: "x plays some role that is not pre-specified in an occurrence of the activity a." No class represents "a role" as a thing in its own right — the third concept in this repository (after Quality, Relation) where TUpper reifies nothing. See `role.md`'s Source Definitions.
