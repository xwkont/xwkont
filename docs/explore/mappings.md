# Mapping network

Pick a reviewed concept to see its **mapping assertions** as a force-directed graph. Nodes are source terms (`Ontology:Term`); edges are relation categories from the crosswalk YAML. Drag nodes to rearrange.

<div id="xwk-mapping-network" aria-live="polite">
  <p>Loading mapping network…</p>
</div>

### Edge colors

| Relation category | Meaning (short) |
|---|---|
| close-match | Strong alignment without claiming identity |
| exact-equivalence-candidate | Strongest candidate equivalence (still hedged) |
| overlap | Partial shared coverage |
| related | Weaker topical relation |
| broader-than | One term scopes wider |
| explicit-non-equivalence | Sources diverge on the record |
| unknown | Insufficient evidence to classify |

Full definitions: [crosswalk methodology](../methodology/crosswalk-methodology.md).
