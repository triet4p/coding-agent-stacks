---
name: foundry-workshop-verification
description: Verify Foundry Workshop filters, Vega selections, Function bindings, exports, and performance on the actual target version.
---

# Foundry Workshop verification

Follow [release and governance](../../rules/release-and-governance.md) and [metric contracts](../../rules/metric-contracts.md). Use for behavior verification; use [Foundry release review](../foundry-release-review/SKILL.md) when proposal checks or dependency releases are the issue.

1. **Identify the target.** Record the module, branch/version, widgets, and consumed Object Types, Functions, and bindings. Map each selection or input to the affected Object Sets, widgets, status labels, and exports. Name the source of truth for each filter and explicitly note self-filter behavior and grains.
2. **Exercise the real surface.** For affected paths, try Select, Clear/deselect, Reset, and refresh on the target. Observe the dataset or Object Set scope, displayed selection labels, Vega highlight or zoom, and downstream widget results. Include rapid changes if recomputation is async; distinguish no filter, loading, stale data, and an empty result. Treat serialized filter workarounds as version-sensitive: test their shape and dependencies rather than assuming a stable API.
3. **Verify Functions and exports when changed.** Check actual binding and inputs (including null/empty), output schema, and representative data. Compare export rows and values to the same dashboard filter scope, grain, and access rights; check that linked data does not fan out rows. For large exports compare native export from a suitable materialized dataset with an authorized async flow rather than assuming a synchronous Function can return any file size.
4. **Measure before optimizing.** Time the same user action with comparable data, filters, and cache conditions. Use Workshop profiling and Function execution evidence to distinguish queries, recomputation, runtime, and rendering. Prefer indexed predicates and small chart inputs; choose backend aggregation, SQL, Function, or precompute based on the bottleneck, interactive filtering, freshness, and current runtime limits. Check metric and interaction parity after any change.

Return: target and bindings, scenarios and observed outcomes (or access gaps), export parity if relevant, and timing evidence with conditions when performance is in scope. A config diff, preview, or build alone is not a live Workshop check.
