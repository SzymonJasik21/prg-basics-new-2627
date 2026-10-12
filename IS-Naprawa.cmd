@echo off
rem Odtworzenie maszyny od zera
d:
cd d:\
rem echo %time:~0,8%
	attrib -S -R c:\drivers\IS.ova
	del /F /Q c:\drivers\IS.ova
rem kopiowanie pliku
	echo.
	echo.
	echo Czekaj, trwa kopiowanie maszyny wirtualnej!
	robocopy \\10.10.0.4\Install\Laboratoria\LabCSI\Janusz c:\drivers "IS.ova" /is /njh /njs /ndl /z /r:10 /w:5
rem 	wolniejsze: powershell Start-BitsTransfer -Source "\\10.10.0.4\Install\Laboratoria\LabCSI\Janusz\IS.ova" -Destination "c:\drivers\IS.ova"	
rem 	xcopy \\10.10.0.4\Install\Laboratoria\LabCSI\Janusz\IS.ova c:\drivers\IS.ova* /h /r /y /q

	attrib +S +R c:\drivers\IS.ova

rem Wylaczenie maszyny
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" controlvm "Golden Image" poweroff > nul

rem skasowanie maszyny
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" unregistervm "Golden Image" --delete > nul
	rmdir /S /Q "d:\Golden Image"
rem import z ova
	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" import c:\drivers\IS.ova --vsys 0 --basefolder "D:\\" --unit 14 --disk "D:\Golden Image\Golden Image-disk001.vmdk" > nul

rem zrobienie migawki
 	"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" snapshot "Golden Image" take "start"
@echo on
