# Information Artifact Ontology (IAO) OWL Ontology

> **Local reference identifier:** `xwkont:ref:iao-owl`
> **Slug:** `iao-owl`
> **Editorial status:** `candidate`
> **Created:** `2026-07-01`
> **Modified:** `2026-07-01`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | Information Artifact Ontology (IAO) | An OWL ontology, not a paper — cited as a primary source document per `ADR-0012`'s provisions for non-paper artifacts, following the same pattern as `xwkont:ref:gangemi-dul`. |
| Creator | OBO Foundry IAO working group (Alan Ruttenberg and others, per in-file attribution comments) | The ontology's foundational theory is due to Barry Smith and Werner Ceusters — see `xwkont:ref:ceusters-smith-2015`. |
| Contributor | unknown | |
| Publisher | OBO Foundry / GitHub (information-artifact-ontology/IAO) | |
| Source type | OWL ontology (machine-readable, not a paper) | |
| Version or edition | fetched from the `master` branch, 2026-07-01 | |
| Identifier or URL | <https://github.com/information-artifact-ontology/IAO/blob/master/iao.owl>, PURLs under `http://purl.obolibrary.org/obo/IAO_*` | |
| Access date | 2026-07-01 | |
| Snapshot / Stable identifier | unknown — not yet archived | Checked the Wayback Machine for both the raw GitHub file actually fetched and the canonical `purl.obolibrary.org/obo/iao.owl` PURL; neither has an archived snapshot as of 2026-07-01. A snapshot of the GitHub *blob view* (rendered HTML, not the raw file) does exist, but per `ADR-0012` this is not fabricated as a substitute since it is not the same byte stream that was actually quoted from. |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

This is the actual machine-readable IAO ontology, distinct from `xwkont:ref:ceusters-smith-2015` (the Smith & Ceusters 2015 paper that argues for and explains IAO's theoretical foundations). Cite this reference for IAO's exact class IRIs and formal definitions; cite the 2015 paper for the surrounding theoretical justification and discussion of aboutness.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: Information Artifact Ontology (IAO). OBO Foundry. <http://purl.obolibrary.org/obo/iao.owl>.

**Directly verified 2026-07-01** by fetching the OWL/XML source directly (plain-text RDF, no PDF-extraction workaround needed) and grepping for the relevant class definition.

Key finding used in `docs/crosswalks/concepts/information-artifact.md`: `IAO_0000030` ("information content entity") is defined as `rdfs:subClassOf http://purl.obolibrary.org/obo/BFO_0000031` (BFO's Generically Dependent Continuant), with definition: "A generically dependent continuant that is about some thing." This confirms `xwkont:ref:ceusters-smith-2015`'s prose definition and supplies the exact class IRI, previously recorded as `unknown` in the crosswalk's Source Ontology Correspondences table.
