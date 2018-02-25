; Recommended settings for performance
#NoEnv
#SingleInstance force
;ListLines, Off


SetTitleMatchMode, RegEx
AddWindowsToGroup()
StartOfScript:
	WinWait, ahk_group MakeBorderlessList, 
	MakeBorderless()
Goto, StartOfScript


MakeBorderless()
{
	WinSet, Style, -0xC40000,
	WinMove, , , 0, 0, A_ScreenWidth, A_ScreenHeight
	DllCall("SetMenu", "Ptr", WinExist(), "Ptr", 0)
	;Hide Windows Task Bar and Start Button. (Remove the following two lines if you don't want that behaviour)
	;WinHide ahk_class Shell_TrayWnd
	;WinHide Start ahk_class Button
	
	WinWaitClose,
}

AddWindowsToGroup()
{
	; Add a GroupAdd line for each game you want to detect and make borderless
;	GroupAdd, MakeBorderlessList, ahk_exe armoredwarfare.exe$, 
	GroupAdd, MakeBorderlessList, ^Caesar III$ ahk_class ^WinSJBClass$ ahk_exe c3.exe$, 
	GroupAdd, MakeBorderlessList, ^Emperor: Rise of the Middle Kingdom$ ahk_class ^WinSJBClass$ ahk_exe Emperor.exe$,
	GroupAdd, MakeBorderlessList, ahk_exe hl2.exe$, 
	GroupAdd, MakeBorderlessList, ahk_exe mb_wfas.exe$, 
	GroupAdd, MakeBorderlessList, ^Pharaoh ahk_class WinSJBClass$ ahk_exe Pharaoh.exe$, 
	GroupAdd, MakeBorderlessList, ahk_exe rage.exe$, 
	GroupAdd, MakeBorderlessList, ahk_exe rage64.exe$, 
	GroupAdd, MakeBorderlessList, ahk_exe WorldOfTanks.exe$, 
	GroupAdd, MakeBorderlessList, ^Zeus ahk_class ^WinSJBClass$ ahk_exe Zeus.exe$,
}

; Don't add the following games:
; SpecOpsTheLine.exe - Game either crashes or doesn't go borderless.
