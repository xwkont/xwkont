# Concept Crosswalks

<!-- updated at: 2026-07-07 03:30 Z   (2026-07-06 23:30 EDT) -->

One file per concept, each comparing all 8 source ontologies in scope (BFO, DOLCE, SUMO, UFO, GFO, YAMATO, TUpper, GUM — see [ADR-0015](../../adr/ADR-0015-expand-source-ontology-scope-to-eight.md)) against directly-verified primary sources. All 19 reviewed concepts — the original 8 plus all 9 of the `0.2.0` batch ([ADR-0018](../../adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md)) plus `disposition-capacity.md` and `mind-conscious-being-agent.md` — are `reviewed`. Per [ADR-0021](../../adr/ADR-0021-source-classified-core-placement-criterion.md), all 19 qualify for XwkOnt's core module (`data/ontology/core.ttl`); the actual Turtle additions are separately-tracked work, not yet done. **`mind-conscious-being-agent.md` is the 19th `reviewed` concept**, the second reviewed concept of the `0.3.0` batch ([ADR-0018](../../adr/ADR-0018-comprehensive-concept-coverage-staged-via-minor-releases.md)'s two-source rung), narrowed during review to the bearer-level agent/conscious-being entity layer (GUM's mental-process cluster and YAMATO's `mind` were off-ramped to `process.md`/`event.md` and abstract/semi-abstract territory respectively); `symbol-sign-representation.md` remains a `draft` concept in that batch, in progress and pending review, and its `core.ttl` placement is separately-tracked work, not yet done. New crosswalks follow [TEMPLATE.md](TEMPLATE.md) and the structure/status conventions in [docs/INFORMATION_ARCHITECTURE.md](../../INFORMATION_ARCHITECTURE.md) and [docs/methodology/crosswalk-methodology.md](../../methodology/crosswalk-methodology.md).

- [continuant-occurrent.md](continuant-occurrent.md)
- [object.md](object.md)
- [event.md](event.md)
- [process.md](process.md)
- [quality.md](quality.md)
- [role.md](role.md)
- [relation.md](relation.md)
- [information-artifact.md](information-artifact.md)
- [time.md](time.md) — `0.2.0`-batch concept 1
- [space.md](space.md) — `0.2.0`-batch concept 2
- [abstract-concrete.md](abstract-concrete.md) — `0.2.0`-batch concept 3
- [quantity-amount-of-matter.md](quantity-amount-of-matter.md) — `0.2.0`-batch concept 4
- [situation-state-of-affairs.md](situation-state-of-affairs.md) — `0.2.0`-batch concept 5 (weakest cross-source evidence of the batch at drafting time; a follow-up primary-source pass found stronger, same-sense-converging evidence — see its own Scope Note)
- [universal-type.md](universal-type.md) — `0.2.0`-batch concept 6
- [mereology-parthood-aggregate.md](mereology-parthood-aggregate.md) — `0.2.0`-batch concept 7
- [boundary-site.md](boundary-site.md) — `0.2.0`-batch concept 8
- [proposition-content.md](proposition-content.md) — `0.2.0`-batch concept 9
- [disposition-capacity.md](disposition-capacity.md) — `0.3.0`-batch concept 1
- [symbol-sign-representation.md](symbol-sign-representation.md) — `0.3.0`-batch concept 2 (draft, in progress)
- [mind-conscious-being-agent.md](mind-conscious-being-agent.md) — `0.3.0`-batch concept 3
- [TEMPLATE.md](TEMPLATE.md) — template for new concept crosswalks
