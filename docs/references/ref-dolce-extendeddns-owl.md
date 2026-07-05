# DOLCE ExtendedDnS OWL Module (Descriptions and Situations)

> **Local reference identifier:** `xwkont:ref:dolce-extendeddns-owl`
> **Slug:** `dolce-extendeddns-owl`
> **Editorial status:** `candidate`
> **Created:** `2026-07-05`
> **Modified:** `2026-07-05`

## Descriptive Metadata

| Field | Value | Notes |
|---|---|---|
| Title | ExtendedDnS (Descriptions and Situations, with an extended vocabulary for social reification) | Per the ontology's own `rdfs:comment`: "The DnS (Descriptions and Situation) ontology, with an extended vocabulary for social reification." |
| Creator | Aldo Gangemi (OWL engineering) | Same attribution pattern as `xwkont:ref:dolce-lite-owl`; DnS theory itself originates in Gangemi & Mika (2003) and related DOLCE-driven literature, not independently verified in this pass. |
| Contributor | unknown | |
| Publisher | Laboratory for Applied Ontology (LOA-CNR) | Canonical namespace: `http://www.loa-cnr.it/ontologies/ExtendedDnS.owl#`. `owl:imports` `DOLCE-Lite.owl`, `TemporalRelations.owl`, `SpatialRelations.owl`. |
| Source type | OWL ontology (machine-readable, not a paper) | |
| Version or edition | version 397 (per the file's own `owl:versionInfo`, matching `xwkont:ref:dolce-lite-owl`'s version), fetched via the same GitHub mirror (`iddi/sofia`) used for `xwkont:ref:dolce-lite-owl` since the canonical `loa-cnr.it` host did not serve the raw file directly in this pass | |
| Identifier or URL | Canonical: `http://www.loa-cnr.it/ontologies/ExtendedDnS.owl`; fetched from: `https://raw.githubusercontent.com/iddi/sofia/master/eu.sofia.adk.common/ontologies/foundational/ExtendedDnS.owl` | |
| Access date | 2026-07-05 | |
| Snapshot / Stable identifier | No Wayback Machine snapshot found for the raw file itself (`wayback/available` returned no result); repository-level snapshot <http://web.archive.org/web/20200919223520/https://github.com/iddi/sofia> (2020-09-19) used as fallback, consistent with `xwkont:ref:gfo`'s precedent for GitHub-hosted OWL sources without a file-specific snapshot. | |
| Rights/license | unknown | Not verified in this pass. |

## Source Relation Notes

Extends `xwkont:ref:dolce-lite-owl` (core DOLCE-Lite) with the DnS (Descriptions and Situations) module — the formal treatment of `situation`, `description`, `concept`, `figure`, and related social-reification vocabulary that core `DOLCE-Lite.owl` explicitly declines to formalize (see that class's own comment, quoted in `docs/crosswalks/concepts/situation-state-of-affairs.md`'s `note-001`). Fetched specifically to resolve that crosswalk's `uncertainty-002`.

## Rights and License Notes

Not verified in this pass. Treat as unknown rather than guessed.

## Citation and Locator Notes

Recommended citation: ExtendedDnS (Descriptions and Situations). Laboratory for Applied Ontology (LOA-CNR). `http://www.loa-cnr.it/ontologies/ExtendedDnS.owl`. OWL engineering by Aldo Gangemi.

**Direct primary-source verification (2026-07-05):** fetched directly as plain-text OWL/XML and read to resolve `docs/crosswalks/concepts/situation-state-of-affairs.md`'s `uncertainty-002` (whether DOLCE's separate DnS module contains a formal `situation` class beyond core DOLCE-Lite's informal commentary). Confirmed a fully defined `#situation` class:

- `owl:equivalentClass` of the intersection of `non-agentive-social-object`, `setting-for some particular` (DOLCE-Lite), and `satisfies some description`.
- `owl:disjointWith` `collection`, `concept`, `non-agentive-figure`, `information-object`, `figure`, `description`.
- `rdfs:comment`: "A situation is a social object that appears in the domain of an ontology only because there is a description whose components can 'carve up' a view (setting) on that domain. A situation has to satisfy a description..., and it has to be setting for at least one entity. In other words, it is the ontological counterpart (with due local differences or restrictions) of settings (situations from SC, contexts, episodes, states of affairs, structures, configurations, cases, etc.). A perdurant is usually the only mandatory constituent of a setting."

This confirms DOLCE — via its DnS extension, not core DOLCE-Lite — does have a formally defined class matching the "situation"/"state of affairs" sense, materially changing `situation-state-of-affairs.md`'s cross-source evidence count from `uncertainty-001`'s "1 of 8 sources." Used in `situation-state-of-affairs.md`.
