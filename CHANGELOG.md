# Changelog

## [Unreleased]

### Added

- Added `install.ps1` to copy repository rules, skills, and subagent definitions into `~/.agents` and `~/.omp`, with preview mode, identical-file skipping, conflict detection, and backups before forced replacement.
- Added `.omp/agent/config.example.yml` as an optional, shareable OMP agent config preset.

### Changed

- The installer now copies the preset to `~/.omp/agent/config.yml` by default, replacing the full file with the existing conflict, backup, and preview protections; `-UsePresetConfig:$false` opts out.
