#!/bin/bash
# Build script for Balanz Portfolio Tracker
# Creates standalone executables using PyInstaller

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Balanz Portfolio Tracker - Build Script${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Determine platform
PLATFORM=$(uname -s)
case "$PLATFORM" in
    Darwin*)
        PLATFORM_NAME="macOS"
        ;;
    Linux*)
        PLATFORM_NAME="Linux"
        ;;
    MINGW*|MSYS*|CYGWIN*)
        PLATFORM_NAME="Windows"
        ;;
    *)
        echo -e "${RED}Unsupported platform: $PLATFORM${NC}"
        exit 1
        ;;
esac

echo -e "${YELLOW}Platform:${NC} $PLATFORM_NAME"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Error: Virtual environment not found!${NC}"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo -e "${YELLOW}PyInstaller not found. Installing...${NC}"
    pip install pyinstaller>=6.0.0
fi

# Clean previous builds
echo -e "${YELLOW}Cleaning previous builds...${NC}"
rm -rf build dist

# Build the application
echo -e "${YELLOW}Building application...${NC}"
echo "This may take several minutes..."
echo ""

pyinstaller balanz-tracker.spec --clean --noconfirm

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}Build completed successfully!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""

    case "$PLATFORM_NAME" in
        macOS)
            echo -e "${YELLOW}Output location:${NC}"
            echo "  - Application bundle: dist/BalanzTracker.app"
            echo ""
            echo -e "${YELLOW}To run the application:${NC}"
            echo "  open dist/BalanzTracker.app"
            echo ""
            echo -e "${YELLOW}To create a DMG for distribution:${NC}"
            echo "  ./create-dmg.sh"
            ;;
        Linux)
            echo -e "${YELLOW}Output location:${NC}"
            echo "  - Executable: dist/BalanzTracker/BalanzTracker"
            echo ""
            echo -e "${YELLOW}To run the application:${NC}"
            echo "  ./dist/BalanzTracker/BalanzTracker"
            echo ""
            echo -e "${YELLOW}To create a distributable archive:${NC}"
            echo "  cd dist && tar -czf BalanzTracker-linux-x64.tar.gz BalanzTracker/"
            ;;
        Windows)
            echo -e "${YELLOW}Output location:${NC}"
            echo "  - Executable: dist/BalanzTracker/BalanzTracker.exe"
            echo ""
            echo -e "${YELLOW}To run the application:${NC}"
            echo "  dist\\BalanzTracker\\BalanzTracker.exe"
            echo ""
            echo -e "${YELLOW}To create a distributable archive:${NC}"
            echo "  Compress-Archive -Path dist/BalanzTracker -DestinationPath BalanzTracker-windows-x64.zip"
            ;;
    esac

    # Calculate size
    if [ -d "dist/BalanzTracker.app" ]; then
        SIZE=$(du -sh dist/BalanzTracker.app | cut -f1)
        echo -e "${YELLOW}Package size:${NC} $SIZE"
    elif [ -d "dist/BalanzTracker" ]; then
        SIZE=$(du -sh dist/BalanzTracker | cut -f1)
        echo -e "${YELLOW}Package size:${NC} $SIZE"
    fi

else
    echo ""
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}Build failed!${NC}"
    echo -e "${RED}========================================${NC}"
    echo ""
    echo "Check the error messages above for details."
    exit 1
fi

echo ""
