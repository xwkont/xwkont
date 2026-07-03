# Primary-Source Verification: Recurring Patterns

> **Status:** Editorial/operational note, distilled from the 2026-07-01 verification pass across all 8 concept crosswalks
> **Date:** 2026-07-01
> **Related specification:** `docs/methodology/crosswalk-methodology.md`, `ADR-0012`

## Purpose

A single verification pass moved every concept crosswalk from partially secondary-sourced to directly verified against primary sources. That pass surfaced several patterns — a working extraction technique, per-ontology identifier conventions, and citation traps — that will recur every time this repository adds a crosswalk, a source ontology, or a reference record. This note collects them so they aren't rediscovered from scratch each time.

## 1. The PDF-extraction technique

**Problem:** this environment has no `pdftotext`, `pdfplumber`, or similar, and WebFetch cannot parse compressed PDF content streams directly — it reports failure. But WebFetch **does** save the raw PDF bytes locally even when it can't parse them (look for `[Binary content (application/pdf, ...) also saved to ...]` in its output).

**Solution:** run a small Python script against the saved PDF:

1. Regex-extract every `stream...endstream` block from the raw PDF bytes.
2. `zlib.decompress()` each one (most PDF content streams use Flate/zlib compression).
3. Within each decompressed content stream, regex-match PDF text-showing operators: `(...)  Tj` and `[...] TJ` (the array form — extract the parenthesized string runs inside the brackets, ignoring the numeric kerning adjustments).
4. Join the extracted strings, unescape `\(`, `\)`, `\\`, decode as `latin1` (safe for embedded Type1/TrueType font encodings that aren't quite UTF-8).

This has worked, unmodified, on PDFs from six different hosts/publishers so far: arXiv, AAAI (CDN and conference-proceedings PDFs), CEUR-WS, and a WonderWeb EU-project technical report. Expect it to keep working on similarly-generated academic PDFs.

**Known limitation:** word-spacing is sometimes lost or approximated (PDF renderers space words using kerning adjustments in the `TJ` array, not literal space characters), so extracted text may need `grep`-tolerant patterns (e.g., match ignoring internal whitespace) or manual reading around a matched line. Prefer `strings -n 4 <file> | grep ...` as a first-pass search over raw `grep` on the file, since the raw content stream bytes are binary and `grep` alone often reports zero matches even when the text is present in decoded form.

**Corollary:** OWL/RDF ontology files (`.owl`, `.ttl`) almost never need this — they're plain-text XML/Turtle. Fetch them directly with WebFetch, curl, or the GitHub raw-content URL, and `grep`/read normally. Only PDFs (papers, technical reports) need the extraction workaround.

## 2. Per-source identifier conventions — don't force a uniform scheme

Each source ontology has its own identifier convention; XwkOnt's crosswalks should reflect that difference rather than inventing a placeholder that implies false symmetry.

| Source | Convention | Example |
|---|---|---|
| BFO | Opaque numbered IRIs (`BFO_XXXXXXX`), confirmed against `bfo-core.ttl` | `BFO_0000015` (process) |
| DOLCE (core, D18/DOLCE-Lite) | Human-readable, kebab-case class names in the `DOLCE-Lite.owl#` namespace | `http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl#endurant` |
| DOLCE-driven (Masolo et al. 2004, role/concept literature) | No IRIs in the original KR2004 paper itself; the OWL-native rendering lives in DUL, not core DOLCE-Lite | Cite `xwkont:ref:masolo-vieu-2004` for the theory, `xwkont:ref:gangemi-dul`'s `#Role` for an IRI |
| DUL (DOLCE+DnS Ultralite) | PascalCase class names in the `dul/DUL.owl#` namespace — a distinct, renamed lineage from DOLCE-Lite, not interchangeable | `http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#InformationObject` |
| UFO | **No IRI scheme at all** — the 2021 Applied Ontology paper is natural-language prose. gUFO (`purl.org/nemo/gufo`) is a derived OWL implementation with real IRIs, but this repository deliberately does not treat gUFO as identical to UFO's own theoretical claims (see `xwkont:ref:ufo-2021`'s Source Relation Notes) | Record `not applicable` with that rationale, not a gUFO IRI |
| SUMO | No opaque ID scheme — the term name itself, as it appears in `Merge.kif`, is both label and identifier | `Process`, `Attribute` |
| IAO (BFO extension) | Opaque numbered IRIs (`IAO_XXXXXXX`), same OBO Foundry convention as BFO | `IAO_0000030` (information content entity) |

**Rule of thumb:** before filling in a Source Ontology Correspondence's identifier field, check the source's own convention — don't assume every source uses opaque codes just because BFO does, and don't assume every source is code-free just because SUMO is.

## 3. Citation-precision traps found so far

Secondary sources (including DOLCE's and UFO's *own* comprehensive restatement papers) sometimes misattribute or loosely pair citations. Check the citing document's own bibliography before propagating an attribution:

- **"Borgo et al., 2010" ≠ the DOLCE-driven Role paper.** The 2022 DOLCE paper's own text pairs "Borgo et al., 2010" with "Masolo et al., 2004" when discussing Role — but "Borgo et al., 2010" in that paper's bibliography resolves to Borgo, Carrara, Garbacz & Vermaas (2010), *Formalizations of functions within the DOLCE ontology* — a paper about **functions**, not roles. Attribute Role content to Masolo et al. (2004) alone.
- **"DOLCE Lite Plus" (DLP) and "DUL" (DOLCE+DnS Ultralite) are related but not identical.** DUL's own header states it is "a simplification of some parts of the DOLCE Lite-Plus library" — a later, actively-maintained, renamed successor by the same author (Aldo Gangemi), not a synonym. If DLP's own file is ever fetched independently, diff it against DUL rather than assuming identity.
- **UFO's 2021 comprehensive paper doesn't contain every term the wider UFO literature uses.** "Formal relation"/"internal relation" terminology, for instance, is absent from the 2021 paper's full text even though it's commonly used to describe UFO's relation theory — it traces to earlier UFO-adjacent literature (Guarino & Guizzardi). A full-text grep of the extracted paper is the fastest way to check before citing a term "per UFO."

**General practice:** when a crosswalk cites "Source X's paper, reporting on Source Y" for some claim, and Source Y is independently fetchable, fetch it — this repository found real corrections (not just confirmations) roughly as often as it found simple confirmations.

## 4. Reference-record creation for non-paper artifacts

`ADR-0012` governs this, but the pattern is easy to miss: OWL/RDF ontology files, GitHub repositories, and other non-paper artifacts get their own `docs/references/ref-*.md` record, following the same template as journal articles, with two differences:

- **`Snapshot / Stable identifier` is not optional.** Every reference without a DOI needs either a verified Wayback Machine snapshot URL (check `http://archive.org/wayback/available?url=<url>`, then confirm the returned snapshot actually resolves with a HEAD request before citing it) or the literal string `unknown — not yet archived` if no snapshot exists. **Do not write vague prose like "no separate archival snapshot taken in this pass"** — that was an early mistake in this same verification pass, corrected after re-reading `ADR-0012` properly. `ADR-0012` explicitly forbids fabricating a snapshot URL, so `unknown — not yet archived` is the honest, compliant fallback, not a lesser option.
- **A mirror is not the canonical host.** If the canonical publisher/namespace host doesn't serve the raw file directly (this happened with `loa-cnr.it`'s DOLCE-Lite and the original DLP397.owl), a GitHub mirror or similar is an acceptable fallback, but say so explicitly in the reference record's Version/Locator notes, and snapshot the canonical URL separately if it exists — don't silently conflate "what I fetched" with "the canonical source."

## Cross-reference

This note complements `docs/methodology/sumo-modeling-patterns.md` (a content-level cross-cutting finding) — this one is process-level: how the verification work itself was actually done, so the next verification pass (a new concept, a new source ontology, a fresh reference record) doesn't re-solve the same problems from zero.
