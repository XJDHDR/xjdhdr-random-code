; Recommended settings for performance
#NoEnv
ListLines, Off

#MaxThreads 2
SetKeyDelay, , 50,
SetTitleMatchMode, 3

#MaxThreadsPerHotkey 2
F11::
	Toggle := !Toggle
	While Toggle
	{
		Sleep, 100
		If (Toggle <> 1)
		{
			Counter := 0
			Exit
		}
		Counter += 1
		If Counter >= 25
		{
			Counter := 0
			; Put your custom code here
			Click
			; End of custom code
		}
	}
Return
