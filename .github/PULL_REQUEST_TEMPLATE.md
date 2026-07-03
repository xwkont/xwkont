## Summary

<!-- What does this change, and why? -->

## Artifact class

<!-- One of: editorial / ontology documentation / RDF companion / example / publication / crosswalk content / governance -->
<!-- See docs/governance/contributing.md for the full category table. -->

## Validation performed

<!-- Run the checks relevant to the artifact class per the "Required Validation by Change Type"
     table in docs/governance/contributing.md, and paste output or explain why a check doesn't apply.
     For Turtle changes, include the parse/structural-fallback result from
     docs/publication/validation-commands.md. -->

## Review checklist

- [ ] Preserves XwkOnt's scope as a crosswalk project (does not introduce a new foundational ontology)
- [ ] Cites or points to authoritative sources for any source-ontology claims
- [ ] Keeps example data clearly non-authoritative
- [ ] Avoids unsupported equivalence or correspondence claims
- [ ] Does not reintroduce formal RDFS domain/range for `xwkont-core:mapsTo`
- [ ] Does not adopt OWL as the default modeling layer without an ADR
- [ ] Updates related docs/navigation if a term, property, namespace, or release rule changed
- [ ] Deferred or open questions are recorded explicitly rather than resolved by assumption

## Compatibility notes

<!-- Any impact on published namespaces, terms, or release artifacts? See
     docs/governance/change-management.md and docs/governance/release-versioning-policy.md. -->
