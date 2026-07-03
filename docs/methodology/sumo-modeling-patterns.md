# SUMO Modeling Patterns Across Crosswalks

> **Status:** Editorial observation, cross-referenced from four concept crosswalks
> **Date:** 2026-07-01
> **Related specification:** `docs/methodology/crosswalk-methodology.md`

## Purpose

Four of XwkOnt's concept crosswalks — `quality.md`, `role.md`, `relation.md`, and `information-artifact.md` — independently found that SUMO classifies the same rough conceptual territory (dependent particulars, relational particulars, informational content) differently from BFO, DOLCE, and UFO, all of which converge on a shared metaphysical treatment. Each crosswalk recorded this locally as an `editorial observation`; this note collects the pattern across crosswalks so it doesn't have to be rediscovered independently each time, and — just as importantly — states clearly where the pattern *doesn't* hold, so it isn't overgeneralized into a blanket rule about SUMO.

This is a descriptive cross-cutting observation, not a new mapping category or a claim that SUMO is wrong. Per `docs/methodology/crosswalk-methodology.md`'s neutrality rules, XwkOnt does not resolve or rank the source ontologies' modeling choices — this note only makes an already-scattered pattern easier to see.

## The pattern: dependent/relational particulars become SUMO abstracta

For three concepts, BFO, DOLCE, and UFO all treat the concept as a **particular** (a trope, in the philosophical-literature sense) that existentially depends on, or is otherwise tied to, a specific bearer. SUMO instead classifies its analog as an **abstract entity** — a member of SUMO's `Abstract` branch, disjoint from `Physical`, and not itself dependent on any bearer in the way BFO/DOLCE/UFO's analogs are.

| Concept | BFO / DOLCE / UFO treatment | SUMO's analog | SUMO's formal classification |
|---|---|---|---|
| Quality (`quality.md`) | A particular ("trope") existentially dependent on a specific bearer (BFO: inherence; DOLCE: quale/quality-space, citing Goodman 1951 and Campbell 1990's *Abstract Particulars*; UFO: Husserlian "Moment," citing Moltmann 2020) | `Attribute` | `(subclass Attribute Abstract)` — "Qualities which we cannot or choose not to reify into subclasses of." Confirmed directly against `Merge.kif`. |
| Role (`role.md`) | An anti-rigid, dependent/relationally-conditioned type (DOLCE-driven literature: `Concept`/`Role`, anti-rigid and founded; UFO: anti-rigid sortal specializing a Kind) | `SocialRole` | `(subclass SocialRole RelationalAttribute)` — itself a partition of `Attribute`. "The Class of all Attributes that specify the position or status of a CognitiveAgent within an Organization or other Group." Confirmed directly against `Merge.kif`. |
| Relation (`relation.md`) | A mediated or intrinsic dependency between particulars (BFO: `Relational Quality`, a subtype of Quality; DOLCE: immediate/mediated relation; UFO: formal/material relation, the latter requiring a reified `Relator`/`Mode` truthmaker) | `Relation` | `(subclass Relation Abstract)`, `(partition Relation Predicate Function)` — "The Class of relations... Predicates and Functions both denote sets of ordered n-tuples." Confirmed directly against `Merge.kif`. |

Each of these three was independently confirmed by direct primary-source reading (not inferred from a secondary summary), and each crosswalk's own `note-001` records the same underlying observation: BFO/DOLCE/UFO model the concept as a dependent particular tied to a bearer, and SUMO instead models it as an abstract entity in its own right. By the third instance (`relation.md`), the crosswalks stopped treating this as a coincidence and started treating it as a systematic feature of how SUMO structures its entire dependent/relational-particular family.

## Where the pattern does *not* hold: Information Artifact

`information-artifact.md` deliberately checked this pattern against a fourth concept and found the **opposite** result. SUMO's analog there, `ContentBearingPhysical` (and its subclass `ContentBearingObject`), is:

`(subclass ContentBearingPhysical Physical)` — "Any Object or Process that expresses content." Confirmed directly against `Merge.kif`.

This sits under SUMO's `Physical` branch, not `Abstract` — the reverse of the Quality/Role/Relation pattern. Meanwhile, BFO's IAO extension (`Information Content Entity`) and DOLCE's DUL-based `InformationObject` both use a *generic-dependence*/non-physical treatment: informational content that can be copied or realized across multiple physical carriers, independent of any single one of them. So for this concept, SUMO is the one tying content directly to a physical bearer, while BFO and DOLCE are the ones treating it as bearer-independent — an inversion of the Quality/Role/Relation pattern, not a repeat of it.

## What this means for reading SUMO crosswalks

**The pattern is concept-specific, not a general SUMO design principle.** It would be a mistake to conclude "SUMO always classifies dependent-particular-like concepts as abstract entities" — `ContentBearingPhysical` refutes that as a blanket rule. What the four crosswalks actually support is narrower: for the specific family of concepts examined here that BFO/DOLCE/UFO treat as *tropes dependent on a bearer* (Quality, Role, Relation), SUMO consistently reclassifies them as abstract entities instead. Informational content is a different kind of concept in SUMO's own scheme — an expression of content borne by a physical carrier, not a trope-like dependent particular — and SUMO's classification choice there tracks that difference rather than contradicting the pattern.

When evaluating a future crosswalk's SUMO analog, check which side of this distinction the concept falls on (dependent-particular-like, or content/expression-like) before assuming either direction of the pattern will hold.

## Source crosswalks and references

- `docs/crosswalks/concepts/quality.md` — `note-001`, `mapping-004`/`mapping-005`
- `docs/crosswalks/concepts/role.md` — `note-001`, `mapping-004`/`mapping-005`
- `docs/crosswalks/concepts/relation.md` — `note-001`, `mapping-004`
- `docs/crosswalks/concepts/information-artifact.md` — `note-001`
- All SUMO quotations above are verified directly against `Merge.kif` (`xwkont:ref:sumo-niles-pease-2001`), 2026-07-01.
