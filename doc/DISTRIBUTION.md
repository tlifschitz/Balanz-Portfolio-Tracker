# Distribution Guide
## Balanz Portfolio Tracker

This guide covers building and distributing the Balanz Portfolio Tracker application.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Building the Application](#building-the-application)
3. [Platform-Specific Instructions](#platform-specific-instructions)
4. [Distribution Checklist](#distribution-checklist)
5. [GitHub Releases](#github-releases)
6. [Code Signing (Optional)](#code-signing-optional)

---

## Prerequisites

### All Platforms

1. **Python 3.9 or higher**
2. **Virtual environment** with all dependencies installed:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Platform-Specific Requirements

#### macOS
- Xcode Command Line Tools: `xcode-select --install`
- (Optional) For better DMG creation: `brew install create-dmg`

#### Windows
- Windows 10 or higher
- Visual C++ Redistributable (usually pre-installed)

#### Linux
- GTK 3.0 or higher
- WebKit2GTK: `sudo apt-get install libwebkit2gtk-4.0-37` (Debian/Ubuntu)

---

## Building the Application

### Quick Build

#### macOS / Linux
```bash
./build.sh
```

#### Windows
```cmd
build.bat
```

### Manual Build

If you prefer to build manually:

```bash
# Activate virtual environment
source venv/bin/activate  # Windows: venv\Scripts\activate

# Clean previous builds
rm -rf build dist  # Windows: rmdir /s /q build dist

# Build using PyInstaller
pyinstaller balanz-tracker.spec --clean --noconfirm
```

### Build Output

The build process creates:

- **macOS**: `dist/BalanzTracker.app` (Application bundle)
- **Windows**: `dist/BalanzTracker/BalanzTracker.exe` (Executable + dependencies)
- **Linux**: `dist/BalanzTracker/BalanzTracker` (Executable + dependencies)

---

## Platform-Specific Instructions

### macOS

#### 1. Build the Application
```bash
./build.sh
```

#### 2. Create DMG Installer (Recommended)
```bash
./create-dmg.sh
```

This creates:
- `BalanzTracker-1.0.0-macOS.dmg` - Installer disk image
- `BalanzTracker-1.0.0-macOS.dmg.sha256` - Checksum for verification

#### 3. Test the Application
```bash
open dist/BalanzTracker.app
```

#### 4. Distribution Options

**Option A: DMG Installer (Recommended)**
- Distribute the `.dmg` file
- Include the `.sha256` checksum file
- Users drag the app to Applications folder

**Option B: ZIP Archive**
```bash
cd dist
zip -r BalanzTracker-macOS.zip BalanzTracker.app
shasum -a 256 BalanzTracker-macOS.zip > BalanzTracker-macOS.zip.sha256
```

#### Known Issues on macOS

**"BalanzTracker.app is damaged and can't be opened"**

This happens because the app isn't signed. Users can bypass with:
```bash
xattr -cr /Applications/BalanzTracker.app
```

Or right-click → Open → Open anyway

For professional distribution, consider [code signing](#code-signing-optional).

---

### Windows

#### 1. Build the Application
```cmd
build.bat
```

#### 2. Test the Application
```cmd
dist\BalanzTracker\BalanzTracker.exe
```

#### 3. Create Distribution Archive

**Option A: Using PowerShell**
```powershell
Compress-Archive -Path dist\BalanzTracker -DestinationPath BalanzTracker-windows-x64.zip
certutil -hashfile BalanzTracker-windows-x64.zip SHA256 > BalanzTracker-windows-x64.zip.sha256
```

**Option B: Using GUI**
1. Right-click `dist\BalanzTracker` folder
2. Select "Send to" → "Compressed (zipped) folder"
3. Rename to `BalanzTracker-windows-x64.zip`

#### 4. Distribution

Distribute the `.zip` file containing the entire `BalanzTracker` folder.

Users should:
1. Extract the ZIP file
2. Run `BalanzTracker.exe`

#### Known Issues on Windows

**Windows SmartScreen Warning**

Unsigned executables trigger SmartScreen. Users can bypass with:
- Click "More info"
- Click "Run anyway"

For professional distribution, consider [code signing](#code-signing-optional).

---

### Linux

#### 1. Build the Application
```bash
./build.sh
```

#### 2. Test the Application
```bash
./dist/BalanzTracker/BalanzTracker
```

#### 3. Create Distribution Archive
```bash
cd dist
tar -czf BalanzTracker-linux-x64.tar.gz BalanzTracker/
sha256sum BalanzTracker-linux-x64.tar.gz > BalanzTracker-linux-x64.tar.gz.sha256
cd ..
```

#### 4. Distribution

Distribute the `.tar.gz` file.

Users should:
```bash
tar -xzf BalanzTracker-linux-x64.tar.gz
cd BalanzTracker
./BalanzTracker
```

#### Optional: Create Desktop Entry

Create `balanz-tracker.desktop`:
```ini
[Desktop Entry]
Name=Balanz Portfolio Tracker
Comment=Portfolio analytics for Balanz clients
Exec=/path/to/BalanzTracker/BalanzTracker
Icon=/path/to/BalanzTracker/icon.png
Terminal=false
Type=Application
Categories=Office;Finance;
```

---

## Distribution Checklist

Before releasing a new version:

- [ ] Update version number in `balanz-tracker.spec`
- [ ] Test on clean system (VM or fresh install)
- [ ] Build for all target platforms
- [ ] Generate SHA256 checksums for all packages
- [ ] Test installation process on each platform
- [ ] Verify all features work in built version
- [ ] Update CHANGELOG.md with release notes
- [ ] Tag release in git: `git tag v1.0.0`
- [ ] Create GitHub release with binaries

---

## GitHub Releases

### Automated Release (Recommended)

Use the GitHub Actions workflow (`.github/workflows/release.yml`) to automatically build and publish releases.

1. Update version in balanz-tracker.spec and CHANGELOG.md
2. Commit and tag
```bash
git add .
git commit -m "Release v1.0.0"
git tag v1.0.0
git push origin main
git push origin v1.0.0
```

The workflow will:
1. Build for macOS, Windows, and Linux
2. Generate checksums
3. Create a GitHub release
4. Upload all artifacts

### Manual Release

#### 1. Build on Each Platform

Build separately on macOS, Windows, and Linux machines:

**macOS:**
```bash
./build.sh
./create-dmg.sh
```

**Windows:**
```cmd
build.bat
# Then create ZIP manually
```

**Linux:**
```bash
./build.sh
cd dist
tar -czf BalanzTracker-linux-x64.tar.gz BalanzTracker/
sha256sum BalanzTracker-linux-x64.tar.gz > BalanzTracker-linux-x64.tar.gz.sha256
```

#### 2. Create GitHub Release

1. Go to GitHub → Releases → "Draft a new release"
2. Create a new tag (e.g., `v1.0.0`)
3. Write release notes
4. Upload artifacts:
   - `BalanzTracker-1.0.0-macOS.dmg`
   - `BalanzTracker-1.0.0-macOS.dmg.sha256`
   - `BalanzTracker-windows-x64.zip`
   - `BalanzTracker-windows-x64.zip.sha256`
   - `BalanzTracker-linux-x64.tar.gz`
   - `BalanzTracker-linux-x64.tar.gz.sha256`
5. Publish release

---

## Code Signing (Optional)

Code signing eliminates security warnings on macOS and Windows.

### macOS Code Signing

**Requirements:**
- Apple Developer account ($99/year)
- Developer ID Application certificate

**Process:**
```bash
# Sign the app
codesign --deep --force --verify --verbose \
  --sign "Developer ID Application: Your Name (TEAM_ID)" \
  --options runtime \
  dist/BalanzTracker.app

# Verify signature
codesign --verify --deep --verbose=2 dist/BalanzTracker.app

# Notarize (submit to Apple for scanning)
xcrun notarytool submit BalanzTracker-1.0.0-macOS.dmg \
  --apple-id your@email.com \
  --team-id TEAM_ID \
  --password app-specific-password \
  --wait

# Staple notarization ticket
xcrun stapler staple dist/BalanzTracker.app
```

Update `balanz-tracker.spec`:
```python
codesign_identity='Developer ID Application: Your Name (TEAM_ID)',
```

### Windows Code Signing

**Requirements:**
- Code signing certificate (from DigiCert, Sectigo, etc.)
- signtool.exe (included with Windows SDK)

**Process:**
```cmd
signtool sign /f certificate.pfx /p password /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\BalanzTracker\BalanzTracker.exe
```

---

## Build Optimization

### Reduce Package Size

#### 1. Exclude Unused Modules

Edit `balanz-tracker.spec` and add to `excludes`:
```python
excludes=[
    'matplotlib',
    'scipy',
    'IPython',
    'jupyter',
    'notebook',
    'PIL',  # If not using images
    'tkinter',  # If not using Tkinter
],
```

#### 2. Use UPX Compression

UPX (Ultimate Packer for eXecutables) compresses binaries.

Install:
- macOS: `brew install upx`
- Linux: `sudo apt-get install upx`
- Windows: Download from https://upx.github.io/

Enable in spec (already enabled):
```python
upx=True,
```

#### 3. One-File Mode (Trade-offs)

**Pros:** Single executable file
**Cons:** Slower startup, larger file size, potential antivirus issues

Modify spec:
```python
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # Add this
    a.zipfiles,  # Add this
    a.datas,     # Add this
    [],
    exclude_binaries=False,  # Change to False
    # ... rest of config
)

# Remove COLLECT section entirely
```

---

## Troubleshooting

### Build Fails with "Module not found"

Add missing module to `hiddenimports` in `balanz-tracker.spec`:
```python
hiddenimports = [
    # ... existing imports
    'your.missing.module',
]
```

### "Failed to execute script" Error

Run in console mode to see errors:
```python
console=True,  # In exe = EXE(...) section
```

### Large Package Size

- Remove unused dependencies
- Enable UPX compression
- Exclude development dependencies

### Application Crashes on Startup

Test with console mode enabled to see error messages.

Common causes:
- Missing data files (add to `datas` in spec)
- Missing hidden imports
- Path issues (use relative paths)

---

## File Size Reference

Typical sizes for v1.0.0:

| Platform | Format | Compressed | Uncompressed |
|----------|--------|------------|--------------|
| macOS    | DMG    | ~40-50 MB  | ~80-100 MB   |
| Windows  | ZIP    | ~35-45 MB  | ~70-90 MB    |
| Linux    | tar.gz | ~35-45 MB  | ~70-90 MB    |

---

## Additional Resources

- [PyInstaller Documentation](https://pyinstaller.org/)
- [create-dmg Documentation](https://github.com/create-dmg/create-dmg)
- [Apple Code Signing Guide](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)
- [Windows Code Signing](https://docs.microsoft.com/en-us/windows/win32/seccrypto/using-signtool-to-sign-a-file)

---

## Support

For build issues, check:
1. This distribution guide
2. PyInstaller troubleshooting docs
3. Project GitHub issues
4. PRD.md for architecture details
