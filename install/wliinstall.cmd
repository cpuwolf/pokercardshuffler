call env.cmd


rmdir /s /q dist

::pause

python.exe -m PyInstaller  --version-file=file_version_info.txt --windowed --onefile --clean --noconfirm wliray.spec

pause

::"C:\Program Files (x86)\NSIS\makensisw.exe" nsis\winloginspect.nsi