---
name: omp-subagent-flows
description: Orchestrate planned feature delivery in Oh My Pi with asynchronous workers on light or full routes: explicitly required review gates, Bronze-only exact-snapshot checkpoints, and conditional end-of-sprint deep review.
---

# OMP Subagent Flows

## Scope

Use this skill only inside **Oh My Pi (OMP)** when a user requests feature implementation that belongs in a plan or sprint.

Never use this workflow in Codex CLI, Claude Code, or any other coding-agent CLI. Never translate its OMP agent names, tools, lifecycle operations, or artifact URLs to another runtime.

During sprint execution, Main is the orchestrator and plan manager. Keep context minimal: inspect compact results and verification evidence, not implementation context as dispatch preflight. Main does not write worker, evidence, review, or checkpoint records. Its durable flow edits are plans and its own separate supervision files under the assigned repository's `artifacts/` directory (or explicit output root). Never copy artifact details into a plan. Explicit user requests to inspect or edit workflow files are separate from sprint orchestration.

## Minimal context & pointer-only orchestration

Keep orchestration context small; do not preload surrounding files just to prepare a dispatch.

- Main normally reads the immediate prompt, active sprint plan, compact results, gate verdicts, and handoff references. Read a workflow reference only when the current step needs it.
- Do not pre-read subagent prompt bodies, `skill://implement-atomic-task`, source/API/architecture files, completed plans, or full histories for worker preparation. Trust the harness to load named roles and apply overrides.
- When the user explicitly asks Main to inspect or edit such files, targeted reads for that request are allowed; this is not permission for broad preflight exploration.
- **Pointer delegation to workers:** Main never reads and summarizes technical docs into worker prompts. Main supplies pointers only: task ID, acceptance criteria, constraints, and target file paths/ranges (`read path/to/doc.md:40-80`). The worker reads them on demand in its own ephemeral session.
- **Lightweight handoff to reviewers:** Main supplies criterion, worker artifact/history and repository/ref pointers, plus the paired runtime IDs and current review cycle/round. Worker and reviewer communicate directly via `write agent://<id>` for clarification and authorized corrections; Main receives compact transitions and final outcomes, not relayed implementation transcripts.

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
- Auto-routing is not extra commit/push, destructive-action, model-override or advisor-consent permission, and does not waive verification, assigned gates, handoff/history, async safety, or review continuation limits. Existing explicit permissions remain in force only within their own scope.
- If an action genuinely needs authority outside the grant or an unreachable prerequisite, do not invent consent or treat user silence as approval. Leave the affected task blocked with the concrete reason and continue only other safe, authorized work that is independent of it and does not cross a required boundary. Ask only for the genuinely missing decision; never block the authorized sequence on a redundant routing question.

## Invariants

1. Keep at most **two active subagents total**, including implementation workers, reviewers, advisors, and checkpoint executors.
2. Planning remains in the current main session and uses the **exact current model**. Never delegate plan creation or switch models for it.
3. Start each task with a fresh worker; keep that worker available for direct reviewer feedback and corrections. Replace only an ended/unavailable worker or for a concrete reason, preserving handoff/history and review counts. Main owns routing and continuation within user authority; no role is a default and no request/token count ends an attempt.
4. Run one sprint implementation task at a time. An `evidence-reviewer` runs only when its gate is assigned: always on the full route, and on the light route only when Main assigns one. Never batch task-level evidence reviews. A full-route project task also requires a separate Bronze-only exact-snapshot checkpoint at the pre-agreed task or batch boundary before the next independent project task; only a predeclared shared atomic batch, declared and approved as one checkpoint boundary before implementation, may continue through its included tasks before that single checkpoint.
5. Run a `deep-reviewer` only when Main assigns it for meaningful cross-task risk review, and only after every assigned per-task evidence gate and required full-route checkpoint has passed. A correction may require another assigned differential review.
6. One review round is one submitted candidate plus its consolidated assessment, not a message or reviewer check. Two rounds are authorized by default. Main may grant one third round only for evidenced progress, a bounded remaining fix and a concrete check within unchanged scope/criteria. Otherwise ask the owner after round 2; after round 3 without PASS, always stop for the owner. Agent replacement or reopening never resets counts. Never PASS actionable findings.
7. The installed flow definitions for `bronze-task`, `silver-task`, `gold-task`, `evidence-reviewer`, `deep-reviewer`, and checkpoint-executor `bronze-task` assignments are preconfigured `blocking: false`. Main trusts the runtime harness and dispatches directly by role name without pre-reading agent definition bodies. If the runtime reports synchronous execution or no async job manager, report the condition and wait for authorized resolution.
8. Use completion events, meaningful blocker messages, and the adaptive progress timer for supervision; no separate duration-based proactive notice is required.
9. Every subagent enumerates and reads all regular files under `~/.agents/rules/*` before substantive work, including corrections and replacements. Apply relevant rules at their proper precedence; report conflicts or inaccessible files instead of silently ignoring them.
10. Main retains orchestration dispatch authority. Among subagents, only `researcher` may spawn children, freely choosing only `bronze-task` or `researcher` within its assigned research scope without another role-selection ask. Child researchers inherit this permission; all other subagents cannot spawn. Descendants count toward the two-active-subagent limit. This grants no additional scope or commit/push authority.
11. `designer` is optional, outside this flow, and invoked only when the user explicitly requests it; never add it as an automatic worker or gate.
12. Propose quantitative gate reconsideration as soon as credible evidence questions its assumptions, feasibility or tradeoffs; do not wait for the round limit or proof of impossibility. Pause gate-specific optimization, not independent safe work. Only the owner can revise acceptance criteria.

## Roles

- **Main session:** plan management and summary-only orchestration. Main trusts effective definitions at launch without pre-reading prompt bodies, never reads full worker histories, and never writes evidence, review, worker, or checkpoint records; on the light route it inspects enough of the worker's completed result and assigned verification evidence to decide acceptance itself. The bundled OMP generic `task` tool/agent exists outside this flow and must never be selected implicitly as a flow worker, reviewer, advisor, or executor; only the explicit `bronze-task`, `silver-task`, and `gold-task` implementation roles below are flow routes.
- **Worker:** a Main-selected explicit `bronze-task`, `silver-task`, or `gold-task` subagent for one task and its permitted corrections. Start fresh for a new task, but retain a live worker during review. Workers own implementation and their artifacts, may communicate directly with the assigned reviewer, and never change criteria or route themselves. Light workers MAY commit only verified own scope when explicitly authorized with exact repository, Git directory, worktree, target ref and staging ownership; no foreign staged changes, history rewrite or hook/signing bypass. Push needs separate authorization. Full workers do not commit; Silver and Gold never execute checkpoint-only assignments.
- **Evidence reviewer:** independent and read-only on source, worker artifact and plan. Runs only for an assigned gate, may stay active across authorized rounds, and communicates directly with the worker. Owns its report and any required frozen manifest; Main receives compact round outcomes and the final verdict. Never edits worker records, relaxes criteria or executes checkpoints.
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
- Accept a final worker, reviewer, or checkpoint-executor result only when it matches the current task ID, attempt ID, and agent ID, and that agent has completed. For evidence review, also match the authorized cycle/round and criterion reference. A delivery receipt, progress reply, partial handoff, or timer event is not task completion or a gate verdict.
- A matching `ready_for_review` message is an explicit lifecycle signal, not worker completion or acceptance: Main may launch the reviewer while the worker remains active. A matching `changes_requested` outcome consumes that assessment round with `advance: false`, but is not a passing gate. Track each cycle/round outcome once; duplicate or stale messages never increment/reset counts or authorize extra work. Only a completed reviewer result establishes final PASS/FAIL; task acceptance still requires worker final completion.
- If an attempt is cancelled or replaced, invalidate it before continuing. Ignore any later result, message, or timer from that stale attempt for gate decisions; it must never advance the task or sprint.
- Trust the harness to launch the named role asynchronously and apply its effective configuration; do not inspect definition/configuration files before launch. If the runtime reports inline/synchronous execution or no async job manager, stop and surface that condition. Do not silently switch to blocking operation or edit runtime configuration.

### Main's event handling

- Main reacts to delivered job-completion and agent-message events. Do not repeatedly poll status. Use `functions.wait` only when Main is otherwise blocked with no useful work, and only to wait for an event; do not invent a timeout argument or use it as a timer.
- Never supervise workers with eval `handle.wait` or an eval barrier: aborting those waits can cancel the jobs being waited on. Do not attach worker lifetime to a Main-turn wait.
- A Main/user interrupt (including Escape where applicable) interrupts Main's current turn; it is not an explicit cancellation of a detached worker. To stop a specific worker, use the explicit cancellation control for that worker's async job (for an exposed process job, `proc://<job-id>/kill`). Do not confuse cancelling a job with interrupting Main.
- Do not promise detached-job durability across process exit or automatic Main resumption after a user interrupt. A subsequent user prompt may be needed for Main to process queued results.
- A send receipt confirms delivery only; it does not establish that the recipient read, applied, or acknowledged the message. A late reply or tool execution is not by itself evidence that the worker is stalled.

### One-shot timer supervision

- Keep one finite adaptive **10–45-minute** observation timer per active attempt. No duration-based notice or worker deadline. Completion takes precedence; cancel stale timers and never poll.
- Main reads [progress supervision](references/progress-supervision.md) when launching the first active attempt for timer lifecycle, message fields and advisor-offer conditions. Do not preload it for planning or document-only work.
### Continuation, replacement & advisor triggers

- Main supervises attempts through completion/message events and the one-shot timer; no fixed prompt request/token cutoff.
- Continue while evidence improves and the review allowance permits it. After roughly 4–5 matched progress exchanges, reassess; progress messages never bypass an owner-decision boundary.
- A paused attempt resumes on the same attempt ID when authorized.
- For review continuation or evidence-backed doubts about a quantitative gate, use [evidence review cycles](references/evidence-review-cycle.md). Main alone may authorize the conditional third round; further work needs the owner.
- **Worker replacement or pause handoff:** Before stopping, pausing, or replacing an agent ➔ Apply `references/replacement-and-handoff.md`. Successor must read prior handoff and relevant histories.
- **Diagnostic advisor consultation:** If an implementation worker requests diagnostic help ➔ Apply `references/task-advisor.md`.

## Workflow

### 1. Resolve scope and route

Read `skill://manage-plans` for work needing durable planning. Main creates or updates ordered sprint tasks for large work; a bounded small fix needs no new sprint. Resolve acceptance criteria, the authorized repository/worktree and artifact root, then choose light or full with exact required gates. A sprint label alone never selects full.

### 2. Select and launch a worker

1. Apply the routing ask and scoped-authority rules above. Trust the harness to resolve definitions and overrides without preflight file reads; user-reported quota is ground truth. Bronze, Silver and Gold are selectable according to fit; uncertain Silver/Gold fit is a user tradeoff, not an implicit Gold promotion.
2. Brief one fresh async worker with task/attempt IDs, criteria, scope, route/gates, selected role/basis, relevant history refs and quota observation or `unknown`. For assigned review, include cycle/round and [evidence review cycles](references/evidence-review-cycle.md); keep the worker alive at `ready_for_review`. Include explicit repository/git-dir, worktree, `-C` root and ref, or non-project designation and output root.
3. State commit permission or its absence. A light worker may commit only its own verified scope when explicitly authorized with staging ownership; push needs separate authorization. If review is assigned before commit, obtain its matching PASS first. Mixed ownership or unrelated staged changes must not enter the commit: use only safely isolated, wholly owned content with scoped standard porcelain; otherwise report `commit_pending` without altering user state. Never blanket-stage, bypass hooks/signing, amend or rewrite history.
4. Require a worker summary only when an assigned gate or meaningful evidence preservation needs one. Give its exact repository-local artifact path then; ordinary light work may return a compact verified result without a template or manifest. Keep an existing plan task [~] until its assigned criteria and gates are satisfied.
5. Keep the same active worker for review corrections. For a necessary replacement, enforce saved-handoff acknowledgment, old-job termination, relevant history reads, and unchanged review-cycle/count tracking. Reclassify only within routing authority; neither a finding nor a metadata omission automatically requires a new worker or higher role.

### 3. Apply assigned evidence gates

Full-route tasks require independent evidence review; light-route tasks require it only when explicitly assigned. With no review assigned, Main checks the matching completed worker's result against acceptance and its specific verification evidence.

Main, the worker and the reviewer read [evidence review cycles](references/evidence-review-cycle.md) only when a review is assigned, or when evidence calls for early quantitative-gate reconsideration. It defines candidate counting, direct messages, snapshot freezes, conditional round-3 authorization and owner handoff. Keep this protocol in that reference, not duplicated in role briefs.

- Reuse the live pair; `ready_for_review` permits review while the worker stays active. Reviewer remains independent; only matching completed results establish final gates.
- Apply the default-two/conditional-third policy and early owner escalation from the invariants. Never turn optional artifacts or a future checkpoint into evidence prerequisites.
- Evidence PASS is not checkpoint success. Release the worker to finish, then perform any assigned checkpoint on the exact reviewed snapshot.

### 3a. Execute a required full-route checkpoint

Light-route tasks have no checkpoint. On the Full route, only at the pre-agreed task or atomic batch boundary after matching evidence PASS:

Main delegates the frozen reviewed snapshot to a fresh async non-blocking `bronze-task` checkpoint-only executor (never Silver, Gold, or Main). Follow the full Git isolation, porcelain, and verification rules in `references/checkpoint-git-safety.md`.

### 4. Run differential review only when assigned

After all assigned task reviews and required checkpoints pass, launch a fresh async `deep-reviewer` only when meaningful cross-task review is assigned. Give it criteria, verified light results, existing records, and history access. It hunts differential risk without rerunning passed checks.

Accept only its matching completed verdict. Actionable findings reopen tasks under their existing review counts and the shared review-cycle protocol, including conditional round 3 or owner escalation. Reuse a live worker or replace an ended one with handoff/history, then satisfy assigned evidence/checkpoint gates before another required deep review. Deep-review FAIL blocks completion.

### 5. Complete and retire

Main marks [x] only after acceptance and material verification are supported, every assigned review has passed, any assigned commit has succeeded, every required full-route checkpoint has succeeded, and any assigned deep review has no actionable findings. Verified light work may finish uncommitted when no commit was assigned; failed or unavailable assigned commits remain `commit_pending`.

Keep required records readable and concise outcome links in any existing plan. No superseded attempt may advance a gate. End or explicitly cancel jobs that must not continue; Main interruption is not job cancellation. No extra review, checkpoint, deep review or artifact is created just to retire a light task.

## Scheduling rules

1. **Planning:** Main resolves scope, route, acceptance and any needed plan.
2. **Implementation:** one active implementation worker; an optional qualified advisor must fit the two-active limit.
3. **Assigned evidence review:** worker ready and source frozen; one matching reviewer may collaborate directly with the still-active worker.
4. **Correction:** reuse the live pair within authorized rounds; Main may grant the conditional third round, otherwise stop for the owner. Evidence-backed gate doubts may require an earlier owner decision.
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
