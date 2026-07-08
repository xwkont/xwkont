# Aboutness: Towards Foundations for the Information Artifact Ontology (2015)

> **Local reference identifier:** `xwkont:ref:ceusters-smith-2015`
> **Slug:** `ceusters-smith-2015`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Aboutness: Towards Foundations for the Information Artifact Ontology | |
| Creator | Barry Smith, Werner Ceusters | Confirmed via direct primary-source read (CEUR-WS PDF), 2026-07-01. |
| Contributor | unknown | |
| Publisher | CEUR Workshop Proceedings (Proceedings of the 6th International Conference on Biomedical Ontology, ICBO 2015) | |
| Source type | conference paper | CEUR-WS Vol-1515, regular10. |
| Version or edition | ICBO 2015 | |
| Identifier or URL | <https://ceur-ws.org/Vol-1515/regular10.pdf> | Mirrors also at PhilArchive, PhilPapers, ResearchGate, Semantic Scholar. |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | <http://web.archive.org/web/20250615152714/https://ceur-ws.org/Vol-1515/regular10.pdf> (2025-06-15) | Verified retrievable via the Internet Archive Wayback Machine at time of writing, per `ADR-0012`. CEUR-WS URLs are also themselves intended as permanent, but a timestamped snapshot is recorded regardless per `ADR-0012`'s uniform rule. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This is the primary paper behind the Information Artifact Ontology (IAO)'s core `Information Content Entity` (ICE) definition and the `aboutness` relation, both cited in `docs/crosswalks/concepts/information-artifact.md`. IAO is a separate, actively maintained OBO Foundry ontology built on BFO (not part of BFO-2020's own core release, per `xwkont:ref:bfo-2020`) — this paper is IAO's own foundational/theoretical justification, not the OWL file itself. The paper also proposes (but does not finalize as an implemented revision) a broadened definition of ICE requiring aboutness to a "portion of reality" rather than just an "entity," to handle universals, relations, other ICEs, and configurations as targets of aboutness.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Smith, B., & Ceusters, W. (2015). Aboutness: Towards Foundations for the Information Artifact Ontology. In *Proceedings of the 6th International Conference on Biomedical Ontology (ICBO 2015)*. CEUR Workshop Proceedings, Vol-1515.

**Directly verified 2026-07-01** by fetching the CEUR-WS PDF and extracting text manually (Python `zlib` stream decompression + PDF content-stream `Tj`/`TJ` operator parsing, since no PDF-text-extraction tool was available in this environment and WebFetch could not parse the compressed PDF streams directly — same technique used for the DOLCE 2022, UFO 2021, and Masolo et al. 2004 papers elsewhere in this repository).

Key finding used in `docs/crosswalks/concepts/information-artifact.md`: the paper states IAO's current (as of 2015) formal definition of ICE verbatim: "INFORMATION CONTENT ENTITY =def. an ENTITY which is (1) GENERICALLY DEPENDENT on (2) some MATERIAL ENTITY and which (3) stands in a relation of ABOUTNESS to some ENTITY." It further clarifies: "While every ICE is dependent upon some material entity that is its bearer, ICEs themselves are not material entities" — confirming the crosswalk's paraphrase closely. The aboutness relation is grounded in cognitive acts: "acts of thinking, speaking, hearing, writing and reading... through which ICEs are created, understood, and communicated," consistent with the crosswalk's "aboutness relation has roots in the mental realm" characterization.

**Reused for `information-artifact.md`'s new GUM `Name` correspondence (2026-07-07):** the already-extracted ICE definition above was reused (not re-fetched) as the comparison point for GUM's `Name` class ("An accepted but possibly arbitrary label for some entity"), added as `mapping-009` at `low-medium` confidence — a structural, not source-drawn, comparison.
