#!/bin/bash
# Run script for Balanz Portfolio Tracker

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment and run the app
source venv/bin/activate
python app/main.py
