# Full-Route Exact-Snapshot Checkpoint & Git Safety Protocol

This protocol applies only when executing a required checkpoint on the **Full route** (or an explicitly declared shared atomic batch boundary). It is executed solely by a fresh, non-blocking explicit `bronze-task` subagent after matching evidence PASS.

---

## 1. Checkpoint Delegation Criteria

1. Main accepts only matching reviewer `PASS` references tied to the exact base, approved tree/diff snapshot, scope, and explicitly assigned repository/ref. A missing, stale, mismatched, or uncertain reference is not authorization. Resolve ownership or obtain fresh review; do not broaden scope. Main does not run Git, change refs, or write checkpoint records.
2. Assign a fresh async, non-blocking explicit `bronze-task` a checkpoint-only task; only `bronze-task` may execute checkpoints — never `silver-task` or `gold-task`. Give it:
   - Reviewer PASS reference and reviewer-owned manifest with `snapshot_sha256`.
   - Exact repository/git-dir, worktree, `-C` root, target branch/ref, and expected base SHA.
   - Approved scope and exact checkpoint-record path under the assigned repository's `artifacts/`: `artifacts/sprint-<N>/checkpoints/` for sprint work or `artifacts/<task-id>/checkpoints/` for standalone work.
   - The executor changes no source, approves no review, and never pushes.

---

## 2. Pre-Commit Isolation & Ownership Checks

3. The executor verifies the explicit repository and target ref/base, real index, worktree, and ownership before committing:
   - Freeze/check additions, deletions, mode changes, and exact approved content against the review reference.
   - A path is eligible only if wholly task-owned, current worktree content exactly matches reviewed content, and neither index nor worktree contains unrelated user hunks. A path list is not ownership proof.
   - If mixed ownership, base/content drift, or an uncertain snapshot cannot be safely separated, stop with `commit_pending`; request ownership resolution or fresh evidence review. Never infer a repository from cwd or use an ancestor/home repository.

---

## 3. Standard Porcelain & Safe Commit Execution

4. Use standard Git porcelain from the explicitly assigned repository, honoring configured identity, signing, and hooks:
   - If the real index has no unrelated changes and its staged tree exactly equals the approved snapshot, ordinary `git commit` is appropriate.
   - If unrelated paths are staged, commit only fully task-owned paths whose worktree exactly matches reviewed content with ordinary scoped porcelain such as `git commit --only -- <owned_paths>`; explicitly stage genuinely new owned paths only with `git add -- <owned_new_paths>` when needed.
   - If these conditions do not hold, do not guess, craft a synthetic index, blanket-stage (`git add .` / `git add -A`), force-add ignored artifacts, automatically stash/reset/checkout user state, bypass hooks/signing, amend/rewrite history, or push.

---

## 4. Post-Commit Verification

5. Immediately verify:
   - Target ref and expected parent/base commit SHA.
   - Committed paths and content against the approved snapshot.
   - Post-commit `git diff --cached` and `git status`. Remaining staged changes must contain only the user's intended staged changes and no reversion of committed task paths.
   - The executor writes these observations and the PASS reference in its own checkpoint record; a byte-for-byte index comparison does not replace semantic staging checks.
6. A hook/signing/identity rejection, failed commit, changed base/ref, mismatch with the reviewed snapshot, unexpected staged diff, or uncertain result leaves the task `commit_pending`. Do not bypass the failure or discard user state. Resolve ownership/cause and retry only while the same approved snapshot and expected base/ref remain valid; changed content requires fresh evidence PASS.
7. Main decides success only after matching that report to its authorization and records a concise status/reference in the plan; Main never writes the checkpoint record.

---

## 5. Batch & Project Boundaries

- **Atomic batch exception:** A shared atomic batch must be declared and approved as one checkpoint boundary before implementation. Every included task still gets a separate PASS; after the batch's last PASS, one frozen snapshot containing only the batch's approved changes is checkpointed before any task outside it. Never combine unreviewed work or delay independent tasks for convenience.
- **Missing repository authorization:** An actual project task without an explicitly assigned/authorized repository remains `commit_pending`; do not create/init a repository or commit a home/ancestor repository. Only work explicitly classified as non-project in its plan/assignment avoids a project checkpoint; it uses its assigned output root.
- **Corrections after checkpoint:** Reopen without resetting review counts. Reuse a live worker or replace an ended one with handoff/history; apply `evidence-review-cycle.md` for remaining rounds, Main's conditional third-round authority or owner escalation. Obtain current evidence PASS and create a separate checkpoint on top of the earlier commit through a fresh explicit `bronze-task` executor. Never amend/rewrite an earlier checkpoint.
