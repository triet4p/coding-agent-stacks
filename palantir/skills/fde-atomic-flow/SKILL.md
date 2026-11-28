---
name: fde-atomic-flow
description: Coordinate Palantir AI FDE work with self-contained atomic tasks, end-of-turn handoffs, and opt-in parallel execution.
---

# FDE Atomic Flow

The Orchestrator cannot steer a running subagent. Give each Worker a self-contained brief and adjust the next turn, not the current one. Follow the [FDE execution rules](../../rules/execution.md).

## Role responsibilities and returns

The **Orchestrator** owns the goal, delegation, dependency scheduling, and acceptance. Resolve routine decisions directly; ask the owner before changing agreed criteria or exceeding authority.

| Role | Responsibility | Required return |
| --- | --- | --- |
| Planner | When decomposition or dependencies are unclear, design atomic tasks. Do not implement them. | Task IDs, outcomes, acceptance checks, prerequisites, and decisions needed before dispatch. Identify independent slices and who integrates them when applicable. If information is missing, name the affected tasks, assumptions, and open questions. |
| Advisor | Investigate one evidence-backed technical question. Do not take over implementation or decide for the Orchestrator. | Answer or explicitly inconclusive result, evidence examined, rationale and trade-offs, and the next check that would validate the recommendation or resolve the uncertainty. |
| Worker | Deliver one assigned outcome and verify it with the narrowest check that covers the outcome. Do not expand scope or revise acceptance. | Use the Worker return contract below on every outcome, including failures. |

The Planner and Advisor may directly read relevant, authorized evidence, including project files, check output, and Worker handoffs. Give them accessible references and the question or goal, not just the Orchestrator's interpretation. If evidence is missing or inaccessible, they identify the gap and distinguish observations from assumptions. They do not edit implementation state.

## Ask for the model slot before dispatch

AI FDE exposes three selectable subagent model slots: `fast`, `balance`, and `smart`. A slot can point to a different configured model; choose the slot, not its backing model. The Orchestrator is the main session, not a subagent dispatch.

| Role being dispatched | Ask the user to choose |
| --- | --- |
| Worker | `fast` or `balance` |
| Planner | `balance` or `smart` |
| Advisor | `balance` or `smart` |

Ask by default before first dispatch of a role for the named scope. Reuse an explicit choice the user already made for that role and scope; ask again outside it. Ask only for roles actually needed. If multiple choices are needed at once, ask together but keep them separate by role. Do not pick a slot on silence or substitute another if the chosen slot is unavailable; report the gap and ask for an eligible choice. Slot selection does not authorize parallel execution.

## Brief one outcome per Worker

An atomic task has one verifiable acceptance outcome, not necessarily one file or action. Split at an unresolved decision the Worker is not authorized to make, not at a file boundary. Each brief specifies:

1. **Outcome and check:** What must be true and how to verify it.
2. **Scope and inputs:** Writable files or resources, out-of-scope changes, and accessible references or prerequisite results.
3. **Decision boundary:** What the Worker may decide and when it must stop.
4. **Applicable guidance:** Include the relevant rules and on-demand skills from the [Palantir pack index](../../README.md) in the brief for each role that needs them. If a subagent cannot load the references, give it the applicable instructions in the brief; do not assume it inherited the main session's context.

A planned task can contain independently assignable slices that contribute to one acceptance outcome. Brief each slice separately and identify who integrates and verifies the combined outcome.

## Schedule ready work

A plan records dependencies, not a forced sequence. A task or slice is ready when its prerequisites are satisfied and its brief is actionable. If parallel execution could shorten elapsed time, offer the owner **sequential** or **parallel for the named tasks or slices**. Name the work that can overlap, the expected time benefit, and the possible increase in concurrent model usage and integration effort. Explicit prior approval for that scope is enough; without it, run sequentially.

Once approved, dispatch only ready work with non-conflicting write scopes and no dependency on another running Worker's output. This applies both within a task and across tasks. Advance each ready branch as its prerequisites finish; a blocker holds its dependents, not unrelated work. Respect any approved concurrency limit. If concurrent execution or safe integration is unavailable, run sequentially and state why.

## Worker return contract

Return all fields below, whether the outcome is verified, a check failed, or work could not proceed. Use `none` or `not run — <reason>` rather than omitting fields. Never infer or fabricate observations.

| Field | Required content |
| --- | --- |
| Task / slice | The ID or name from the brief. |
| Status | `verified` if all assigned checks passed and the outcome meets acceptance; `failed` if a required check ran and failed; `blocked` if a missing decision or prerequisite prevented delivery or verification. |
| Outcome and state left | What was completed, remaining or unmet criteria, changed paths or deliverables, and whether the partial state is usable by the next Worker. |
| Verification and evidence | Exact checks attempted, observed results, and accessible evidence. List required checks not run and why. |
| Next action | `none` if verified; otherwise the exact decision, missing input, or safe next action. Include relevant attempts and what they showed. |

If blocked, finish only independent, safe work within scope before ending; do not wait for live steering. If FDE interrupts a turn without a usable return, the Orchestrator treats it as unverified, reports the missing handoff, and inspects accessible state before dispatching a continuation.

## Decide and continue

On a failed or blocked turn, the Orchestrator uses the handoff to resolve the issue directly, ask the Advisor one evidence-backed question, or escalate the decision to the owner. Dispatch a fresh brief with the decision and the necessary handoff. Advice is not verification; check the resulting work. Accept a task only when its own criteria are verified, including a combined check after integrating parallel slices. A finished Worker turn alone is not acceptance.

Use [Manage FDE Plans](../fde-manage-plans/SKILL.md) when scope, dependencies, or status need to persist across turns or sessions.
