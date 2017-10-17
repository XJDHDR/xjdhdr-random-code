; Recommended settings for performance
#NoEnv
ListLines, Off

Loop, jre-8u*.exe, 0, 0
	JREInstaller := A_LoopFileLongPath

RunWait, %JREInstaller% "INSTALLCFG=%A_WorkingDir%\Install_Parameters.cfg"

ExitApp
