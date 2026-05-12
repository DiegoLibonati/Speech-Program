# -*- mode: python ; coding: utf-8 -*-

# WARNING: the `.env` file bundled below is copied verbatim into the final
# executable. The development `.env` (with ENVIRONMENT=development and any
# local credentials) MUST NOT be shipped to end users. Before building for
# production, replace the repo-level `.env` with a dedicated production file
# (e.g. copy `build/.env.prod` over `.env`) or change the `datas` entry to
# point at a separate production env file. Never commit production secrets.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
