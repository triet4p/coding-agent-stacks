#Requires -Version 5.1
<#
.SYNOPSIS
Installs coding-agent-stacks rules, skills, subagent definitions, and an optional preset config.
.EXAMPLE
.\install.ps1 -WhatIf
.EXAMPLE
.\install.ps1 -Force
.EXAMPLE
.\install.ps1 -UsePresetConfig:$false
.EXAMPLE
.\install.ps1 -HomePath 'C:\Users\another-user'
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string] $HomePath = $HOME,
    [switch] $Force,
    [switch] $UsePresetConfig = $true
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($HomePath)) {
    throw 'HomePath must not be empty.'
}
$destinationHome = [System.IO.Path]::GetFullPath($HomePath)
$payloadRoots = @('.agents/rules', '.agents/skills', '.omp/agent/agents')
$plan = @()
$conflicts = @()
function Get-ContentDigest([string] $Path) {
    $stream = [System.IO.File]::OpenRead($Path)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        return [System.BitConverter]::ToString($sha256.ComputeHash($stream))
    } finally {
        $sha256.Dispose()
        $stream.Dispose()
    }
}


# Preflight the entire payload before copying any files.
foreach ($relativeRoot in $payloadRoots) {
    $sourceRoot = Join-Path $PSScriptRoot $relativeRoot
    if (-not (Test-Path -LiteralPath $sourceRoot -PathType Container)) {
        throw "Missing payload directory: $sourceRoot. Run this script from a complete repository clone."
    }
    $sourceFiles = @(Get-ChildItem -LiteralPath $sourceRoot -File -Recurse -Force | Sort-Object FullName)
    if ($sourceFiles.Count -eq 0) {
        throw "Empty payload directory: $sourceRoot"
    }
    foreach ($file in $sourceFiles) {
        $relativeFile = $file.FullName.Substring($sourceRoot.Length).TrimStart([char[]]'\/')
        $relativePath = Join-Path $relativeRoot $relativeFile
        $destination = Join-Path $destinationHome $relativePath
        $parent = Split-Path -Parent $destination
        while ($parent) {
            if (Test-Path -LiteralPath $parent) {
                if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
                    throw "Destination parent is not a directory: $parent"
                }
                break
            }
            $parent = Split-Path -Parent $parent
        }
        $exists = Test-Path -LiteralPath $destination
        if ($exists -and -not (Test-Path -LiteralPath $destination -PathType Leaf)) {
            throw "Destination is not a file: $destination"
        }
        if ($exists) {
            $sourceHash = Get-ContentDigest $file.FullName
            $destinationHash = Get-ContentDigest $destination
            if ($sourceHash -eq $destinationHash) {
                continue
            }
            $conflicts += $destination
        }
        $plan += [pscustomobject]@{
            Source = $file.FullName
            Destination = $destination
            RelativePath = $relativePath
            Exists = $exists
        }
    }
}
if ($UsePresetConfig) {
    $presetSource = Join-Path $PSScriptRoot '.omp/agent/config.example.yml'
    if (-not (Test-Path -LiteralPath $presetSource -PathType Leaf)) {
        throw "Missing preset config: $presetSource. Run this script from a complete repository clone or disable it with -UsePresetConfig:`$false."
    }

    $relativePath = '.omp/agent/config.yml'
    $destination = Join-Path $destinationHome $relativePath
    $parent = Split-Path -Parent $destination
    while ($parent) {
        if (Test-Path -LiteralPath $parent) {
            if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
                throw "Destination parent is not a directory: $parent"
            }
            break
        }
        $parent = Split-Path -Parent $parent
    }

    $exists = Test-Path -LiteralPath $destination
    if ($exists -and -not (Test-Path -LiteralPath $destination -PathType Leaf)) {
        throw "Destination is not a file: $destination"
    }
    $presetMatches = $false
    if ($exists) {
        $sourceHash = Get-ContentDigest $presetSource
        $destinationHash = Get-ContentDigest $destination
        if ($sourceHash -eq $destinationHash) {
            $presetMatches = $true
        } else {
            $conflicts += $destination
        }
    }
    if (-not $presetMatches) {
        $plan += [pscustomobject]@{
            Source = $presetSource
            Destination = $destination
            RelativePath = $relativePath
            Exists = $exists
        }
    }
}


if ($conflicts.Count -gt 0 -and -not $Force) {
    throw ("Existing files differ; nothing was installed. Use -Force to back up and replace them:`n" + ($conflicts -join "`n"))
}

$backupId = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffZ') + '-' + [Guid]::NewGuid().ToString('N')
$installed = 0
$backedUp = 0
foreach ($entry in $plan) {
    $action = 'Install file'
    if ($entry.Exists) {
        $action = 'Back up and replace file'
    }
    if ($PSCmdlet.ShouldProcess($entry.Destination, $action)) {
        if ($entry.Exists) {
            # Backups stay inside the corresponding .agents or .omp root.
            $parts = $entry.RelativePath -split '[\\/]', 2
            $backupRoot = Join-Path (Join-Path $destinationHome $parts[0]) '.install-backups'
            $backup = Join-Path (Join-Path $backupRoot $backupId) $parts[1]
            [System.IO.Directory]::CreateDirectory((Split-Path -Parent $backup)) | Out-Null
            Copy-Item -LiteralPath $entry.Destination -Destination $backup
            Write-Host "Backup: $backup"
            $backedUp++
        }
        [System.IO.Directory]::CreateDirectory((Split-Path -Parent $entry.Destination)) | Out-Null
        Copy-Item -LiteralPath $entry.Source -Destination $entry.Destination -Force
        $installed++
    }
}

if ($WhatIfPreference) {
    Write-Host "Preview: $($plan.Count) file(s) need installation; no files changed."
} else {
    Write-Host "Installed $installed file(s); backed up $backedUp file(s). Destination: $destinationHome"
}
