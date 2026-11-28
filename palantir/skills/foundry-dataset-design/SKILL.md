---
name: foundry-dataset-design
description: Design or review Foundry datasets and transforms, including shared data contracts, composite key collisions, join cardinality, and incremental correctness.
---

# Foundry dataset design

Follow [dataset contracts](../../rules/dataset-contracts.md), [metric contracts](../../rules/metric-contracts.md) when producing a KPI, and [release and governance](../../rules/release-and-governance.md). Use for dataset and transform changes, not live Workshop troubleshooting.

1. **Trace the contract.** Identify inputs, owning project, layer, consumers, and expected output grain. Record schema (columns, types, and nullability) and the existing key. Pick the layer that owns the work; inspect lineage instead of assuming the name of a dataset reflects its purpose.
2. **Prove identity.** Profile nulls and group by the normalized candidate key to find duplicates. Compare conflicting rows against the grain: same entity with conflicting facts, or distinct entities? For a composite key, test null versus literal values, delimiters or escaping, and stable values across runs. If a discriminator is needed, validate it against the source and reread downstream key consumers before changing the contract. If considering a hash, show why a source key is unavailable and test the canonical inputs for indistinguishable rows.
3. **Prove the transform.** Check the unique side of each declared join and compare row count and distinct grain before and after. For a deliberate grain change, validate the new grain and totals instead. Cover missing and unmatched FK cases. Run appropriate build expectations for key and schema; use a compact counterexample for plausible fan-out or null collisions. For business mappings subject to change, consider a governed reference dataset rather than repeated code changes; reuse stable schema and key helpers instead of copying them.
4. **Check computation mode if incremental.** Inspect actual input transaction modes and how late arrivals, updates, deletes, and reference changes affect prior output. Choose snapshot, append, or an explicit stateful merge/replay based on those semantics. Check first build, delta, and replay against snapshot-equivalent results for the same input history, including duplicates spanning batches. Check build logs for the observed mode; a snapshot-only preview is not incremental proof.

Return: layer and lineage, output grain/schema/key and null handling, join and computation-mode decisions, actual checks and results, and any unresolved data or access gap. Treat an inaccessible check as unverified.
