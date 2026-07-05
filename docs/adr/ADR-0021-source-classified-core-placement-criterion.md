# ADR-0021: Core Placement Is Source-Classified, Existentially Quantified — Not Cross-Source Popularity

- **Status:** Accepted
- **Date:** 2026-07-05

## Context: Why This Review Happened

`ADR-0020` defined "core" for XwkOnt (the base module a project's own vocabulary is built from, as distinct from optional extension modules) but explicitly declined to decide which of the 17 currently-`reviewed` concepts actually belong there — that placement criterion was left as separate, not-yet-started work. This ADR is that criterion.

The first framing considered was, again, judgment-based: XwkOnt evaluates each concept's structural importance or cross-source recurrence and sorts it into core or extension by that evaluation. The maintainer rejected this approach a second time, more sharply: XwkOnt should not apply its own judgment about whether a concept is "core" at all. If a source ontology classifies a concept as part of its own core/base module, that classification stands on its own — it is not negated by the fact that other sources don't share it, or that it isn't "widely adopted" across the crosswalk. Wide adoption is a social fact, not a validity criterion (the maintainer's own example: "the world is flat" was widely accepted, and being widely accepted didn't make it true — the inverse holds too: a concept isn't disqualified from being core just because most sources don't happen to treat it that way).

## Deliberation

**1. This isn't a new principle invented for this decision — it's already documented, in three places.** `docs/ARCHITECTURAL_PRINCIPLES.md` already states:
- **Principle 4 — Source First:** *"Authoritative sources remain authoritative. XwkOnt links to, cites, and compares them."*
- **Principle 6 — Neutrality:** *"XwkOnt documents and compares. It does not advocate or replace existing foundational ontologies."*
- **Principle 7 — Open-World Philosophy:** *"The project assumes knowledge evolves."*

Requiring cross-source agreement before honoring one source's own core-module classification would itself be an act of advocacy — XwkOnt asserting "this source's internal structure doesn't count until enough others agree with it," which is exactly the kind of correctness judgment Neutrality rules out, and exactly the "widely-accepted = valid" conflation Open-World Philosophy is written to avoid.

**2. The quantifier has to be existential (∃), not majority-based, once Source First is taken seriously.** If a concept is real evidence against simply requiring "most sources agree it's core," then the honest reading of Source First is: **one** source's own core-module classification is sufficient on its own. Requiring two, or a majority, would be an arbitrary threshold with no more principled grounding than requiring zero (i.e., XwkOnt's own judgment) — it just moves the same problem to a different number.

**3. Tested directly against the concept this whole investigation started from.** Situation/State of Affairs (`situation-state-of-affairs.md`) is the sharpest available test case: GFO's `Configuration`/`Situation` classes live in `gfo-base.owl` — GFO's *own* core module (per `ADR-0020`'s evidence). DOLCE's real treatment lives in its DnS extension. UFO's lives only in the OntoUML vocabulary, this project's own already-established secondary/derived-artifact tier for UFO (used this way across `role.md`, `universal-type.md`, and `situation-state-of-affairs.md` itself). Under this ADR's rule, Situation is core — full stop — because GFO alone places it in GFO's own core, regardless of what DOLCE and UFO do with it internally.

**4. The consequence flagged when this was first discussed (nearly all 17 reviewed concepts will likely qualify as core) is not a defect — it is the correct result of taking Source First seriously, not a sign the rule is too loose.** Most crosswalk correspondences built so far were sourced from a source's own core/base file to begin with, precisely because that is where each source's foundational vocabulary typically lives. A rule that produced a small, hand-picked "core" subset would be the one requiring an undocumented judgment call — this rule doesn't, and that it turns out permissive is a consequence of the evidence, not a design flaw.

**5. This does not touch how trustworthy any individual correspondence is judged to be.** Per the maintainer's own framing, "concept usage can be determined by the user in the concept's crosswalk" — a concept's placement in XwkOnt-core only answers "does this belong in the base module," not "how much should a given ontologist trust this specific correspondence." That judgment already lives in each crosswalk's own confidence values and Semantic Comparison Notes, untouched by this ADR.

## What Counts as a Source's Own "Core" — Verified So Far

| Source | Core artifact (verified) | Extension artifact(s) (verified) | Status |
|---|---|---|---|
| BFO | `bfo-core.ttl` (`21838-2/owl/`, `BFO-ontology/BFO-2020`) | Separate relation-ontology / IAO extension files | Modularized, directly verified (`ADR-0020`) |
| DOLCE | DOLCE-Lite (2009-relabeled "DOLCE-CORE") | DnS (`ExtendedDnS.owl`) | Modularized, directly verified (`ADR-0020`, this session's `situation-state-of-affairs.md` pass) |
| GFO | `modules/gfo-base.owl` | `modules/situation/*.ttl`; the parallel `gfo-core:` namespace found inside the situation module (GFO's own README: "parallel extensions... not all... consistent") | Modularized, directly verified (`ADR-0020`, this session) |
| UFO | The 2021 comprehensive paper (Guizzardi et al.) — UFO's own primary theoretical exposition | The OntoUML vocabulary artifact — a derived modeling-notation artifact, already treated as secondary/fallback evidence throughout this repository's existing crosswalks | Not file-modularized the way BFO/DOLCE/GFO are, but already artifact-tiered by this project's own established practice — reused here, not newly invented |
| SUMO, YAMATO, TUpper, GUM | Not checked in this pass | Not checked in this pass | **Unresolved** — only matters for a concept whose *sole* supporting source is one of these four; not yet a blocker for any of the 17 concepts, all of which have at least one BFO/DOLCE/GFO/UFO correspondence |

## Decision

**A concept belongs in XwkOnt's core module (`xwkont-core:`, `data/ontology/core.ttl`) if at least one contributing source ontology's correspondence for that concept is drawn from that source's own core/base-module artifact — existentially quantified, not majority-quantified.** No cross-source popularity, adoption-count, or structural-importance filter is applied on top of this. A source placing a concept in its own extension tier does not count against that concept's core status if any other contributing source places it in that source's own core tier; a concept whose *every* contributing source locates it only in that source's own extension tier does not qualify for XwkOnt-core under this rule (it may still be a real, `reviewed` Concept — placement and review status are independent, per `ADR-0020`'s own scope).

This is a placement criterion, not a re-review — it does not change any crosswalk's editorial status, confidence values, or mapping assertions. It only answers the single question `ADR-0020` deferred: does this concept go in the base module or an extension module.

## Scope

This ADR does **not**:

- Apply this criterion to the 17 currently-`reviewed` concepts and sort them — that remains a separate, mechanical (not judgment-based) follow-on pass: for each concept, check whether any of its Source Ontology Correspondences rows cites a source's own core/base artifact (largely already recorded in each crosswalk's existing Reference column) against the table above.
- Resolve SUMO/YAMATO/TUpper/GUM's own internal core/extension modularization (if any) — deferred until a concept's placement actually depends on one of those four sources alone.
- Decide the physical file/directory/namespace structure of XwkOnt's own future extension module(s) — still separate implementation work per `ADR-0020`.
- Revisit the original 8 `0.1.0` concepts already in `core.ttl` — no re-verification is required or proposed; nothing in this ADR casts doubt on their existing placement.

## Consequences

### Positive

- Closes `ADR-0020`'s deferred placement question with a rule that requires zero XwkOnt-side structural judgment, fully consistent with Source First, Neutrality, and Open-World Philosophy as already documented — not a new principle invented for this decision.
- Directly testable against evidence already collected: most of the per-source core/extension classification work for BFO, DOLCE, GFO, and UFO was already done incidentally across this session's `situation-state-of-affairs.md` investigation and `ADR-0020` itself.
- Avoids an unprincipled numeric threshold (why 2 sources and not 3, or a majority) that a stricter quantifier would have required defending.

### Trade-offs

- Likely results in most or all of the 17 reviewed concepts qualifying as XwkOnt-core, leaving the extension tier sparsely populated (or empty) until weaker-evidence future batches (per the internal version-roadmap's queued, 1–2-source-threshold candidates) are drafted and reviewed — the tier this ADR makes room for may not see real use for some time.
- SUMO/YAMATO/TUpper/GUM's own core/extension structure (if any) remains unresolved; a future concept whose only source is one of these four will need that gap closed before this rule can be applied to it.

## References

- `docs/adr/ADR-0020-define-core-as-base-module-not-domain-tier.md` (extended, not reopened)
- `docs/ARCHITECTURAL_PRINCIPLES.md` (Principle 4 — Source First; Principle 6 — Neutrality; Principle 7 — Open-World Philosophy)
- `docs/crosswalks/concepts/situation-state-of-affairs.md` (the test case: GFO core-classified, DOLCE/UFO extension-classified)
- `docs/references/ref-gfo.md`, `docs/references/ref-dolce-borgo-2022.md`, `docs/references/ref-bfo-2020.md`, `docs/references/ref-dolce-extendeddns-owl.md` (per-source core/extension evidence)
