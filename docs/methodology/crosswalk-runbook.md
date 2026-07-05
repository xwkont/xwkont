# Crosswalk Runbook: Selecting, Sourcing, and Drafting a Concept

> **Status:** Accepted, in active use
> **Date:** 2026-07-04
> **Related specification:** `docs/methodology/crosswalk-methodology.md`, `docs/methodology/primary-source-verification.md`, `docs/governance/contributing.md`, `docs/crosswalks/concepts/TEMPLATE.md`, `ADR-0015`, `ADR-0018`

## Purpose

This is the step-by-step procedure for taking a concept from "candidate" to a `draft` crosswalk ready for maintainer review. It doesn't introduce new rules — it sequences the rules that already exist across `crosswalk-methodology.md` (mapping categories), `primary-source-verification.md` (fetch/extraction technique), `contributing.md` (workflow and evidence expectations), and `TEMPLATE.md` (the artifact shape) into one ordered checklist, because those documents are each correct on their own topic but none of them says "do X, then Y, then Z." This is the process every `0.1.0` and `0.2.0` concept crosswalk actually followed; new concepts (starting with `0.3.0`) should follow the same sequence.

## Step 1 — Confirm the concept is admissible

- Check `TODO.md`'s queue and `docs/evaluations/foundational-ontology-concept-terms-matrix.md` for the candidate's source-count evidence.
- Per `ADR-0018`, a candidate's matrix source-count ranking is the primary admission evidence for a batch; the original seven-point selection checklist (source accessibility, session-sized scope, likelihood of revealing real semantic differences, citability, template fit) is secondary, per-concept scoping guidance — it decides *when* a matrix-justified candidate is ready to work, not *whether* it belongs in the candidate space.
- Record the batch's admission threshold (e.g. `0.2.0` used ≥3 sources) and confirm the candidate meets it before starting research — but treat the seed's source list and count as a hypothesis to verify, not a settled fact (every `0.2.0` concept's seed count changed at least slightly after direct verification; see Step 3).

## Step 2 — Create or confirm the session branch

Following the project's session-based workflow: check out a dedicated working branch from current `main` before drafting. All of this concept's commits happen on that branch.

## Step 3 — Fetch and verify all 8 sources directly

Per `ADR-0015`, every crosswalk checks all 8 source ontologies (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM) — not just the sources the seed named. This is where most of the actual work happens:

1. **Reuse cached artifacts first.** By the time a batch is a few concepts in, most sources' primary files (`bfo-core.ttl`, `DOLCE-Lite.owl`, `Merge.kif`, the UFO 2021 paper's extracted text, `modules/gfo-base.owl`, the YAMATO 2010 report, `TUpper-Terms.html`, `GUM-31.owl`) are already fetched from prior concepts in the same batch — re-grep those rather than re-fetching.
2. **For sources not yet fetched**, use the PDF-extraction technique in `primary-source-verification.md` for paper/report sources (regex `stream...endstream`, zlib-decompress, extract `Tj`/`TJ` text-showing operators) — OWL/RDF files don't need this, fetch and read them directly.
3. **Full-text search each source for the concept**, don't assume the seed's claimed term is right — grep case-insensitively for the working label and plausible synonyms. Confirmed absences are recorded as findings (`non-equivalence` claim type), not silently skipped.
4. **Use each source's own identifier convention** (opaque `BFO_XXXXXXX`/`IAO_XXXXXXX` IDs, DOLCE-Lite's kebab-case names, SUMO's term-name-as-identifier, UFO's "no IRI scheme" for the 2021 paper vs. OntoUML's real IRIs, GFO's `w3id.org/gfo/...` IRIs, YAMATO's identifier-free prose, TUpper's PSL/COLORE term names, GUM's PascalCase) — see `primary-source-verification.md`'s table. Don't invent a placeholder scheme.
5. **Watch for citation-precision traps**: name collisions across sources (e.g. UFO's `category` vs. GFO's `Category` denoting different things), secondary-source misattributions, and a source's own prose discussing a concept informally without reifying it as a class (check whether the real formal treatment lives in a separate, not-yet-adopted module, e.g. DOLCE's DnS) before claiming an absence.

## Step 4 — Fill in the template, section by section

Use `docs/crosswalks/concepts/TEMPLATE.md` directly. Populate in this order (later sections depend on earlier ones):

1. **Scope Note** — selection rationale with real source-count evidence (not backfilled from the seed), what the concept covers and excludes, cross-cutting findings established this session, and whether core.ttl placement is an open question (it almost always is at `draft` stage — a class is only added to `data/ontology/core.ttl` once the crosswalk reaches `reviewed`).
2. **Labels, Alternate Labels, and Source Terminology** — one row per source, including explicit "no class found" rows for confirmed absences.
3. **Source Definitions and Contextual Notes** — the actual quotes/paraphrases, one row per source term, each with claim type (`direct quotation`/`paraphrase`/`editorial observation`/`inference`), reference, and locator recording exactly how it was verified (`**verified**: <file>, fetched and read directly <date>`).
4. **Source Ontology Correspondences** — one row per source with a real correspondence, IRI or "not applicable" per that source's own convention, and an inclusion rationale.
5. **Semantic Comparison Notes** — the cross-cutting philosophical/technical findings, each with a confidence level and supporting references.
6. **Mapping Assertions** — per `crosswalk-methodology.md`'s categories (`exact-equivalence-candidate`, `close-match`, `broader-than`, `narrower-than`, `related`, `overlap`, `incompatible`, `unknown`, `explicit-non-equivalence`). Reserve `close-match` for pairs that are the *same formal kind* differing only in scope/axioms/usage; use `overlap` when the divergence is structural (different formal kind, e.g. a region vs. a quantity, or an abstract vs. a physical classification) — this distinction has been under-applied at least twice (see the `2026-07-04` review-response fixes to `time.md`/`space.md`), so check it explicitly rather than defaulting to `close-match` for anything that seems similar.
7. **Uncertainty, Non-Equivalence, and Open Questions** — every open question, including ones with a recommended resolution — record the recommendation and rationale, but leave the actual decision for maintainer review if it affects `core.ttl` structure. Don't convert unresolved uncertainty into an equivalence claim for convenience.
8. **Provenance and References** — one line per source, stating verification status (`verified`, `verified absence`, `verified absence, scoped`, etc.) and date.
9. **Review History** — leave as `*(unreviewed)*` with a summary of what this drafting pass found, corrected, or left open.
10. **Future Work** — concrete, actionable follow-ups (which uncertainty items to resolve, what to fetch next, what the next concept in the batch should be).

## Step 5 — Self-check before committing

- Re-read `docs/INFORMATION_ARCHITECTURE.md`'s slug/filename rules, local identifier patterns (`xwkont:concept:<slug>`, `xwkont:mapping:...`, `xwkont:ref:...`), and claim-typing rules if this is a new contributor's first crosswalk in a session — don't assume they're memorized.
- Run `docs/governance/contributing.md`'s Review Checklist and the validation commands relevant to the artifact class (crosswalk = Markdown only, no `core.ttl` touch expected at `draft`).
- Confirm every reference used has a `docs/references/ref-*.md` record (or reuses an existing one) per `ADR-0012`.
- `git status --short` clean check before calling the concept done.

## Step 6 — Commit and update navigation

- Commit the new/updated crosswalk file with a `feat:` (new concept) or `fix:`/`docs:` (correction) Conventional Commits message.
- Update `TODO.md`'s batch item with a per-concept findings summary, and `docs/crosswalks/README.md`'s index if this is a new file.

## Step 7 — Batch-level review

Once every concept in the batch is drafted, an external or maintainer review pass checks the batch as a whole — cross-crosswalk consistency (does one crosswalk's finding correct another's, and has that correction actually been applied?), mapping-category strictness, and whether any concept's evidentiary base is too thin to advance with the rest of the batch (`HOLD`) versus ready with targeted fixes (`PASS WITH FIXES`) versus ready as-is (`PASS`). Apply mechanical fixes directly; record scope/structure decisions (e.g. "model as one class or two") as maintainer-confirmable recommendations in the crosswalk's own Uncertainty section rather than silently deciding `core.ttl` structure. A concept that gets a genuine `HOLD` should stay at `draft`, not be pushed to `reviewed` by lowering the evidentiary bar — see `docs/crosswalks/concepts/situation-state-of-affairs.md`'s `uncertainty-001` for a worked example of a concept that failed its own admission bar on direct verification and was left open rather than forced through.

## What this runbook does not cover

- The mapping-category definitions and confidence vocabulary themselves — see `crosswalk-methodology.md`.
- The PDF-extraction technique's implementation details — see `primary-source-verification.md`.
- How a `draft` crosswalk becomes `reviewed` and lands in `core.ttl` — that's a maintainer review decision per `docs/governance/contributing.md` and `docs/governance/release-versioning-policy.md`, not a mechanical step this runbook can specify in advance.
