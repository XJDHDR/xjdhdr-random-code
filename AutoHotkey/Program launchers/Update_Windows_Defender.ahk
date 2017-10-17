; Recommended settings for performance
#NoEnv
ListLines, Off


RunWait, "%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate -MMPC, , Hide UseErrorLevel, 

ExitApp, %A_LastError%
