---
name: manage-plans
description: Maintain scope, acceptance criteria, milestones, and current task status for large work; keep execution logs and temporary handoffs out of plans.
---

# Manage Plans Skill

## Purpose
Use plans for large tasks, features, or bugs that need durable scope and sequencing. Small bounded fixes do not require a new sprint. Plans describe intended work and its current state, not the sequence of tool calls used to execute it.

## Workflow

### 1. Create or Update Global Plan file

- **File Location:** `docs/PLAN.md`
- **Purpose:** This file serves as the single source of truth for the overall project plan. It should be updated whenever there are a new sprint plan or changes to existing plans.
- **Content:** The file should contain a high-level overview of the project, including current sprint goals, major milestones, and links to detailed sprint plans, not the detailed breakdown of tasks.


*Notes*: You can view an example of template in [_GLOBAL_PLAN_TEMPLATE.md](./references/_GLOBAL_PLAN_TEMPLATE.md).

### 2. Create or Update Sprint Plan file
- **File Location:** `docs/sprint-plans/sprint-<N>.md`
- **Purpose:** This file contains the detailed breakdown of tasks for a specific sprint. It should be created at the start of a sprint and updated as work progresses.
- **Content:** Sprint goal, acceptance criteria, ordered atomic tasks, and current status. Status per task: `[ ]` pending / `[~]` in progress / `[x]` done. Record the chosen lightweight or full workflow and any required review/commit boundary concisely; a sprint label does not require full-flow gates.
- **What is an Atomic Task?** An atomic task is a task that focuses on a single concern and can be completed in one focused implementation step. If a task touches more than one concern, it should be split into multiple atomic tasks.
- Separate agreed acceptance requirements from proposed research/performance targets; record numeric targets with their measurement conditions and approval status. Do not invent hard gates from aspirational estimates. Existing assigned gates remain binding until the owner explicitly changes them.
- In `omp-subagent-flows`, follow `skill://omp-subagent-flows/references/evidence-review-cycle.md` when review or early quantitative-gate reconsideration applies. Two rounds are authorized by default; Main may grant a third only for evidenced progress and a bounded fix/check. Otherwise ask the owner after round 2; after round 3 without PASS, stop. Keep `[~]` with `blocked: owner_decision_required` when needed. Record owner-approved criterion changes with old/new requirements and rationale; detailed round records and Main's extension rationale stay outside the plan.

*Notes*: You can view an example of template in [_SPRINT_PLAN_TEMPLATE.md](./references/_SPRINT_PLAN_TEMPLATE.md).

### 3. Update State, Not an Execution Diary

- Main updates the existing task entry only on a meaningful scope/status change, durable decision, real blocker, or verified outcome. Add concise evidence/commit links when useful; do not append one entry per turn.
- Never put dispatch receipts, agent/model selection logs, progress requests, timer/wait events, tool retries, copied outputs, or detailed handoffs in `docs/PLAN.md` or `sprint-<N>.md`. Routine coordination stays in chat and trace.
- If Main or a worker needs to save temporary supervision state, pause/resume state, or a detailed handoff, write a separate task/attempt-scoped file under the authorized repository's `artifacts/` directory. For a sprint, use `artifacts/sprint-<N>/handoffs/` or `artifacts/sprint-<N>/state/`; a standalone task may use `artifacts/<task-id>/`. Never use another project's artifacts, a global home log, or `local://` for these durable files.
- Resolve the repository/artifact root from the assignment, not cwd or an ancestor repository. Explicit non-project work uses its explicitly assigned output root.
- Preserve previous handoff files and link to them rather than copying their contents into the plan. Do not create a temporary-state file for every action.
