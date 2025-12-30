#!/bin/bash
# Create DMG installer for macOS distribution
# Requires: create-dmg (install via: brew install create-dmg)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Creating macOS DMG installer...${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}Error: This script only works on macOS${NC}"
    exit 1
fi

# Check if app bundle exists
if [ ! -d "dist/BalanzTracker.app" ]; then
    echo -e "${RED}Error: Application bundle not found!${NC}"
    echo "Please run ./build.sh first"
    exit 1
fi

# Get version from app (or use default)
VERSION="1.0.0"
DMG_NAME="BalanzTracker-${VERSION}-macOS"

# Remove old DMG if it exists
rm -f "${DMG_NAME}.dmg"

echo -e "${YELLOW}Creating DMG: ${DMG_NAME}.dmg${NC}"
echo ""

# Check if create-dmg is installed
if command -v create-dmg &> /dev/null; then
    # Use create-dmg tool (recommended)
    create-dmg \
        --volname "Balanz Portfolio Tracker" \
        --window-pos 200 120 \
        --window-size 600 400 \
        --icon-size 100 \
        --icon "BalanzTracker.app" 175 120 \
        --hide-extension "BalanzTracker.app" \
        --app-drop-link 425 120 \
        --no-internet-enable \
        "${DMG_NAME}.dmg" \
        "dist/BalanzTracker.app"
else
    # Fallback to hdiutil (built-in macOS tool)
    echo -e "${YELLOW}Note: create-dmg not found. Using basic DMG creation.${NC}"
    echo -e "${YELLOW}For better DMG styling, install create-dmg:${NC}"
    echo "  brew install create-dmg"
    echo ""

    # Create temporary directory
    TMP_DIR=$(mktemp -d)
    cp -R "dist/BalanzTracker.app" "$TMP_DIR/"

    # Create DMG
    hdiutil create -volname "Balanz Portfolio Tracker" \
        -srcfolder "$TMP_DIR" \
        -ov \
        -format UDZO \
        "${DMG_NAME}.dmg"

    # Clean up
    rm -rf "$TMP_DIR"
fi

if [ -f "${DMG_NAME}.dmg" ]; then
    # Calculate checksum
    echo ""
    echo -e "${YELLOW}Calculating SHA256 checksum...${NC}"
    CHECKSUM=$(shasum -a 256 "${DMG_NAME}.dmg" | cut -d' ' -f1)
    echo "$CHECKSUM  ${DMG_NAME}.dmg" > "${DMG_NAME}.dmg.sha256"

    SIZE=$(du -sh "${DMG_NAME}.dmg" | cut -f1)

    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}DMG created successfully!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo -e "${YELLOW}File:${NC} ${DMG_NAME}.dmg"
    echo -e "${YELLOW}Size:${NC} $SIZE"
    echo -e "${YELLOW}SHA256:${NC} $CHECKSUM"
    echo -e "${YELLOW}Checksum file:${NC} ${DMG_NAME}.dmg.sha256"
    echo ""
    echo -e "${YELLOW}To distribute:${NC}"
    echo "  1. Upload ${DMG_NAME}.dmg to your distribution platform"
    echo "  2. Include the SHA256 checksum for verification"
    echo "  3. Users can verify with: shasum -a 256 -c ${DMG_NAME}.dmg.sha256"
    echo ""
else
    echo ""
    echo -e "${RED}DMG creation failed!${NC}"
    exit 1
fi
