#SingleInstance Force
SetTitleMatchMode 2
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

global OffsetVar:=0	;Controls how many minutes the time is offset
global OffsecVar:=0	;Controls how many seconds the time is offset
IfExist Offset.txt
{
	FileReadLine, OffsetVar, Offset.txt, 1
	FileReadLine, OffsecVar, Offset.txt, 2
}
MissionList=
IfNotExist Missions.txt	
{
	FileAppend, Albatross`nAnvil`nBanshee`nBasilisk`nCavalry`nCerberus`nDire Wolf, Missions.txt
	FileAppend,`nErebos`nFrostbite`nGhost Hunter`nHarbinger`nHydra`nKodiak`nLeviathan, Missions.txt
	FileAppend,`nLife Jacket`nMeltdown`nOnyx`nPerseus, Missions.txt
	FileAppend,`nPhalanx`nPrometheus`nQuarterback`nRaiding Party`nRed Opossum`nRicochet, Missions.txt
	FileAppend,`nRolling Thunder`nSapphire`nScorpio`nSnake Bite`nSpearhead, Missions.txt
	FileAppend,`nStarry Night`nStormy Winter`nTiger Claw`nTsunami`nUmbrella, Missions.txt
	FileAppend,`nWatchdog`nWildfire`nZero Hour, Missions.txt
}
Loop, Read, Missions.txt	;Missions.txt contains a list of all missions seperated by newlines
	MissionList=%MissionList%%A_LoopReadLine%|
Gui, Font, s12
yVar:=4
newTime := A_Hour * 60 + A_Min - OffsetVar + 150
if(OffsecVar > 45)
	newTime--
Transform, rVar, Mod, %newTime%, 30
CalcVar =
CalcVar += -%rVar%, minutes
Loop 10 {
	Gui, Add, DropDownList, vMH%A_Index% W304 X5 Y%yVar% gSaveList R50, %MissionList%
	Gui, Add, DropDownList, vMM%A_Index% W304 X319 Y%yVar% gSaveList R50, %MissionList%
	;Gui, Add, DropDownList, vME%A_Index% W200 X425 Y%yVar% gSaveList R50, %MissionList%
	yVar+=3
	Gui, Add, Text, vCD%A_Index% X628 Y%yVar% W200, 00:00
	yVar+=26
	TVar=
	Loop 14 {
		FormatTime, SVar, %CalcVar%, hh:mm
		TVar=%TVar%%A_Space%%A_Space%%A_Space%%SVar%
		CalcVar+=30, minutes
	}
	CalcVar+=-417, minutes
	Gui, Add, Text, vTimeLine%A_Index% X5 Y%yVar%, %TVar%
	yVar+=25
}
Loop, Read, HL.txt
	GuiControl, ChooseString, MH%A_Index%, %A_LoopReadLine%
Loop, Read, ML.txt
	GuiControl, ChooseString, MM%A_Index%, %A_LoopReadLine%
;Loop, Read, EL.txt
;	GuiControl, ChooseString, ME%A_Index%, %A_LoopReadLine%
yVar+=-4
Gui, Add, Edit, X5 W55 vMinBox Y%yVar% Number, %OffsetVar%
Gui, Add, Edit, X63 W55 vSecBox Y%yVar% Number, %OffsecVar%
yVar--
Gui, Add, Button, X120 W295 H30 Y%yVar% gSetTimeOffset, Set Time Offset (Minutes/Seconds)
Gui, Add, Button, X420 W205 H30 Y%yVar% gClearList, Clear All Missions
Gui, Add, Button, X630 W90 H30 Y%yVar% gHelpButton, Help
IfNotExist Pos.txt
{
	FileAppend, 0`n, Pos.txt
	FileAppend, 0, Pos.txt
}
FileReadLine, xPos, Pos.txt, 1
FileReadLine, yPos, Pos.txt, 2
Gui, Show, W730 H570 X%xPos% Y%yPos%, PvE Rotation Tracker by Wiser Guy
GoSub EverySecond
SetTimer EverySecond, 1000
return

EverySecond:
newTime := A_Hour * 3600 + A_Min * 60 + A_Sec - OffsetVar * 60 - OffsecVar + 9000
Loop 10 {
	newTime -= 180
	Transform, rVar, Mod, %newTime%, 1800
	cVar:=1800-rVar
	if(cVar < 180){
		mVar:=AZ(floor(cVar/60))
		sVar:=AZ(mod(cVar,60))
		Gui, Font, cRed
		GuiControl, Text, CD%A_Index%, %mVar%:%sVar% - Active
		GuiControl, Font, CD%A_Index%
	}
	else{
		cVar-=180
		nextTime =
		nextTime += %cVar%, seconds
		FormatTime, nextTime, %nextTime%, hh:mm
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
	FileDelete, HL.txt
	FileDelete, ML.txt
	;FileDelete, EL.txt
	Loop 10 {
		GuiControlGet TempVar,, MH%A_Index%
		FileAppend %TempVar%`n,HL.txt
		GuiControlGet TempVar,, MM%A_Index%
		FileAppend %TempVar%`n,ML.txt
		;GuiControlGet TempVar,, ME%A_Index%
		;FileAppend %TempVar%`n,EL.txt
	}
return

Clearlist:
	Loop 10	{
		GuiControl, Choose, MH%A_Index%, 0
		GuiControl, Choose, MM%A_Index%, 0
		;GuiControl, Choose, ME%A_Index%, 0
	}
	GuiControlGet OffsetVar,, MinBox
	GuiControlGet OffsecVar,, SecBox
return

SetTimeOffset:
	FileDelete, Offset.txt
	GuiControlGet OffsetVar,, MinBox
	GuiControlGet OffsecVar,, SecBox
	if(OffsetVar > 29)
	{
		Transform, OffsetVar, Mod, %OffsetVar%, 30
		GuiControl,,MinBox,%OffsetVar%
	}
	if(OffsecVar > 59)
	{
		Transform, OffsecVar, Mod, %OffsecVar%, 60
		GuiControl,,SecBox,%OffsecVar%
	}
	FileAppend, %OffsetVar%`n%OffsecVar%, Offset.txt

	newTime := A_Hour * 60 + A_Min - OffsetVar + 150
	if(OffsecVar > 45)
		newTime--
	Transform, rVar, Mod, %newTime%, 30
	CalcVar =
	CalcVar += -%rVar%, minutes
	Loop 10	{
	TVar=
		Loop 14 {
			FormatTime, SVar, %CalcVar%, hh:mm
			TVar=%TVar%%A_Space%%A_Space%%A_Space%%SVar%
			CalcVar+=30, minutes
		}
		CalcVar+=-417, minutes
		GuiControl, Text, TimeLine%A_Index%, %TVar%
	}
	GoSub EverySecond
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
	MsgBox,,PvE Rotation Tracker v1.05 by Wiser Guy, %MessageText%
return

GuiClose:
	WinGetPos, tx, ty,,,PvE Rotation Tracker by Wiser Guy
	FileDelete, Pos.txt
	FileAppend, %tx%`n, Pos.txt
	FileAppend, %ty%, Pos.txt	
ExitApp
