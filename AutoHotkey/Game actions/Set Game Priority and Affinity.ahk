; Recommended settings for performance
#NoEnv
#SingleInstance force
;ListLines, Off


SetTitleMatchMode, 1
AddAllWindowsToAffinityGroup()
AddAllWindowsToPriorityGroup()
StartOfScript:
	WinWaitActive, ahk_group ChangeGameAffinityList, 
	Sleep, 1000
	
	sGroupToCheck := "SingleCore"
	If ( CheckIfWindowInPassedAffinityGroup(sGroupToCheck) != True )
		sGroupToCheck := "DualCore"
	Else If ( CheckIfWindowInPassedAffinityGroup(sGroupToCheck) != True )
		sGroupToCheck := "QuadCore"
	Else If ( CheckIfWindowInPassedAffinityGroup(sGroupToCheck) != True )
		sGroupToCheck := "HexaCore"
	CheckIfWindowInPassedAffinityGroup(sGroupToCheck)
	
	sGroupToCheck := "RealtimePriority"
	If ( CheckIfWindowInPassedPriorityGroup(sGroupToCheck) != True )
		sGroupToCheck := "HighPriority"
	If ( CheckIfWindowInPassedPriorityGroup(sGroupToCheck) != True )
		sGroupToCheck := "AboveNormalPriority"
	If ( CheckIfWindowInPassedPriorityGroup(sGroupToCheck) != True )
		sGroupToCheck := "NormalPriority"
	If ( CheckIfWindowInPassedPriorityGroup(sGroupToCheck) != True )
		sGroupToCheck := "BelowNormalPriority"
	If ( CheckIfWindowInPassedPriorityGroup(sGroupToCheck) != True )
		sGroupToCheck := "LowPriority"
	CheckIfWindowInPassedPriorityGroup(sGroupToCheck)
	
	WinWaitClose, ahk_group ChangeGameAffinityList
Goto, StartOfScript


AddAllWindowsToAffinityGroup()
{
	; Add a GroupAdd line for each game you want to detect
	
	GroupAdd, DualCore, Oblivion ahk_class Oblivion ahk_exe Oblivion.exe,

	GroupAdd, QuadCore, PAYDAY 2 ahk_class diesel win32 ahk_exe payday2_win32_release.exe,

	
	GroupAdd, ChangeGameAffinityList, ahk_group SingleCore
	GroupAdd, ChangeGameAffinityList, ahk_group DualCore
	GroupAdd, ChangeGameAffinityList, ahk_group QuadCore
	GroupAdd, ChangeGameAffinityList, ahk_group HexaCore
	GroupAdd, ChangeGameAffinityList, ahk_group OctaCore
}


AddAllWindowsToPriorityGroup()
{
	; Add a GroupAdd line for each game you want to detect
	
	GroupAdd, HighPriority, Oblivion ahk_class Oblivion ahk_exe Oblivion.exe,
	GroupAdd, HighPriority, PAYDAY 2 ahk_class diesel win32 ahk_exe payday2_win32_release.exe,

	
	GroupAdd, ChangeGamePriorityList, ahk_group RealtimePriority
	GroupAdd, ChangeGamePriorityList, ahk_group HighPriority
	GroupAdd, ChangeGamePriorityList, ahk_group AboveNormalPriority
	GroupAdd, ChangeGamePriorityList, ahk_group NormalPriority
	GroupAdd, ChangeGamePriorityList, ahk_group BelowNormalPriority
	GroupAdd, ChangeGamePriorityList, ahk_group LowPriority
}


CheckIfWindowInPassedAffinityGroup(sGroupToCheck)
{
	WinGet, iGamePID, PID, ahk_group %sGroupToCheck%, 	; Get the PID of the detected window
	If iGamePID
	{
		ChangeGameAffinity_%sGroupToCheck%(iGamePID)
		Return, True
	}
	Return, False
}


ChangeGameAffinity_SingleCore(iPassedGamePID)
{
	SetAffinityOfPassedProgram(iPassedGamePID, 4)
}

ChangeGameAffinity_DualCore(iPassedGamePID)
{
	SetAffinityOfPassedProgram(iPassedGamePID, 12)
}

ChangeGameAffinity_QuadCore(iPassedGamePID)
{
	SetAffinityOfPassedProgram(iPassedGamePID, 60)
}

ChangeGameAffinity_HexaCore(iPassedGamePID)
{
	SetAffinityOfPassedProgram(iPassedGamePID, 252)
}

ChangeGameAffinity_OctaCore(iPassedGamePID)
{
	SetAffinityOfPassedProgram(iPassedGamePID, 1020)
}


SetAffinityOfPassedProgram(iGamePIDToAlter, iAffinityMask)
{
	handleProcess := DllCall( "OpenProcess", Int, 1536, Int, 0, Int, iGamePIDToAlter )		; 1536 = 0x800 = PROCESS_QUERY_INFORMATION and PROCESS_SET_INFORMATION
	DllCall( "SetProcessAffinityMask", Int, handleProcess, Int, iAffinityMask )
	DllCall( "CloseHandle", Int, handleProcess )
}


CheckIfWindowInPassedPriorityGroup(sGroupToCheck)
{
	WinGet, iGamePID, PID, ahk_group %sGroupToCheck%, 	; Get the PID of the detected window
	If iGamePID
	{
		ChangeGamePriority_%sGroupToCheck%(iGamePID)
		Return, True
	}
	Return, False
}


ChangeGameAffinity_RealtimePriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, R
}

ChangeGameAffinity_HighPriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, H
}

ChangeGameAffinity_AboveNormalPriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, A
}

ChangeGameAffinity_NormalPriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, N
}

ChangeGameAffinity_BelowNormalPriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, B
}

ChangeGameAffinity_LowPriority(iPassedGamePID)
{
	Process, Priority, %iGamePID%, L
}
