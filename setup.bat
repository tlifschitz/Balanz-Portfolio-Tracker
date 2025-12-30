@echo off
REM Setup script for Balanz Portfolio Tracker (Windows)

echo ========================================
echo Balanz Portfolio Tracker - Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.9 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if exist "venv" (
    echo Virtual environment already exists. Removing...
    rmdir /s /q venv
)

python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo Virtual environment created successfully
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
echo This may take a few minutes...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Setup completed successfully!
    echo ========================================
    echo.
    echo To run the application:
    echo   run.bat
    echo.
    echo Or manually:
    echo   1. venv\Scripts\activate.bat
    echo   2. python app\main.py
    echo.
) else (
    echo.
    echo ========================================
    echo Setup failed!
    echo ========================================
    echo.
    echo Please check the error messages above
    pause
    exit /b 1
)

pause
