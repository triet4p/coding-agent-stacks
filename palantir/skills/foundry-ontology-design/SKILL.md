---
name: foundry-ontology-design
description: Design or review Foundry Object Types, Link Types, Actions, and writeback; distinguish business entities from intermediate datasets.
---

# Foundry Ontology design

Follow [dataset contracts](../../rules/dataset-contracts.md) and [release and governance](../../rules/release-and-governance.md). Use when changing the semantic model, not for a dataset-only transformation with no semantic impact.

1. **Pick business entities.** Name each entity as a user understands it. Record its lifecycle, how users find or act on it, and which consumers reuse it. Keep lookup-only, join-only, and intermediate aggregation data as datasets unless it represents a meaningful entity in its own right.
2. **Map objects to data.** Record each Object Type and backing dataset, its identity and PK projection, and important property types and nullability. Validate uniqueness at object grain; changing an existing PK requires checking existing links, Actions, edits, and consumers for identity changes.
3. **Model relationships.** Record meaning, direction, cardinality at each end, and the PK/FK or mapping dataset. For many-to-many, check uniqueness of relationship pairs at the stated grain and both endpoints. If the relationship has meaningful properties or a lifecycle, consider its own Object Type. Check missing and orphaned endpoints as well as representative traversal.
4. **Define edits and reads.** For Actions, specify validation, permissions, expected object state, and what is stored in the Ontology Edit Layer versus the backing dataset. If downstream datasets must consume edits, identify the approved materialization path, refresh timing, and checks. Do not infer persistence in the backing dataset from a successful Workshop save.
5. **Check consumers.** On the authorized target verify object lookup, representative links, and any Action path in scope. Review affected Workshop/Function bindings after changes. If an Action cannot be safely exercised, report the unverified behavior; do not mutate production to obtain proof.

Return: entity-to-backing map, PK and cardinality evidence, Action/edit/materialization decisions, tested consumers, and gaps or unresolved design decisions.
