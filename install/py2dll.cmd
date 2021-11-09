call env.cmd

del "cpuwolf\*.pyd"
del "cpuwolf\*.c"


del "cpuwolfapp\*.pyd"
del "cpuwolfapp\*.c"

python.exe setup.py build_ext --inplace


pause