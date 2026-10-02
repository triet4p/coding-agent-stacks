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
- If progress meets the criteria for help, request a Main-brokered `task-advisor` consultation using a compact, ID-correlated `advisor_request`; do not spawn an advisor. Continue only independent safe work while it runs, otherwise wait for an event rather than retrying redundantly. Advice is not evidence: try any relevant suggestion and record what actually happened.

### 3. Record Task Evidence
- Before requesting review, write `artifacts/sprint-<N>/task-<M>.md` using the [task-summary template](./references/_ARTIFACT_SUMMARY_TEMPLATE.md). Use the sprint/task identifiers in the active plan.
- Record the observable outcome, changed files, exact verification commands or scenarios and results, and any open findings. If no permanent test was warranted, say why; do not claim a test ran if it did not.
- Record any advisor consultation as a bounded summary with task/attempt/consultation IDs, question, diagnostic conclusion, and the worker's attempted result; include an approval reference for any authorized GPT-6.1 Sol override. Never copy full conversations or trajectories into the artifact.
- Keep `artifacts/` ignored by Git (add it to the project's `.gitignore` if necessary); never commit task artifacts. Send the artifact path and verification evidence to the orchestrator or reviewer.
- Workers do not create project commits, update project refs, or fill Main-owned evidence-gate/commit fields in the artifact. An artifact documents worker evidence and is not review approval or commit evidence.

### 4. Complete After the Gate
- **In OMP, the worker hands off for per-task evidence review; PASS precedes but does not complete a project-backed task. Main immediately checkpoints the exact reviewed snapshot before assigning the next independent project task, using standard Git porcelain and verifying the commit and post-commit staged diff. Main marks [x] only after both evidence PASS and a successful checkpoint.** A failed or unavailable checkpoint stays `commit_pending`, blocks [x] and the next independent task, and must not bypass hooks/signing or discard user state. If reviewed content changes, obtain a fresh evidence PASS. Any later correction gets a fresh evidence review and a separate new commit; never amend an earlier checkpoint. End-of-sprint deep review remains a separate gate.
- For this current user-global configuration rollout only, the artifact records that the edits are not a project commit; Main marks [x] after its evidence gate passes under the rollout plan. Do not treat this as a generic project commit exception.
