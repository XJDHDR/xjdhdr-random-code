; Recommended settings for performance
#NoEnv
ListLines, Off


RunWait, "%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate -MMPC, , Hide, 

Run, %Comspec% /c start /low /min "Windows Defender weekly scan" "%A_ScriptDir%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 2, , Hide UseErrorLevel,

DetectHiddenWindows, On
WinWait, ahk_exe MpCmdRun.exe,
Process, Priority, MpCmdRun.exe, L
WinWaitClose, ahk_exe MpCmdRun.exe, 

ExitApp, %A_LastError%
