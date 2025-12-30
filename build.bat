@echo off
REM Build script for Balanz Portfolio Tracker (Windows)
REM Creates standalone executables using PyInstaller

echo ========================================
echo Balanz Portfolio Tracker - Build Script
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Error: Virtual environment not found!
    echo Please run setup.bat first
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if PyInstaller is installed
where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller>=6.0.0
)

REM Clean previous builds
echo Cleaning previous builds...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

REM Build the application
echo Building application...
echo This may take several minutes...
echo.

pyinstaller balanz-tracker.spec --clean --noconfirm

REM Check if build was successful
if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Build completed successfully!
    echo ========================================
    echo.
    echo Output location:
    echo   - Executable: dist\BalanzTracker\BalanzTracker.exe
    echo.
    echo To run the application:
    echo   dist\BalanzTracker\BalanzTracker.exe
    echo.
    echo To create a distributable archive:
    echo   1. Right-click dist\BalanzTracker folder
    echo   2. Select "Send to" ^> "Compressed (zipped) folder"
    echo   Or use PowerShell:
    echo   Compress-Archive -Path dist\BalanzTracker -DestinationPath BalanzTracker-windows-x64.zip
    echo.
) else (
    echo.
    echo ========================================
    echo Build failed!
    echo ========================================
    echo.
    echo Check the error messages above for details.
    exit /b 1
)

pause
