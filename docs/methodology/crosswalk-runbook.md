# Crosswalk Runbook: Selecting, Sourcing, and Drafting a Concept

> **Status:** Accepted, in active use
> **Date:** 2026-07-04 (non-distinct-candidate off-ramp added 2026-07-06, corrected same day after its first real application surfaced two gaps; a lesson-learned subsection added to Step 1 the same day, on not pre-ranking unverified candidates by "evidentiary strength"; a governing principle added the same day, above Step 1, stating explicitly that a crosswalk maps the territory rather than judging it — added after this specific lesson had to be repeated more than once in one session)
> **Related specification:** `docs/methodology/crosswalk-methodology.md`, `docs/methodology/primary-source-verification.md`, `docs/governance/contributing.md`, `docs/crosswalks/concepts/TEMPLATE.md`, `ADR-0015`, `ADR-0018`

## Purpose

This is the step-by-step procedure for taking a concept from "candidate" to a `draft` crosswalk ready for maintainer review. It doesn't introduce new rules — it sequences the rules that already exist across `crosswalk-methodology.md` (mapping categories), `primary-source-verification.md` (fetch/extraction technique), `contributing.md` (workflow and evidence expectations), and `TEMPLATE.md` (the artifact shape) into one ordered checklist, because those documents are each correct on their own topic but none of them says "do X, then Y, then Z." This is the process every `0.1.0` and `0.2.0` concept crosswalk actually followed; new concepts (starting with `0.3.0`) should follow the same sequence.

## Governing principle: a crosswalk maps the territory, it does not judge it

**This principle sits above every step below and applies to all of them, not just admission (Step 1) or the Off-ramp.** Stated directly, per explicit maintainer direction (2026-07-06), after this same lesson had to be repeated more than once in a single session:

A crosswalk's job is to capture the lay of the land — what each source ontology actually says, verified against its own primary artifact, and how the sources relate to or diverge from each other. **If two sources' evidence overlaps, say it overlaps. If a comparison is genuinely uncertain or vague, say it is uncertain or vague.** Do not resolve that overlap or vagueness into a confident conclusion. That resolution — deciding what the overlap or vagueness *means* for XwkOnt's own structure (how many documents to use, whether a candidate is distinct, which of two plausible readings is correct) — is an editorial/scope judgment, and per this repository's standing practice, that judgment belongs to the maintainer, not to whoever is drafting or verifying the crosswalk.

Two concrete failures from the same session prompted this section, both worth reading as worked examples of what NOT to do:

1. **Quality Space/Quale** was first recorded as "resolved... not a distinct concept" — stating a scope conclusion as if it were a settled fact, when only the underlying source-evidence finding (`quality.md` already contains this content) was actually settled. Corrected to "recommended, pending maintainer confirmation" and only marked settled after the maintainer explicitly confirmed it. See this file's own Off-ramp section.
2. **Symbol/Sign/Representation**'s scope-overlap check read `information-artifact.md`'s prose summary and concluded "distinct" — but a second, more mechanical check (comparing the new draft's actual cited evidence against `information-artifact.md`'s own Source Definitions/Correspondences tables) found the two crosswalks share the same primary-source quotation as their respective strongest evidence. That fact is now recorded in both crosswalks' YAML as an explicit, unresolved uncertainty item — not narrowed, not off-ramped, not left ambiguous either. Stated as a fact, on both sides, with the resolution left open.

**What this means in practice, at every step of this runbook:**

- Mapping categories and confidence levels (`crosswalk-methodology.md`) are themselves evidence-based classifications, not free interpretive choices — but the categories `unknown` and `explicit-non-equivalence` exist precisely so that genuine uncertainty or genuine non-overlap can be *stated as such* rather than forced into a stronger claim the evidence doesn't support. Reaching for `unknown` is not a failure to reach a conclusion; recording the actual state of the evidence is the conclusion.
- When a scope-overlap check is required (see the Off-ramp section), it must compare the new draft's actual cited evidence against the existing crosswalk's actual tables — not just its Scope Note or summary prose. A topical read is not the same check as an evidentiary one.
- When independent verification finds a fact that has more than one legitimate resolution (a candidate might be distinct, or might not; a batch composition question could reasonably go either way), record the fact, cite the evidence, and stop. Do not pick the resolution that seems most reasonable and present it as decided. This is not a failure of judgment — it is the correct scope of what a crosswalk-drafting or verification pass is for.
- If you find yourself writing a sentence that reads as a conclusion ("X is/is not a distinct concept," "candidate A is weaker than candidate B," "this exclusion is justified because...") without a cited piece of evidence directly supporting that specific conclusion, stop and ask whether it belongs in an Uncertainty item addressed to the maintainer instead.

## Step 1 — Confirm the concept is admissible

- Check `TODO.md`'s queue and `docs/evaluations/foundational-ontology-concept-terms-matrix.md` for the candidate's source-count evidence.
- Per `ADR-0018`, a candidate's matrix source-count ranking is the primary admission evidence for a batch; the original seven-point selection checklist (source accessibility, session-sized scope, likelihood of revealing real semantic differences, citability, template fit) is secondary, per-concept scoping guidance — it decides *when* a matrix-justified candidate is ready to work, not *whether* it belongs in the candidate space.
- Record the batch's admission threshold (e.g. `0.2.0` used ≥3 sources) and confirm the candidate meets it before starting research — but treat the seed's source list and count as a hypothesis to verify, not a settled fact (every `0.2.0` concept's seed count changed at least slightly after direct verification; see Step 3).
- Verification can also show the candidate isn't distinct at all, rather than just changing its source count — see "Off-ramp" below, which applies once Step 3's research is underway, not as a substitute for starting it.

### Do not rank candidates by "evidentiary strength" before any of them have been verified

**Lesson learned (2026-07-06):** when expanding the `0.3.0` batch from four two-source candidates to include six 1-source ones, two (Non-physical/Social Object, List/Sequence) were excluded as "weakest/least-verified" based on a subjective read of `TODO.md`'s existing hedge-language ("not yet checked elsewhere," "genuinely untested"). On direct comparison, that classification did not survive scrutiny: two of the four candidates that were *kept* (Change, Modality) carry essentially identical hedge-language ("not yet checked whether any other source draws this same distinction," "untested elsewhere"), and a third kept candidate (Ontological Level/Stratum) is explicitly flagged **"weak"** in `TODO.md`'s own pre-existing text — a stronger admission of uncertainty than either excluded candidate had. The exclusion was reversed once this was pointed out.

The mistake was not "using judgment" — pre-verification candidates necessarily carry uncertainty, and that's expected. The mistake was **treating an unsystematic impression of hedge-language as if it were a considered comparison**, arriving at a two-tier split that didn't actually track any consistent criterion across all six candidates it was supposedly applied to. This is a source-strength judgment call, of exactly the kind that Step 1's own admission-threshold logic already governs: at this stage, no candidate at or above the batch's stated threshold (source count, matrix ranking) has actually been through Step 3's verification yet, so nothing is known about their *relative* strength beyond the threshold itself — only Step 3's actual fetch-and-verify work can surface that.

**Rule going forward:** do not exclude a candidate from a batch on a "this one seems weaker" basis unless every candidate at the same nominal tier (e.g. all six 1-source candidates, not just some of them) is compared against the same explicit, stated criteria, with the comparison shown, not asserted. Default to admitting every candidate that meets the batch's stated threshold. If a real resource constraint later requires cutting the batch down, that's a distinct, explicit decision (capacity, not quality) and should be presented to the maintainer as exactly that, not disguised as an evidentiary judgment made before the evidence-gathering step has even run. Genuine evidentiary differences between candidates are a legitimate output of Step 3's verification pass for each concept — that's where "which of these is actually thinner" gets answered, and that answer should inform *future* batch prioritization, not gate entry into the current one.

## Step 2 — Create or confirm the session branch

Following the project's session-based workflow: check out a dedicated working branch from current `main` before drafting. All of this concept's commits happen on that branch.

## Step 3 — Fetch and verify all 8 sources directly

Per `ADR-0015`, every crosswalk checks all 8 source ontologies (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM) — not just the sources the seed named. This is where most of the actual work happens:

1. **Reuse cached artifacts first.** By the time a batch is a few concepts in, most sources' primary files (`bfo-core.ttl`, `DOLCE-Lite.owl`, `Merge.kif`, the UFO 2021 paper's extracted text, `modules/gfo-base.owl`, the YAMATO 2010 report, `TUpper-Terms.html`, `GUM-31.owl`) are already fetched from prior concepts in the same batch — re-grep those rather than re-fetching.
2. **For sources not yet fetched**, use the PDF-extraction technique in `primary-source-verification.md` for paper/report sources (regex `stream...endstream`, zlib-decompress, extract `Tj`/`TJ` text-showing operators) — OWL/RDF files don't need this, fetch and read them directly.
3. **Full-text search each source for the concept**, don't assume the seed's claimed term is right — grep case-insensitively for the working label and plausible synonyms. Confirmed absences are recorded as findings (`non-equivalence` claim type), not silently skipped.
4. **Use each source's own identifier convention** (opaque `BFO_XXXXXXX`/`IAO_XXXXXXX` IDs, DOLCE-Lite's kebab-case names, SUMO's term-name-as-identifier, UFO's "no IRI scheme" for the 2021 paper vs. OntoUML's real IRIs, GFO's `w3id.org/gfo/...` IRIs, YAMATO's identifier-free prose, TUpper's PSL/COLORE term names, GUM's PascalCase) — see `primary-source-verification.md`'s table. Don't invent a placeholder scheme.
5. **Watch for citation-precision traps**: name collisions across sources (e.g. UFO's `category` vs. GFO's `Category` denoting different things), secondary-source misattributions, and a source's own prose discussing a concept informally without reifying it as a class (check whether the real formal treatment lives in a separate, not-yet-adopted module, e.g. DOLCE's DnS) before claiming an absence.

## Off-ramp — when verification shows the candidate isn't distinct

Step 3's verification sometimes shows the candidate doesn't merit its own crosswalk at all: the source terms named in the seed turn out to be already fully covered by an existing `reviewed` concept's own Source Definitions, Comparison Notes, and Mapping Assertions, rather than describing a genuinely separate category. `Quality Space / Quale` (evaluated 2026-07-06, `0.3.0` batch) is the first worked example: its seed terms (DOLCE `quale`/`quality-space`, GFO `Property_value`/`Value_space`) were already directly quoted and mapped inside `quality.md`, and its remaining candidate-concepts.md rows (DOLCE `temporal-location_q`/`spatial-location_q`, YAMATO `quality value`/`categorical`) turned out on direct verification to be genuine subtypes/subdivisions of already-covered material, not a distinct "quality space" category.

**Correction (2026-07-06, same day):** this section's first version got two things wrong when actually applied to `Quality Space / Quale`, both fixed below and folded into the required steps so they don't recur:

- It called the outcome "resolved," implying the *scoping* question ("does this need its own document?") had been decided. Only the underlying source-evidence finding (*"quality.md already contains this content"*) is a settled fact; whether that finding means "no separate crosswalk" is an editorial judgment about how XwkOnt organizes its own artifacts, and this repo's own precedent (`situation-state-of-affairs.md`'s scope-instability question, left open for maintainer review rather than self-decided) says that judgment belongs to the maintainer, not to whoever ran the verification pass — even when that verification was thorough and independently re-checked. Every disposition recorded this way is a **recommendation pending maintainer confirmation**, not a closure, until the maintainer actually says so.
- Retagging `candidate-concepts.md`'s rows away from the original bucket name lost the literal search term ("Quality Space / Quale" no longer appeared anywhere in the file) — exactly backwards for a public contribution backlog whose whole purpose is being searched. The fix is Step 3 below: the original term must survive in the retagged text itself, and the covering concept's own YAML must gain a real, structured pointer back to it (an actual Alternate Label row, not just prose), not only a note in a secondary tracking file.

Do not force a redundant crosswalk document into existence just because a batch slot was assigned to a candidate. Per "Reuse Before Introduce," concluding "not a distinct concept" is itself a legitimate, useful outcome — the honest alternative to inventing a document whose content just restates what already exists elsewhere. When this happens:

1. **Do not create `docs/crosswalks/concepts/<slug>.md` or a YAML SSOT.** There is nothing to encode that isn't already encoded under the covering concept's own identifier.
2. **Record the disposition in `TODO.md`'s batch item as a recommendation, not a closure** — leave the checkbox unchecked (`[ ]`, not `[x]`) and say explicitly "recommended NOT a distinct concept, pending maintainer confirmation," stating which existing concept covers it and why, so the reasoning is auditable later and the maintainer has something concrete to confirm or reject.
3. **Retag every `docs/crosswalks/candidate-concepts.md` row** that fed the now-closed candidate bucket, pointing it at the concept that actually covers it, using the form `<Concept> (was tagged "<original bucket name>"; recommended YYYY-MM-DD, pending maintainer confirmation: <one-line reason>)` — the original bucket name **must** appear verbatim in the retagged text so a literal search for it still finds this row. This file is the public contribution backlog — a row that drops the searched-for term, or that reads as a closed decision, would either send a contributor to a dead end silently or invite them to redo the same investigation.
4. **Add a real Alternate Label to the covering concept's own YAML** (`LabelEntry` with `role: Alternate label`, `label_source: XwkOnt`), naming the resolved-away candidate, plus a Future Work note cross-referencing the evaluation and marking it pending confirmation. This is what makes the covering concept's own canonical file directly searchable by the old candidate name, not just the backlog file — don't rely on prose alone when the schema already has a structured field for exactly this (`docs/crosswalks/concepts/TEMPLATE.md`'s "Alternate label" role).
5. **Update any release/batch tracking** (e.g. `_private/version-roadmap.md`) so running-total arithmetic doesn't keep counting a still-pending candidate as if it might still ship as its own concept, but without asserting the disposition as final there either.
6. **State a concrete revisit condition, not a vague one**, wherever the disposition is recorded. "Revisit later" is not actionable; "revisit if a source is found that reifies the value-space/quality-space layer as an entity independent of a specific quality" is. Source ontologies gain new modules, this repo's own source list can grow (`ADR-0015` already extended it from 4 to 8 sources once), and a candidate recommended as non-distinct today is not settled forever even after maintainer confirmation — record what evidence would change the determination, the same way `uncertainty` items elsewhere record impact and follow-up rather than a bare open flag.

This disposition is a distinct third state from two others already in use, and the terminology should not be conflated:

- **Ungrouped** (`docs/crosswalks/candidate-concepts.md`'s own term) — not yet triaged into any bucket at all. No investigation has happened.
- **"likely NOT core"** (`TODO.md`'s existing flag, e.g. for GUM's fine-grained linguistic leaf classes) — a real, distinct class, judged too fine-grained or source-specific to warrant its own XwkOnt concept, independent of whether it overlaps another concept's content.
- **Recommended non-distinct, pending maintainer confirmation** (this section) — the candidate WAS investigated at crosswalk-attempt depth (Step 3's actual fetch-and-verify work), the finding is that its content is already inside an existing concept, and that finding has been handed to the maintainer as a recommendation, not silently enacted.

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
