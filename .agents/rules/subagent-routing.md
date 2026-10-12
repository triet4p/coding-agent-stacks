# Subagent Routing and Records

## Report the role, not the model

- For every subagent, including `gold-task`, report only its agent type/role. Do not include provider/model names, model IDs/selectors or effort values in assistant-authored chat, routing asks, briefs, logs, plans, artifacts, handoffs or reports.
- Keep required task/attempt/runtime-agent IDs, actual history references, scope, verification and gate results. These identify the work, not its model. Do not copy model metadata from earlier records into new output.
- Inspect effective routing privately when needed for dispatch or consent checks. Never fabricate successful application of an override.
- Model values needed by agent definitions, user configuration or an actual dispatch API are execution data, not reporting fields. Do not remove or rewrite them to satisfy this output rule. Historical records and runtime-generated traces are not retroactively rewritten.

## Honor user overrides

- Honor explicit user-selected per-call overrides when supported; otherwise use the named role's effective configuration. Applicable user/project routing overrides take priority over the agent definition's default.
- Inspect applicable overrides before dispatch. Do not mask a configured override with a cached selector, copied skill value or an unnecessary per-call model argument. Normal named-agent dispatch should let the runtime apply the user's effective routing.
- Applying an already authorized/configured override needs no new permission merely because it differs from the definition. Scoped auto-routing does not authorize inventing a new model override or changing persistent settings.
- Use only supported dispatch fields; do not invent overrides or temporarily rewrite shared/session configuration as a workaround. Preserve separately required consultation approval and other permissions; request consent by role and task/consultation scope without logging model metadata.

## Ask separately for each task in a batch

- Unless the user already selected roles or granted auto-routing for the covered work, use one `ask` call with one distinct question per task. A request for T3–T5 needs at least three task questions, not one shared "which agent for this batch?" question.
- Each question identifies its task ID and concrete work/outcome, then presents the applicable subagent roles, recommendation/reason, light/full gates and commit permission. Batch the questions, not the task descriptions into a single generic question. Omit model metadata.
- Bind each answer to its own task. A role selected for T3 does not select that role for T4/T5. A per-task explicit selection takes precedence over a broader auto-routing grant; any offered batch-auto option must name its exact scope and cannot hide other task questions when no prior grant exists.

## Main session minimal context & pointer delegation

- **Strict context whitelist:** To eliminate token bloat (reading 50–60K tokens before doing any work), Main reads ONLY:
  1. The active sprint plan (`docs/sprint-plans/sprint-N.md`) or the user's immediate prompt.
  2. Delivered compact worker results, reviewer gate reports, and handoff references.
- **Forbidden reads for Main:**
  - Never read subagent prompt bodies (`.omp/agent/agents/*.md`). The OMP harness automatically loads agent definitions upon `functions.task(agent=...)`.
  - Never read `skill://implement-atomic-task` (the worker reads its own execution skill in its isolated session).
  - Never read codebase source files, API implementations, or extensive technical documentation to "prepare context" for workers.
  - Never read completed/past sprint plans in `docs/sprint-plans/` or full history transcripts (`history://...`).
- **Pointer delegation to workers:** Main provides file pointers and acceptance criteria (`read path/to/spec.md:lines`), never pre-reading and summarizing codebase context into the worker prompt. The worker reads on demand in its own ephemeral session.
- **Lightweight handoff between subagents:** When transitioning from worker to reviewer or executor, Main transfers pointers only: `task_id`, `attempt_id`, `worker_artifact_path`, `worker_history_uri` (`history://<runtime-agent-id>`), and commit/base refs. The reviewer reads the worker artifact and history directly. Subagents may communicate directly via `write agent://<id>` for clarifications; Main does not act as a transcript relay.
