# Workspace Boundary

All file operations — read, write, create, edit, delete, move, and Git operations that touch files — stay inside the current workspace unless an explicit exception below applies.

## Boundary

- The boundary is the session's current working directory plus any explicitly assigned repository, worktree, or output root named in the active assignment or plan.
- Never infer an assignment root from cwd or an ancestor/home directory. If the assignment names no repository, there is no repository: do not substitute one.
- This rule binds Main and every subagent (`bronze-task`, `silver-task`, `gold-task`, `researcher`, `scout`, `task-advisor`, `evidence-reviewer`, `deep-reviewer`, checkpoint executors).

## Reads

- Default to reading only inside the boundary.
- Allowed outside the boundary without asking: the mandatory `~/.agents/rules/*` reads, skill content loaded via `skill://`, and agent definitions resolved by the harness at dispatch.
- Any other read outside the boundary requires user approval first. Ask with the exact path and the reason; do not read speculatively while waiting.

## Writes

- Writes outside the boundary are forbidden: no creating directories, files, or symlinks; no editing, deleting, or moving; no Git commits, checkouts, or resets affecting paths outside the boundary.
- The only exception is an explicit user authorization naming the exact outside path and operation. A read approval is not a write approval.
- Never use a temporary directory outside the workspace. When scratch space is needed, use `<workspace>/.tmp/` and ensure it is ignored (`.gitignore`) so it never enters a commit or review snapshot.

## Violation handling

- If a brief, assignment, or prior record points outside the boundary, stop that step and report the offending path to Main (workers) or the owner (Main) instead of following it.
- A pack, report, or handoff that required an out-of-boundary read must state the approval that covered it.
