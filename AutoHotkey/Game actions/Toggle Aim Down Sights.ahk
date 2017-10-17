; Recommended settings for performance
#NoEnv
;ListLines, Off


#UseHook On  ; I need AutoHotKey to create a keyboard hook. JC2 blocks AHK's regular method of defining hotkeys.
#InstallMouseHook
#IfWinActive, ahk_exe metro2033.exe, 
RButton::
	ButtonDown := not ButtonDown
	If (ButtonDown) 
	{
		SendPlay {m down}
	}
	Else
	{
		SendPlay {m up}
	}
Return
