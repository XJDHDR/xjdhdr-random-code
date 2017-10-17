; Recommended settings for performance
#NoEnv
ListLines, Off

; Uncomment the below command if AutoHotkey does not detect you pressing F10
;#InstallKeybdHook


F10::
	ButtonDown := not ButtonDown
	If (ButtonDown) 
	{
		SendInput {Click down}
	}
	Else
	{
		SendInput {Click up}
	}
Return
