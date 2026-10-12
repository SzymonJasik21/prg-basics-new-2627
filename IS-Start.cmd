@echo off
rem odtworzenie migawki
d:
cd d:\
rem start maszyny	
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" setextradata "Golden Image" "GUI/Fullscreen" "false"
 	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "Golden Image" --type gui
@echo on