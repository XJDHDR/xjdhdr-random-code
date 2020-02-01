; Recommended settings for performance
#NoEnv
ListLines, Off

RunWait, Dism.exe /online /Cleanup-Image /StartComponentCleanup, , Hide UseErrorLevel, 

RunWait, Cleanmgr.exe /Sagerun:1, , Hide UseErrorLevel, 
ExitApp, %A_LastError%
