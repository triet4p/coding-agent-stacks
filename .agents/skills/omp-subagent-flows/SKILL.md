---
name: omp-subagent-flows
description: Orchestrate planned feature delivery in Oh My Pi with asynchronous workers and reviewers, per-task evidence gates, and a final differential deep review.
---

# OMP Subagent Flows

## Scope

Use this skill only inside **Oh My Pi (OMP)** when a user requests feature implementation that belongs in a plan or sprint.

Never use this workflow in Codex CLI, Claude Code, or any other coding-agent CLI. Never translate its OMP agent names, tools, lifecycle operations, or artifact URLs to another runtime.

The main session is an orchestrator. It may inspect plans, task status, returned agent outputs, and review artifacts; select and brief subagents, transfer handoffs, invoke planning and review skills, and decide whether gates pass. It must not inspect implementation details, edit product code, debug code, or execute sprint tasks itself.

## Invariants

1. Keep at most **two active subagents total**, including workers and reviewers.
2. Planning remains in the current main session and uses the **exact current model**. Never delegate plan creation or switch models for it.
3. Use a fresh worker for each task or correction; transfer the prior worker's artifact and unresolved findings instead of reviving an idle agent. **`task` is the default; `hard-task` is never sticky.** Stop at **250K tokens** for a partial handoff and never exceed **300K tokens** in one worker.
4. Run one sprint implementation task at a time. Run an `evidence-reviewer` after each completed task and pass its gate before proceeding. Independently gated project tasks must also commit before the next independent task; only a predeclared shared atomic batch may continue through its included tasks before one checkpoint. Never batch task-level evidence reviews.
5. Run a `deep-reviewer` only at the end of the sprint, after every task has passed its evidence gate and every required project commit checkpoint has succeeded. A correction may require another end-of-sprint differential review.
6. A review with actionable findings does not pass. Correct the findings and run a fresh review at the same level.
7. All four flow agents (`task`, `hard-task`, `evidence-reviewer`, `deep-reviewer`) declare `blocking: false`. Before each launch, inspect the **effective** agent definition, including project-level overrides. If the effective definition is blocking, or async execution is disabled/unavailable, do not launch that flow agent synchronously, silently repair the override, or edit runtime configuration; report the condition to Main's user and wait for an authorized resolution.
8. For work expected to exceed 5 minutes, every worker and reviewer proactively messages Main with its task/sprint ID, attempt ID, current stage, and reason it will run long. If that becomes clear only during execution, message then. Work lasting 5 minutes or less needs no proactive message. This notice is independent of timer supervision and is not a gate verdict.
9. Every subagent enumerates and reads all regular files under `~/.agents/rules/*` before substantive work, including for corrections and replacements. Apply relevant rules at their proper precedence; report conflicts or inaccessible files instead of silently ignoring them.

## Roles

- **Main session:** orchestration and gate decisions only. The user-defined `~/.omp/agent/agents/task.md` overrides OMP's bundled `task` agent; project-level definitions may override the user definition. Main checks the effective definition before launch.
- **Worker:** a fresh `task` (default) or `hard-task` subagent for one sprint task or correction. The worker's implementation details and evidence live in its handoff artifact.
- **Evidence reviewer:** a read-only `evidence-reviewer` for one completed task.
- **Deep reviewer:** a read-only `deep-reviewer`, default model `opencode-go/glm-5.3-flash:high`, that differentially reviews the entire sprint after all per-task evidence gates pass. It hunts risks and ambiguities without re-checking what the evidence reviews established.

## Async jobs, events, interruption, and progress

### Launch and result acceptance

- Launch each flow agent as an asynchronous job and record the task ID, unique attempt ID, agent ID, returned job ID, and role. Give replacements a new attempt ID. The async launch/result and agent-message events are Main's supervision channels; progress messages are not completion events.
- Accept a worker or reviewer result only when it matches the current task ID, attempt ID, and agent ID, and the corresponding worker/reviewer has completed. A launch receipt, message-delivery receipt, progress reply, partial handoff, or timer event is not task completion or a gate verdict.
- If an attempt is cancelled or replaced, invalidate it before continuing. Ignore any later result, message, or timer from that stale attempt for gate decisions; it must never advance the task or sprint.
- Check that the effective role definition has `blocking: false` and that async execution is enabled before launch. If OMP instead runs inline, reports no async job manager, or falls back to synchronous execution, stop and surface the configuration/runtime condition. Do not silently switch to blocking operation or edit runtime configuration.

### Main's event handling

- Main reacts to delivered job-completion and agent-message events. Do not repeatedly poll status. Use `functions.wait` only when Main is otherwise blocked with no useful work, and only to wait for an event; do not invent a timeout argument or use it as a timer.
- Never supervise workers with eval `handle.wait` or an eval barrier: aborting those waits can cancel the jobs being waited on. Do not attach worker lifetime to a Main-turn wait.
- A Main/user interrupt (including Escape where applicable) interrupts Main's current turn; it is not an explicit cancellation of a detached worker. To stop a specific worker, use the explicit cancellation control for that worker's async job (for an exposed process job, `proc://<job-id>/kill`). Do not confuse cancelling a job with interrupting Main.
- Do not promise detached-job durability across process exit or automatic Main resumption after a user interrupt. A subsequent user prompt may be needed for Main to process queued results.
- A send receipt confirms delivery only; it does not establish that the recipient read, applied, or acknowledged the message. A late reply or tool execution is not by itself evidence that the worker is stalled.

### One-shot timer supervision

- For every active attempt, Main starts exactly one finite background shell timer with an adaptive observation interval of **10–30 minutes**. Use an existing finite async shell timer (for example, a PowerShell `Start-Sleep` command launched through Bash with async enabled) that emits a marker containing the task ID, attempt ID, and timer-generation ID. This timer is an observation prompt, not `task.maxRuntimeMs`, a worker deadline, or a reason to stop work.
- Choose the interval from current task context and observed progress, not from elapsed time alone. Keep only one timer generation active per attempt. Do not rearm/restart timers in a hot loop.
- On worker/reviewer completion, completion takes precedence: cancel its timer job if still active and invalidate that timer generation. If a completion and timer event race, handle completion first. Ignore a late timer whose task, attempt, or generation is no longer current.
- On a current timer event, Main sends exactly one outstanding `progress_request` to the matching agent, carrying `task_id`, `attempt_id`, `agent_id`, `progress_request_id`, and `timer_generation`. Do not issue another request while one is outstanding. The delivery receipt is not an acknowledgment.
- The matching progress reply carries all of those IDs and these fields: `stage`, `completed_since_last_report`, `new_evidence`, `current_blocker`, `attempts`, `results`, `next_action`, and `help_needed`. The worker/reviewer compares changes since its previous report. Main compares reported deltas and evidence; elapsed time alone is not difficulty or a stall. The timer event and progress reply never substitute for completion or review.
- After a matching reply, if the same attempt remains active and no request is outstanding, Main starts the next one-shot timer generation at an adaptive 10–30-minute interval. Do not keep restarting the timer while a reply is pending. Workers continue to send the required >5-minute proactive notice independently of this timer.
- Do not automatically request help, replace a worker, or advance a gate solely because a timer expires. Keep implementation details in worker artifacts; Main's messages and records stay orchestration-only.

### Main-brokered task-advisor consultations
- A worker may request diagnostic help before a timer fires when it sees repeated identical errors or failed hypotheses, no new evidence across multiple distinct attempts, or an unchanged blocker with no discriminating next action. The request is never an automatic consequence of elapsed time or a fixed attempt counter. A timer-triggered progress reply may prompt Main to ask the worker to prepare a question only after Main compares its reported deltas and sees non-progress; time alone is not a trigger.
- The worker sends Main one compact `advisor_request` with matching `task_id`, `attempt_id`, and a unique `consultation_id`, plus the goal/criterion, current blocker, bounded evidence/snippets, distinct tried hypotheses and their results, constraints, and one exact question. Do not forward full conversations, trajectories, session logs, or unrelated context. Workers never spawn advisors or change model/config/depth themselves.
- Main brokers each request to a fresh `task-advisor` sibling, checks its effective definition/model and `blocking: false`, and confirms async execution is available before launch. Keep at most one active consultation per worker and at most two active subagents total; the worker and advisor consume both slots. Use the existing `task` tool schema: with batch enabled, provide required `context` and one `tasks[]` item containing `agent`, `task`, and `solutionSpace`; with batch disabled, use one flat task item. The task item `tools` field exposes parent eval-kernel tools; it is not an agent-tool whitelist. Do not invent a task model-override field.
- Main forwards only the bounded request payload to the advisor and routes a result back only when all three IDs match the active consultation. Main coordinates rather than solving the worker's implementation. While consultation is pending, the worker continues only independent safe work; if none exists, it waits for a completion/message event without redundant retries. The advisor's response is diagnostic advice, never implementation evidence, approval, or a gate verdict; the worker must independently try relevant advice and report the observed result.
- A consultation is one-shot and non-recursive: an advisor result alone does not trigger another request. Before requesting again, the worker first tries relevant advice and records the observed outcome, or provides genuinely new discriminating evidence. Do not use repeated consultations as an unbounded escalation chain.
- Before review or commit, Main resolves or explicitly cancels every outstanding consultation and invalidates its IDs. Worker completion, cancellation/replacement, and gate transition take precedence over late advisor output: do not route it to a completed worker or let it alter a reviewed snapshot. Ignore stale results, even if their IDs otherwise look plausible.
- The default `task-advisor` model is exactly `opencode-go/deepseek-v4.1-flash:max`. Before each launch, Main checks effective project/user agent and model overrides and does not silently repair them. Before any advisor override selecting the GPT-6.1 Sol model family at any provider or effort, Main tells the user the task and consultation IDs, exact resolved model and effort, and blocker/escalation reason, then explicitly asks for approval scoped to that consultation; launch only after explicit approval. Silence, prior approval, urgency, failure, or approval of the default-model rollout is not consent. Denial or pending approval means use the verified default DeepSeek selection or wait, never an unauthorized fallback. Record a bounded approval reference when applicable. If the available dispatch schema cannot express a per-call override, report that limitation; do not invent syntax or change persistent defaults/configuration.
- An effective user/project routing override that resolves `task-advisor` to the GPT-6.1 Sol family is covered by the same consent rule as an explicitly proposed override. Approval is one-use and bound to that task/consultation pair; it cannot authorize another attempt. After a denial or while approval is pending, launch only if the effective selector is actually the exact default DeepSeek; otherwise wait and report the routing limitation.
- The advisor is distinct from OMP's built-in passive advisor. Do not change its configuration, task recursion depth, or add cooldowns, enforced counters, or logging. Record only a bounded consultation summary and the worker's attempted result in the normal task artifact.

Before each advisor launch, Main verifies that the effective `task-advisor` definition is non-blocking and that async execution is enabled. If either check fails, Main does not launch synchronously or silently alter configuration; it reports the condition and waits for an authorized resolution.

## Workflow

### 1. Resolve the plan

1. Inspect the existing global plan and sprint plans using the locations and conventions defined by `manage-plans`.
2. Determine whether an existing pending or active sprint already covers the requested feature.
3. If it does, use that sprint and preserve its task order.
4. If it does not, invoke `manage-plans` directly in the current Main session, with the exact current model, to create or update the plan and sprint plan.
5. Do not spawn a planning subagent or begin implementation until the feature is represented by ordered sprint tasks.

### 2. Select and launch a worker

1. Classify each task before assignment. Use `task` by default, including when the task is unfamiliar, large, slow, or has ordinary review findings. Use `hard-task` only when the task demonstrably requires sustained high-complexity reasoning about interacting correctness constraints (for example, concurrency ordering, an irreversible migration with cross-system invariants, or a nontrivial algorithm), or when a documented escalation meets that bar. A risky domain alone is insufficient. Record the specific reason in the brief and gate record.
2. Before launch, inspect the effective agent definition and async availability as described above. Launch one fresh async worker for the task or correction; transfer the prior artifact, accepted evidence, unresolved findings, and affected boundaries. Do not resume an idle agent for a new assignment.
3. Assign exactly one sprint implementation task at a time. Main marks it [~] in the active sprint plan, then briefs the `task` or `hard-task` worker to read `skill://implement-atomic-task` and verify behavior before handoff. Include task ID, unique attempt ID, acceptance criteria, affected boundaries, explicit project root/repository when project-backed, sprint-plan location, required `artifacts/sprint-<N>/task-<M>.md` path, any `hard-task` justification, and the >5-minute proactive-message requirement. Project-backed tasks stay [~] until evidence PASS and successful exact-snapshot commit; this current global-configuration rollout stays [~] until its evidence gate passes and is documented as not a project commit.
4. Track the async worker through completion and messages, not status polling. At 250K tokens, require a partial handoff and end that attempt; never continue it toward 300K. Keep the task [~], invalidate the old attempt, and transfer its artifact and unresolved findings to a fresh worker with a new attempt ID.
5. Reclassify every new task independently. `hard-task` is justified only for that task or a documented escalation that meets the classification bar; ordinary next tasks return to `task`.

An evidence finding requires correction, not automatic escalation. Keep the same task ID and artifact across correction attempts; record failed attempts and remaining obstacles. A single mistake, review finding, tool failure, or slow progress does not justify `hard-task`. Before each replacement, preserve plan state, accepted evidence, unresolved findings, and the superseded attempt ID. Ignore late events from the superseded attempt.

### 3. Run evidence gates

After each implementation task is completed, and before assigning any project task outside an explicitly predeclared shared atomic batch:

1. Confirm the matching worker's completion event and keep its handoff artifact.
2. Start one fresh async `evidence-reviewer`, after checking its effective definition and async availability. Give it the task acceptance criteria, changed scope, project root, `artifacts/sprint-<N>/task-<M>.md`, worker output, sprint-plan location, and verification evidence.
3. Accept a review only after the matching reviewer job completes. Read its returned output or artifact; a progress message or completion status without the review evidence is not a verdict.
4. Classify findings as actionable or non-actionable from cited evidence.
5. If actionable findings exist, launch a fresh worker with the same task ID, a new attempt ID, the same artifact, and the review findings. Have it correct, re-verify, update the artifact, and keep the sprint task [~]. After that worker completes, run a fresh async evidence review. Do not overlap reviewers for the same work.
6. A passing evidence review is the **evidence gate**, not committed completion for a project-backed task. Main records the gate result, then immediately runs that task's project commit checkpoint below before assigning another independent project task. Only Main marks [x]: for project-backed tasks, only after both evidence PASS and successful commit; for this current user-global configuration rollout only, after evidence PASS with the artifact explicitly recording that the edits are not a project commit. A worker's success, stale PASS, or artifact is not authorization to commit.
7. If a project commit is unavailable or fails, keep that project task `commit_pending`; do not mark [x] or assign the next independent project task. Resolve the blocker and retry only the same unchanged approved snapshot safely. Any changed content requires a fresh evidence review. The current global-configuration rollout has no project commit target and is not a generic exception for project work.

### 3a. Freeze and commit the reviewed project snapshot

For each independently gated project task, after the matching worker has completed and stopped editing and the read-only reviewer has completed with PASS:

1. Main confirms the explicitly assigned project repository and target branch/ref, freezes the reviewed base and exact approved tree/diff (including additions, deletions, and mode changes), and records its scope and snapshot/tree hash with the evidence-review reference. Confirm the selected repository, base/ref, index, worktree, and ownership still support that snapshot. A PASS for a different or stale snapshot does not authorize a commit. A named-path list is a scope reference, not proof of ownership: inspect staged and unstaged changes on every candidate path. A path is eligible for a scoped commit only when it is wholly task-owned, its current worktree content exactly matches the reviewed content, and neither its index nor worktree contains unrelated user hunks. If mixed ownership or base/content drift cannot be safely separated, stop with `commit_pending` and ask for ownership resolution and/or a fresh evidence review.
2. Main commits that snapshot before assigning the next project task using standard Git porcelain from the explicitly assigned repository, honoring configured identity, signing, and hooks. If the real index has been reviewed as free of unrelated changes and its staged tree exactly equals the approved snapshot, ordinary `git commit` is appropriate. When unrelated paths are already staged, commit only fully task-owned paths whose worktree content exactly matches the reviewed snapshot with ordinary scoped porcelain such as `git commit --only -- <owned_paths>`; stage genuinely new owned paths only with explicit `git add -- <owned_new_paths>` when needed. If these conditions do not hold, do not guess, craft a synthetic index, or treat path names alone as isolation: leave the task `commit_pending` and request ownership resolution/re-review. Do not bypass hooks or signing.
3. Immediately inspect the resulting commit and post-commit state: verify the target ref and expected parent/base, the commit SHA and committed paths/content against the reviewed snapshot, and `git diff --cached`/status. The remaining staged diff must contain only the user's intended staged changes and no reversion of committed task paths. Record this evidence with the target repository/ref, base SHA, reviewed snapshot/scope, and evidence-review reference; a byte-for-byte index comparison does not replace these semantic staging checks. Never use `git add .`, `git add -A`, force-add ignored task artifacts, automatic stash/reset/checkout, or amend/history rewriting. Do not commit from an implicit ancestor or home repository.
4. A hook/signing/identity rejection, failed commit, changed base/ref, mismatch with the reviewed snapshot, unexpected staged diff, or uncertain result leaves the task `commit_pending`; do not mark [x] or assign the next independent project task. Do not bypass the failure or discard user state. Resolve ownership or the cause and retry only while the same approved snapshot and expected base/ref remain valid; any changed content requires a fresh evidence PASS first. Record success only after verifying the target ref resolves to the recorded commit and the post-commit checks above pass.

Each independently gated task gets its own immediate checkpoint; do not hold successful tasks for a sprint-end commit. The sole batching exception is a genuinely shared atomic batch explicitly defined as one checkpoint boundary before implementation: Main may finish only that batch's included work, each included task must have a completed PASS gate, and one frozen snapshot must contain only the batch's approved changes. Commit the batch immediately after its last PASS and before any task outside it, using the same ownership, porcelain, and post-commit checks above. If the batch cannot be safely separated, keep it `commit_pending`; never combine unreviewed work or delay independent tasks for convenience.

If no project repository has been assigned or authorized for an actual project task, do not create/init one or commit the user's home/ancestor repository. Report the repository blocker and keep that project task `commit_pending` until a target is supplied/authorized. The current user-global configuration rollout is outside project-commit scope because it uses a separate temporary evidence workspace; record that fact, do not represent it as a project commit, and do not turn this rollout-specific boundary into a general commit-skip option.

After any later correction, including a deep-review correction, reopen the affected task, assign a fresh correction worker, obtain a fresh evidence review, and create a new separate commit on top of the earlier checkpoint. Never amend or rewrite an earlier task commit. Deep review treats cited passed evidence gates and Main-recorded commit checkpoints as established ground, then hunts differential risks.

### 4. Run the sprint gate

After all task-level evidence gates and required project commit checkpoints have passed:

1. Ensure every evidence reviewer has completed or been explicitly cancelled. Keep its report and artifact readable for the deep reviewer.
2. Start one fresh async `deep-reviewer` only at the end-of-sprint gate. Give it the sprint acceptance criteria, per-task evidence-review reports and artifact locations, worker verification evidence, and Main-recorded project commit evidence. It must not re-verify passed checks; it treats cited review and commit evidence as established ground while hunting differential risks, ambiguities, and cross-task interactions the evidence reviews may have missed.
3. Accept its review only after the matching deep-reviewer job completes and its report is read.
4. If it reports actionable findings, reopen the affected task, assign a fresh correction worker, obtain a fresh evidence review, and make a new separate commit on top of the earlier checkpoint; never amend/rewrite it. Main marks [x] only after the correction's fresh evidence PASS and successful separate commit, then run a fresh end-of-sprint deep review.
5. Repeat until the latest deep review has no unresolved actionable findings.

The deep reviewer does not replace evidence review, and passed evidence reviews do not replace the sprint-wide differential review.

### 5. Complete and retire

Declare the sprint complete only when all of the following are true:

- every planned task has a passing evidence review, and every project-backed task's required commit checkpoint has succeeded;
- no project-backed task remains `commit_pending`;
- the latest sprint-wide deep review has no unresolved actionable findings;
- corrections and re-reviews are complete, with each correction checkpoint separate from the earlier commit;
- plan and sprint status reflect the verified result;
- relevant worker artifacts, reviewer reports, and commit evidence have been inspected and recorded;
- no superseded attempt can advance a gate.

Keep artifacts readable. Explicitly cancel failed, duplicate, or over-budget jobs that must not continue; do not mistake Main's interruption for job cancellation.

## Scheduling rules

Use these legal states:

1. **Planning:** zero active subagents; Main resolves or creates the plan.
2. **Implementation:** one active sprint implementation worker.
3. **Evidence review:** the implementation worker is complete; one active `evidence-reviewer`.
4. **Correction:** one fresh worker attempt after the reviewer completes, followed by a fresh evidence review.
5. **Commit pending:** a project-backed task has evidence PASS but its required exact-snapshot commit has not been confirmed; no [x] and no next independent project task. The current global-configuration rollout is explicitly outside project-commit scope.
6. **Deep review:** all task evidence gates and required task commit checkpoints have passed; one active `deep-reviewer`.
7. **Complete:** no unresolved findings; all required async jobs have completed or been explicitly cancelled.

Never exceed two active subagents total. Main uses job-completion and message events, with `functions.wait` only when otherwise blocked; it does not poll or use eval wait/barriers for supervision. A timer is a separate finite background shell job and never changes the worker's task timeout. If a gate is pending, keep the task in progress until a matching completion event and evidence justify advancement.
When assigning project work, identify the assigned project repository/root explicitly; a current directory or ancestor/home Git repository is never an implicit target. For global configuration work without a project repository, record that it is outside project-commit scope; do not use this as a generic skip-commit option.
Orchestrator handoffs include the evidence verdict/reference and, for each project-backed task, the commit state/SHA and reviewed-snapshot reference; for the current global-configuration rollout, state explicitly that no project commit was made.

## Orchestrator output

Report only orchestration-relevant state: selected plan and sprint, active agent roles, assigned task and attempt IDs, worker-type justification or transition, gate results with artifact references, unresolved findings, replacements or cancellations and their reasons, and final completion status. Leave implementation details to worker and reviewer artifacts.