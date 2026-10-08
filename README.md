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
