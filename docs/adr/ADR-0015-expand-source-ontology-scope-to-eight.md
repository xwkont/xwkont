# ADR-0015: Expand Source-Ontology Scope to Include GFO, YAMATO, TUpper, and GUM

- **Status:** Accepted
- **Date:** 2026-07-02

## Context

Since the first concept crosswalk, XwkOnt's crosswalk practice has treated four source ontologies — BFO, DOLCE, SUMO, UFO — as the project's working scope. This was never a single explicit enumeration in `README.md` or `docs/FOUNDING_PRINCIPLES.md` (neither names specific source ontologies; both describe scope generically as "the world's major foundational ontologies"). It was, instead, a de facto scope established by repeated practice: every concept crosswalk's Source Ontology Correspondence table, `docs/STANDARDS_BASELINE.md`, `docs/evaluations/meta-ontology-standards-evaluation.md`, and multiple ontology-spec documents (`docs/ontology/core-ontology.md`, `core-glossary.md`, `core-axioms.md`, `core-validation.md`) all consistently name the same four.

`xwkont:ref:borgo-galton-kutz-2022` (Borgo, Galton & Kutz, 2022, "Foundational ontologies in action," the editorial introducing an *Applied Ontology* special issue) covers seven foundational ontologies via common modeling cases: BFO, DOLCE, GFO, GUM, TUpper, UFO, and YAMATO. `continuant-occurrent.md` flagged the resulting gap as `uncertainty-004` on 2026-07-01, during the primary-source verification pass, deliberately deferring the scope question rather than deciding it at the same time.

This research (2026-07-02) investigated this question. Its planned first step — directly verifying `xwkont:ref:borgo-galton-kutz-2022`'s full text — was blocked: the paper is behind Cloudflare/paywall protection on every mirror checked (publisher host, DOI redirect, institutional repository, author self-archive pages), not merely difficult to parse. That is recorded in `docs/references/ref-borgo-galton-kutz-2022.md`'s "Full-text access attempt" note; the reference remains `candidate`, not `reviewed`.

Lacking the editorial's own comparative framing, this research instead investigated each of the four non-included ontologies directly:

- **GFO** (General Formal Ontology, Herre et al., Onto-Med research group) — actively maintained; OWL files (`gfo.owl`, `gfo-basic.owl`) in a public GitHub repository (`Onto-Med/GFO`); a GFO 2.0 successor has been in development since 2020 (`Onto-Med/GFO-2.0`). Directly fetchable in the same way BFO's and DOLCE's OWL files already were.
- **YAMATO** (Yet Another More Advanced Top-level Ontology, Mizoguchi, Osaka University, since 1999) — single-maintainer, but has its own dedicated *Applied Ontology* 2022 paper (Mizoguchi & Borgo, `10.3233/AO-210257`) separate from the editorial, and hosted OWL/Hozo files at `hozo.jp`.
- **TUpper** (Grüninger, Ru & Thai) — now part of **ISO/IEC 21838-4:2023** (Top-Level Ontologies, Part 4), the same standards family BFO occupies as ISO/IEC 21838-2. Has its own *Applied Ontology* 2022 paper (`10.3233/AO-220263`).
- **GUM** (Generalized Upper Model, Bateman, University of Bremen) — a linguistically-motivated ontology mediating between natural language and domain knowledge, a different orientation from the other seven's general-purpose top-level framing. Stable OWL DL identifier at `purl.org/net/gum2`. Has its own *Applied Ontology* 2022 paper (`10.3233/AO-210258`).

None of the four lack a fetchable primary source; unavailability is not a reason to exclude any of them. The maintainer, presented with this research, decided to add all four rather than a subset or none.

## Decision

XwkOnt's source-ontology scope is expanded from four to eight: **BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM.**

This is a scope expansion, not a redefinition — the existing four remain exactly as verified in the primary-source verification pass; nothing about their content, confidence values, or identifier conventions changes. The four new sources join the same crosswalk methodology (`docs/methodology/crosswalk-methodology.md`), the same per-source identifier-convention practice (`docs/methodology/primary-source-verification.md` §2 — each source's own native ID scheme, not a forced uniform one), and the same primary-source-verification bar that pass established (direct fetch and extraction, not secondary-source paraphrase) before any crosswalk row can cite them.

Crosswalk-content work itself (adding GFO/YAMATO/TUpper/GUM correspondences across all 8 existing concept crosswalks, and the reference records their primary sources require) is **not** performed by this ADR. It is tracked as future work in `TODO.md`. This ADR settles the scope question; it does not itself do the ~4x expansion of crosswalk content that follows from it.

## Scope

This ADR amends the project's de facto source-ontology scope as reflected in practice across `docs/STANDARDS_BASELINE.md`, `docs/evaluations/meta-ontology-standards-evaluation.md`, and the ontology-spec documents' illustrative source lists. Those documents' existing four-source phrasing is historical/contextual prose (describing what was true when each was written), not a live scope declaration, and is not edited by this ADR — this ADR itself is the authoritative scope statement going forward, consistent with the ADR/README precedence order in `docs/PROJECT_LIFECYCLE.md`. `continuant-occurrent.md`'s `uncertainty-004` is resolved by this ADR and updated accordingly.

This ADR does not change `ADR-0009`'s mapping-assertion schema, `ADR-0013`/`ADR-0014`'s confidence vocabulary, or `docs/INFORMATION_ARCHITECTURE.md`'s crosswalk template structure — a ninth column in the Source Ontology Correspondence table (or four new rows, depending on template layout) is a content change within the existing template, not a template change.

## Rationale

Three considerations favored all four over a subset or none:

1. **Reuse Before Introduce, applied to TUpper specifically:** TUpper's ISO/IEC 21838-4:2023 status makes it, if anything, a *stronger* case for inclusion than SUMO already is (SUMO has no ISO standardization and is the crosswalk's consistently lowest-confidence source). Excluding a ratified standard in the same family as BFO's own ISO/IEC 21838-2 would be inconsistent with why BFO was included in the first place.
2. **No fetchability blocker for any of the four:** the original hesitation (the earlier deferral) was about workload, not availability. This research confirmed all four have real, direct primary sources — three with their own dedicated 2022 *Applied Ontology* papers beyond the blocked editorial, one (GFO) with the most straightforward GitHub-OWL fetch path of any source ontology in the project including the existing four.
3. **Coherence of the comparison set:** GFO, YAMATO, TUpper, and GUM are exactly the four ontologies the Borgo/Galton/Kutz special issue treats as peers of BFO/DOLCE/UFO (and, per SUMO's low-confidence-but-included precedent, GUM's different linguistic orientation is not disqualifying — SUMO already establishes that a structurally different source ontology belongs in the crosswalk if it's independently well-evidenced). Adding a subset would require a principled reason to exclude specific ones, and no such reason survived this research — TUpper is arguably the *strongest* candidate, not the weakest, undercutting a TUpper-only alternative on the grounds that it would exclude equally well-evidenced peers for no clear reason.

## Consequences

### Positive

- Crosswalk coverage now matches the actual comparative literature (`xwkont:ref:borgo-galton-kutz-2022`'s own scope), closing the mismatch `uncertainty-004` flagged.
- TUpper's inclusion strengthens, not weakens, the project's "Reuse Before Introduce" posture — a ratified ISO standard is exactly the kind of source XwkOnt should prioritize crosswalking.
- Each of the four has an independently fetchable primary source already identified, so the eventual verification work (unlike the blocked editorial itself) is not expected to hit the same Cloudflare/paywall wall.

### Trade-offs

- Crosswalk-content workload roughly doubles: 8 existing concepts × 4 new sources = up to 32 new Source Ontology Correspondence rows, each needing the same primary-source-verification rigor applied to the original four, plus new `docs/references/ref-*.md` records for each new source's primary artifacts (GFO's OWL files, YAMATO's paper/OWL, TUpper's ISO standard and/or paper, GUM's paper/OWL). This is substantial future work, not completed by this ADR.
- YAMATO's single-maintainer status is a real, if modest, continuity risk relative to the institutionally-backed GFO and the ISO-standardized TUpper — worth noting in YAMATO's eventual reference record, not a reason to exclude it now.
- `xwkont:ref:borgo-galton-kutz-2022` itself remains unverified (full text still inaccessible); the BFO/DOLCE framing claim it's currently cited for in `continuant-occurrent.md` is unaffected by this ADR and remains an open citation gap.

## References

- `docs/crosswalks/concepts/continuant-occurrent.md` (`uncertainty-004`, now resolved)
- `docs/references/ref-borgo-galton-kutz-2022.md` (full-text access attempt, 2026-07-02)
- `docs/methodology/primary-source-verification.md` (per-source identifier convention practice, to be extended to the four new sources)
- `docs/STANDARDS_BASELINE.md`, `docs/evaluations/meta-ontology-standards-evaluation.md` (historical four-source context, not edited by this ADR)
- ISO/IEC 21838-4:2023 (TUpper)
