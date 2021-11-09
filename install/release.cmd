set MYROOT=%~dp0..\
cd %MYROOT%dist
::for /d %%f in ("*UTC") do 
robocopy "." "\\ORSDRM02.amr.corp.intel.com\public_wideopen\WinLogInspect" *install.exe /e
::robocopy "." "\\VMSPFSFSSH11.ccr.corp.intel.com\TMSIsharedriver\02_Windowssharing\WinLogInspect" *install.exe /e
robocopy "." "\\tsiewin1.amr.corp.intel.com\WWAN\WinLogInspect" *install.exe /e
pause