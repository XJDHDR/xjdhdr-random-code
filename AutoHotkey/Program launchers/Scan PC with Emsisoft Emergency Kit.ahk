; Recommended settings for performance
#NoEnv
ListLines, Off
DetectHiddenWindows, On


UrlDownloadToFile, http://dl.emsisoft.com/EmsisoftEmergencyKit.exe , %A_Temp%\EmsisoftEmergencyKit.exe
IfNotExist, %A_Temp%\EmsisoftEmergencyKit.exe
	RunWait, PowerShell "Invoke-WebRequest -OutFile $Env:Temp\EmsisoftEmergencyKit.exe http://dl.emsisoft.com/EmsisoftEmergencyKit.exe", , Hide,

FileRemoveDir, %ProgramFiles%\Emsisoft Emergency Kit, 1
Run, %Comspec% /c start /low /min "Downloaded Emsisoft archive extraction" "%ProgramFiles%\7-Zip\7z.exe" x "%A_Temp%\EmsisoftEmergencyKit.exe" -y -aoa -o"%ProgramFiles%\Emsisoft Emergency Kit\", , Hide, 
WinWait, ahk_exe 7z.exe,
Process, Priority, 7z.exe, L
WinWaitClose, ahk_exe 7z.exe, 
FileDelete, %A_Temp%\EmsisoftEmergencyKit.exe

RunWait, "%ProgramFiles%\Emsisoft Emergency Kit\bin64\a2cmd.exe" /update, , Hide, 
RunWait, "%ProgramFiles%\Emsisoft Emergency Kit\bin64\a2cmd.exe" /update, , Hide, 

RunWait, %Comspec% /c start /low /min "Emsisoft weekly scan" "%ProgramFiles%\Emsisoft Emergency Kit\bin64\a2cmd.exe" /deep /rk /m /t /a /n /ac /dda /log="%A_Desktop%\EmsisoftScan.txt" /q="%ProgramFiles%\Emsisoft Emergency Kit\Quarantine", %ProgramFiles%\Emsisoft Emergency Kit, Min UseErrorLevel, 

ExitApp, %A_LastError%
