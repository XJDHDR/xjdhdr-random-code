; Recommended settings for performance
#NoEnv
;ListLines, Off

Gui, New, +AlwaysOnTop +Border -MaximizeBox -Resize -SysMenu, Game chooser
Gui, Add, Text, , Please select the program and game you are downloading the mod for
iNoCount += funcAddButton("Fallout 4", "gFallout4", "Mod Organizer: Fallout &4")
iNoCount += funcAddButton("Skyrim SE", "gSkyrimSE", "Mod Organizer: &Skyrim Special &Edition")
iNoCount += funcAddButton("Skyrim", "gSkyrim", "Mod Organizer: Skyrim")
iNoCount += funcAddButton("Fallout New Vegas", "gFalloutNewVegas", "Mod Organizer: Fallout &New Vegas")
iNoCount += funcAddButton("Fallout 3", "gFallout3", "Mod Organizer: Fallout &3")
iNoCount += funcAddButton("Oblivion", "gOblivion", "Mod Organizer: &Oblivion")
iNoCount += funcAddButton("Morrowind", "gMorrowind", "Mod Organizer: &Morrowind")
iNoCount += funcAddButton("Vortex", "gVortex", "&Vortex")
iNoCount += funcAddButton("NMM", "gNMM", "&Nexus Mod Manager")
iNoCount += funcAddButton("Custom 1", "gCustom1", "Unused")
iNoCount += funcAddButton("Custom 2", "gCustom2", "Unused")
iNoCount += funcAddButton("Custom 3", "gCustom3", "Unused")
iNoCount += funcAddButton("Custom 4", "gCustom4", "Unused")
If (iNoCount < 13)
	Gui, Show, AutoSize Center, 
Else
{
	MsgBox, No buttons were created. You need to set at least one of the "Activate Option" parameters in "Mod Manager install locations.ini" to "Yes" for this program to work.
	ExitApp
}
Return


Fallout4:
SkyrimSE:
Skyrim:
FalloutNewVegas:
Fallout3:
Oblivion:
Morrowind:
Vortex:
NMM:
Gui, Destroy
IniRead, sManagerLocation, %A_ScriptDir%\Mod Manager install locations.ini, Mod Manager locations, %A_ThisLabel%, Nothing
If (sManagerLocation = "Nothing")
{
	MsgBox, Error: Selected Mod Manager's install location could not be read from INI. This is caused by either not placing "Mod Manager install locations.ini" in the same folder as "Multiple Mod Managers for 'Mod Manager Download' button.exe" or by the INI file being damaged, corrupt or not set up correctly. Please fix the problem before trying another mod download.
	ExitApp
}
If (SubStr(sManagerLocation, 1, 13) = "%A_ScriptDir%") ; check if the first 13 characters are the literal text "%A_ScriptDir%"
    sManagerLocation := A_ScriptDir . SubStr(sManagerLocation, 14)
If (A_ThisLabel = "Vortex")
{
	If (FileExist(sManagerLocation . "\Vortex.exe") <> "")
		Run, "%sManagerLocation%\Vortex.exe"  -d "%1%",
	Else
		MsgBox, Vortex was not found. Please ensure you specified the correct location in the INI file.
}
Else If (A_ThisLabel = "NMM")
{
	If (FileExist(sManagerLocation . "\NexusClient.exe") <> "")
		Run, "%sManagerLocation%\NexusClient.exe" "%1%",
	Else
		MsgBox, Nexus Mod Manager was not found. Please ensure you specified the correct location in the INI file.
}
Else
{
	If (FileExist(sManagerLocation . "\nxmhandler.exe") <> "")
	{
;		Run, "%sManagerLocation%\nxmhandler.exe" "%1%",
		Run, "%sManagerLocation%\ModOrganizer.exe" "%1%",
;		FileAppend, "%sManagerLocation%\nxmhandler.exe" %1%, %A_ScriptDir%\passed command.txt,
;		Pause
	}
	Else
		MsgBox, Mod Organizer was not found. Please ensure you specified the correct location in the INI file.
}
ExitApp
Return


Custom1:
Custom2:
Custom3:
Custom4:
Gui, Destroy
IniRead, sManagerLocation, %A_ScriptDir%\Mod Manager install locations.ini, %A_ThisLabel%, Mod Manager location, Nothing
If (sManagerLocation = "Nothing")
{
	MsgBox, Error: Selected Mod Manager's install location could not be read from INI. This is caused by either not placing "Mod Manager install locations.ini" in the same folder as "Multiple Mod Managers for 'Mod Manager Download' button.exe" or by the INI file being damaged, corrupt or not set up correctly. Please fix the problem before trying another mod download.
	ExitApp
}
IniRead, sProgramToRun, %A_ScriptDir%\Mod Manager install locations.ini, %A_ThisLabel%, Program to run, Nothing
If (sProgramToRun = "Nothing")
{
	MsgBox, Error: Selected Mod Manager's program to run could not be read from INI. This is caused by either not placing "Mod Manager install locations.ini" in the same folder as "Multiple Mod Managers for 'Mod Manager Download' button.exe" or by the INI file being damaged, corrupt or not set up correctly. Please fix the problem before trying another mod download.
	ExitApp
}
IniRead, sProgramArguments, %A_ScriptDir%\Mod Manager install locations.ini, %A_ThisLabel%, Command Line Arguments, Nothing
If (sProgramArguments = "Nothing")
{
	MsgBox, Error: Selected Mod Manager's program to run could not be read from INI. This is caused by either not placing "Mod Manager install locations.ini" in the same folder as "Multiple Mod Managers for 'Mod Manager Download' button.exe" or by the INI file being damaged, corrupt or not set up correctly. Please fix the problem before trying another mod download.
	ExitApp
}
If (FileExist(sManagerLocation . "\" . sProgramToRun) <> "")
	Run, %sManagerLocation%\%sProgramToRun% %sProgramArguments%,
Else
	MsgBox, The custom mod manager specified was not found. Please ensure you specified the correct location in the INI file.
ExitApp
Return


funcAddButton(sParameterName, sLabelName, sButtonText)
{
	IniRead, sOptionActivated, %A_ScriptDir%\Mod Manager install locations.ini, Activate Option, %sParameterName%, Nothing
	If (sOptionActivated <> "No") && (sOptionActivated <> "Yes")
	{
		MsgBox, The INI file parameter "Activate Option\%sParameterName%" is not set to a valid option. Please change this parameter to either "Yes" or "No" (without quotation marks). This program will now exit without proceeding further.
		ExitApp
	}
	Else If (sOptionActivated = "Yes")
	{
		If (sParameterName = "Custom 1") || (sParameterName = "Custom 2") || (sParameterName = "Custom 3") || (sParameterName = "Custom 4")
			IniRead, sButtonText, %A_ScriptDir%\Mod Manager install locations.ini, %sParameterName%, Button Name, Invalid Custom Button Name
		Gui, Add, Button, -Wrap %sLabelName%, %sButtonText%
		Return, 0
	}
	Return, 1
}