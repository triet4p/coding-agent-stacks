#Requires -Version 5.1
<#
.SYNOPSIS
Copies installed rules, skills, and subagent definitions from a home directory back into this repository.
.DESCRIPTION
Reverse direction of install.ps1: reads the live payload under a home directory
(normally $HOME) and copies new or changed files into this repository checkout.

The home directory is strictly read-only for this script: nothing under it is
ever written, backed up, or deleted. All writes stay inside this repository
checkout, so review them with git status/diff before committing.

The local config (~/.omp/agent/config.yml) is never synced back. It holds
machine-local state; update .omp/agent/config.example.yml by hand when the
shareable preset itself changes.
.EXAMPLE
.\sync-from-home.ps1 -WhatIf
.EXAMPLE
.\sync-from-home.ps1
.EXAMPLE
.\sync-from-home.ps1 -HomePath 'D:\AgentHome' -Prune
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string] $HomePath = $HOME,
    [switch] $Prune
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($HomePath)) {
    throw 'HomePath must not be empty.'
}
$sourceHome = [System.IO.Path]::GetFullPath($HomePath)
$repoRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$payloadRoots = @('.agents/rules', '.agents/skills', '.omp/agent/agents')
$plan = @()
$stale = @()
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
    $homeRoot = Join-Path $sourceHome $relativeRoot
    if (-not (Test-Path -LiteralPath $homeRoot -PathType Container)) {
        throw "Missing installed payload directory: $homeRoot."
    }
    $repoDir = Join-Path $repoRoot $relativeRoot
    $homeFiles = @(Get-ChildItem -LiteralPath $homeRoot -File -Recurse -Force | Sort-Object FullName)
    if ($homeFiles.Count -eq 0) {
        throw "Empty installed payload directory: $homeRoot"
    }
    $seen = @{}
    foreach ($file in $homeFiles) {
        $relativeFile = $file.FullName.Substring($homeRoot.Length).TrimStart([char[]]'\/')
        $relativePath = Join-Path $relativeRoot $relativeFile
        $seen[$relativeFile] = $true
        $destination = Join-Path $repoDir $relativeFile
        # Keep every write inside this repository checkout.
        $resolved = [System.IO.Path]::GetFullPath($destination)
        if (-not $resolved.StartsWith($repoDir + [System.IO.Path]::DirectorySeparatorChar)) {
            throw "Refusing to write outside the repository: $destination"
        }
        $exists = Test-Path -LiteralPath $destination
        if ($exists -and -not (Test-Path -LiteralPath $destination -PathType Leaf)) {
            throw "Repository path is not a file: $destination"
        }
        if ($exists) {
            $homeHash = Get-ContentDigest $file.FullName
            $repoHash = Get-ContentDigest $destination
            if ($homeHash -eq $repoHash) {
                continue
            }
        }
        $plan += [pscustomobject]@{
            Source = $file.FullName
            Destination = $destination
            RelativePath = $relativePath
            Exists = $exists
        }
    }
    if (Test-Path -LiteralPath $repoDir -PathType Container) {
        foreach ($repoFile in @(Get-ChildItem -LiteralPath $repoDir -File -Recurse -Force | Sort-Object FullName)) {
            $relativeFile = $repoFile.FullName.Substring($repoDir.Length).TrimStart([char[]]'\/')
            if (-not $seen.ContainsKey($relativeFile)) {
                $stale += (Join-Path $relativeRoot $relativeFile)
            }
        }
    }
}

$copied = 0
foreach ($entry in $plan) {
    $action = 'Copy new file into repository'
    if ($entry.Exists) {
        $action = 'Update repository file from home'
    }
    if ($PSCmdlet.ShouldProcess($entry.Destination, $action)) {
        [System.IO.Directory]::CreateDirectory((Split-Path -Parent $entry.Destination)) | Out-Null
        Copy-Item -LiteralPath $entry.Source -Destination $entry.Destination -Force
        Write-Host "$action`: $($entry.RelativePath)"
        $copied++
    }
}

$pruned = 0
foreach ($relativePath in $stale) {
    $target = Join-Path $repoRoot $relativePath
    if ($Prune) {
        if ($PSCmdlet.ShouldProcess($target, 'Remove repository file missing from home')) {
            Remove-Item -LiteralPath $target -Force
            Write-Host "Pruned: $relativePath"
            $pruned++
        }
    } else {
        Write-Host "Repo-only (left alone; use -Prune to remove): $relativePath"
    }
}

if ($WhatIfPreference) {
    Write-Host "Preview: $($plan.Count) file(s) would be copied from home; $($stale.Count) repo-only file(s) would be left alone."
} else {
    Write-Host "Synced $copied file(s), pruned $pruned file(s). Home untouched: $sourceHome"
}
