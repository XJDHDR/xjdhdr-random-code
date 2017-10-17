; Recommended settings for performance
#NoEnv
ListLines, Off

Gui, New, +AlwaysOnTop +Border -MaximizeBox -Resize -SysMenu, Game chooser
Gui, Add, Text, , Please select the game you are downloading the mod for
Gui, Add, Button, Default -Wrap gSkyrim, &Skyrim
Gui, Add, Button, -Wrap gFalloutNewVegas, Fallout &New Vegas
Gui, Add, Button, -Wrap gFallout3, Fallout &3
Gui, Add, Button, -Wrap gOblivion, &Oblivion 
Gui, Show, AutoSize Center, 

Return


Skyrim:
FalloutNewVegas:
Fallout3:
Oblivion:
Gui, Destroy
IniRead, MOLocation, %A_ScriptDir%\Mod Organizer install locations.ini, MO locations, %A_ThisLabel%, Nothing
If MOLocation = Nothing
{
	MsgBox, Error: MO install location could not be found. This is caused by either not placing "Mod Organizer install locations.ini" in the same folder as "Start Mod Organizer NMM downloader.exe" or by the INI file being damaged to the point of being unusable. Please fix the problem before trying another mod download.
	ExitApp
}
If (SubStr(MOLocation, 1, 13) = "%A_ScriptDir%") ; check if the first 13 characters are the literal text "%A_ScriptDir%"
    MOLocation := A_ScriptDir . SubStr(MOLocation, 14)
Run, %MOLocation%\nxmhandler.exe %1%
ExitApp
Return
