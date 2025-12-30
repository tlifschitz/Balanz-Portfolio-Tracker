# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Balanz Portfolio Tracker
Builds a standalone executable with all dependencies bundled.
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import sys
from pathlib import Path

block_cipher = None

# Determine platform
is_macos = sys.platform == 'darwin'
is_windows = sys.platform == 'win32'
is_linux = sys.platform.startswith('linux')

# Collect all static files (HTML, CSS, JS)
static_files = [
    ('app/ui/static', 'app/ui/static'),
]

# Collect data files from dependencies
datas = static_files
datas += collect_data_files('certifi')  # SSL certificates
datas += collect_data_files('fastapi')
datas += collect_data_files('uvicorn')

# Hidden imports that PyInstaller might miss
hiddenimports = [
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'httpx',
    'httpx._client',
    'httpx._config',
    'httpx._models',
    'httpx._transports',
    'httpx._transports.default',
    'pydantic',
    'pydantic.json',
    'pandas',
    'webview',
    'webview.platforms',
]

# Add platform-specific hidden imports
if is_macos:
    hiddenimports += [
        'webview.platforms.cocoa',
        'Foundation',
        'WebKit',
        'AppKit',
    ]
elif is_windows:
    hiddenimports += [
        'webview.platforms.winforms',
        'webview.platforms.cef',
        'webview.platforms.edgechromium',
    ]
elif is_linux:
    hiddenimports += [
        'webview.platforms.gtk',
    ]

a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',  # Exclude unused heavy dependencies
        'scipy',
        'IPython',
        'jupyter',
        'notebook',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BalanzTracker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window on Windows
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # TODO: Add icon file path
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BalanzTracker',
)

# macOS .app bundle
if is_macos:
    app = BUNDLE(
        coll,
        name='BalanzTracker.app',
        icon=None,  # TODO: Add icon file path
        bundle_identifier='com.balanz.portfoliotracker',
        info_plist={
            'CFBundleName': 'Balanz Portfolio Tracker',
            'CFBundleDisplayName': 'Balanz Portfolio Tracker',
            'CFBundleVersion': '1.0.0',
            'CFBundleShortVersionString': '1.0.0',
            'NSHighResolutionCapable': True,
            'LSMinimumSystemVersion': '10.13.0',
            'NSRequiresAquaSystemAppearance': False,
        },
    )
