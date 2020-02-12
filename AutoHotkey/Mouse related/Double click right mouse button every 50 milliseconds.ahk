; Recommended settings for performance
#NoEnv
ListLines, Off

#MaxThreads 2
SetKeyDelay, , 500,
SetTitleMatchMode, 3

#MaxThreadsPerHotkey 2
F11::
	Toggle := !Toggle
	While Toggle
	{
		Sleep, 10
		If (Toggle <> 1)
		{
			Counter := 0
			Exit
		}
		Counter += 1
		If Counter >= 5
		{
			Counter := 0
			; Put your custom code here
;			SendInput, {RButton}
			DllCall("mouse_event", uint, 0x0008, int, 0 ,int, 0, uint, 0, int, 0)
			Sleep, 10
			DllCall("mouse_event", uint, 0x0010, int, 0 ,int, 0, uint, 0, int, 0)
			Sleep, 10
;			Send r
			DllCall("mouse_event", uint, 0x0008, int, 0 ,int, 0, uint, 0, int, 0)
			Sleep, 10
			DllCall("mouse_event", uint, 0x0010, int, 0 ,int, 0, uint, 0, int, 0)
			; End of custom code
		}
	}
Return
