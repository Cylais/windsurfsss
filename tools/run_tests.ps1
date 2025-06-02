<#
.SYNOPSIS
    Runs the test suite for the memory synchronization system.
.DESCRIPTION
    This script runs the unit tests for the memory synchronization tools,
    including both the file-based memory bank and SQLite memory system integration.
#>

param (
    [switch]$Coverage = $false,
    [string]$TestPattern = "test_*.py"
)

$ErrorActionPreference = "Stop"

# Check if virtual environment exists
$venvPath = ".venv"
if (-not (Test-Path $venvPath)) {
    Write-Error "Virtual environment not found. Run setup_environment.ps1 first."
    exit 1
}

# Activate virtual environment
$activateScript = if ($IsWindows) { "$venvPath\Scripts\Activate.ps1" } else { "$venvPath/bin/Activate.ps1" }
if (-not (Test-Path $activateScript)) {
    Write-Error "Failed to find virtual environment activation script at: $activateScript"
    exit 1
}

& $activateScript

# Ensure test directory exists
$testDir = "tests"
if (-not (Test-Path $testDir)) {
    New-Item -ItemType Directory -Path $testDir | Out-Null
    Write-Host "Created test directory: $testDir" -ForegroundColor Yellow
}

# Find test files
$testFiles = Get-ChildItem -Path $testDir -Filter $TestPattern -Recurse -File | 
            Where-Object { $_.FullName -notlike '*__pycache__*' } | 
            Select-Object -ExpandProperty FullName

if (-not $testFiles) {
    Write-Host "No test files found matching pattern: $TestPattern" -ForegroundColor Yellow
    exit 0
}

Write-Host "Running tests..." -ForegroundColor Green
Write-Host "Test files: $($testFiles -join ', ')"

# Run tests with coverage if requested
if ($Coverage) {
    # Install coverage if not already installed
    $coverageInstalled = pip show coverage 2>&1 | Select-String -Pattern "Name: coverage" -Quiet
    if (-not $coverageInstalled) {
        Write-Host "Installing coverage..." -ForegroundColor Cyan
        pip install coverage
    }
    
    # Run tests with coverage
    Write-Host "Running tests with coverage..." -ForegroundColor Cyan
    python -m coverage run -m unittest discover -s tests -p $TestPattern
    
    # Generate coverage report
    if ($LASTEXITCODE -eq 0) {
        python -m coverage report -m
        
        # Generate HTML report
        $coverageHtmlDir = "htmlcov"
        python -m coverage html -d $coverageHtmlDir
        Write-Host "Coverage HTML report available at: $PWD\$coverageHtmlDir\index.html" -ForegroundColor Green
    }
} else {
    # Run tests without coverage
    python -m unittest discover -s tests -p $TestPattern -v
}

# Exit with appropriate status
exit $LASTEXITCODE
