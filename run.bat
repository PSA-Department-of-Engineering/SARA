@echo off
REM SARA - Quick Start Script for Windows Command Prompt
REM This script activates the virtual environment, installs dependencies, and runs the application

echo.
echo ======================================
echo   SARA - Quick Start
echo ======================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [!] Virtual environment not found. Creating one...
    python -m venv .venv
    if errorlevel 1 (
        echo [X] Failed to create virtual environment
        exit /b 1
    )
)

REM Activate virtual environment
echo [*] Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install/Update dependencies
echo [*] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [X] Failed to install dependencies
    exit /b 1
)

REM Run the application
echo [*] Running SARA application...
python main.py

if errorlevel 1 (
    echo [X] Application exited with errors
    exit /b 1
)

echo.
echo [✓] SARA completed successfully
