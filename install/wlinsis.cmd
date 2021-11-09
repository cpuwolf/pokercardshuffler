call env.cmd

pip.exe list
pipdeptree -fl
pynsist installer.cfg

popd
pause