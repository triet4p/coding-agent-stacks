# coding-agent-stacks

Rules, skills, and subagent definitions for the coding-agent workflow.

## Install

Clone the repository, then run the installer from PowerShell:

```powershell
git clone https://github.com/triet4p/coding-agent-stacks.git
cd coding-agent-stacks
.\install.ps1
```

Requires Windows PowerShell 5.1 or PowerShell 7+. The installer uses its own location to find the payload, so it can also be invoked from another working directory. It does not require Git after cloning or extracting the repository.

If Windows blocks local scripts, invoke this downloaded script with a process-only execution policy override after reviewing it:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

This does not change the saved execution policy. On systems with PowerShell 7, use `pwsh -NoProfile -File ./install.ps1`.

### Installed paths

| Repository payload | Destination |
| --- | --- |
| `.agents/rules/` | `~/.agents/rules/` |
| `.agents/skills/` (including references, assets, and scripts) | `~/.agents/skills/` |
| `.omp/agent/agents/` | `~/.omp/agent/agents/` |
| `.omp/agent/config.example.yml` (enabled by default) | `~/.omp/agent/config.yml` |

The default destination is PowerShell's `$HOME`. To install into a different home directory:

```powershell
.\install.ps1 -HomePath 'D:\AgentHome'
```

By default, the installer copies `.omp/agent/config.example.yml` from the repository byte-for-byte to `$HomePath/.omp/agent/config.yml` (normally `~/.omp/agent/config.yml`), preserving the relative directory and changing only the filename. This is a complete config-file replacement, not a merge. Identical files are skipped; a differing destination config blocks all installation writes unless `-Force` is used. A forced replacement backs up the old file under `~/.omp/.install-backups/<run-id>/agent/config.yml`.

To disable the preset entirely, including any check or change to an existing config, invoke the script directly from PowerShell:

```powershell
.\install.ps1 -UsePresetConfig:$false
```

Windows PowerShell 5.1's `-File` mode has limitations passing `$false` to switch parameters; use the direct invocation above (or call the script from `-Command`) to reliably opt out.

The sample contains config settings, including model/provider selections, but excludes local setup/onboarding metadata (`setupVersion`), `dev.autoqaConsent` consent, auth tokens/credentials, and private user paths or state. These selections do not authenticate providers; configure provider accounts and access separately. The installer does not install the OMP application or copy other settings, credentials, sessions, databases, private memory, benchmarks, or repository artifacts. Restart OMP after installation to reload the definitions.

### Preview and update

Preview a fresh installation:

```powershell
.\install.ps1 -WhatIf
```

Identical files are skipped. If any destination file has different contents, the installer stops before copying any files and lists the conflicts. To preview or apply replacement:

```powershell
.\install.ps1 -Force -WhatIf
.\install.ps1 -Force
```

Each replaced file is backed up first under the corresponding `~/.agents/.install-backups/<run-id>/` or `~/.omp/.install-backups/<run-id>/`, preserving its path relative to that root. The installer prints each backup path. Restore a backup by copying it back to its original path.

Unrelated files are preserved; the installer does not remove old or custom definitions. Installation is a file copy, not a symlink. Repeat the installer after obtaining repository updates. Filesystem failures can leave a partially applied installation; resolve the error and rerun, using the printed backups if necessary.

### Sync back from home

If the installed payload under `$HOME` was edited directly, copy it back into this repository with:

```powershell
.\sync-from-home.ps1 -WhatIf
.\sync-from-home.ps1
```

The script reads the same three roots in the opposite direction (home to repository), copies new or changed files, and skips identical ones. The home directory is never written to. Repo-only files that no longer exist at home are reported and left alone unless `-Prune` is passed. The local config (`~/.omp/agent/config.yml`) is never synced back; update `.omp/agent/config.example.yml` by hand when the shareable preset itself changes. Review the result with `git status`/`git diff` before committing.

## OMP workflow

Worker routing is user-controlled. Before dispatch, Main uses `ask` unless you already selected a role or granted routing authority for a task, batch, session, or sprint. The proposal includes subagent role, task fit, quota observed or `unknown`, workflow and commit permission together. Gold remains eligible for medium tasks; neither Gold nor Silver is an automatic default. Chat, asks, briefs and saved records identify subagents by role/type and required work IDs only, never model/provider names, selectors or effort values.

For a batch such as **T3–T5**, Main presents **three separate task questions in one `ask`**, each explaining that task's work/outcome, role recommendation, workflow/gates and commit permission. Each answer applies to its own task; a batch-wide generic question is not a substitute. Existing explicit role selections or auto-routing authority still avoid redundant questions.

For unattended work, authorize auto-routing in a normal message or steer, for example: **"Main tự chọn agent cho task 3–8, không hỏi lại; không commit/push."** The routing ask also offers **"Auto cho dãy task này"**, describing the exact covered tasks and restrictions. Main acknowledges once and chooses workers, including in-scope corrections/replacements, without further routing asks—even with unknown quota or comparable Silver/Gold fit. Authority ends when those tasks finish or you revoke it; it grants no extra Git, destructive-action, model-override or advisor-consent permissions. A genuinely unauthorized/blocked action stays blocked; other independent authorized work may continue without crossing required gates. This is an instruction-level ask choice, not a new runtime setting or CLI flag.

Applicable configured routing overrides take priority over agent defaults. Main inspects them privately, lets normal named-agent dispatch honor them, and never masks them with cached values or unnecessary per-call arguments. Optional per-call overrides are used only when supported; otherwise dispatch uses the role's effective configuration, without changing shared/session settings as a workaround. This rule does not change model values in definitions/configuration or redact existing history/runtime-generated traces. See `.agents/rules/subagent-routing.md`.

- **Light:** default for bounded low-risk fixes. The worker implements and verifies the changed behavior. Independent evidence review is optional when needed; once assigned, its gate is binding. No automatic checkpoint or deep review.
- **Full:** for material risk, contract/interacting changes, or your explicit requirement. Required evidence gates and a separate Bronze-only exact-snapshot checkpoint use the agreed task/batch boundary. Deep review runs only when assigned for meaningful cross-task risk.
- **Commits:** a light-route Bronze, Silver, or Gold worker may commit only its own verified changes when explicitly authorized for the exact repository/worktree/ref. Unrelated staged changes, history rewrites, and hook/signing bypass are forbidden. Push requires separate authorization. Full-route workers do not commit; the separate checkpoint executor is Bronze.
- **Attempts:** Main manages continuation and replacement without prompt-level request/token cutoffs. Two incomplete Silver attempts trigger a route reassessment, not automatic promotion. Replacing an agent requires its detailed saved handoff and supplies all relevant attempt/history references to the successor.
- **Plans:** `docs/PLAN.md` and `sprint-<N>.md` contain scope, acceptance criteria, current status, durable decisions/blockers, and concise outcome links—not per-turn dispatch/progress/wait/retry logs.
- **Minimal context:** Main strictly limits its reads to the active sprint plan and compact returned summaries, eliminating 50–60K token preflight bloat. Main never reads subagent prompt bodies, worker skills, or codebase docs to "prepare context"; it passes pointers (file paths, criteria, history URIs) and lets workers/reviewers inspect on demand in their isolated sessions or communicate directly via peer messaging.
- **Saved state:** detailed handoffs and needed temporary supervision state are separate attempt-scoped files under that repository's `artifacts/`, never inside a sprint plan or another project's/global artifact root. Pauses require a handoff; resume requires authorization. Explicit non-project work uses its explicitly assigned output root.

These are instruction-level policies, not changes to OMP's runtime budget settings. Required verification remains mandatory on both routes; a job ending, yielding, or submitting is not proof that acceptance criteria passed.
