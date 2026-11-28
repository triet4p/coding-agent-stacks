---
name: fde-manage-plans
description: Maintain durable AI FDE plans with verifiable outcomes and explicit dependencies instead of a forced task sequence.
---

# Manage FDE Plans

Use this optional skill when scope or dependencies need to survive across turns or sessions. Skip it for a clear standalone task. Update the existing project plan when one exists; otherwise use the project's plan location or `docs/PLAN.md`.

## Record only durable work state

- **Plan:** Goal, constraints, overall acceptance, and durable decisions.
- **Task:** Stable ID, one outcome, acceptance check, prerequisite task IDs or required external inputs, and state (`pending`, `in progress`, `blocked`, `verified`). State why a task is blocked; link evidence for verified work when useful.
- **Slices (only when useful):** Within a task, record each slice's outcome, dependencies, and write scope. Name the join owner and combined acceptance check. Do not mark the parent verified until the slices are integrated and the combined check passes.

The Planner proposes structure and dependencies; the Orchestrator maintains status based on evidence. Keep dispatch receipts, raw output, and detailed handoffs out of the plan. Do not treat task IDs or their order on the page as dependencies.

## Example

| ID | Outcome | Depends on | Acceptance check |
| --- | --- | --- | --- |
| T1 | Freeze the import contract | None | Input and error cases are agreed with the owner. |
| T2a | Implement the importer | T1 | Importer checks cover valid and invalid inputs. |
| T2b | Write user-facing examples | T1 | Examples match the agreed contract without using T2a output. |
| T2 | Deliver a usable, documented import flow | T2a, T2b | Run the documented example against the integrated importer. |

T2a and T2b are slices of T2; they can run together only with scoped approval and non-conflicting write scopes. The Orchestrator assigns the T2 join and accepts T2 on the combined check. Apply the same readiness rule to independent top-level tasks under [FDE Atomic Flow](../fde-atomic-flow/SKILL.md).
