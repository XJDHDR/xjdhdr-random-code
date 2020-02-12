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
	
	sAffinityGroupToCheck := "SingleCore"
	If ( CheckIfWindowInPassedAffinityGroup(sAffinityGroupToCheck) != True )
	{
		sAffinityGroupToCheck := "DualCore"
		If ( CheckIfWindowInPassedAffinityGroup(sAffinityGroupToCheck) != True )
		{
			sAffinityGroupToCheck := "QuadCore"
			If ( CheckIfWindowInPassedAffinityGroup(sAffinityGroupToCheck) != True )
			{
				sAffinityGroupToCheck := "HexaCore"
				CheckIfWindowInPassedAffinityGroup(sAffinityGroupToCheck)
			}
		}
	}
	
	sPriorityGroupToCheck := "RealtimePriority"
	If ( CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck) != True )
	{
		sPriorityGroupToCheck := "HighPriority"
		If ( CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck) != True )
		{
			sPriorityGroupToCheck := "AboveNormalPriority"
			If ( CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck) != True )
			{
				sPriorityGroupToCheck := "NormalPriority"
				If ( CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck) != True )
				{
					sPriorityGroupToCheck := "BelowNormalPriority"
					If ( CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck) != True )
					{
						sPriorityGroupToCheck := "LowPriority"
						CheckIfWindowInPassedPriorityGroup(sPriorityGroupToCheck)
					}
				}
			}
		}
	}
	
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


ChangeGamePriority_RealtimePriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, R
}

ChangeGamePriority_HighPriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, H
}

ChangeGamePriority_AboveNormalPriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, A
}

ChangeGamePriority_NormalPriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, N
}

ChangeGamePriority_BelowNormalPriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, B
}

ChangeGamePriority_LowPriority(iPassedGamePID)
{
	Process, Priority, %iPassedGamePID%, L
}
