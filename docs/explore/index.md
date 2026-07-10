# Explore

Interactive views over XwkOnt's reviewed crosswalks and core comparison vocabulary. These pages are **projections** of repository data (LinkML YAML + `core-ontology.mmd`) — the Git files remain the source of truth.

<div id="xwk-explore-stats" aria-live="polite"></div>

<div class="xwk-callout-grid">
  <a class="xwk-callout" href="coverage/">
    <strong>Coverage matrix</strong>
    Which of the eight source ontologies appear in each reviewed concept crosswalk.
  </a>
  <a class="xwk-callout" href="mappings/">
    <strong>Mapping network</strong>
    Drag a force-directed graph of source-term mapping assertions for any concept.
  </a>
  <a class="xwk-callout" href="core/">
    <strong>Core hierarchy</strong>
    Interactive Mermaid class diagram of the XwkOnt core scaffold.
  </a>
</div>

## How to read these views

- **Filled cells** in the coverage matrix mean the concept's correspondence table includes that source (count = number of correspondence rows).
- **Edges** in the mapping network are mapping assertions (`close-match`, `overlap`, `explicit-non-equivalence`, etc.), not claims of philosophical identity.
- Graphs are for orientation. Authoritative wording lives on each [concept crosswalk](../crosswalks/concepts/README.md) page.

Data files are regenerated at site build time by [`scripts/generate-explore-data.py`](https://github.com/xwkont/xwkont/blob/main/scripts/generate-explore-data.py).
