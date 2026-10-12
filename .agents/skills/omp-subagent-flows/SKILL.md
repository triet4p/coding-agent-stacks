---
name: omp-subagent-flows
description: Orchestrate planned feature delivery in Oh My Pi with asynchronous workers on light or full routes: explicitly required review gates, Bronze-only exact-snapshot checkpoints, and conditional end-of-sprint deep review.
---

# OMP Subagent Flows

## Scope

Use this skill only inside **Oh My Pi (OMP)** when a user requests feature implementation that belongs in a plan or sprint.

Never use this workflow in Codex CLI, Claude Code, or any other coding-agent CLI. Never translate its OMP agent names, tools, lifecycle operations, or artifact URLs to another runtime.

The main session is only an orchestrator and plan manager. It keeps its own context minimal and concise, avoiding token-heavy preflight reads. On the light route it may inspect a worker's compact result and verification evidence to make its acceptance check; it never reads full agent histories, codebase source files, or subagent prompt bodies, and never writes worker, evidence, review, or checkpoint records. Its durable edits are plans plus Main's own separate supervision files under the assigned project repository's `artifacts/` directory (or explicit output root). Never copy artifact details into a plan.

## Minimal context & pointer-only orchestration

To prevent orchestrator context bloat (consuming tens of thousands of tokens before work even starts), Main enforces strict context boundaries:

- **Context whitelist for Main:** when starting or orchestrating a task, Main reads ONLY:
  1. The active sprint plan (`docs/sprint-plans/sprint-N.md`) or the user's immediate steer/prompt.
  2. Delivered compact worker results, reviewer gate verdicts, and handoff references.
- **Strictly forbidden for Main to read:**
  - NEVER read subagent prompt bodies (`.omp/agent/agents/*.md`). The OMP harness automatically loads agent definitions upon `functions.task(agent=...)`. Main dispatches directly by agent name.
  - NEVER read `skill://implement-atomic-task` (this is the worker's execution skill; the worker reads it in its own isolated session).
  - NEVER read codebase source code, API implementations, or extensive architecture docs to "prepare context" for workers.
  - NEVER read past/completed sprint plans in `docs/sprint-plans/` or full history transcripts (`history://...`).
- **Pointer delegation to workers:** Main never reads and summarizes technical docs into worker prompts. Main supplies pointers only: task ID, acceptance criteria, constraints, and target file paths/ranges (`read path/to/doc.md:40-80`). The worker reads them on demand in its own ephemeral session.
- **Lightweight handoff to reviewers:** when transitioning from implementation to review, Main transfers pointers only: `task_id`, `attempt_id`, `worker_artifact_path`, `worker_history_uri` (`history://<runtime-agent-id>`), and commit/base refs. The reviewer reads the worker artifact and `history://<worker-agent-id>` directly. Subagents may communicate directly via `write agent://<id>` for clarifications; Main does not act as a transcript relay.

## Route selection: light default, full by condition

Main selects the route for each task or atomic batch before dispatch, repeats it with exact required gates in the worker brief, and records it in an existing sprint plan's workflow line when a plan is needed. A bounded light fix needs no new plan.

- **Light is the default for bounded, low-risk work** with a clear acceptance contract: the worker implements the assigned concern and runs the specific behavior check named in its brief. An evidence review is optional on this route and is assigned only when risk, evidence preservation, or the user requires it; once assigned, it is binding and a FAIL is not ignored. A worker may commit its own verified scope only when the assignment explicitly authorizes that commit. Light-route work has no automatic per-task evidence gate, no automatic project checkpoint, and no deep review merely because the work was called a sprint. Project-backed light work may finish verified and uncommitted when no commit was assigned; an assigned commit that fails or is unavailable leaves the task `commit_pending`.
- **Full is for material risk, contract or interaction changes, or a user requirement**: explicitly required evidence gates per task, a separate Bronze-only exact-snapshot checkpoint at the pre-agreed task or batch boundary, and a deep review only when Main assigns one for meaningful cross-task risk. Required full-route gates cannot be dropped, merged, or downgraded at cutover; changing a route is a deliberate recorded decision, not a convenience.
- Gates declared on either route are mandatory. Main records the route, the exact assigned gates, and any commit authorization (or its absence) in the brief and any existing plan so a successor can see what was actually required.

## Routing ask and scoped authority

- Before dispatching any worker, Main asks the user to choose the role **unless** the user has already explicitly selected a role for the current work or granted scoped routing authority for a task, batch, session, or sprint. A prior selection or granted scope stays in force within its declared boundaries; Main does not re-ask for confirmation inside that scope.
- The ask presents the bounded task, candidate subagent roles and selection rationale, quota observation or `unknown`, recommended light/full route and required gates, and commit authority together. Include exact repository, Git directory, worktree, target ref and staging ownership when commit is authorized. Do not include model/provider names, selectors or effort values.
- For a requested batch without prior role choices or auto-routing authority, send one `ask` call with one question per task. T3–T5 requires at least three separate task questions. Each question names the task ID, concrete work/outcome, eligible roles, recommendation/reason, route/required gates and commit permission; no model metadata. Bind each answer to that task, not the entire batch. Valid choices are explicit Bronze/Silver/Gold and scoped Main selection. A per-task explicit choice takes precedence over broader auto authority; any batch-auto option states its exact scope and does not replace the task questions. Obsolete `task`/`hard-task` implementation roles and the implicit bundled generic `task` are invalid flow choices.
- Never apply an implicit Gold default, and never resolve an uncertain Silver/Gold choice by automatic promotion. Without routing authority, ask; with routing authority, Main chooses from task fit and the user's constraints without re-asking. Bronze fits known procedures; Silver fits bounded reasoning with clear rules and a positive fit; Gold fits medium work involving context, design choices, diagnosis, or integration and needs no prior Silver failure. The user's stated quota/cost preference overrides tier stereotypes, and quota is reported as observed or `unknown` without fabricated measurements.
- Scoped routing authority persists only within its declared scope and never becomes persistent configuration. Honor applicable configured overrides without logging their values; never claim an override was applied when it was not observed.

### Auto-routing for an unattended task sequence

- Accept explicit authority from an ordinary user/steer message, such as "Main tự chọn agent cho các task 3–8, không hỏi lại", or from an `ask` option labeled **"Auto cho dãy task này"**. Offer that option with the concrete covered task IDs/range or named batch/sprint and any role/quota restrictions in its description. Selecting one worker role alone does not authorize auto-routing for later tasks.
- Main acknowledges the covered scope and restrictions once, then autonomously selects and launches workers for that sequence, including in-scope correction and replacement attempts. Do not call `ask` again for role selection, routine escalation within allowed roles, unknown quota, or comparable Silver/Gold fit. Use known definitions, task evidence and the user's preferences; quota `unknown` is not a reason to wait for an absent user.
- Keep authority in the current task/sequence context and pass its bounded reference in worker briefs. It ends when the covered work completes or the user revokes/narrows it; unrelated/new tasks are not included. A steer changing authority governs subsequent dispatches and does not by itself cancel a live worker.
- Auto-routing is not extra commit/push, destructive-action, model-override or advisor-consent permission, and does not waive verification, required gates, detailed replacement handoff/history or async safety. Existing explicit permissions remain in force only within their own scope.
- If an action genuinely needs authority outside the grant or an unreachable prerequisite, do not invent consent or treat user silence as approval. Leave the affected task blocked with the concrete reason and continue only other safe, authorized work that is independent of it and does not cross a required boundary. Ask only for the genuinely missing decision; never block the authorized sequence on a redundant routing question.

## Invariants

1. Keep at most **two active subagents total**, including implementation workers, reviewers, advisors, and checkpoint executors.
2. Planning remains in the current main session and uses the **exact current model**. Never delegate plan creation or switch models for it.
3. Use a fresh worker for each task or correction; transfer the prior worker's artifact and unresolved findings instead of reviving an idle agent. Gold is eligible for medium reasoning; Silver for bounded reasoning with clear rules; Bronze for known procedures and full-route checkpoints. No medal is a sticky or implicit default. Main may auto-select within explicit user authority. Honor applicable user routing overrides before agent defaults. Main owns continuation/replacement; no fixed request/token count ends an attempt.
4. Run one sprint implementation task at a time. An `evidence-reviewer` runs only when its gate is assigned: always on the full route, and on the light route only when Main assigns one. Never batch task-level evidence reviews. A full-route project task also requires a separate Bronze-only exact-snapshot checkpoint at the pre-agreed task or batch boundary before the next independent project task; only a predeclared shared atomic batch, declared and approved as one checkpoint boundary before implementation, may continue through its included tasks before that single checkpoint.
5. Run a `deep-reviewer` only when Main assigns it for meaningful cross-task risk review, and only after every assigned per-task evidence gate and required full-route checkpoint has passed. A correction may require another assigned differential review.
6. A review with actionable findings does not pass. Correct the findings and run a fresh review at the same level.
7. The installed flow definitions for `bronze-task`, `silver-task`, `gold-task`, `evidence-reviewer`, `deep-reviewer`, and checkpoint-executor `bronze-task` assignments are preconfigured `blocking: false`. Main trusts the runtime harness and dispatches directly by role name without pre-reading agent definition bodies. If the runtime reports synchronous execution or no async job manager, report the condition and wait for authorized resolution.
8. For work expected to exceed 5 minutes, every worker, reviewer, and checkpoint executor proactively messages Main with task/sprint ID, attempt ID, current stage, and reason it will run long. If that becomes clear only during execution, message then. Work lasting 5 minutes or less needs no proactive message. This notice is independent of timer supervision and is not a gate verdict.
9. Every subagent enumerates and reads all regular files under `~/.agents/rules/*` before substantive work, including corrections and replacements. Apply relevant rules at their proper precedence; report conflicts or inaccessible files instead of silently ignoring them.

## Roles

- **Main session:** plan management and summary-only orchestration. Main trusts effective definitions at launch without pre-reading prompt bodies, never reads full worker histories, and never writes evidence, review, worker, or checkpoint records; on the light route it inspects enough of the worker's completed result and assigned verification evidence to decide acceptance itself. The bundled OMP generic `task` tool/agent exists outside this flow and must never be selected implicitly as a flow worker, reviewer, advisor, or executor; only the explicit `bronze-task`, `silver-task`, and `gold-task` implementation roles below are flow routes.
- **Worker:** a fresh Main-selected explicit `bronze-task`, `silver-task`, or `gold-task` subagent for one task or correction on the assigned route. Gold is eligible for medium reasoning; Silver for bounded reasoning; neither is an automatic default. Main selects within user routing authority, honoring applicable user overrides before agent defaults. Workers never reroute themselves and report only their role, not model metadata. They own implementation and any assigned artifact; ordinary light work may return a compact result. Light workers MAY commit only verified own scope when explicitly authorized with the exact repository, Git directory, worktree, target ref and staging ownership; no foreign staged changes, amend/rebase/history rewrite or hook/signing bypass. Push needs separate authorization. Full workers do not commit; Silver and Gold never execute full-route checkpoint-only assignments.
- **Evidence reviewer:** a fresh `evidence-reviewer`, read-only on assigned source, worker artifact, and plan. It runs only when Main assigns its gate — required on the full route, optional but then binding on the light route — and once assigned, a FAIL is not ignored. It receives the worker artifact and may inspect the assigned source and worker history directly. It owns and writes its detailed report under the assigned project's `artifacts/sprint-<N>/reviews/` directory (or the explicit assigned output root for non-project work), and its frozen-snapshot manifest only when a full-route checkpoint is planned or the assignment explicitly requires one; Main receives only the compact verdict, reviewed-snapshot reference, findings summary, and report path.
- **Deep reviewer:** a fresh `deep-reviewer`, read-only on source and existing records, using its effective agent definition, that Main may assign for cross-task differential review after every assigned per-task gate and required full-route checkpoint has passed. It reads worker artifacts, evidence-review reports, and executor checkpoint records directly, treating cited passed gates and required checkpoint records as established ground; for light-route tasks without assigned gates it treats the worker's verified result and any explicitly authorized worker commit as evidence, and does not require records that were never assigned. It may inspect worker history directly when needed, but does not redo passed checks. It owns its report.
- **Checkpoint executor:** on the full route, after a matching evidence PASS, Main may assign a fresh, non-blocking async explicit `bronze-task` agent — only `bronze-task` may execute checkpoints; never `silver-task` or `gold-task` — a checkpoint-only assignment for the exact frozen snapshot. The executor does not edit product/source content or approve the evidence gate; it owns the checkpoint record under the assigned project's `artifacts/sprint-<N>/checkpoints/` directory (or the explicit assigned output root for non-project work). Main alone authorizes this assignment and decides whether its compact result establishes checkpoint success.

### Model resolution

Apply `~/.agents/rules/subagent-routing.md` to every worker, advisor, reviewer and checkpoint executor. Main dispatches directly by explicit agent name without reading agent markdown prompt files; the OMP runtime resolves the installed definition and applies configured user/project overrides automatically. Do not cache a selector or copy one from a skill.

Normally dispatch by explicit agent name without a per-call model argument so the runtime honors configured overrides. Use an explicitly requested per-call override only when the supported API provides it; otherwise continue with the named role's effective configuration. Do not invent fields, mask configured overrides or temporarily rewrite shared/session settings as a workaround.

Report only role/type plus required work IDs and evidence. Do not put model/provider names, selectors or effort values in routing asks, briefs, chat, logs, plans, artifacts, handoffs or reports; do not copy them from prior histories. Actual execution configuration/API fields may contain the necessary values, but are not reporting metadata. Never fabricate successful application of an override. This is an instruction-output rule, not a runtime trace-redaction mechanism.

Resolve the record root from the active plan or assignment rather than from this global skill or the current working directory. Store task artifacts, reviewer reports, and checkpoint records below the assigned project's repository `artifacts/` directory; explicit non-project work uses its explicitly assigned output root. Never use `local://` for durable work records, never another project's artifacts, and never a global home log. Workers, reviewers, and checkpoint executors own their own records; Main writes only plan/status references, concise summaries, and its own separate supervision/handoff files.

### Handoff and temporary-state files
Plans stay stable: scope, criteria, current status, milestones, decisions, blockers, and concise outcome links only. Never put per-turn dispatch receipts, model logs, progress requests, timer events, or copied handoffs in `docs/PLAN.md` or `sprint-<N>.md`.

Detailed handoffs and temporary supervision state are separate attempt-scoped files under the assigned project's `artifacts/` directory (`artifacts/sprint-<N>/handoffs/` or `artifacts/<task-id>/`). Explicit non-project work uses its assigned output root. Before pausing or replacing an agent, follow the mandatory handoff protocol in `references/replacement-and-handoff.md`.

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

- For every active attempt, Main starts exactly one finite background shell timer with an adaptive observation interval of **10–30 minutes**. Use an existing finite async shell timer (for example, a PowerShell `Start-Sleep` command launched through Bash with async enabled) that emits a marker containing the task ID, attempt ID, and timer-generation ID. This timer is an observation prompt, not a worker deadline or a reason to stop work.
- Choose the interval from current task context and observed progress, not from elapsed time alone. Keep only one timer generation active per attempt. Do not rearm/restart timers in a hot loop.
- On worker, reviewer, or checkpoint-executor completion, completion takes precedence: cancel its timer job if still active and invalidate that timer generation. If a completion and timer event race, handle completion first. Ignore a late timer whose task, attempt, or generation is no longer current.
- On a current timer event, Main sends exactly one outstanding `progress_request` to the matching agent, carrying `task_id`, `attempt_id`, `agent_id`, `progress_request_id`, and `timer_generation`. Do not issue another request while one is outstanding. For any implementation `bronze-task`, `silver-task`, or `gold-task` worker only (including corrections), when no advisor request, positive interest, or consultation is pending, Main includes the single field `advisor_offer: "Bạn cần advisor gì không?"` in that same request; it is not a separate message. Omit the offer while any advisor request, positive interest, or consultation is pending. Reviewers and checkpoint executors — including a `bronze-task` executor — never receive this offer.
- The matching progress reply carries all of those IDs and these fields: `stage`, `completed_since_last_report`, `new_evidence`, `current_blocker`, `attempts`, `results`, `next_action`, and `help_needed`. A worker additionally returns `advisor_needed: false|true` and may include one complete `advisor_request` payload when qualified; `false` is a cheap decline and triggers no follow-up, while `true` without the complete request is pending interest, not a consultation. A `true` reply or offer alone never launches an advisor. Reviewers and checkpoint executors do not consume implementation-advisor consultations. Main compares reported deltas and evidence; elapsed time alone is not difficulty or a stall. A timer event or progress reply never substitutes for completion or review.
- After a matching reply, if the same attempt remains active and no request is outstanding, Main starts the next one-shot timer generation at an adaptive 10–30-minute interval. Do not keep restarting the timer while a reply is pending. Workers continue to send the required >5-minute proactive notice independently of this timer.
### Continuation, replacement & advisor triggers

- Main supervises attempts through completion/message events and the one-shot timer; no fixed prompt request/token cutoff.
- Continue an active attempt while it adds discriminating evidence. After ~4–5 matched progress exchanges, explicitly reassess progress, blocker, and next safe action.
- A paused attempt resumes on the same attempt ID when authorized.
- After two Silver implementation/correction attempts leave criteria unmet, Main may propose Gold for unresolved reasoning/design/integration within user authority.
- **Worker replacement or pause handoff:** Before stopping, pausing, or replacing an agent ➔ Apply `references/replacement-and-handoff.md`. Successor must read prior handoff and relevant histories.
- **Diagnostic advisor consultation:** If an implementation worker requests diagnostic help ➔ Apply `references/task-advisor.md`.

## Workflow

### 1. Resolve scope and route

Read `skill://manage-plans` for work needing durable planning. Main creates or updates ordered sprint tasks for large work; a bounded small fix needs no new sprint. Resolve acceptance criteria, the authorized repository/worktree and artifact root, then choose light or full with exact required gates. A sprint label alone never selects full.

### 2. Select and launch a worker

1. Apply the routing ask and scoped-authority rules above. Resolve current definitions and overrides; user-reported quota is ground truth, not something to re-measure to contradict the user. Bronze, Silver and Gold are selectable according to fit; uncertain Silver/Gold fit is a user tradeoff, not an implicit Gold promotion.
2. Brief one fresh async implementation worker with task/attempt IDs, criteria, authorized scope, route, required gates, selected role and selection basis, relevant history refs, quota observation or `unknown`, and the >5-minute notice rule. Omit model/provider names, selectors and effort values. Include explicit repository/git-dir, worktree, `-C` root and target ref for project work, or an explicit non-project designation and output root.
3. State commit permission or its absence. A light worker may commit only its own verified scope when explicitly authorized with staging ownership; push needs separate authorization. If review is assigned before commit, obtain its matching PASS first. Mixed ownership or unrelated staged changes must not enter the commit: use only safely isolated, wholly owned content with scoped standard porcelain; otherwise report `commit_pending` without altering user state. Never blanket-stage, bypass hooks/signing, amend or rewrite history.
4. Require a worker summary only when an assigned gate or meaningful evidence preservation needs one. Give its exact repository-local artifact path then; ordinary light work may return a compact verified result without a template or manifest. Keep an existing plan task [~] until its assigned criteria and gates are satisfied.
5. For continuation/replacement, enforce the saved-handoff acknowledgment, old-job termination, all relevant related-attempt/history references and explicit required history reads above. Track completion/message events, not polling. Reclassify each new task independently; findings require correction, not automatic escalation.

### 3. Apply assigned evidence gates

Full-route tasks require independent evidence review; light-route tasks require it only when explicitly assigned. With no review assigned, Main checks the matching completed worker's result against acceptance and its specific verification evidence.

For an assigned review:

1. Check the effective `evidence-reviewer` role and async availability without reading its prompt body. Supply pointers only: task/attempt IDs, criteria, changed scope, worker artifact path, worker history URI (`history://<worker-agent-id>`), explicit repository/ref, any plan reference, and exact report path. The reviewer inspects worker artifact and history directly; subagents may communicate directly via `write agent://<id>`. A planned full-route checkpoint also requires the reviewer-owned frozen manifest described in `evidence-reviewer.md`.
2. Accept only the matching completed reviewer's verdict and actual report reference. A progress message, stale PASS, artifact alone or runtime completion is not a verdict. Add only concise current status/outcome references to a plan.
3. Actionable findings or material missing proof mean FAIL. Assign a fresh correction attempt with the findings and relevant prior handoff/history, then a fresh review at the same level. Once assigned, an optional light review is binding; neither smoke nor a worker commit bypasses FAIL.
4. PASS satisfies that review only. Light work may finish once its other assigned criteria, verification and any assigned commit succeed. Full project work remains in progress until the checkpoint succeeds at its pre-agreed task/batch boundary.
### 3a. Execute a required full-route checkpoint

Light-route tasks have no checkpoint. On the Full route, only at the pre-agreed task or atomic batch boundary after matching evidence PASS:

Main delegates the frozen reviewed snapshot to a fresh async non-blocking `bronze-task` checkpoint-only executor (never Silver, Gold, or Main). Follow the full Git isolation, porcelain, and verification rules in `references/checkpoint-git-safety.md`.

### 4. Run differential review only when assigned

After all assigned task reviews and required checkpoints pass, launch a fresh async `deep-reviewer` only when meaningful cross-task review is assigned. Give it criteria, verified light results, existing records, and history access. It hunts differential risk without rerunning passed checks.

Accept only its matching completed verdict. Actionable findings reopen the affected task; fresh corrections satisfy that task's assigned requirements before another required deep review. Assigned deep-review FAIL blocks completion; absence of an assigned deep review does not.

### 5. Complete and retire

Main marks [x] only after acceptance and material verification are supported, every assigned review has passed, any assigned commit has succeeded, every required full-route checkpoint has succeeded, and any assigned deep review has no actionable findings. Verified light work may finish uncommitted when no commit was assigned; failed or unavailable assigned commits remain `commit_pending`.

Keep required records readable and concise outcome links in any existing plan. No superseded attempt may advance a gate. End or explicitly cancel jobs that must not continue; Main interruption is not job cancellation. No extra review, checkpoint, deep review or artifact is created just to retire a light task.

## Scheduling rules

1. **Planning:** Main resolves scope, route, acceptance and any needed plan.
2. **Implementation:** one active implementation worker; an optional qualified advisor must fit the two-active limit.
3. **Assigned evidence review:** worker complete; one matching reviewer, only when required.
4. **Correction:** fresh worker attempt; fresh assigned review follows when applicable.
5. **Full-route checkpoint:** matching PASS and frozen snapshot; one fresh Bronze executor, no next independent task beyond the agreed boundary.
6. **Commit pending:** an assigned worker commit or required checkpoint failed/unavailable; no completion, and no crossing an unmet full-route boundary.
7. **Assigned deep review:** all prerequisite assigned gates passed; one differential reviewer.
8. **Complete:** criteria, verification and only the assigned gates satisfied; required jobs completed or explicitly cancelled.

Never exceed two active subagents total. Use completion/message events and `functions.wait` only when otherwise blocked; no polling or worker eval wait/barriers. An observation timer is a separate finite shell job, never a worker deadline. Keep pending gates in progress.

Routine role/dispatch, timer, progress and retry metadata stays in chat/trace, not sprint plans; never include model metadata in assistant-authored records. Save genuinely needed handoff or temporary supervision state separately under the assigned repository's `artifacts/`. Plans retain scope, acceptance, current status, milestones, durable decisions/blockers and concise verified outcome references only.

## Orchestrator output

Report the current task/attempt, selected route and subagent role, quota observation or `unknown`, meaningful outcome/blocker, matching assigned gate results and actual record refs, and completion status. Do not report model/provider names, selectors or effort values, or fabricate successful application of an override. Keep detailed implementation/review/Git evidence in its owner's record; never copy full transcripts or model metadata into new output or plans.

## Change history

Detailed version history is maintained in `references/change-history.md` and project `CHANGELOG.md`.
