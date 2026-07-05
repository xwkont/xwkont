# YAMATO: Yet Another More Advanced Top-level Ontology (Mizoguchi, 2010 technical report)

> **Local reference identifier:** `xwkont:ref:yamato-mizoguchi-2010`
> **Slug:** `yamato-mizoguchi-2010`
> **Editorial status:** `candidate`
> **Created:** `2026-07-02`
> **Modified:** `2026-07-05`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | YAMATO: Yet Another More Advanced Top-level Ontology | A technical report, not the later (2022) peer-reviewed Applied Ontology paper — see Source Relation Notes. |
| Creator | Riichiro Mizoguchi | The Institute of Scientific and Industrial Research, Osaka University. |
| Contributor | not applicable | Single-author report. |
| Publisher | Self-hosted at `hozo.jp` (Mizoguchi's ontology library) | Not a journal or formal publisher. |
| Source type | technical report (PDF) | Dated 2010-12-16 per filename convention (`YAMATO101216.pdf`). |
| Version or edition | 2010-12-16 | Predates the later dedicated 2022 Applied Ontology paper (Mizoguchi & Borgo, `10.3233/AO-210257`). |
| Identifier or URL | <https://www.hozo.jp/onto_library/YAMATO101216.pdf> | No DOI. |
| Access date | 2026-07-02 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20241229221619/https://www.hozo.jp/onto_library/YAMATO101216.pdf> (2024-12-29), verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. | |
| Rights/license | unknown | Not stated on the source page; not guessed. |

## Source Relation Notes

**This is not the 2022 Applied Ontology paper** (Mizoguchi & Borgo, "YAMATO: Yet another more advanced top-level ontology," `10.3233/AO-210257`, `dl.acm.org/doi/10.3233/AO-210257`) that `ADR-0015` originally flagged as YAMATO's dedicated comparative-literature citation. That paper is hosted on the same SAGE/IOS Press `journals.sagepub.com` platform as the blocked `xwkont:ref:borgo-galton-kutz-2022` and returned the identical Cloudflare block (HTTP 403 on direct fetch, 2026-07-02) — not independently verified in this pass, and not cited in this record.

This 2010 technical report is YAMATO's own foundational document, self-hosted and freely fetchable, and predates but substantively overlaps with the 2022 paper's content on the continuant/occurrent (object/process) split — the same terminology and Newtonian/3D-modeling framing recurs in secondary descriptions of YAMATO's later versions. Cite this record for YAMATO's continuant/occurrent-equivalent treatment; if the 2022 paper becomes accessible in a future pass, cross-check against it before raising confidence on any claim sourced only here.

**YAMATO's OWL/Hozo files were not fetched in this pass.** The `hozo.jp` download links (`download.php?filename=...`) require submitting a name/organization/email registration form before releasing the file — this is an access gate, not a fetchability problem, but automating a form submission with fabricated personal details was not attempted. If the OWL file is fetched later (e.g., by the maintainer manually completing the registration), record the class IRIs here and update this note.

## Rights and License Notes

Not stated on the source page or within the PDF; do not assert a license.

## Citation and Locator Notes

Recommended citation: Mizoguchi, R. (2010). *YAMATO: Yet Another More Advanced Top-level Ontology*. Technical report, Institute of Scientific and Industrial Research, Osaka University. `https://www.hozo.jp/onto_library/YAMATO101216.pdf`.

**Direct primary-source verification (2026-07-02):** the PDF was fetched directly and its text extracted using the Flate-decompression + `Tj`/`TJ`-operator technique documented in `docs/methodology/primary-source-verification.md` §1. Relevant passages (Section 2.1, "Basic distinctions"):

- On the overall standpoint: "The standpoint taken in YAMATO consists of Newtonian world point of view and 3D-like modeling, that is, the world is considered as being composed of the three-dimensional Euclidean space with the absolute time and both object(continuant) and process (occurrent) exist with equal importance in a mutually-dependent manner."
- Basic distinction (4), "Continuant(Object) vs. Occurrent(Process)": "This is one of the most controversial issues and has a long history of debate. It is sometimes called 3D model vs. 4D model... YAMATO is based on a solid theory of objects, processes and events, and it deals with them of equal importance (Galton 2009). Furthermore, it clearly identifies events are made of processes and while processes can change, events cannot. We do not use the term perdurant for explaining processes because it blocks to talk about the difference between processes and events."

YAMATO uses "Continuant" and "Occurrent" as its own top-level labels (parenthetically glossed as "Object" and "Process" respectively) — unlike GFO (which uses Presential/Occurrent) or TUpper/GUM (which use no continuant/occurrent-style labels at all). YAMATO explicitly declines to use "perdurant" for its occurrent-side term, and treats objects and processes as mutually dependent rather than one being ontologically prior to the other — a different emphasis from BFO/DOLCE/UFO's framing. No OWL class IRIs are recorded here (see Rights and License Notes on the registration gate above); cite this record by section/quotation, not by IRI.

**Reused for `object.md` (2026-07-02):** Section 5 ("Objects, Processes and Events") gives a relational definition of Object, quoting Galton (2009): "an object is a unity which is what enacts its external processes... the object is the interface between its internal and external processes: it is a point of stability in the world in virtue of which certain processes are characterized as internal and others as external." See `object.md`'s Source Definitions and correspondence row 007.

**Reused for `event.md` (2026-07-02):** the same Section 2.1 "Basic distinctions" passage already quoted above ("it clearly identifies events are made of processes and while processes can change, events cannot") is YAMATO's own explicit process/event distinction — the most direct process/event criterion found among the four ADR-0015 sources. No OWL class IRI available (registration gate not completed). See `event.md`'s Source Definitions and correspondence row 008.

**Reused for `process.md` (2026-07-02):** the same Section 2.1 passage is also YAMATO's only "process" content found in this pass — the report does not subdivide Occurrent/Process into finer-grained classes the way GFO does, so this reuse largely restates `continuant-occurrent.md`'s existing Occurrent(Process) finding rather than adding new evidence. See `process.md`'s Source Definitions and correspondence row 006.

**Reused for `information-artifact.md` (2026-07-02):** a different section of the same PDF ("Ontology of informational objects" / "A conceptual model of representation") was extracted, distinct from the Section 2.1 content used elsewhere. YAMATO gives the most developed Information-Object treatment of any source in this crosswalk: "By representation, we here mean content-bearing thing... A representation is composed of two parts, form and content... it becomes a physical individual only when it becomes a representing thing." Also directly critiques BFO: "BFO deals with representation (informational object) only at the highest level. It is called generically-dependent entity and it is not further elaborated what they are." References an earlier, less-disseminated Mizoguchi (2004) representation paper, not independently fetched. See `information-artifact.md`'s Source Definitions and correspondence row 004.

**Reused for `quality.md` (2026-07-02):** yet another section of the same PDF ("Quality and quantity") was extracted. YAMATO's own abstract names "Quality and quantity" as one of its three main contributions (alongside representation and process/event); it defines a four-tier apparatus (Generic quality type / Quality role type / Quality / Quality instance) and directly engages DOLCE's quality-space concept by name: "One of the most sophisticated property ontologies is found in DOLCE... However, there are other ways of quality description... which seem not to be covered by DOLCEs quality ontology." See `quality.md`'s Source Definitions and correspondence row 006.

**Reused for `relation.md` (2026-07-02):** two further sections of the same PDF were extracted — "Entity and relation" and the concluding "Roles, functions and relations." YAMATO's own text directly denies that relations are abstract: "Relation is sometimes considered as abstract. But it is not true... it is time-dependent and hence cannot be abstract," using "the marital-relation with Mr. A and Ms. B" as its worked example — a direct rebuttal-shaped non-equivalence with SUMO's abstracta treatment. YAMATO also discloses it has no fully elaborated relation theory of its own: "Relations are not incorporated in YAMATO... because Hozo deals with relations... in different worlds," with Hozo (its implementation tool) supplying three built-in relations (is-a, part-of, attribute-of). See `relation.md`'s Source Definitions and correspondence row 006.

**Reused for `role.md` (2026-07-02):** the "Quality and quantity" section (already extracted for `quality.md`) supplies a general Role example: "The notion of quality role satisfies context-dependence which is one of the most important properties of roles. In the case of teacher role, a school is its context in which teacher role is defined" — directly comparable to BFO's own "student role... university" example. The concluding "Roles, functions and relations" section (already extracted for `relation.md`) adds: "roles are defined within a context which they necessarily depends on in our role theory (Mizoguchi 2007)... roles are used in defining all the types in YAMATO" — the most foundational role for the Role concept of any source in this repository, though the full theory is deferred to Mizoguchi (2007), not independently fetched. See `role.md`'s Source Definitions and correspondence row 006.

**Reused for `time.md` (2026-07-04):** the same PDF's full extracted text was searched directly for "time"/"temporal"/"interval" while researching a Time crosswalk. All occurrences are ordinary, undefined vocabulary used to characterize the physical/semi-abstract/abstract split (things "need time and space to exist") and to distinguish action from event ("An action exists in an open interval without either end of the time interval, while an event exists in a closed interval") — never as a dedicated, defined YAMATO class. **No Time category was found in this document.** This is recorded in `time.md` as "not found in the one YAMATO document that is fetchable," not as a flat "YAMATO has no Time category" — YAMATO's OWL/Hozo files remain behind the `hozo.jp` registration gate (unresolved, same status as noted above) and the 2022 paper remains blocked, so the absence claim is scoped to what was actually checked. See `time.md`'s Source Definitions row for YAMATO and its Uncertainty section.

**Reused for `docs/methodology/source-ontology-module-conventions.md` (2026-07-05, checking `ADR-0021`'s YAMATO gap):** the already-extracted 2010 technical report text and a secondary-literature search both found no evidence of YAMATO modularizing itself into a core/base module versus extension modules — no "core" terminology, and no other structural base/extension split found in what's fetchable. Recorded as "not found in what's checked," not a confirmed absence — YAMATO's OWL/Hozo files remain behind the same registration gate noted above, and the 2022 paper remains blocked, so a future pass with either of those artifacts could still surface a modular structure not visible in the 2010 report alone.
