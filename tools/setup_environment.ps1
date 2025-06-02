<#
.SYNOPSIS
    Sets up the development environment for the Windsurf Project Startup Pack (Memory Synchronization Tools).
.DESCRIPTION
    This script creates a Python virtual environment and installs all required dependencies for memory sync, onboarding, and automation tools.
    - Robust error handling and onboarding guidance
    - Ready for manual, CI, and automated use
    - Mirrors cross-platform onboarding best practices

.ONBOARDING
    Usage Examples:
    - Manual:
        powershell -ExecutionPolicy Bypass -File tools/setup_environment.ps1
        powershell -ExecutionPolicy Bypass -File tools/setup_environment.ps1 -Dev
    - CI/CD:
        - name: Setup Python Environment
          run: powershell -ExecutionPolicy Bypass -File tools/setup_environment.ps1
    - Troubleshooting:
        - Review output for errors (Python not found, missing requirements, etc)
        - See Troubleshooting Tips at the end of this script
    - Python/Linux/Mac users:
        - Use the equivalent Python script (setup_environment.py) if available, or manually create a venv and install requirements.

.NOTES
    - This script should be run from the project root.
    - For advanced onboarding, see memory_system_guide.ps1 and session protocols.
#>

param (
    [switch]$Dev = $false
)

$ErrorActionPreference = "Stop"

# Step 1: Check if Python is installed
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "Python is not installed or not in PATH. Please install Python 3.7 or higher."
    exit 1
}

# Step 2: Validate Python version
$versionMatch = [regex]::Match($pythonVersion, '(\d+)\.(\d+)')
if (-not $versionMatch.Success -or 
    [int]$versionMatch.Groups[1].Value -lt 3 -or 
    ([int]$versionMatch.Groups[1].Value -eq 3 -and [int]$versionMatch.Groups[2].Value -lt 7)) {
    Write-Error "Python 3.7 or higher is required. Found: $pythonVersion"
    exit 1
}

Write-Host "Setting up environment for Windsurf Project Startup Pack..." -ForegroundColor Green

# Step 3: Create virtual environment if missing
$venvPath = ".venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv $venvPath
}

# Step 4: Activate virtual environment
$activateScript = if ($IsWindows) { "$venvPath\Scripts\Activate.ps1" } else { "$venvPath/bin/Activate.ps1" }
if (-not (Test-Path $activateScript)) {
    Write-Error "Failed to create virtual environment. Activation script not found at: $activateScript"
    exit 1
}

# Step 5: Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Cyan
& $activateScript
pip install --upgrade pip
pip install -r requirements.txt

if ($Dev) {
    Write-Host "Installing development dependencies..." -ForegroundColor Cyan
    pip install -r requirements-dev.txt
}

Write-Host "`nEnvironment setup complete!" -ForegroundColor Green
Write-Host "To activate the virtual environment, run:"
Write-Host "    .\$venvPath\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "`nTo run the memory sync tools, use:"

# Troubleshooting Tips
Write-Host "`nTROUBLESHOOTING TIPS:" -ForegroundColor Magenta
Write-Host "- If you see 'Python is not installed', ensure Python 3.7+ is in your PATH."
Write-Host "- If pip fails, try running 'python -m ensurepip --upgrade' inside the venv."
Write-Host "- For permission errors, run PowerShell as Administrator."
Write-Host "- For cross-platform setup, see setup_environment.py or run equivalent venv/pip commands manually."
Write-Host "- For further onboarding help, see memory_system_guide.ps1 or ask the Architect agent."
Write-Host "    python -m tools.run_memory_sync [command]" -ForegroundColor Yellow
