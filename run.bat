@echo off
REM Run script for Balanz Portfolio Tracker (Windows)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Error: Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Activate virtual environment and run the application
call venv\Scripts\activate.bat
python app\main.py

REM Keep window open if there was an error
if %errorlevel% neq 0 (
    echo.
    echo Application exited with an error
    pause
)
