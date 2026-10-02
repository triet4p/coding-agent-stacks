---
name: remote-server-execution
description: Connect from Windows PowerShell to an authenticated remote server over OpenSSH and execute work there through a Git-synchronized loop. Use whenever a task requires running commands, jobs, or runtimes on a remote host instead of locally.
---

# Remote Server Execution

Execute work on a remote server from a Windows workstation via PowerShell OpenSSH,
keeping local and remote checkouts synchronized through Git. This skill covers
connection and execution mechanics only — what to run is the caller's job.

## 1. Connect

- Use Windows PowerShell OpenSSH (`powershell.exe` → `ssh`, `scp`).
- Prefer existing key/session authentication; pass `-o BatchMode=yes` for
  non-interactive commands so a missing key fails fast instead of hanging on a
  password prompt.
- If key auth genuinely blocks, stop and report — do not work around it.
- NEVER embed, persist, or log passwords, keys, or tokens: not in commands,
  files, shell history, Git config/history, logs, or evidence artifacts.

## 2. Inspect before mutating (read-only first)

- Locate the existing project checkout with bounded inspection (known home
  directory paths first, never destructive filesystem-wide search).
- Record: remote user/home, repo path, current commit (`git rev-parse HEAD`),
  `git status --porcelain`, runtime versions, available devices (CPU/GPU).
- Treat remote uncommitted changes and untracked files as someone else's work.
- NEVER `reset`, `clean`, force-push, or overwrite remote state.

## 3. Synchronize via Git (commit → push → pull)

- Commit locally on the current branch with an accurate message; push without
  force; record the exact commit hash.
- On the server, update with fast-forward only (`git pull --ff-only`) and
  verify with `git rev-parse HEAD`.
- If untracked workdir copies block fast-forward (untracked-overwrite guard),
  move them aside to `/tmp/<run>-keep`, pull, `diff -r` the committed files
  for byte-parity, copy back only what belongs, remove the aside. No reset.
- If the checkout is dirty or diverged, use a safe separate checkout/worktree
  for the exact pushed commit instead of touching the existing one.
- All remote compute must run at one verified commit; cite that hash with
  every result.

## 4. Execute

- Prefer the repo's own environment convention (`uv run --no-sync`,
  `.venv/bin/python`, etc.); verify the interpreter and key packages first.
- Set explicit paths (source dir, data, checkpoints, outputs) — never scan
  mounts or guess among candidates. Fail fast with errors naming the variable.
- Short jobs run in the foreground; capture exit code, stdout/stderr, wall
  time, and device info.
- Long jobs run detached (`nohup … &` with a master log); poll the log on a
  long cadence (5–10 minutes), never spin.
- On failure: diagnose root cause locally, fix, run focused checks, commit,
  push, pull the new exact commit, rebuild run copies, and rerun. Do not hide
  failures or stop at the first actionable error.

## 5. Bring results back (bounded)

- Copy back only review-sized artifacts: executed records, logs, manifests,
  metrics, summaries, representative figures. Verify integrity (sizes,
  checksums, or byte-compare) after transfer.
- Keep large raw outputs (datasets, embeddings, archives, checkpoints, bulk
  logs) server-side and uncommitted; record their exact remote paths.
- Never commit checkpoint binaries, datasets, credentials, or bulk data.
- Set `PYTHONDONTWRITEBYTECODE=1` and never import from copied trees when
  verifying, so review tooling does not pollute the deliverables.

## 6. Report

- Final commit hash (local == remote), remote path, environment/device,
  commands with exit codes and timings, output paths and sizes, key results
  with artifact references, and explicit limitations (sample, seed, device,
  single-run status).
- Distinguish operational success (exit 0, valid outputs) from scientific
  conclusions; state what the run does and does not establish.
