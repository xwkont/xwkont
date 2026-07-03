# <Reference Title>

> **Local reference identifier:** `xwkont:ref:<slug>`  
> **Slug:** `<slug>`  
> **Editorial status:** `draft`  
> **Created:** `YYYY-MM-DD`  
> **Modified:** `YYYY-MM-DD`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | `<title>` | DCMI `title`. |
| Creator | `<name/unknown>` | DCMI `creator`; do not guess. |
| Contributor | `<name/unknown/not applicable>` | DCMI `contributor`. |
| Publisher | `<publisher/unknown>` | DCMI `publisher`. |
| Source type | `<ontology specification/article/web page/book/etc.>` | Project controlled text. |
| Version or edition | `<version/unknown>` | Record source-native value. |
| Identifier or URL | `<identifier/URL/unknown>` | DCMI `identifier`. Prefer a DOI (`https://doi.org/<doi>`) when the work has one, per `ADR-0012`. |
| Access date | `YYYY-MM-DD/not applicable/unknown` | Required for web resources when known. |
| Snapshot / Stable identifier | `<archival snapshot URL/DOI (if already given above)/unknown — not yet archived>` | Per `ADR-0012`. Required for web content without a DOI (project websites, code repositories, technical reports). Never fabricate a snapshot URL — record `unknown — not yet archived` if one has not been independently verified as retrievable. |
| Rights/license | `<SPDX expression/unknown/custom/mixed>` | SPDX when known. |

## Source Relation Notes

Record whether this reference supersedes, republishes, translates, quotes, or is derived from another source.

## Rights and License Notes

Explain unknown, ambiguous, custom, or mixed rights information without guessing. Use SPDX identifiers or expressions only when they accurately represent the source metadata.

## Citation and Locator Notes

Record recommended citation details, stable URLs, section names, page ranges, ontology IRIs, term IRIs, or other locators needed for crosswalk provenance.
