; Recommended settings for performance
#NoEnv
ListLines, Off

UpKey = w
DownKey = s
SpeedUpKey = Space

#MaxThreads 2
#MaxThreadsPerHotkey 2
#IfWinActive, ahk_exe VisualBoyAdvance-M.exe, 
F11::
	Toggle := !Toggle
	Send, {%SpeedUpKey% down}
	While Toggle
	{
	; Put your custom code here
		If (Toggle <> 1)
		{
			SetKeyDelay, , 40,
			Send, {%SpeedUpKey% up}
			Send, {%SpeedUpKey%}
			Send, {%SpeedUpKey%}
			Exit
		}
		
		SetKeyDelay, , 1,

		IfWinNotActive, ahk_exe VisualBoyAdvance-M.exe, 
			WinActivate,  ahk_exe VisualBoyAdvance-M.exe, 
		Send, {%DownKey% 2}
	
		If (Toggle <> 1)
		{
			SetKeyDelay, , 40,
			Send, {%SpeedUpKey% up}
			Send, {%SpeedUpKey%}
			Send, {%SpeedUpKey%}
			Exit
		}

		Sleep, 20

		If (Toggle <> 1)
		{
			SetKeyDelay, , 40,
			Send, {%SpeedUpKey% up}
			Send, {%SpeedUpKey%}
			Send, {%SpeedUpKey%}
			Exit
		}
		
		IfWinNotActive, ahk_exe VisualBoyAdvance-M.exe, 
			WinActivate,  ahk_exe VisualBoyAdvance-M.exe, 
		Send, {%UpKey% 2}
	
		If (Toggle <> 1)
		{
			SetKeyDelay, , 40,
			Send, {%SpeedUpKey% up}
			Send, {%SpeedUpKey%}
			Send, {%SpeedUpKey%}
			Exit
		}

		Sleep, 20
	; End of custom code
	}
Return
