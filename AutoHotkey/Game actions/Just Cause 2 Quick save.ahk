; Recommended settings for performance
#NoEnv
ListLines, Off

; Any text to the right of a semicolon (;) is a comment and is ignored by AutoHotKey
; Modify essential settings

; This script allows you to quickly save your game in slot #10 by pressing F5. 
; It also allows you to quickly save your game then exit by pressing F11.
; The script also closes itself after you exit the game.
; It also features crash detection where if you exit the game or it crashes and you restart it within 60 seconds, you won't have to reload the script.

SetKeyDelay, , 100,
SetTitleMatchMode, 3
CoordMode, Mouse, Client
JC2StartProcedure:	; Create a label to jump here if Just Cause 2 is run again within 60 seconds
WinWaitActive, ahk_exe JustCause2.exe, ; Wait for JC2 to be started
WinWaitClose, ahk_exe JustCause2.exe, ; Wait for JC2 to exit or crash
Loop {
	LoopStart:
	Sleep, 5000 ; Wait for 5 seconds
	If (TimeWaited > 60)
		ExitApp ; If I've waited for 60 seconds in total, stop the script from running.
	Else
	{
		IfWinActive, ahk_exe JustCause2.exe, ; Otherwise, check if JC2 was opened again in the last 5 seconds.
		{
			TimeWaited = 0 ; It was. Reset the 60 second timer and jump back to the beginning of the script.
			Goto, JC2StartProcedure
		}
		Else
		{
			TimeWaited += 5 ; It wasn't. Let's wait for another 5 seconds.
			Goto, LoopStart
		}
	}
}
ExitApp


SaveGame:
Send, {Esc}  ; Open the main menu.
MouseGetPos, OriginalMouseX, OriginalMouseY, ; Get the mouse cursor's current position.
Sleep, 600
; The following commands are used to calculate the game's resolution settings and whether or not it is fullscreen.
; They are placed in the hotkey subroutine to detect changes caused by the player changing the resolution settings ingame.
WinGet, JC2MinMax, MinMax, ahk_exe JustCause2.exe  ; Get the maximized state of JC2's window
WinGetPos, JC2PosX, JC2PosY, JC2WinWidth, JC2WinHeight, ahk_exe JustCause2.exe,  ; Get it's position and dimensions
WindowedFactor := 0  ; Assume it is windowed until proven otherwise
if (JC2MinMax = 0) && (JC2PosX = 0) && (JC2PosY = 0) && (JC2WinWidth = A_ScreenWidth) && (JC2WinHeight = A_ScreenHeight)  ; Test if JC2 is fullscreen and adjust WindowedFactor accordingly
{
	WindowedFactor := 2
}
PositionMouseX := Round(JC2WinWidth / 423 * 110) ; Do some maths to calculate where "Save Game" option's X-coordinate is.
If WindowedFactor = 0
	PositionMouseY := Round(JC2WinHeight / 143 * 53) ; Do some maths to calculate where "Save Game" option's Y-coordinate is (fullscreen state).
Else
	PositionMouseY := Round(JC2WinHeight / 143 * 55) ; Do some maths to calculate where "Save Game" option's Y-coordinate is (windowed state).
MouseMove, %PositionMouseX%, %PositionMouseY%, 5, ; Move mouse cursor to "Save Game" option
Send, {Enter} ; Open the Save Game menu
Sleep, 300
Send, {Up} ; Select the 10th save slot
Sleep, 25
Send, {Enter} ; Overwrite the 10th save slot.
Sleep, 25
Send, {Up} ; Select Yes to confirm overwrite.
Sleep, 25
Send, {Enter} ; Accept my choice to overwrite the save game.
MouseMove, %OriginalMouseX%, %OriginalMouseY%, ; Move the mouse cursor back to it's original position.
Sleep, 7000 ; Wait 7 seconds for the game to finish saving.
Return


#UseHook On  ; I need AutoHotKey to create a keyboard hook. JC2 blocks AHK's regular method of defining hotkeys.
#IfWinActive,  ahk_exe JustCause2.exe, ; Only hook F5 if the player has JC2 open and maximized.
F5::
Gosub, SaveGame
Send, {Esc} ; Go back to the main menu.
Sleep, 25
Send, {Esc} ; Exit the main menu.
Return

F11::
Gosub, SaveGame
Send, {Esc} ; Go back to the main menu.
Sleep, 25
Send, {Up 2} ; Select the "Exit Game" option.
Sleep, 25
Send, {Enter} ; Activate the "Exit Game" option.
Sleep, 25
Send, {Up} ; Select the "Yes" option.
Sleep, 25
Send, {Enter} ; Activate the "Yes" option.
ExitApp
Return
