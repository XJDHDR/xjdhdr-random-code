#SingleInstance Force
SetTitleMatchMode 2
ListLines, Off
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Global DayChange:=0	;If the day is changed, offset the time accordingly.
If Not (InStr(FileExist(PvE Rotation Tracker data), "D"))
	FileCreateDir, PvE Rotation Tracker data

IfNotExist, PvE Rotation Tracker data\Timing and Position data.ini
{
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Minutes
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Seconds
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Clock Format, Use 24 Hour Clock
	IniWrite, 3, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Minutes
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Seconds
}
Global OffsetMinVar := 0
IniRead, OffsetMinVar, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Minutes,		;Controls how many minutes the time is offset
If (OffsetMinVar = ERROR)
{
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Minutes
	OffsetMinVar := 0
}
Global OffsetSecVar := 0
IniRead, OffsetSecVar, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Seconds,		;Controls how many seconds the time is offset
If (OffsetSecVar = ERROR)
{
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Seconds
	OffsetSecVar := 0
}
Global Use24HourClock := 0
IniRead, Use24HourClock, PvE Rotation Tracker data\Timing and Position data.ini, Clock Format, Use 24 Hour Clock,	;Controls whether a 12 or 24 hour clock is used
If (Use24HourClock = ERROR)
{
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Clock Format, Use 24 Hour Clock
	Use24HourClock := 0
}
Global iContractLengthMinutes := 0
IniRead, iContractLengthMinutes, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Minutes,	;Defines how many minutes a contract is available for
If (iContractLengthMinutes = ERROR)
{
	IniWrite, 3, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Minutes
	iContractLengthMinutes := 3
}
Global iContractLengthSeconds := 0
IniRead, iContractLengthSeconds, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Seconds,	;Controls whether a 12 or 24 hour clock is used
If (iContractLengthSeconds = ERROR)
{
	IniWrite, 0, PvE Rotation Tracker data\Timing and Position data.ini, Contract Length, Seconds
	iContractLengthSeconds := 0
}



IniRead, TempDayVar, PvE Rotation Tracker data\Timing and Position data.ini, Date, Date, 0
If (TempDayVar = 0)
{
	IniWrite, %A_YYYY%%A_MM%%A_DD%, PvE Rotation Tracker data\Timing and Position data.ini, Date, Date
	TempDayVar = %A_YYYY%%A_MM%%A_DD%
}
If(A_YYYYA_MMA_DD != TempDayVar)
	DayChange := 1

IfNotExist, PvE Rotation Tracker data\Mission Ratings.ini
{
	IniWrite, Perseus, 			PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, 1
	IniWrite, Rolling Thunder, 	PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, 2
	IniWrite, Stormy Winter, 	PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, 3
	IniWrite, Kodiak, 			PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, 4
	IniWrite, Albatross, 		PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, 5
	
	IniWrite, Ghost Hunter, 	PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 1
	IniWrite, Meltdown, 		PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 2
	IniWrite, Banshee, 			PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 3
	IniWrite, Wildfire, 		PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 4
	IniWrite, Tsunami, 			PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 5
	IniWrite, Life Jacket, 		PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, 6
	
	IniWrite, Cerberus, 		PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 1
	IniWrite, Frostbite, 		PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 2
	IniWrite, Quarterback, 		PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 3
	IniWrite, Leviathan, 		PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 4
	IniWrite, Harbinger, 		PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 5
	IniWrite, Hydra, 			PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, 6
	
	IniWrite, Anvil, 			PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, 1
	IniWrite, Umbrella, 		PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, 2
	IniWrite, Cavalry, 			PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, 3
	IniWrite, Spearhead, 		PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, 4
	IniWrite, Zero Hour, 		PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, 5
}
ExcellentMissions =
GoodMissions =
BadMissions =
TerribleMissions =
Loop
{
	IniRead, TempVar, PvE Rotation Tracker data\Mission Ratings.ini, Excellent Missions, %A_Index%, 0
	If TempVar = 0
	{
		StringTrimLeft, ExcellentMissions, ExcellentMissions, 1
		Break
	}
	ExcellentMissions = %ExcellentMissions%`,%TempVar%
}
Loop
{
	IniRead, TempVar, PvE Rotation Tracker data\Mission Ratings.ini, Good Missions, %A_Index%, 0
	If TempVar = 0
	{
		StringTrimLeft, GoodMissions, GoodMissions, 1
		Break
	}
	GoodMissions = %GoodMissions%`,%TempVar%
}
Loop
{
	IniRead, TempVar, PvE Rotation Tracker data\Mission Ratings.ini, Bad Missions, %A_Index%, 0
	If TempVar = 0
	{
		StringTrimLeft, BadMissions, BadMissions, 1
		Break
	}
	BadMissions = %BadMissions%,%TempVar%
}
Loop
{
	IniRead, TempVar, PvE Rotation Tracker data\Mission Ratings.ini, Terrible Missions, %A_Index%, 0
	If TempVar = 0
	{
		StringTrimLeft, TerribleMissions, TerribleMissions, 1
		Break
	}
	TerribleMissions = %TerribleMissions%,%TempVar%
}

MissionList=
IfNotExist, PvE Rotation Tracker data\Missions List.txt	
{
	FileAppend,Albatross(*)`nAnvil(*)`nBanshee`nBasilisk`nCavalry(*)`nCerberus(*)`nDire Wolf, PvE Rotation Tracker data\Missions List.txt
	FileAppend,`nErebos`nFrostbite(*)`nGhost Hunter`nHarbinger`nHydra(`+)`nKodiak, PvE Rotation Tracker data\Missions List.txt
	FileAppend,`nLeviathan`nLife Jacket`nMeltdown`nOnyx`nPerseus(`+)`nPhalanx(*), PvE Rotation Tracker data\Missions List.txt
	FileAppend,`nPrometheus`nQuarterback(*)`nRaiding Party(*)`nRed Opossum`nRicochet`nRolling Thunder, PvE Rotation Tracker data\Missions List.txt
	FileAppend,`nSapphire(*)`nScorpio(`+)`nSnake Bite(`+)`nSpearhead`nStarry Night(`+), PvE Rotation Tracker data\Missions List.txt
	FileAppend,`nStormy Winter`nTiger Claw`nTsunami`nUmbrella(`+)`nWatchdog`nWildfire(`+)`nZero Hour(*), PvE Rotation Tracker data\Missions List.txt
}
Loop, Read, PvE Rotation Tracker data\Missions List.txt	;Missions List.txt contains a list of all missions separated by newlines
	MissionList=%MissionList%%A_LoopReadLine%|

Gui, Font, s12
yVar:=4
newTime := A_Hour * 60 + A_Min - OffsetMinVar + DayChange * 40 + 150
Transform, rVar, Mod, %newTime%, 50
CalcVar =
CalcVar += -%rVar%, minutes
Loop 10 {
	Gui, Add, DropDownList, x5 y%yVar% w180 gSaveList vMH%A_Index%, %MissionList%
	Gui, Add, Progress, 	x190 y%yVar% w20 cGray vProgH%A_Index%
	GuiControl, , ProgH%A_Index%, 100
	IniRead, TempVar, PvE Rotation Tracker data\Saved Mission Settings.ini, Hard, %A_Index%, %A_Space%
	GuiControl, ChooseString, MH%A_Index%, %TempVar%
	Difficulty = H
	Gosub, ChangeColour
	
	Gui, Add, DropDownList, x215 y%yVar% w180 gSaveList vMM%A_Index%, %MissionList%
	Gui, Add, Progress, 	x400 y%yVar% w20 cGray vProgM%A_Index%
	GuiControl,, ProgM%A_Index%, 100
	IniRead, TempVar, PvE Rotation Tracker data\Saved Mission Settings.ini, Medium, %A_Index%, %A_Space%
	GuiControl, ChooseString, MM%A_Index%, %TempVar%
	Difficulty = M
	Gosub, ChangeColour
	
	Gui, Add, DropDownList, x425 y%yVar% w180 gSaveList vME%A_Index%, %MissionList%
	Gui, Add, Progress, 	x610 y%yVar% w20 cGray vProgE%A_Index%
	GuiControl,, ProgE%A_Index%, 100
	IniRead, TempVar, PvE Rotation Tracker data\Saved Mission Settings.ini, Easy, %A_Index%, %A_Space%
	GuiControl, ChooseString, ME%A_Index%, %TempVar%
	Difficulty = E
	Gosub, ChangeColour
	
	yVar+=3
	Gui, Add, Text, x635 y%yVar% w200 vCD%A_Index%, 00:00
	yVar+=26
	TVar=
	Loop 14 {
		If (Use24HourClock = 0)
			FormatTime, SVar, %CalcVar%, hh:mm
		Else
			FormatTime, SVar, %CalcVar%, HH:mm
		TVar=%TVar%%A_Space%%A_Space%%A_Space%%SVar%
		CalcVar+=30, minutes
	}
	CalcVar+=-695, minutes
	Gui, Add, Text, vTimeLine%A_Index% x5 y%yVar%, %TVar%
	yVar+=25
}
yVar+=-4
Gui, Add, Edit, x5 y%yVar% w55 vMinBox Number, %OffsetMinVar%
Gui, Add, Edit, x63 y%yVar% w55 vSecBox Number, %OffsetSecVar%
yVar--
Gui, Add, Button, x120 y%yVar% w295 h30 gSetTimeOffset, Set Time Offset (Minutes/Seconds)
Gui, Add, Button, x425 y%yVar% w200 h30 gClearList, Clear All Missions
Gui, Add, Button, x630 y%yVar% w90 h30 gHelpButton, Help
IniRead, xPos, PvE Rotation Tracker data\Timing and Position data.ini, Position, X, 100
IniRead, yPos, PvE Rotation Tracker data\Timing and Position data.ini, Position, Y, 100
Gui, Show, W740 H570 X%xPos% Y%yPos%, PvE Rotation Tracker by Wiser Guy and XJDHDR
GoSub EverySecond
SetTimer EverySecond, 1000
TimeToMidnight := -1 * (86400000 - A_Hour * 3600000 - A_Min * 60000 - A_Sec * 1000 - A_MSec)
SetTimer MidnightFix, %TimeToMidnight%
return

EverySecond:
newTime := A_Hour * 3600 + A_Min * 60 + A_Sec - OffsetMinVar * 60 - OffsetSecVar + DayChange * 2400 + 9000
Loop 10 {
	newTime -= (iContractLengthMinutes * 60 + iContractLengthSeconds)
	Transform, rVar, Mod, %newTime%, 3000
	cVar:=3000-rVar
	if(cVar < 180){
		mVar:=AZ(floor(cVar/60))
		sVar:=AZ(mod(cVar,60))
		Gui, Font, cRed
		GuiControl, Text, CD%A_Index%, %mVar%:%sVar% - Active
		GuiControl, Font, CD%A_Index%
	}
	else{
		cVar -= (iContractLengthMinutes * 60 + iContractLengthSeconds)
		nextTime =
		nextTime += %cVar%, seconds
		If (Use24HourClock = 0)
			FormatTime, nextTime, %nextTime%, hh:mm
		Else
			FormatTime, nextTime, %nextTime%, HH:mm
		mVar:=AZ(floor(cVar/60))
		sVar:=AZ(mod(cVar,60))
		Gui, Font, cBlack
		GuiControl, Text, CD%A_Index%, %mVar%:%sVar% - %nextTime%
		GuiControl, Font, CD%A_Index%
	}
}
return

AZ(x){
	return SubStr( "0" x, -1)
}

SaveList:
	Loop 10 {
		GuiControlGet TempVar,, MH%A_Index%
		Difficulty = H
		Gosub, ChangeColour
		IniWrite, %TempVar%, PvE Rotation Tracker data\Saved Mission Settings.ini, Hard, %A_Index%
		
		GuiControlGet TempVar,, MM%A_Index%
		Difficulty = M
		Gosub, ChangeColour
		IniWrite, %TempVar%, PvE Rotation Tracker data\Saved Mission Settings.ini, Medium, %A_Index%
		
		GuiControlGet TempVar,, ME%A_Index%
		Difficulty = E
		Gosub, ChangeColour
		IniWrite, %TempVar%, PvE Rotation Tracker data\Saved Mission Settings.ini, Easy, %A_Index%
	}
return

Clearlist:
	Loop 10	{
		GuiControl, Choose, MH%A_Index%, 0
		GuiControl, +cGray, ProgH%A_Index%
		GuiControl, Choose, MM%A_Index%, 0
		GuiControl, +cGray, ProgM%A_Index%
		GuiControl, Choose, ME%A_Index%, 0
		GuiControl, +cGray, ProgE%A_Index%
	}
	IniWrite, %A_YYYY%%A_MM%%A_DD%, PvE Rotation Tracker data\Timing and Position data.ini, Date, Date
	GuiControlGet OffsetMinVar,, MinBox
	GuiControlGet OffsetSecVar,, SecBox
	DayChange:=0
return

SetTimeOffset:
	GuiControlGet OffsetMinVar,, MinBox
	GuiControlGet OffsetSecVar,, SecBox
	if(OffsetMinVar > 49)
	{
		Transform, OffsetMinVar, Mod, %OffsetMinVar%, 50
		GuiControl,,MinBox,%OffsetMinVar%
	}
	if(OffsetSecVar > 59)
	{
		Transform, OffsetSecVar, Mod, %OffsetSecVar%, 60
		GuiControl,,SecBox,%OffsetSecVar%
	}
	IniWrite, %OffsetMinVar%, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Minutes
	IniWrite, %OffsetSecVar%, PvE Rotation Tracker data\Timing and Position data.ini, Offset, Seconds

	newTime := A_Hour * 60 + A_Min - OffsetMinVar + DayChange * 40 + 150
	Transform, rVar, Mod, %newTime%, 50
	CalcVar =
	CalcVar += -%rVar%, minutes
	Loop 10	{
	TVar=
		Loop 14 {
			If (Use24HourClock = 0)
				FormatTime, SVar, %CalcVar%, hh:mm
			Else
				FormatTime, SVar, %CalcVar%, HH:mm
			TVar=%TVar%%A_Space%%A_Space%%A_Space%%SVar%
			CalcVar+=50, minutes
		}
		CalcVar+=-695, minutes
		GuiControl, Text, TimeLine%A_Index%, %TVar%
	}
return

MidnightFix:
	DayChange:=1
return

HelpButton:
	MessageText=Use the drop-down lists to select the missions that are currently active.
	MessageText=%MessageText%`nAny changes made to the drop-down lists are automatically saved.
	MessageText=%MessageText%`n`nTo adjust the time to match the contract deadline timer:
	MessageText=%MessageText%`n1) Enter a minute value in the 1st bottom left input text box
	MessageText=%MessageText%`n2) Enter a second value in the 2nd bottom left input text box
	MessageText=%MessageText%`n3) Press the "Set Time Offset" button
	MessageText=%MessageText%`n`nYou must press the "Clear All Missions" button when the map rotation
	MessageText=%MessageText%`nchanges to a new set of missions in order to properly offset the time.
	MessageText=%MessageText%`n`nEdit the Missions.txt file in order to add new missions.
	MessageText=%MessageText%`n`nColour guide for boxes next to mission entries:
	MessageText=%MessageText%`n- Light green = One of the top 5 missions in the game.
	MessageText=%MessageText%`n- Dark  green = The 6th to 11th top missions for income.
	MessageText=%MessageText%`n- Light red   = One of the 5 worst missions to play.
	MessageText=%MessageText%`n- Dark  red   = The 6th to 11th worst missions in the game.
	MessageText=%MessageText%`n- Dark yellow = Average missions`; not the best or worst income sources.
	MessageText=%MessageText%`n`nSome missions have a plus or asterisk next to their name. These symbols indicate the mission's suitability for Arty players.
	MessageText=%MessageText%`n- A Plus indicates missions I consider excellent for Arty. There are no significant disadvantages to Arty on these maps.
	MessageText=%MessageText%`n- An Asterisk indicates missions I consider between okay and good. There are some problems with these missions for Arty.
	MessageText=%MessageText%`n- No Plus or Asterisk means I consider playing Arty on that map a bad idea and would recommend either waiting or picking a different class.
	MsgBox,,PvE Rotation Tracker v1.2 by Wiser Guy and XJDHDR, %MessageText%
return

ChangeColour:
	If TempVar in %ExcellentMissions%
		GuiControl, +cLime, Prog%Difficulty%%A_Index%
	Else If TempVar in %GoodMissions%
		GuiControl, +cGreen, Prog%Difficulty%%A_Index%
	Else If TempVar in %BadMissions%
		GuiControl, +cMaroon, Prog%Difficulty%%A_Index%
	Else If TempVar in %TerribleMissions%
		GuiControl, +cRed, Prog%Difficulty%%A_Index%
	Else If !TempVar
		GuiControl, +cGray, Prog%Difficulty%%A_Index%
	Else
		GuiControl, +cOlive, Prog%Difficulty%%A_Index%
Return

GuiClose:
	WinGetPos, tx, ty,,,PvE Rotation Tracker by Wiser Guy and XJDHDR
	IniWrite, %tx%, PvE Rotation Tracker data\Timing and Position data.ini, Position, X
	IniWrite, %ty%, PvE Rotation Tracker data\Timing and Position data.ini, Position, Y
ExitApp