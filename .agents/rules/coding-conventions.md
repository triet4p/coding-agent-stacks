# Coding Conventions

Applies to every implementation worker and reviewer, in every project. A project-level conventions file (`AGENTS.md` at the repo root, or the path named in the brief) takes precedence on style details; the budgets and bans below are floors no project convention may waive. If the project names none, this file is the default — never "no conventions".

## File budget

- Soft cap ~800 lines per source file; hard cap ~1500. New files must land under the soft cap.
- Files already over the cap are grandfathered: frozen, never refactored for size alone. Edits to them must not grow them — put new concerns in new files, shrink opportunistically while touching them for other reasons. Never append a new concern to a grandfathered file.
- Measure with `wc -l`. Generated files and fixture data are excluded but must be marked as generated or live under a fixtures path.

## Phase-agnostic code

Plan/sprint/task IDs (`P0x`, `PX`, `SX-TY`, `ASE-Sn-Tm`, `sprint-N`, …) live only in plans, artifacts, and commit messages. They are banned from durable code across four layers:

1. File and module names (`p4_verify.rs` → domain name, e.g. `verify.rs`).
2. Header and doc comments — headers describe the current domain only; history belongs in `CHANGELOG.md`, never in a `//!`/`/**` chronicle.
3. Identifiers and string literals, including user-facing usage text and version strings (`ase-p4-bundle-v1` → `ase-bundle-v1`).
4. Test/fixture references to contracts — point at the contract path, not the phase that produced it.

Exception: quoting a historical identifier verbatim for back-compat (migration shims, wire constants) — isolate it, name it legacy, and never propagate the pattern.

## Portability

- No absolute or machine-specific paths in code, tests, or checked-in config. Paths are relative to the repo root, passed as arguments, or read from environment/config.
- No scratch directories outside the workspace (see `workspace.md`); no hardcoded usernames, home directories, or system temp paths.

## Conventions file

- The worker brief always names the conventions path. The worker reads it before implementing; a missing file is a question to Main, not a license to improvise.
- Reviewers check this rule explicitly (see `evidence-review-cycle.md`): file budget, phase-agnostic naming, portability, no history in code headers. Violations are findings, not style notes.
