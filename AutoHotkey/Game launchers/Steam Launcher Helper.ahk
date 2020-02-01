; Recommended settings for performance
#NoEnv
#SingleInstance Ignore

ListLines, Off
DetectHiddenWindows, On
SetTitleMatchMode, 2

; Retrieves launcher/client path from .ini or ask user to point them
IniRead, sGameLauncher, %A_ScriptDir%\SteamOverlayHelper.ini, General, Launcher,
If (sGameLauncher = "ERROR")
{
	MsgBox, Please select the location of the game's launcher.
	Try FileSelectFile, sSelectedFile, 3, %A_ScriptDir%\, Please select the location of the game's launcher, Executables (*.exe)
	Catch
		ExitApp
	IniWrite, %sSelectedFile%, %A_ScriptDir%\SteamOverlayHelper.ini, General, Launcher
	IniRead, sGameLauncher, %A_ScriptDir%\SteamOverlayHelper.ini, General, Launcher,
}

IniRead, sGameClient, %A_ScriptDir%\SteamOverlayHelper.ini, General, Client,
If (sGameClient = "ERROR")
{
	MsgBox, Please select the location of the game's Client.
	Try FileSelectFile, sSelectedFile, 3, %A_ScriptDir%\, Please select the location of the game's Client, Executables (*.exe)
	Catch
		ExitApp
	IniWrite, %sSelectedFile%, %A_ScriptDir%\SteamOverlayHelper.ini, General, Client
	IniRead, sGameClient, %A_ScriptDir%\SteamOverlayHelper.ini, General, Client,
}

IniRead, sDefaultPostGameExitLauncherDetectionBehaviour, %A_ScriptDir%\SteamOverlayHelper.ini, Post game exit behaviour, Launcher Treatment,
If (sDefaultPostGameExitLauncherDetectionBehaviour = "ERROR")
{
	InputBoxPrompt:
	Try InputBox, sInputBoxInput, Select default post game exit behaviour, Please define the default behaviour for what happens after you exit the game and the Steam Overlay Helper program detects that the game's launcher is still running by typing in exactly one of the following words (and nothing else):`n`nAsk - This option will ask you what to do every time`nReveal - This option will unminimise the launcher's window and activate it`nIgnore - This option will leave the launcher the way it is and not attempt to do anything to it`nClose - This option will close the launcher`n`nNote: You can change this option at a later date by editing "SteamOverlayHelper.ini", , 530, 370, , , , , Reveal
	Catch
		ExitApp
	If ( sInputBoxInput != "Ask" ) And ( sInputBoxInput != "Reveal" ) And ( sInputBoxInput != "Ignore" ) And ( sInputBoxInput != "Close" )
	{
		MsgBox, 49, Invalid input, You did not type a valid option into the text box. Please try again.,
		IfMsgBox, Cancel
			ExitApp
		Goto, InputBoxPrompt
	}
	Else
	{
		IniWrite, %sInputBoxInput%, %A_ScriptDir%\SteamOverlayHelper.ini, Post game exit behaviour, Launcher Treatment
		IniRead, sDefaultPostGameExitLauncherDetectionBehaviour, %A_ScriptDir%\SteamOverlayHelper.ini, Post game exit behaviour, Launcher Treatment,
	}
}


; Grab Game and Launcher EXE names from their paths
SplitPath, sGameLauncher, sLauncherName, 
SplitPath, sGameClient, sClientName, 


; Here comes the script
OutputDebug, [1/5] starting laucher
Process, Exist, %sLauncherName%,
iDetectedPID := ErrorLevel
If iDetectedPID > 0
	ExitApp
	
Run, %sGameLauncher%,

ClientDetectionScriptStart:
OutputDebug, [2/5] waiting for launcher to start game...
iLauncherClosedStrikes := 0
Loop
{
	For objGameInstance In ComObjGet("winmgmts:").ExecQuery("Select * from Win32_Process where Name='" sClientName "'")
		Break, 2
	Sleep, 1000
	If iLauncherClosedStrikes >= 3
		ExitApp
	Process, Exist, %sLauncherName%,
	iDetectedPID := ErrorLevel
	If iDetectedPID = 0
		iLauncherClosedStrikes += 1
}
OutputDebug, [3/5] game instance detected
iLauncherClosedStrikes := 0
sGameClientCommandLine := objGameInstance.CommandLine
OutputDebug, [4/5] killing game instance
Process, Close, %sClientName%

If FileExist(A_ScriptDir "\SteamOverlayHelper - Last Commandline Arguments used.txt")
	FileDelete, %A_ScriptDir%\SteamOverlayHelper - Last Commandline Arguments used.txt
FileAppend, %sGameClientCommandLine%, %A_ScriptDir%\SteamOverlayHelper - Last Commandline Arguments used.txt,

OutputDebug, [5/5] starting game again
iLengthGameClientPath := StrLen(sGameClient) + 4
sGameClientCommandLine := SubStr(sGameClientCommandLine, iLengthGameClientPath)
OutputDebug, %sGameClientCommandLine%

RunWait, "%sGameClient%" %sGameClientCommandLine%, 

Sleep, 3000
Process, Exist, %sLauncherName%,
iDetectedPID := ErrorLevel
If ( iDetectedPID > 0 ) And ( sDefaultPostGameExitLauncherDetectionBehaviour == "Ask" )
{
	MsgBox, 35, Launcher still running, The launcher for the Steam game you just exited is still running. Would you like to unminimise the launcher?`n`nYes - Unminimise and activate the launcher's window`nNo - Leave the launcher's window the way it is currently`nCancel - Close the launcher,
	IfMsgBox, Yes
	{
		WinRestore , ahk_exe %sLauncherName%,
	}
	IfMsgBox, Cancel
	{
		Process, Close, %sLauncherName%,
		ExitApp
	}
	
	Goto, ClientDetectionScriptStart
}
Else If ( iDetectedPID > 0 ) And ( sDefaultPostGameExitLauncherDetectionBehaviour == "Reveal" )
{
	WinRestore , ahk_exe %sLauncherName%,
	Goto, ClientDetectionScriptStart
}
Else If ( iDetectedPID > 0 ) And ( sDefaultPostGameExitLauncherDetectionBehaviour == "Close" )
{
	Process, Close, %sLauncherName%,
}


ExitApp
