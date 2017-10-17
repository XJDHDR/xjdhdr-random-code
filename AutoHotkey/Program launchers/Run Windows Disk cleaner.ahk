; Recommended settings for performance
#NoEnv
ListLines, Off


RunWait, Cleanmgr.exe /Sagerun:1, , Min UseErrorLevel, 
ExitApp, %A_LastError%
