# SARA - Quick Start Script for PowerShell
# This script activates the virtual environment, installs dependencies, and runs the application

Write-Host "🚀 Starting SARA..." -ForegroundColor Cyan

# Check if virtual environment exists
if (-not (Test-Path ".\.venv\Scripts\Activate.ps1")) {
    Write-Host "❌ Virtual environment not found. Creating one..." -ForegroundColor Yellow
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
        exit 1
    }
}

# Activate virtual environment
Write-Host "📦 Activating virtual environment..." -ForegroundColor Cyan
& .\.venv\Scripts\Activate.ps1

# Install/Update dependencies
Write-Host "📥 Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Run the application
Write-Host "✨ Running SARA application..." -ForegroundColor Green
python main.py

# Check exit code
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Application exited with errors" -ForegroundColor Red
    exit 1
}

Write-Host "✅ SARA completed successfully" -ForegroundColor Green
