# Changelog

## [Unreleased]

### Added

- Added `install.ps1` to copy repository rules, skills, and subagent definitions into `~/.agents` and `~/.omp`, with preview mode, identical-file skipping, conflict detection, and backups before forced replacement.
- Added `.omp/agent/config.example.yml` as an optional, shareable OMP agent config preset.
- Added `designer` subagent definition (`google-antigravity/gemini-3.8-flash:high`) specialized for UI/UX construction, visual audit, image generation, diagrams, and vision inspection.
- Added `researcher` subagent definition (`google-antigravity/gemini-3.8-flash:high`) specialized for deep technical and web research, documentation verification, API updates, and paper discovery.

### Changed

- The installer now copies the preset to `~/.omp/agent/config.yml` by default, replacing the full file with the existing conflict, backup, and preview protections; `-UsePresetConfig:$false` opts out.
- Replaced automatic worker-tier selection with user-controlled `ask` routing and scoped delegation, presenting subagent role, task fit, quota observations, workflow and commit permission together.
- Added a lightweight default for bounded low-risk fixes, with independent evidence review only when assigned; retained required full-route evidence and Bronze exact-snapshot checkpoints at agreed boundaries, with conditional deep review.
- Allowed explicitly authorized light-route Bronze, Silver, and Gold workers to commit their own verified scope; push still requires separate authorization.
- Kept sprint/global plans limited to durable scope, current status, decisions, blockers, and outcome links; saved detailed handoffs and temporary state in separate files under the assigned repository's `artifacts/`.
- Retained Main-owned attempt lifetime and required replacement/history handoffs without automatic Gold promotion or request/token cutoffs.
- Clarified unattended auto-routing grants via user/steer messages or an "Auto cho dãy task này" ask choice with an explicit task range; Main handles in-scope selection/corrections/replacements without redundant asks, while respecting revocation, independent permission boundaries and genuine blockers.
- Added a shared role-only subagent reporting rule: omit model/provider names, selectors and effort values from new chat, routing asks, briefs, logs and durable records; prioritize applicable user routing overrides over agent defaults without masking them or silently falling back.
- Required one task-specific routing question per requested batch task in a single `ask`, with concrete work/outcome and task-bound answers; retained prior auto-routing authority.
- Enforced strict minimal context boundaries and pointer delegation for the Main session, eliminating preflight reads of subagent prompt bodies, worker execution skills, codebase files, and past sprint plans; handoffs between workers and reviewers transfer IDs, paths, and history URIs only.
