CoordMode, Mouse, Client

Loop
{
	WinActivate, ARMORED WARFARE - aw.my.com - Mozilla Firefox ahk_class MozillaWindowClass ahk_exe firefox.exe,
	Send {f5}
	Sleep, 15000	; 15 seconds
	BlockInput, On
	Send {Home}
	Send {Down}
	Send {PgDn}
	MouseMove, 406, 650 , 3,
	Click, 406, 650
	Sleep, 6000
;	MouseMove, 1230, 1056 , 3,
;	Click, 1230, 1056
	BlockInput, Off
	Sleep, 1200000	; 20 minutes
}