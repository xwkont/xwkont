# ADR-0019: Reinforce "Concept" Against Ontology-Alignment/Meta-Ontology Practitioner Usage

- **Status:** Accepted
- **Date:** 2026-07-04

## Context: Why This Review Happened

`ADR-0011` justified "Concept" as XwkOnt's organizing unit, but only against ISO 1087, SKOS, Description Logic, OWL/RDFS, and the source ontologies' own labels (BFO/UFO's "Universal," SUMO's "Class," Cyc's "Collection"). The maintainer raised a sharper concern directly: XwkOnt's stated purpose is to be a *reference* trusted and used by working ontologists — not a terminology-science exercise read only by terminology scientists. A project that reinvents or misapplies the field's own vocabulary risks being dismissed as "another wannabe," exactly the credibility failure XwkOnt cannot afford if its whole value proposition is being a trustworthy crosswalk. `ADR-0011`'s survey never checked whether "Concept" is actually what the **ontology-alignment/matching practitioner community** or the **meta-ontology research tradition** call this notion. This ADR is that check, done honestly — including the points where the investigation initially pointed away from "Concept," not just the ones that confirmed it.

## Deliberation: How the Investigation Actually Went

**1. Three candidates entered the room.** "Concept" (status quo), "Category" (surfaced when checking what each of the 8 source ontologies calls its own top-level notion), and "Entity" (surfaced when checking SSSOM and OAEI, the ontology-alignment standards this project already cites). All three looked initially plausible.

**2. The first real finding pointed away from "Concept."** Checking SSSOM's own schema, Euzenat & Shvaiko's canonical ontology-matching definitions (the literature underlying OAEI), and ISO/IEC 21838-1 (the standard BFO and TUpper are literally published under) all turned up a different word than "Concept" — "Entity" from the alignment community, "Category" from ISO 21838. Neither community uses "Concept" as its own umbrella term for this notion. Taken at face value, this looked like a real problem for `ADR-0011`.

**3. A matrix column made the "Category" finding concrete, and complicated it.** Building a per-source terminology cross-reference (`docs/evaluations/foundational-ontology-concept-terms-matrix.md`) found DOLCE, SUMO, GFO, YAMATO, and GUM directly self-describe their own top-level notion as some form of "category" — 5 of 8 sources, a strong signal. Re-checking BFO and TUpper specifically (they hadn't self-declared a term) found they didn't need to: both are published as Parts 2 and 4 of ISO/IEC 21838, which defines "Category" in §3.19 on their behalf. That raised the count to 7 of 8, with only UFO lacking a traceable term. At this point "Category" looked like the stronger, more field-grounded choice, and "Concept" looked like an outlier.

**4. Checking the meta-ontology tradition (Guarino) didn't settle it — it complicated it differently.** Guarino's earlier work (with Giaretta, 1994-95) used "category" as its own umbrella term. But his most mature, most-cited paper (FOIS 1998) explicitly settled on "a hierarchy of **concepts** related by subsumption relationships." So even within one influential author's own body of work, the term drifted from Category to Concept over time. This ruled out a clean "the meta-ontology tradition agrees with X" resolution either way.

**5. The turning point: recognizing that "category" names each source's own internal analog of the same role, not a competing name for XwkOnt's pivot.** `ADR-0011` already defines a **Term** — "a specific source ontology's label or designation for a concept." Re-reading SSSOM's schema directly (not a summary) showed "Entity" is SSSOM's own name for exactly this Term role (a specific source ontology's own class, e.g. BFO's `object`) — not a competing name for XwkOnt's cross-source pivot. `skos:Concept` is even listed as one valid value inside SSSOM's own `EntityTypeEnum`, meaning SSSOM already accommodates XwkOnt's framing rather than contradicting it.

**6. Checking the closest real precedent — ROMULUS — confirmed the same structure independently.** ROMULUS (Khan & Keet, University of Cape Town) is the one prior project that did almost exactly what XwkOnt does: align BFO, DOLCE, and GFO. Its own methodology paper (KEOD 2013) formally defines a correspondence as a 5-tuple `⟨id, e, e′, r, n⟩` where `e` and `e′` are **entities** drawn directly from each source ontology (`e ⊆ Q_L(o)`) — the same Term-role finding as step 5, independently confirmed. It also surfaced something more important: **ROMULUS's formal model has no pivot notion at all.** It aligns source entities to other source entities, pairwise, with nothing standing between them. XwkOnt's crosswalk files (grouping many pairwise correspondences under one shared heading like "Object" or "Time") are doing something ROMULUS's own formal apparatus never modeled or needed a word for.

**7. An initial attempt to name each source's own internal analog "Category" (citing ISO/IEC 21838-1 §3.19) turned out to be a wrong turn, corrected before this ADR was finalized.** The idea was: each source's own general, domain-neutral class (BFO's `role`, DOLCE's `physical-object`) plays, *within that one ontology*, the same structural role XwkOnt's Concept plays *across all 8* — so name that role "Category" and treat it as a second, formally-adopted term alongside "Concept." Working through the actual documentation this created (a matrix column, a README passage) surfaced two real problems: (a) citing ISO/IEC 21838-1 as the anchor for *all* sources was anachronistic for the 5 that used "category"-family words years or decades before that 2021 standard existed — only BFO and TUpper are actually governed by it; (b) a column literally headed "Category" containing the value "category" for most rows was circular and conveyed nothing. The maintainer's own read cut through this: each source's own "category" (or "Universal," or whatever it uses) is already fully describable as *that source's own Term for its internal Concept-analog*, using the Concept/Term pair `ADR-0011` already defines — reflexively, one level down — without needing a second formally-named role at all. "Category" survives in this ADR only as a **finding** (the word several sources happen to use), not as an XwkOnt-adopted role name.

## Research Summary Table

| Community checked | Term found | Role it actually names |
|---|---|---|
| SSSOM (`ADR-0009`) — own schema, `EntityTypeEnum` | **Entity** | Source-side item being mapped — XwkOnt's existing **Term**, not the pivot. `skos:Concept` is itself a valid `EntityTypeEnum` value. |
| Euzenat & Shvaiko (canonical ontology-matching literature, underlies OAEI) | **Entity** | Same role — pairwise, source-side. |
| ROMULUS (Khan & Keet) — closest real prior-art project | **Entity** (formal 5-tuple correspondence definition) | Confirms the same, and reveals ROMULUS has **no pivot notion at all** to compare against. |
| ISO/IEC 21838-1 §3.19 (governs BFO Part 2, TUpper Part 4) | "Category" | A finding — what BFO/TUpper's governing standard, and 5 other sources independently, call their own internal general/domain-neutral class. Not adopted by XwkOnt as a second role name (see step 7). |
| Guarino & Giaretta 1995 / KR-94 | "category" | Guarino's earlier usage. |
| Guarino, FOIS 1998 (most-cited) | **Concept** | Guarino's own settled, later usage. |
| MOF (OMG) | Class/Classifier | Confirms `ADR-0011`'s existing, unrelated rejection of "Class." |

## Decision

**"Concept" stands, reinforced by this investigation rather than weakened by it** — but only once the investigation is followed all the way through, not stopped at step 3 above where it initially looked like it was heading toward "Category."

**No second, formally-named role ("Category") is introduced.** Each source ontology's own general, domain-neutral class — and whatever word (if any) that source uses for it — is documented using the Concept/Term relationship `ADR-0011` already defines, applied reflexively: a source's own word (e.g. DOLCE's "category," GFO's "Category"/"Universal," BFO's inherited "Category" via ISO/IEC 21838-1) is that source's own **Term** for its internal analog of a Concept. This requires no new vocabulary and avoids both problems found in step 7 (anachronistic citation, circular column headers).

Mapping assertions run **source-term-to-source-term** (e.g. BFO's `occurrent` ↔ DOLCE's `perdurant`), confirmed against XwkOnt's own existing mapping tables — the same pairwise structure SSSOM, Euzenat & Shvaiko, and ROMULUS all use for their "Entity"-to-"Entity" correspondences. XwkOnt's Concept is the human-readable heading a cluster of those correspondences is filed under, not a third node they pass through.

Not every source has a self-declared term for its own Concept-analog: DOLCE, SUMO, GFO, YAMATO, and GUM self-describe it directly (mostly as "category"); BFO and TUpper inherit "Category" from ISO/IEC 21838-1 (as Parts 2 and 4 of that standard) rather than declaring their own; UFO has none found. `docs/evaluations/foundational-ontology-concept-terms-matrix.md`'s Terminology Cross-Reference records this per-source, without asserting uniformity where none exists. Both of that document's tables use the column heading **"Concept Term"** — reusing `ADR-0011`'s existing Concept/Term pair directly, rather than a heading synonymous with "Category" or any other unadopted label.

## Scope

This ADR does not reopen `ADR-0011`'s Decision, Scope, or Rationale sections — it reinforces the same conclusion with evidence the original survey did not check. It does not introduce "Category" (or any other word) as a second formal organizing-unit term. It does not change any identifier, template field, or artifact structure. It does not change the crosswalk template's mapping-assertion structure (`ADR-0007`, `ADR-0009`), which already runs source-term-to-source-term as described above.

## Consequences

### Positive

- Closes a real, maintainer-raised credibility gap in `ADR-0011` with actual practitioner-literature evidence, not just terminology-science citations, and documents the genuine deliberation — including a wrong turn corrected before publication — rather than a post-hoc-tidy rationale.
- Avoids introducing an unneeded second term: everything this ADR needed to say about source ontologies' own vocabulary is already expressible via `ADR-0011`'s existing Concept/Term pair, applied reflexively.
- Zero migration cost — no identifier, template, or crosswalk-content change required.

### Trade-offs

- Some ontologists specifically steeped in the ISO 21838/BFO tradition may still expect "Category" to be XwkOnt's own pivot term, having not read this reasoning; the credibility bet is that the visible reasoning here — including the wrong turn and its correction — is what earns trust, not the word choice alone.
- Describing a source's own "category"/"Universal" as "that source's Term for its Concept-analog" is a slightly more abstract framing than a dedicated "Category" label would have been; documentation should stay precise about this to avoid the exact confusion step 7 walked back.

## References

- `docs/adr/ADR-0011-adapt-iso-1087-concept-as-organizing-unit.md` (extended, not superseded)
- `docs/adr/ADR-0009-adapt-sssom-for-mapping-assertions.md`
- `docs/adr/ADR-0015-expand-source-ontology-scope-to-eight.md`
- ISO/IEC 21838-1:2021, Top-Level Ontologies — Part 1: Requirements (§3.1 Entity, §3.2 Class, §3.19 Category, §3.20 Top-Level Ontology)
- `docs/evaluations/comparable-projects-survey.md` (ROMULUS, WFOL)
- `docs/evaluations/foundational-ontology-concept-terms-matrix.md` (Terminology Cross-Reference)
- Khan, Z.C. & Keet, C.M., "Addressing Issues in Foundational Ontology Mediation," KEOD 2013
- Khan, Z.C. & Keet, C.M., "The ROMULUS resource for using foundational ontologies," OWLED 2014
- Guarino, N., "Formal Ontology and Information Systems," FOIS 1998
- Guarino, N. & Giaretta, P., "Ontologies and Knowledge Bases: Towards a Terminological Clarification," 1995
- Euzenat, J. & Shvaiko, P., "Ontology Matching" (canonical ontology-alignment reference)
