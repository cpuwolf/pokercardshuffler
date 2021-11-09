# -*- mode: python -*-

block_cipher = None


a = Analysis(['pokercardshuffle.py'],
             pathex=['/Users/apple/code/pyff777wingflexfix'],
             binaries=[],
             datas=[('logo.ico','.'),('danger.ico','.')],
             hiddenimports=[],
             hookspath=['hooks3'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pokercardshuffle',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='logo.ico')
app = BUNDLE(exe,
             a.datas, 
             name='pokercardshuffle.app',
             icon='logo.icns')
