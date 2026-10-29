# Subagent Routing and Records

## Report the role, not the model

- For every subagent, including `gold-task`, report only its agent type/role. Do not include provider/model names, model IDs/selectors or effort values in assistant-authored chat, routing asks, briefs, logs, plans, artifacts, handoffs or reports.
- Keep required task/attempt/runtime-agent IDs, actual history references, scope, verification and gate results. These identify the work, not its model. Do not copy model metadata from earlier records into new output.
- Trust the harness to resolve named roles and configured overrides; do not read agent definitions or configuration files as routine dispatch preflight. Never fabricate successful application of an override. For separately required consent, use available runtime metadata; if it is insufficient, request consultation-scoped approval rather than broadening preflight reads.
- Model values needed by agent definitions, user configuration or an actual dispatch API are execution data, not reporting fields. Do not remove or rewrite them to satisfy this output rule. Historical records and runtime-generated traces are not retroactively rewritten.

## Honor user overrides

- Honor explicit user-selected per-call overrides when supported; otherwise use the named role's effective configuration. Applicable user/project routing overrides take priority over the agent definition's default.
- Dispatch by named role and let the harness apply applicable overrides. Do not mask a configured override with a cached selector, copied skill value or an unnecessary per-call model argument.
- Applying an already authorized/configured override needs no new permission merely because it differs from the definition. Scoped auto-routing does not authorize inventing a new model override or changing persistent settings.
- Use only supported dispatch fields; do not invent overrides or temporarily rewrite shared/session configuration as a workaround. Preserve separately required consultation approval and other permissions; request consent by role and task/consultation scope without logging model metadata.

## Ask separately for each task in a batch

- Unless the user already selected roles or granted auto-routing for the covered work, use one `ask` call with one distinct question per task. A request for T3–T5 needs at least three task questions, not one shared "which agent for this batch?" question.
- Each question identifies its task ID and concrete work/outcome, then presents the applicable subagent roles, recommendation/reason, light/full gates and commit permission. Batch the questions, not the task descriptions into a single generic question. Omit model metadata.
- Bind each answer to its own task. A role selected for T3 does not select that role for T4/T5. A per-task explicit selection takes precedence over a broader auto-routing grant; any offered batch-auto option must name its exact scope and cannot hide other task questions when no prior grant exists.

## Child delegation and optional specialists

- Main retains orchestration dispatch authority. Among subagents, only `researcher` may spawn children, and only `bronze-task` or `researcher`. Researcher may choose these roles freely within its assigned research scope without another routing ask; child researchers inherit the same permission, while Bronze children cannot spawn. All other subagents must not spawn children.
- This permission does not expand scope, commit/push authority, or applicable concurrency limits. In an active flow, count descendants toward the two-active-subagent total.
- `designer` is optional and outside the sprint flow. Invoke it only on the user's explicit request; do not insert it as an automatic worker, advisor, or gate.

## Main session minimal context & pointer delegation

- **Minimal orchestration context:** Main normally reads only the immediate prompt, active sprint plan, compact results, gate verdicts, and handoff references. Read workflow references only when the current step needs them, not as an exhaustive preflight.
- Do not read agent prompt bodies, the worker's `implement-atomic-task` skill, source/API/architecture files, completed plans, or full histories merely to prepare a dispatch. Trust the harness to load role definitions and apply overrides.
- These limits prevent unnecessary context loading during orchestration; they do not prohibit targeted reads when the user explicitly asks Main to inspect or edit those files. Keep such reads limited to the requested work.
- **Pointer delegation to workers:** Main provides file pointers and acceptance criteria (`read path/to/spec.md:lines`), never pre-reading and summarizing codebase context into the worker prompt. The worker reads on demand in its own ephemeral session.
- **Lightweight handoff between subagents:** Main transfers criterion, artifact/history, repository/ref pointers and paired IDs with review cycle/round. Worker and evidence reviewer communicate directly for clarification and authorized corrections; Main gets compact transitions/outcomes. Follow the shared flow review policy: two rounds by default, a third only on Main's evidence-based authorization, then owner decision if still not PASS. Replacement never resets counts; quantitative-gate concerns may require earlier owner input.
