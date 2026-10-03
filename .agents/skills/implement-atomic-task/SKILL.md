---
name: implement-atomic-task
description: Implement and verify one atomic task, record evidence, and hand it off for the required review gate.
---

# Implement Atomic Task Skill

## Purpose
This skill is the **worker's procedure for one atomic task**. It does not replace sprint planning (`manage-plans`) or the per-task and end-of-sprint review gates (`omp-subagent-flows`).

## Workflow

### 1. Implement One Concern
- Read the assigned task's acceptance criteria and project conventions; change only what is needed to satisfy that concern.
- Keep the task **[~] in progress** while implementing and correcting review findings. Do not mark your own work [x] merely because implementation is finished.

### 2. Verify Behavior
- Exercise the changed behavior with the most specific runnable command or scenario; record what ran and what was observed. Run affected existing tests when the changed contract requires it.
- Add or update a **permanent automated test only when it protects an observable behavior against a plausible regression**. Do not create a test just to satisfy a checklist, assert incidental wiring or source text, or substitute a test file for a runtime smoke check.
- For a documentation or workflow-only task, check the edited instructions and their cross-references instead of inventing an automated test. Report any verification limitation honestly.
- If a bounded, evidence-backed unresolved technical question or material uncertainty could benefit from diagnostic input—even before repeated failures—send one qualified Main-brokered `advisor_request`; competing plausible hypotheses with no safe discriminating next action are one example. Repeated failures, no new evidence across distinct attempts, and an unchanged blocker are examples, not prerequisites. Elapsed time or a fixed attempt count alone, a generic request, or open-ended task delegation does not qualify. Include matching `task_id`, `attempt_id`, unique `consultation_id`, goal/criterion, blocker, bounded relevant evidence, tried hypotheses/results (or say none were safely tested), constraints, and one exact actionable question. Never spawn an advisor. On every matching progress request, return `advisor_needed: false|true`; `false` is a cheap decline, while `true` without a complete request is pending interest only and never launches help. Include the complete request in that reply when qualified, or send one qualified request directly; advice is not evidence, so independently try relevant advice and record its observed result.

### 3. Record Task Evidence

- Before requesting review, write `<evidence-root>/artifacts/sprint-<N>/task-<M>.md` using the [task-summary template](./references/_ARTIFACT_SUMMARY_TEMPLATE.md). Resolve `<evidence-root>` from the active plan or assignment; never infer it from the current directory. Never use `local://` for durable records.
- Record the observable outcome, changed files, explicit project/non-project scope, exact verification scenarios and results, bounded advisor evidence, and any open findings. If no permanent test was warranted, say why; do not claim a test ran if it did not.
- Keep implementation details in this artifact. The worker's final handoff to Main is compact: task/attempt IDs, outcome, changed paths, exact verification result, artifact path, and unresolved findings or advisor reference. Do not send full histories, trajectories, or logs.
- The evidence reviewer receives the artifact path and may inspect the assigned worker's history and source directly; Main does not relay full histories. The reviewer writes its own report under `<evidence-root>/artifacts/sprint-<N>/reviews/` and returns a compact verdict, reviewed-snapshot reference, findings, and report path. It does not edit the worker artifact.
- Keep task artifacts outside commits. Implementation workers do not create project commits, update refs, approve their own work, or write reviewer/checkpoint records. A fresh default `task` agent may execute only an explicitly Main-authorized checkpoint-only assignment tied to a matching evidence PASS and exact frozen snapshot; it must not edit source/product content and writes its separate checkpoint record. A worker artifact is not review approval or commit evidence.

### 4. Complete After the Gate

- Hand off for per-task evidence review; implementation completion is not approval. A project-backed task remains **[~]** until its matching evidence review is PASS and a fresh `task` agent has successfully completed the explicitly authorized checkpoint-only assignment for the frozen reviewed snapshot. Main—not the worker or reviewer—authorizes that assignment and decides whether the executor's separate checkpoint record establishes success. A failed or unavailable checkpoint remains `commit_pending`, blocks [x] and the next independent project task, and must not bypass hooks/signing or discard user state.
- A project-backed task requires an explicitly assigned and authorized repository, worktree, and target ref. Missing repository information does not turn project work into non-project work. Only a task designated non-project in its plan/assignment avoids a project Git checkpoint; its evidence and scope still belong under the assigned evidence root.
- If reviewed content changes, obtain a fresh evidence PASS before another checkpoint. Any later correction gets a fresh review and a separate new commit; never amend an earlier checkpoint.
- The worker records its own evidence only. The reviewer owns its report, the fresh checkpoint executor owns its checkpoint record, and Main edits only the plan/status and concise links or summaries to those records.
