# Palantir AI FDE pack

Load [execution rules](rules/execution.md) and [FDE Atomic Flow](skills/fde-atomic-flow/SKILL.md) explicitly in the intended AI FDE session using the instruction or skill mechanism available there. Add [Manage FDE Plans](skills/fde-manage-plans/SKILL.md) only when project scope, dependencies, or task status need to persist. This pack does not assume automatic discovery or an OMP-style command.

The pack lives outside `.agents/` and `.omp/` so the normal installer and home sync do not include it. Keeping the Worker contract and orchestration flow in one skill avoids mismatched handoff rules; keeping durable planning separate lets small jobs skip it. Unlike OMP's live steering, FDE makes decisions between Worker turns.

Before dispatch, choose the FDE model slot for each needed role: **Worker** `fast` or `balance`; **Planner** and **Advisor** each `balance` or `smart`. The Orchestrator asks unless you already made an explicit choice for that role and scope. This is separate from approval to run in parallel.

To prioritize elapsed time when independent work is ready, select parallel execution for a named scope. For example: “Run T2a and T2b in parallel, then verify T2 after both finish.” Extra concurrent model usage is a trade-off, not a reason to force a linear plan. Without approval, execute sequentially in dependency order.

## Foundry rules and skills

Load the applicable rules before work on Foundry resources. Load only the skills needed for the current task.

| Rule | Applies to |
| --- | --- |
| [Dataset contracts](rules/dataset-contracts.md) | Project boundaries, `shared`, grain, primary keys, joins. |
| [Metric contracts](rules/metric-contracts.md) | KPI definitions and equivalent results across pipelines, Workshop, and exports. |
| [Release and governance](rules/release-and-governance.md) | Access, markings, approvals, dependency bindings, and release checks. |

| Skill | Load when |
| --- | --- |
| [Foundry dataset design](skills/foundry-dataset-design/SKILL.md) | Designing or changing datasets and transforms. |
| [Foundry Ontology design](skills/foundry-ontology-design/SKILL.md) | Designing Object Types, links, Actions, or writeback. |
| [Foundry Workshop verification](skills/foundry-workshop-verification/SKILL.md) | Changing or diagnosing filters, charts, Functions, exports, or performance. |
| [Foundry release review](skills/foundry-release-review/SKILL.md) | Reviewing a branch, proposal, or release candidate. |

The layer and publishing rules are pack conventions, not claims about what Foundry technically allows. Check runtime-dependent features and limits on the target environment instead of importing numbers from past projects.
