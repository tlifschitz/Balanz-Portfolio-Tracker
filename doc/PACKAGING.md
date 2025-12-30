# Packaging & Distribution - Quick Start

This guide helps you quickly understand and use the packaging infrastructure for Balanz Portfolio Tracker.

---

## 🎯 Quick Links

- **Build the app**: See [Building](#building) below
- **Distribute the app**: See [DISTRIBUTION.md](doc/DISTRIBUTION.md)
- **Detailed setup**: See [PACKAGING.md](doc/PACKAGING.md)

---

## ✅ What's Included

The packaging infrastructure provides:

✅ **Build Scripts** - One command to build for your platform
✅ **GitHub Actions** - Automatic releases when you push a tag
✅ **Cross-Platform** - macOS, Windows, and Linux support
✅ **Documentation** - Comprehensive guides for all scenarios
✅ **Checksums** - SHA256 verification for all releases
✅ **DMG Creator** - Professional macOS installers

---

## 🚀 Building

### Prerequisites

```bash
# Install Python dependencies (includes PyInstaller)
./setup.sh  # macOS/Linux
setup.bat   # Windows
```

### Build Commands

#### macOS
```bash
./build.sh              # Creates BalanzTracker.app
./create-dmg.sh         # Creates distributable DMG
```

#### Windows
```cmd
build.bat              REM Creates BalanzTracker.exe
```

#### Linux
```bash
./build.sh             # Creates BalanzTracker executable
```

### What You Get

After building, you'll find in the `dist/` folder:

- **macOS**: `BalanzTracker.app` (and `BalanzTracker-X.X.X-macOS.dmg` if you ran create-dmg.sh)
- **Windows**: `BalanzTracker/BalanzTracker.exe` (folder with executable and dependencies)
- **Linux**: `BalanzTracker/BalanzTracker` (folder with executable and dependencies)

---

## 🏷️ Creating a Release

### Automated (Recommended)

```bash
# 1. Update version in balanz-tracker.spec and CHANGELOG.md
# 2. Commit and tag
git add .
git commit -m "Release v1.0.0"
git tag v1.0.0
git push origin main
git push origin v1.0.0

# GitHub Actions will automatically:
# - Build for macOS, Windows, and Linux
# - Create GitHub release
# - Upload all binaries with checksums
```

### Manual

Build on each platform separately and create a GitHub release manually. See [DISTRIBUTION.md](DISTRIBUTION.md#manual-release) for details.

---

## 📁 File Structure

```
Balanz Portfolio Tracker/
├── balanz-tracker.spec          # PyInstaller configuration
├── build.sh                     # Build script (macOS/Linux)
├── build.bat                    # Build script (Windows)
├── create-dmg.sh                # DMG creator (macOS only)
├── setup.sh / setup.bat         # Environment setup
├── run.sh / run.bat             # Run from source
├── .github/workflows/
│   └── release.yml              # Automated release workflow
├── DISTRIBUTION.md              # Detailed distribution guide
├── PACKAGING_SUMMARY.md         # Implementation details
└── CHANGELOG.md                 # Version history
```

---

## 🛠️ Customization

### Change App Name
Edit `balanz-tracker.spec`:
```python
name='YourAppName',  # In exe = EXE(...)
```

### Add App Icon
1. Create icon files:
   - macOS: `.icns` file
   - Windows: `.ico` file
2. Update `balanz-tracker.spec`:
```python
icon='path/to/icon.icns',  # or icon.ico
```

### Change Version
Update in:
- `balanz-tracker.spec` (CFBundleVersion)
- `CHANGELOG.md`
- Git tag when releasing

### Exclude More Modules
Edit `balanz-tracker.spec`:
```python
excludes=[
    'matplotlib',
    'scipy',
    # Add more here
],
```

### Add Hidden Imports
Edit `balanz-tracker.spec`:
```python
hiddenimports = [
    # Existing imports...
    'your.module.here',
],
```

---

## 🐛 Troubleshooting

### "Module not found" Error

**Solution**: Add module to `hiddenimports` in `balanz-tracker.spec`

### "Failed to execute script" Error

**Solution**: Enable console mode to see errors:
```python
console=True,  # In exe = EXE(...) in spec file
```

### Build Too Large

**Solutions**:
- Add unused modules to `excludes` in spec file
- Ensure UPX compression is enabled: `upx=True`
- Remove unused dependencies from `requirements.txt`

### Windows SmartScreen Warning

**Why**: Executable is not signed
**User workaround**: Click "More info" → "Run anyway"
**Developer solution**: Code signing certificate (see DISTRIBUTION.md)

### macOS "Damaged App" Warning

**Why**: App is not signed or notarized
**User workaround**: `xattr -cr /Applications/BalanzTracker.app`
**Developer solution**: Apple Developer certificate + notarization (see DISTRIBUTION.md)

---

## 📊 Typical Build Sizes

| Platform | Compressed | Uncompressed |
|----------|------------|--------------|
| macOS DMG | ~40-50 MB | ~80-100 MB |
| Windows ZIP | ~35-45 MB | ~70-90 MB |
| Linux tar.gz | ~35-45 MB | ~70-90 MB |

---

## ✨ Features

### PyInstaller Spec File
- ✅ Platform detection
- ✅ Hidden imports for all dependencies
- ✅ Static file collection
- ✅ UPX compression
- ✅ macOS .app bundle with Info.plist
- ✅ Windows console mode control

### Build Scripts
- ✅ Platform detection
- ✅ Virtual environment verification
- ✅ Clean builds (removes old artifacts)
- ✅ Progress feedback
- ✅ Error handling
- ✅ Size calculation

### GitHub Actions
- ✅ Multi-platform builds in parallel
- ✅ Automatic checksum generation
- ✅ GitHub release creation
- ✅ Artifact upload
- ✅ Release notes generation

### Documentation
- ✅ User installation guides
- ✅ Developer build guides
- ✅ Distribution procedures
- ✅ Troubleshooting guides
- ✅ Code signing instructions

---

## 🎓 Learning Path

1. **Start here**: [README.md](README.md) - Understand the project
2. **Build locally**: Run `./build.sh` to create a build
3. **Test build**: Run the built application from `dist/`
4. **Deep dive**: Read [DISTRIBUTION.md](DISTRIBUTION.md) for full details
5. **Create release**: Follow automated release process
