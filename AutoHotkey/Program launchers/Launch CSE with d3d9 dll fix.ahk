#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
;ListLines, Off

If FileExist(A_ScriptDir . "\d3d9.dll")
	FileMove, %A_ScriptDir%\d3d9.dll, %A_ScriptDir%\d3d9-NoLoad.dll,

Try
{
	Run, *RunAs "%A_ScriptDir%\obse_loader - CSE.exe" -editor -notimeout,
}

WinWait , %A_ScriptDir%\TESConstructionSet.exe, , 60,
WinWaitClose, %A_ScriptDir%\TESConstructionSet.exe,

If FileExist(A_ScriptDir . "\d3d9-NoLoad.dll")
	FileMove, %A_ScriptDir%\d3d9-NoLoad.dll, %A_ScriptDir%\d3d9.dll,
