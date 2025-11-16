#!/bin/bash
# SARA - Quick Start Script for Unix/Linux/Mac
# This script activates the virtual environment, installs dependencies, and runs the application

set -e  # Exit on error

echo "🚀 Starting SARA..."

# Check if virtual environment exists
if [ ! -f ".venv/bin/activate" ]; then
    echo "❌ Virtual environment not found. Creating one..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv/bin/activate

# Install/Update dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

# Run the application
echo "✨ Running SARA application..."
python main.py

echo "✅ SARA completed successfully"
