; Recommended settings for performance
#NoEnv
ListLines, Off
#MaxThreads 2
SetKeyDelay, , 75,
SetTitleMatchMode, 3

#MaxThreadsPerHotkey 2
#IfWinActive, ahk_exe KillingFloor.exe, 
F11::
	Toggle := !Toggle
	While Toggle
	{
	; Put your custom code here
		Loop, 4
		{
			Send, {XButton2}
			Loop, 50
			{
				If (Toggle <> 1)
					Exit
				IfWinNotActive, ahk_exe KillingFloor.exe, 
					Exit
				Sleep, 100
			}
		}
		Send, {XButton2}
		Sleep, 400
		If (Toggle <> 1)
			Exit
		IfWinNotActive, ahk_exe KillingFloor.exe, 
			Exit
		Send, e 
		Sleep, 50
		If (Toggle <> 1)
			Exit
		IfWinNotActive, ahk_exe KillingFloor.exe, 
			Exit
		Click
		Sleep, 400
		Send, {Esc}, 
		Sleep, 50
		Send, d
		Loop, 38
		{
			If (Toggle <> 1)
				Exit
			IfWinNotActive, ahk_exe KillingFloor.exe, 
				Exit
			Sleep, 100
		}
	; End of custom code
	}
Return
