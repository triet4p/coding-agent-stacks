# Shell Command Execution Rules

## Environment

- Primary development environment is **Windows**.
- **PowerShell** is the canonical shell.
- Prefer native OMP file tools when they are available and appropriate.
- When shell-based filesystem discovery or inspection is needed, prefer PowerShell-native commands.

### PowerShell filesystem commands

Prefer:

- `Get-ChildItem` for listing files and directories.
- `Get-Content` for reading file contents.
- `Select-String` for text search.
- `Test-Path` for checking whether a path exists.
- `Resolve-Path` for resolving a path.
- `Get-Item` for file or directory metadata.

For explicit user-provided paths, prefer `-LiteralPath`.

Do not assume Unix utilities such as `ls`, `find`, `grep`, `sed`, `awk`, or `cat` are available unless the task is explicitly running inside a Unix-compatible shell.

If a native OMP filesystem/search tool is unavailable or returns `Tool not found`, fall back to PowerShell-native commands before concluding that the file or directory is inaccessible.

## Commands That Require the External Environment

Shell or PowerShell commands that use system tools or may require resources outside the sandbox **must be executed in the external environment** using:

` sandbox_permissions: require_escalated `

This includes, but is not limited to:

- `docker`
- `docker compose`
- `openssl`
- `gh` (GitHub CLI)
- `git`

Apply the same rule to similar commands when they require any of the following:

- network access;
- credentials or authenticated sessions;
- system daemons;
- sockets;
- host-level resources;
- resources that may be restricted or unavailable inside the sandbox.

Do not treat such a command as successfully validated merely because an invocation inside the sandbox appears to run.

If a command in this category fails in the sandbox, or there is any indication that sandbox restrictions affected its behavior:

1. Retry it with `sandbox_permissions: require_escalated`.
2. Provide a short, specific reason for requesting elevated execution.
3. Evaluate success or failure based on the escalated execution result.

## Read-Only Inspection

For read-only inspection of repositories or directories:

1. Use native OMP read/search tools when they work.
2. For shell-based discovery on Windows, use PowerShell-native commands.
3. Access an explicit absolute path when the task provides one; do not assume a path outside the current workspace is inaccessible.
4. Verify accessibility with `Test-Path`, `Get-ChildItem`, or a direct read before reporting a permission problem.
5. Do not modify files unless the user explicitly requests a write operation.
