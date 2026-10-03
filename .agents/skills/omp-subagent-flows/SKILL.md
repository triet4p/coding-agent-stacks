---
name: omp-subagent-flows
description: Orchestrate planned feature delivery in Oh My Pi with asynchronous workers and reviewers, per-task evidence gates, and a final differential deep review.
---

# OMP Subagent Flows

## Scope

Use this skill only inside **Oh My Pi (OMP)** when a user requests feature implementation that belongs in a plan or sprint.

Never use this workflow in Codex CLI, Claude Code, or any other coding-agent CLI. Never translate its OMP agent names, tools, lifecycle operations, or artifact URLs to another runtime.

The main session is only an orchestrator and plan manager. It may inspect and edit plans, select and brief agents, match compact task/attempt-correlated summaries to current attempts, coordinate workflow transitions, and decide gates. It does not inspect implementation details or full agent histories, edit product/source files, debug, execute sprint work or Git operations, or write task, evidence, review, log, or checkpoint records. Its only durable edits are plans: keep statuses current and add concise outcome/gate/checkpoint summaries with links to the worker artifact, reviewer report, frozen PASS reference, and executor checkpoint record. Never copy artifact details into a plan.

## Invariants

1. Keep at most **two active subagents total**, including implementation workers, reviewers, advisors, and checkpoint executors.
2. Planning remains in the current main session and uses the **exact current model**. Never delegate plan creation or switch models for it.
3. Use a fresh worker for each task or correction; transfer the prior worker's artifact and unresolved findings instead of reviving an idle agent. **`task` is the default; `hard-task` is never sticky.** Stop at **250K tokens** for a partial handoff and never exceed **300K tokens** in one worker.
4. Run one sprint implementation task at a time. Run an `evidence-reviewer` after each completed task and pass its gate before proceeding. Project-backed tasks also require an exact-snapshot checkpoint before the next independent project task; only a predeclared shared atomic batch may continue through its included tasks before one checkpoint. Never batch task-level evidence reviews.
5. Run a `deep-reviewer` only at the end of the sprint, after every task has passed its evidence gate and every required project checkpoint has succeeded. A correction may require another end-of-sprint differential review.
6. A review with actionable findings does not pass. Correct the findings and run a fresh review at the same level.
7. The effective definitions for `task`, `hard-task`, `evidence-reviewer`, `deep-reviewer`, and checkpoint-executor `task` assignments must be `blocking: false`; inspect project-level overrides before launch. If a flow definition is blocking, or async execution is disabled/unavailable, do not launch synchronously, silently repair an override, or edit runtime configuration; report the condition and wait for authorized resolution.
8. For work expected to exceed 5 minutes, every worker, reviewer, and checkpoint executor proactively messages Main with task/sprint ID, attempt ID, current stage, and reason it will run long. If that becomes clear only during execution, message then. Work lasting 5 minutes or less needs no proactive message. This notice is independent of timer supervision and is not a gate verdict.
9. Every subagent enumerates and reads all regular files under `~/.agents/rules/*` before substantive work, including corrections and replacements. Apply relevant rules at their proper precedence; report conflicts or inaccessible files instead of silently ignoring them.

## Roles

- **Main session:** plan management and summary-only orchestration. The user-defined `~/.omp/agent/agents/task.md` overrides OMP's bundled `task` agent; project-level definitions may override the user definition. Main checks effective definitions before launch, edits only plans, and never reads full worker histories or writes evidence records.
- **Worker:** a fresh `task` (default) or `hard-task` subagent for one sprint task or correction. It owns implementation and its task artifact; its final handoff to Main is compact and points to that artifact.
- **Evidence reviewer:** a fresh `evidence-reviewer`, read-only on assigned source, worker artifact, and plan. It receives the worker artifact and may inspect the assigned source and worker history directly. It owns and writes its detailed report under `<evidence-root>/artifacts/sprint-<N>/reviews/`; Main receives only the compact verdict, reviewed-snapshot reference, findings summary, and report path.
- **Deep reviewer:** a fresh `deep-reviewer`, read-only on source and existing records, default model `opencode-go/glm-5.3-flash:high`, that differentially reviews the sprint after all per-task gates and required checkpoints pass. It reads worker artifacts, evidence-review reports, and executor checkpoint records directly; it may inspect worker history directly when needed, but does not redo passed checks. It owns its report.
- **Checkpoint executor:** after an evidence PASS, Main may assign a fresh, non-blocking async default `task` agent a checkpoint-only assignment for the exact frozen snapshot. The executor does not edit product/source content or approve the evidence gate; it owns the checkpoint record under `<evidence-root>/artifacts/sprint-<N>/checkpoints/`. Main alone authorizes this assignment and decides whether its compact result establishes checkpoint success.

Use the evidence root named by the active plan or assignment; resolve it from that source of truth rather than from this global skill or the current working directory. Store task artifacts, reviewer reports, and checkpoint records below `<evidence-root>/artifacts/sprint-<N>/`. Never use `local://` for durable work records. Workers, reviewers, and checkpoint executors own their own records; Main writes only plan/status references and concise summaries.

## Async jobs, events, interruption, and progress

### Launch and result acceptance

- Launch each flow agent as an asynchronous job and record the task ID, unique attempt ID, agent ID, returned job ID, and role. Give replacements a new attempt ID. The async launch/result and agent-message events are Main's supervision channels; progress messages are not completion events.
- Accept a worker, reviewer, or checkpoint-executor result only when it matches the current task ID, attempt ID, and agent ID, and that agent has completed. A launch receipt, message-delivery receipt, progress reply, partial handoff, or timer event is not task completion or a gate verdict.
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
- On worker, reviewer, or checkpoint-executor completion, completion takes precedence: cancel its timer job if still active and invalidate that timer generation. If a completion and timer event race, handle completion first. Ignore a late timer whose task, attempt, or generation is no longer current.
- On a current timer event, Main sends exactly one outstanding `progress_request` to the matching agent, carrying `task_id`, `attempt_id`, `agent_id`, `progress_request_id`, and `timer_generation`. Do not issue another request while one is outstanding. For a `task` or `hard-task` worker only, when no advisor request, positive interest, or consultation is pending, Main includes the single field `advisor_offer: "Bạn cần advisor gì không?"` in that same request; it is not a separate message. Omit the offer while any advisor request, positive interest, or consultation is pending. Reviewers and checkpoint executors do not receive this offer.
- The matching progress reply carries all of those IDs and these fields: `stage`, `completed_since_last_report`, `new_evidence`, `current_blocker`, `attempts`, `results`, `next_action`, and `help_needed`. A worker additionally returns `advisor_needed: false|true` and may include one complete `advisor_request` payload when qualified; `false` is a cheap decline and triggers no follow-up, while `true` without the complete request is pending interest, not a consultation. A `true` reply or offer alone never launches an advisor. Reviewers and checkpoint executors do not consume implementation-advisor consultations. Main compares reported deltas and evidence; elapsed time alone is not difficulty or a stall. A timer event or progress reply never substitutes for completion or review.
- After a matching reply, if the same attempt remains active and no request is outstanding, Main starts the next one-shot timer generation at an adaptive 10–30-minute interval. Do not keep restarting the timer while a reply is pending. Workers continue to send the required >5-minute proactive notice independently of this timer.
- Do not automatically request help, replace a worker, or advance a gate solely because a timer expires. Keep implementation details in worker artifacts; Main's messages and plan remain orchestration-only.

### Main-brokered task-advisor consultations

- A worker may request diagnostic help before a timer fires when it has a bounded, evidence-backed unresolved technical question or material uncertainty that genuinely useful diagnostic input could inform, including competing plausible hypotheses with no safe discriminating next action. Repeated identical errors or failed hypotheses, no new evidence across distinct attempts, and an unchanged blocker without a discriminating next action are examples, not prerequisites. Elapsed time or a fixed attempt count alone is never sufficient; generic or open-ended task delegation does not qualify.
- A worker's `advisor_request` contains the matching `task_id`, `attempt_id`, a unique `consultation_id`, goal/criterion, current blocker, bounded relevant evidence/snippets, tried hypotheses and their results (or an explicit statement that none were safely tested yet), constraints, and one exact actionable question. Do not send full conversations, trajectories, histories, logs, or unrelated context. Workers never spawn advisors or change model/config/depth themselves.
- The timer's `advisor_offer` is part of the existing progress request, not a separate message. `advisor_needed: false` is a cheap decline. A `true` reply, offer, elapsed time, or timer event alone never launches an advisor: Main requires a complete bounded `advisor_request` and validates that its exact question is actionable, the supplied evidence is relevant, and the request explains why diagnostic help is needed. A `true` without that payload is pending interest, not a consultation; do not re-offer or send a separate follow-up. The worker may add the complete request to its next normal progress reply or send one qualified request directly.
- Deduplicate by active task/attempt and blocker/criterion: do not launch or forward a duplicate while a request, pending interest, or consultation exists, and allow at most one active consultation per worker and two active subagents total. Omit further advisor offers while any request, pending interest, or consultation exists. Before asking again after a consultation, the worker must first try relevant advice and record the observed result, or provide genuinely new discriminating evidence.
- Main brokers a qualified request to a fresh `task-advisor` sibling, checks its effective definition/model and `blocking: false`, and confirms async execution is available before launch. Use the existing `task` tool schema: with batch enabled, provide required `context` and one `tasks[]` item containing `agent`, `task`, and `solutionSpace`; with batch disabled, use one flat task item. The task item's `tools` field exposes parent eval-kernel tools; it is not an agent-tool whitelist. Do not invent a task model-override field.
- Main forwards only the bounded request and routes a result back only when task, attempt, and consultation IDs all match. While it is pending, the worker continues only independent safe work; otherwise it waits for a completion/message event without redundant retries. Advice is diagnostic only, never implementation evidence, approval, or a gate verdict; the worker independently tries relevant advice and records the result.
- Before review, checkpoint execution, or replacement, Main resolves or explicitly cancels every outstanding consultation and invalidates its IDs. Worker completion, cancellation/replacement, and gate transition take precedence over late advisor output. Ignore stale results, even if their IDs otherwise look plausible.
- The default `task-advisor` model is exactly `opencode-go/deepseek-v4.1-flash:max`. Before each launch, Main checks effective project/user agent and model overrides and does not silently repair them. Before any advisor override selecting the GPT-6.1 Sol model family at any provider or effort, Main tells the user the task and consultation IDs, exact resolved model and effort, and blocker/escalation reason, then explicitly asks for approval scoped to that consultation; launch only after explicit approval. Silence, prior approval, urgency, failure, or approval of a different rollout is not consent. Denial or pending approval means use the verified default DeepSeek selection or wait, never an unauthorized fallback. Record a bounded approval reference when applicable. If the dispatch schema cannot express a per-call override, report that limitation; do not invent syntax or change persistent defaults/configuration.
- An effective user/project routing override resolving `task-advisor` to the GPT-6.1 Sol family follows the same consent rule. Approval is one-use and bound to that task/consultation pair. After denial or while approval is pending, launch only if the effective selector is exactly the default DeepSeek; otherwise wait and report the routing limitation.
- The advisor remains read-only and distinct from OMP's built-in passive advisor. Do not change advisor configuration or recursion depth, or add cooldowns, enforced counters, or telemetry/logging. Record only a bounded consultation summary and attempted result in the worker's normal task artifact. Evidence and deep reviewers do not consume task-advisor consultations.

Before each advisor launch, Main verifies that the effective `task-advisor` definition is non-blocking and async execution is enabled. If either check fails, Main does not launch synchronously or silently alter configuration; it reports the condition and waits for an authorized resolution.

## Workflow

### 1. Resolve the plan

1. Inspect the existing global plan and sprint plans using the locations and conventions defined by `manage-plans`.
2. Determine whether an existing pending or active sprint already covers the requested feature.
3. If it does, use that sprint and preserve its task order.
4. If it does not, invoke `manage-plans` directly in the current Main session, with the exact current model, to create or update the plan and sprint plan.
5. Do not spawn a planning subagent or begin implementation until the feature is represented by ordered sprint tasks.

### 2. Select and launch a worker

1. Classify each task before assignment. Use `task` by default, including for unfamiliar, large, slow, or ordinary-review work. Use `hard-task` only when the task demonstrably requires sustained high-complexity reasoning about interacting correctness constraints (for example, concurrency ordering, an irreversible migration with cross-system invariants, or a nontrivial algorithm), or a documented escalation meets that bar. A risky domain alone is insufficient. Record the specific justification in the brief and plan.
2. Inspect the effective definition and async availability. Launch one fresh async worker per implementation task or correction; transfer the prior artifact, accepted evidence, unresolved findings, and affected boundaries. Do not resume an idle agent for new work.
3. Assign exactly one sprint implementation task at a time. Main marks it [~] in the active sprint plan, then briefs the worker to read `skill://implement-atomic-task`. Include task/attempt IDs, criteria, affected boundaries, explicit project repository/worktree/ref if project-backed (or explicit non-project designation), sprint-plan location, absolute evidence root, required `<evidence-root>/artifacts/sprint-<N>/task-<M>.md` path, any `hard-task` justification, and the >5-minute proactive-message requirement. A task is not non-project merely because its repository was omitted. Project-backed tasks stay [~] until evidence PASS and successful checkpoint; an explicitly non-project task does not require a project Git checkpoint.
4. Track the worker through completion and messages, not polling. At 250K tokens, require a partial handoff and end that attempt; never continue it toward 300K. Keep the task [~], invalidate the old attempt, and transfer its artifact and unresolved findings to a fresh worker with a new attempt ID.
5. Reclassify every new task independently. `hard-task` is justified only for that task or a documented escalation meeting the classification bar; ordinary next tasks return to `task`.

An evidence finding requires correction, not automatic escalation. Keep the same task ID and worker artifact across correction attempts; record failed attempts and remaining obstacles there. A single mistake, review finding, tool failure, or slow progress does not justify `hard-task`. Before replacement, preserve plan state, accepted evidence, unresolved findings, and the superseded attempt ID. Ignore late events from the superseded attempt.

### 3. Run evidence gates

After each implementation task completes, and before assigning any project task outside an explicitly predeclared shared atomic batch:

1. Confirm the matching worker completion and its handoff artifact at `<evidence-root>/artifacts/sprint-<N>/task-<M>.md`.
2. Start one fresh async `evidence-reviewer` after checking its effective definition and async availability. Give it the criteria, changed scope, explicit project root/repository, worker artifact, source access, worker history access, sprint-plan location, and verification evidence. The reviewer inspects details directly; Main does not relay full histories.
3. Accept a verdict only from the matching completed reviewer. The reviewer writes its own report under `<evidence-root>/artifacts/sprint-<N>/reviews/` and returns a compact verdict (`PASS`/`FAIL`), reviewed base/snapshot/scope reference, findings summary, and report path. Main matches that summary to the current task/attempt and adds only a concise reference/status to the plan; it does not write or transcribe the report.
4. Classify actionable findings from the reviewer's cited evidence. A progress message, artifact alone, stale PASS, or completion status without a matching verdict is not a gate result.
5. For actionable findings, launch a fresh worker with the same task ID, a new attempt ID, the same artifact, and the findings. It corrects, re-verifies, updates its artifact, and keeps the task [~]. Then run a fresh async evidence review; never overlap reviewers for that task.
6. Evidence PASS is the evidence gate, not project-backed completion. After PASS, Main authorizes the checkpoint-only assignment below for the exact frozen reviewed snapshot before any next independent project task. Only Main marks a project task [x], and only after both PASS and a successful executor checkpoint. An explicitly designated non-project task may be completed after PASS without a project Git checkpoint; do not use missing repository information as that designation.
7. If the checkpoint is unavailable or fails, keep the project task `commit_pending`; do not mark [x] or assign the next independent project task. Resolve the blocker and retry only the same unchanged approved snapshot safely. Any changed content requires fresh evidence PASS.

### 3a. Delegate the exact-snapshot project checkpoint

For each project-backed task, or a predeclared shared atomic batch after every included task has separately passed its evidence gate:

1. Main accepts only a matching reviewer `PASS` tied to the exact base, approved tree/diff snapshot, scope, and explicitly assigned repository/ref. It authorizes a fresh executor with that frozen PASS reference and snapshot identity. A missing, stale, mismatched, or uncertain reference is not authorization; resolve ownership or obtain a fresh review. Main does not run Git, change refs, write checkpoint evidence, or authorize broader scope.
2. Assign a fresh async, non-blocking default `task` agent a checkpoint-only task. `hard-task` is not sticky and is not the default executor. Check its effective definition and async availability; keep the two-active-agent limit. Give it the reviewer PASS reference, exact repository/git-dir, worktree, `-C` root, target branch/ref, expected base SHA, approved scope and tree/diff snapshot hash, and the checkpoint-record path under `<evidence-root>/artifacts/sprint-<N>/checkpoints/`. The executor may perform only the authorized Git checkpoint and verification; it must not edit product/source content, broaden scope, approve the review, or push.
3. The executor verifies the explicit repository and target ref/base, real index, worktree, and ownership before committing. Freeze/check additions, deletions, mode changes, and exact approved content against the review reference. A path is eligible only if wholly task-owned, current worktree content exactly matches reviewed content, and neither index nor worktree contains unrelated user hunks. A named-path list is not ownership proof. If mixed ownership, base/content drift, or an uncertain snapshot cannot be safely separated, stop with `commit_pending`; request ownership resolution or a fresh evidence review. Never infer a repository from cwd or use an ancestor/home repository.
4. Use standard Git porcelain from the explicitly assigned repository, honoring configured identity, signing, and hooks. If the real index has no unrelated changes and its staged tree exactly equals the approved snapshot, ordinary `git commit` is appropriate. If unrelated paths are staged, commit only fully task-owned paths whose worktree exactly matches reviewed content with ordinary scoped porcelain such as `git commit --only -- <owned_paths>`; stage genuinely new owned paths only with explicit `git add -- <owned_new_paths>` when needed. If these conditions do not hold, do not guess, craft a synthetic index, or treat path names alone as isolation. Never bypass hooks/signing, run `git add .` or `git add -A`, force-add ignored artifacts, automatically stash/reset/checkout, amend/rewrite history, or push.
5. Immediately verify the target ref and expected parent/base, commit SHA, committed paths/content against the approved snapshot, and post-commit `git diff --cached`/status. Remaining staged changes must contain only the user's intended staged changes and no reversion of committed task paths. The executor writes these observations and the PASS reference in its own checkpoint record; a byte-for-byte index comparison does not replace semantic staging checks.
6. A hook/signing/identity rejection, failed commit, changed base/ref, mismatch with the reviewed snapshot, unexpected staged diff, or uncertain result leaves the task `commit_pending`. Do not bypass the failure or discard user state. Resolve ownership/cause and retry only while the same approved snapshot and expected base/ref remain valid; changed content requires fresh evidence PASS. The executor's compact completion identifies the record and success/failure. Main decides success only after matching that report to its authorization and records a concise status/reference in the plan; Main never writes the checkpoint record.

Each independently gated project task gets its own immediate checkpoint before the next independent task. The sole batching exception is a genuinely shared atomic batch declared as one checkpoint boundary before implementation: every included task still gets a separate PASS; after the batch's last PASS, one frozen snapshot containing only the batch's approved changes is checkpointed before any task outside it. Apply the same ownership, porcelain, and post-commit checks; never combine unreviewed work or delay independent tasks for convenience.

An actual project task without an explicitly assigned/authorized repository remains `commit_pending`; do not create/init a repository or commit a home/ancestor repository. Only work explicitly classified as non-project in its plan/assignment avoids a project checkpoint; it still uses its assigned evidence root and evidence gate. No rollout-specific or missing-repository exception changes project-backed status.

After any later correction, including a deep-review correction, reopen the affected task, assign a fresh correction worker, obtain a fresh evidence review, and create a separate checkpoint on top of the earlier commit through a fresh checkpoint-only executor. Never amend or rewrite an earlier checkpoint. Deep review treats cited passed evidence gates and executor checkpoint records as established ground, then hunts differential risks.

### 4. Run the sprint gate

After all task-level evidence gates and required project commit checkpoints have passed:

1. Ensure every evidence reviewer has completed or been explicitly cancelled. Keep its report, worker artifact, and any executor checkpoint record readable for the deep reviewer; Main needs only their compact result summaries and paths.
2. Start one fresh async `deep-reviewer` only at the end-of-sprint gate. Give it the sprint criteria, worker artifacts, evidence-review reports, and executor checkpoint records directly. It must not re-verify passed checks; treat cited review and checkpoint evidence as established ground while hunting differential risks, ambiguities, and cross-task interactions.
3. Accept a verdict only after the matching deep-reviewer job completes and returns its compact result and report path. Main adds a concise reference/status to the plan; the reviewer owns the detailed report.
4. If actionable findings exist, reopen the affected task, assign a fresh correction worker, obtain a fresh evidence review, and authorize a separate checkpoint through a fresh checkpoint-only executor; never amend/rewrite an earlier commit. Main marks [x] only after the correction's fresh PASS and successful checkpoint, then runs a fresh end-of-sprint deep review.
5. Repeat until the latest deep review has no unresolved actionable findings.

The deep reviewer does not replace evidence review, and passed evidence reviews do not replace the sprint-wide differential review.

### 5. Complete and retire

Declare the sprint complete only when all of the following are true:

- every planned task has a passing evidence review, and every project-backed task's required checkpoint has succeeded;
- no project-backed task remains `commit_pending`;
- the latest sprint-wide deep review has no unresolved actionable findings;
- corrections and re-reviews are complete, with each correction checkpoint separate from the earlier commit;
- plan and sprint status reflect the verified result;
- worker artifacts, reviewer reports, and checkpoint records remain readable and their concise result references are in the plan;
- no superseded attempt can advance a gate.

Keep artifacts readable. Explicitly cancel failed, duplicate, or over-budget jobs that must not continue; do not mistake Main's interruption for job cancellation.

## Scheduling rules

Use these legal states:

1. **Planning:** zero active subagents; Main resolves or creates the plan.
2. **Implementation:** one active sprint implementation worker.
3. **Evidence review:** the implementation worker is complete; one active `evidence-reviewer`.
4. **Correction:** one fresh worker attempt after the reviewer completes, followed by a fresh evidence review.
5. **Checkpoint execution:** evidence PASS is matched to the frozen snapshot; one fresh checkpoint-only `task` executor is active, with no next independent project task assigned.
6. **Commit pending:** a project-backed task has evidence PASS but its required exact-snapshot checkpoint is not confirmed; no [x] and no next independent project task.
7. **Deep review:** all task evidence gates and required project checkpoints have passed; one active `deep-reviewer`.
8. **Complete:** no unresolved findings; all required async jobs have completed or been explicitly cancelled. Explicitly designated non-project tasks need an evidence PASS but no project Git checkpoint.

Never exceed two active subagents total, including advisors and checkpoint executors. Main uses job-completion and message events, with `functions.wait` only when otherwise blocked; it does not poll or use eval wait/barriers. A timer is a separate finite background shell job and never changes a worker's task timeout. If a gate is pending, keep the task in progress until a matching completion event and evidence justify advancement.
When assigning project work, identify the exact authorized repository/git-dir, worktree, `-C` root, target ref, and evidence root; cwd or an ancestor/home repository is never an implicit target. Missing repository information does not reclassify project work as non-project. Only an explicit non-project designation avoids a project checkpoint.
Orchestration handoffs and plan entries contain compact summaries and references: task/attempt and current status, matching evidence verdict/report, frozen reviewed snapshot, checkpoint state/record/SHA, and unresolved findings. Main does not transcribe artifact contents.

## Orchestrator output

Report only orchestration-relevant state: selected plan and sprint; active agent roles and IDs; assigned task and attempt IDs; worker-type justification or transition; compact gate/checkpoint results with artifact paths and frozen-snapshot references; unresolved findings; replacements or cancellations and their reasons; and final completion status. Leave implementation, review, and Git details in their owner-written artifacts. Never return full histories or transcripts.
 
## Change history

- 2026-10-03: Allowed bounded, evidence-backed diagnostic requests before repeated failures; clarified request qualification and generalized evidence-root selection to the active plan or assignment.
