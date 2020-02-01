; Recommended settings for performance
#NoEnv
#SingleInstance force
;ListLines, Off
CoordMode, Pixel, Client


SetTitleMatchMode, 1
AddWindowsToGroup()
StartOfScript:
	WinWaitActive, ahk_group MakeBorderlessList, 
	Sleep, 1000
	
	sGroupToCheck := "StandardGameList"
	If ( MakeBorderlessIfWindowInPassedGroup(sGroupToCheck) != True )
		sGroupToCheck := "CheckIfWindowDisplayingSomethingFirst"
	If ( MakeBorderlessIfWindowInPassedGroup(sGroupToCheck) != True )
		sGroupToCheck := "MaximiseFirst"
	If ( MakeBorderlessIfWindowInPassedGroup(sGroupToCheck) != True )
		sGroupToCheck := "HideWindowBordersOffscreen"
	If ( MakeBorderlessIfWindowInPassedGroup(sGroupToCheck) != True )
		sGroupToCheck := "MaximiseAndCheckIfWindowDisplayingSomethingFirst"
	MakeBorderlessIfWindowInPassedGroup(sGroupToCheck)
	WinWaitClose, ahk_group MakeBorderlessList
Goto, StartOfScript



AddWindowsToGroup()
{
	; Add a GroupAdd line for each game you want to detect and make borderless
	
	GroupAdd, StandardGameList, Armored Warfare v ahk_class CryENGINE ahk_exe armoredwarfare.exe, 
	GroupAdd, StandardGameList, Caesar III ahk_class WinSJBClass ahk_exe c3.exe, 
	GroupAdd, StandardGameList, Company Of Heroes ahk_class Plat::Window {DB3DC0D7-BBA3-4d06-BCD8-40CD448B4AE3} ahk_exe RelicCOH.exe, 
	GroupAdd, StandardGameList, Emperor: Rise of the Middle Kingdom ahk_class WinSJBClass ahk_exe Emperor.exe,
	GroupAdd, StandardGameList, ahk_class GZDoomMainWindow ahk_exe gzdoom.exe, , , GZDOOM ahk_class GZDoomMainWindow ahk_exe gzdoom.exe,		; GZ Doom
	GroupAdd, StandardGameList, ahk_exe hl2.exe, 
	GroupAdd, StandardGameList, Osmos ahk_class OsmosGame ahk_exe Osmos.exe,
	GroupAdd, StandardGameList, PAYDAY 2 ahk_class diesel win32 ahk_exe payday2_win32_release.exe,
	GroupAdd, StandardGameList, Pharaoh ahk_class WinSJBClass ahk_exe Pharaoh.exe, 
	GroupAdd, StandardGameList, ahk_exe rage.exe, 
	GroupAdd, StandardGameList, ahk_exe rage64.exe, 
	GroupAdd, StandardGameList, ahk_class Canvas ahk_exe SporeApp.exe, 
	GroupAdd, StandardGameList, Total War: WARHAMMER 2 ahk_class Warhammer2 ahk_exe Warhammer2.exe, 
	GroupAdd, StandardGameList, ahk_exe WorldOfTanks.exe, 

;	GroupAdd, CheckIfWindowDisplayingSomethingFirst, ,	

	GroupAdd, MaximiseFirst, Zeus ahk_class WinSJBClass ahk_exe Zeus.exe, 	; Window isn't correct size until it has reached the main menu.
	
;	GroupAdd, MaximiseFirst, , 
	
	GroupAdd, MaximiseAndCheckIfWindowDisplayingSomethingFirst, Mount&Blade With Fire and Sword ahk_class MB Window ahk_exe mb_wfas.exe, 	; Mouse activation point doesn't line up with cursor otherwise.

;	GroupAdd, HideWindowBordersOffscreen, , 
	
	GroupAdd, MakeBorderlessList, ahk_group StandardGameList
	GroupAdd, MakeBorderlessList, ahk_group CheckIfWindowDisplayingSomethingFirst
	GroupAdd, MakeBorderlessList, ahk_group MaximiseFirst
	GroupAdd, MakeBorderlessList, ahk_group MaximiseAndCheckIfWindowDisplayingSomethingFirst
	GroupAdd, MakeBorderlessList, ahk_group HideWindowBordersOffscreen
}
; Don't add the following games:
;	GroupAdd, MakeBorderlessList, Mount&Blade With Fire and Sword ahk_class MB Window ahk_exe mb_wfas.exe, 		- Mouse activation point doesn't line up with cursor.
;	GroupAdd, MakeBorderlessList, ahk_exe SpecOpsTheLine.exe$, 													- Game either crashes or doesn't go borderless.


MakeBorderlessIfWindowInPassedGroup(sGroupToCheck)
{
	WinGet, handleGameWindow, ID, ahk_group %sGroupToCheck%, 	; Get a handle to the active window
	If handleGameWindow
	{
		MakeBorderless_%sGroupToCheck%(handleGameWindow)
		Return, True
	}
	Return, False
}


MakeBorderless_CheckIfWindowDisplayingSomethingFirst(handleGameWindow)
{
	CheckCentreOfWindowColour(handleGameWindow)
	MakeBorderless_StandardGameList(handleGameWindow)
}


MakeBorderless_StandardGameList(handleGameWindow)
{
	DllCall("SetMenu", "Ptr", handleGameWindow, "Ptr", 0)
	WinSet, Style, -0xC40000,
	WinGetPos, iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight, ahk_id %handleGameWindow%
	
	iMonitorNumber := GetCurrentMonitor(iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight)
	SysGet, iSelectedDesktopBorder, MonitorWorkArea, %iMonitorNumber%
	
	If (iWinPosBorderTop >= iSelectedDesktopBorderLeft && iWinPosBorderLeft >= iSelectedDesktopBorderTop && iWinPosBorderRight <= iSelectedDesktopBorderRight && iWinPosBorderBottom <= iSelectedDesktopBorderBottom)
	{
		iWinNewTopLeftCornerPosHor  := (( iSelectedDesktopBorderRight  - iSelectedDesktopBorderLeft ) /2 ) - ( iWinWidth  / 2 ) + iSelectedDesktopBorderLeft
		iWinNewTopLeftCornerPosVert := (( iSelectedDesktopBorderBottom - iSelectedDesktopBorderTop  ) /2 ) - ( iWinHeight / 2 ) + iSelectedDesktopBorderTop
		
		WinMove, iWinNewTopLeftCornerPosHor, iWinNewTopLeftCornerPosVert
	}
	Else
	{
		SysGet, iSelectedMonDimensions, Monitor, %iMonitorNumber%
		iSelectedMonWidth  := iSelectedMonDimensionsRight  - iSelectedMonDimensionsLeft
		iSelectedMonHeight := iSelectedMonDimensionsBottom - iSelectedMonDimensionsTop
		WinMove, ahk_id %handleGameWindow%, , iSelectedMonDimensionsLeft, iSelectedMonDimensionsTop, iSelectedMonWidth, iSelectedMonHeight
	}
}


MakeBorderless_MaximiseAndCheckIfWindowDisplayingSomethingFirst(handleGameWindow)
{
	CheckCentreOfWindowColour(handleGameWindow)
	MakeBorderless_MaximiseFirst(handleGameWindow)
}


MakeBorderless_MaximiseFirst(handleGameWindow)
{
	PostMessage, 0x112, 0xF030, , , ahk_id %handleGameWindow%,  ; 0x112 = WM_SYSCOMMAND, 0xF030 = SC_MAXIMIZE
	Sleep, 100
	DllCall("SetMenu", "Ptr", handleGameWindow, "Ptr", 0)
	WinSet, Style, -0xC40000,
	WinGetPos, iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight, ahk_id %handleGameWindow%
	
	iMonitorNumber := GetCurrentMonitor(iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight)
	SysGet, iSelectedMonDimensions, Monitor, %iMonitorNumber%
	iSelectedMonWidth  := iSelectedMonDimensionsRight  - iSelectedMonDimensionsLeft
	iSelectedMonHeight := iSelectedMonDimensionsBottom - iSelectedMonDimensionsTop
	WinMove, ahk_id %handleGameWindow%, , iSelectedMonDimensionsLeft, iSelectedMonDimensionsTop, iSelectedMonWidth, iSelectedMonHeight
}


MakeBorderless_HideWindowBordersOffscreen(handleGameWindow)
{
	VarSetCapacity(pntClientRect, 16)
	DllCall("GetClientRect", "uint", handleGameWindow, "uint", &pntClientRect)
	iWinClientAreaWidth  := NumGet( pntClientRect,  8, "int" )
	iWinClientAreaHeight := NumGet( pntClientRect, 12, "int" )
	
	WinGetPos, iWinPosBorderLeft, iWinPosBorderTop, iWinWidth, iWinHeight, ahk_id %handleGameWindow%, 
	JEE_ClientToScreen(handleGameWindow, 0, 0, iTmpScreenCoordX, iTmpScreenCoordY)
	JEE_ScreenToWindow(handleGameWindow, iTmpScreenCoordX, iTmpScreenCoordY, iWinCoordForClientCoord0X, iWinCoordForClientCoord0Y)
	
	iMonitorNumber := GetCurrentMonitor(iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight)
	SysGet, iSelectedMonDimensions, Monitor, %iMonitorNumber%
	
	iSizeOfRightWindowBorder  := iWinWidth  - iWinCoordForClientCoord0X - iWinClientAreaWidth
	iSizeOfBottomWindowBorder := iWinHeight - iWinCoordForClientCoord0Y - iWinClientAreaHeight
	
	iNewTopLeftCornerLocationX := 0 - iWinCoordForClientCoord0X
	iNewTopLeftCornerLocationY := 0  - iWinCoordForClientCoord0Y
	iNewWindowWidth  := A_ScreenWidth  + iSizeOfRightWindowBorder
	iNewWindowHeight := A_ScreenHeight + iSizeOfBottomWindowBorder
	
	ListVars
	WinMove, ahk_id %handleGameWindow%, , iNewTopLeftCornerLocationX, iNewTopLeftCornerLocationY, iNewWindowWidth, iNewWindowHeight,
}

;MakeBorderless_HideWindowBordersOffscreen(handleGameWindow)
;{
;	VarSetCapacity(pntClientRect, 16)
;	DllCall("GetClientRect", "uint", handleGameWindow, "uint", &pntClientRect)
;	iWinClientAreaWidth  := NumGet( pntClientRect,  8, "int" )
;	iWinClientAreaHeight := NumGet( pntClientRect, 12, "int" )
;	
;	WinGetPos, iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight, ahk_id %handleGameWindow%
;	JEE_ClientToScreen(handleGameWindow, 0, 0, iTmpScreenCoordX, iTmpScreenCoordY)
;	JEE_ScreenToWindow(handleGameWindow, iTmpScreenCoordX, iTmpScreenCoordY, iWinCoordForClientCoord0X, iWinCoordForClientCoord0Y)
;	
;	iMonitorNumber := GetCurrentMonitor(iWinPosBorderTop, iWinPosBorderLeft, iWinWidth, iWinHeight)
;	SysGet, iSelectedMonDimensions, Monitor, %iMonitorNumber%
;	
;	iNewTopLeftCornerLocationX := iSelectedMonDimensionsLeft - iWinCoordForClientCoord0X
;	iNewTopLeftCornerLocationY := iSelectedMonDimensionsTop  - iWinCoordForClientCoord0Y
;	iNewWindowWidth  := iSelectedMonDimensionsRight  + iWinWidth  - iWinClientAreaWidth  - iWinCoordForClientCoord0X
;	iNewWindowHeight := iSelectedMonDimensionsBottom + iWinHeight - iWinClientAreaHeight - iWinCoordForClientCoord0Y
;	
;	WinMove, ahk_id %handleGameWindow%, , iNewTopLeftCornerLocationX, iNewTopLeftCornerLocationY, iNewWindowWidth, iNewWindowHeight,
;}


CheckCentreOfWindowColour(handleGameWindow)
{
	ColourChecker:
	WinGetPos, , , iWinWidth, iWinHeight, ahk_id %handleGameWindow%
	iWinCentreX := iWinWidth / 2
	iWinCentreY := iWinHeight / 2
	PixelGetColor, CentrePixelColour, iWinCentreX, iWinCentreY
	If ( CentrePixelColour = "0x000000" )
	{
		Sleep, 1000
		Goto, ColourChecker
	}
}


; Thanks to irl404 on the AutoHotkey forum for this function
; https://autohotkey.com/board/topic/85457-detecting-the-screen-the-current-window-is-on/
GetCurrentMonitor(iWinXPos, iWinYPos, iWinWidth, iWinHeight)
{
	iWinMidX := iWinXPos + iWinWidth / 2
	iWinMidY := iWinYPos + iWinHeight / 2
	SysGet, iNumberOfMonitors, MonitorCount
	If iNumberOfMonitors = 1
		Return, 1
	Loop %iNumberOfMonitors%
	{
		SysGet, iMonitorArea, Monitor, %A_Index%
		If (iWinMidX > iMonitorAreaLeft && iWinMidX < iMonitorAreaRight && iWinMidY < iMonitorAreaBottom && iWinMidY > iMonitorAreaTop)
		Return, A_Index
	}
	SysGet, iPrimaryMonitor, MonitorPrimary
	Return, iPrimaryMonitor
}


; Thanks to Jeeswg on the AutoHotkey forum for these functions
; https://www.autohotkey.com/boards/viewtopic.php?t=38472
JEE_ClientToScreen(hWnd, iWinClientCoordX, iWinClientCoordY, ByRef iWinScreenCoordX, ByRef iWinScreenCoordY)
{
	VarSetCapacity(pntClientCoordinates, 8)
	NumPut(iWinClientCoordX, &pntClientCoordinates, 0, "Int")
	NumPut(iWinClientCoordY, &pntClientCoordinates, 4, "Int")
	DllCall("user32\ClientToScreen", Ptr,hWnd, Ptr,&pntClientCoordinates)
	iWinScreenCoordX := NumGet(&pntClientCoordinates, 0, "Int")
	iWinScreenCoordY := NumGet(&pntClientCoordinates, 4, "Int")
}

JEE_ScreenToWindow(hWnd, iWinScreenCoordX, iWinScreenCoordY, ByRef iWinWindowCoordX, ByRef iWinWindowCoordY)
{
	VarSetCapacity(pntWinRect, 16)
	DllCall("user32\GetWindowRect", Ptr,hWnd, Ptr,&pntWinRect)
	iTmpFetchedNumX := NumGet(&pntWinRect, 0, "Int")
	iTmpFetchedNumY := NumGet(&pntWinRect, 4, "Int")
	iWinWindowCoordX := iWinScreenCoordX - iTmpFetchedNumX
	iWinWindowCoordY := iWinScreenCoordY - iTmpFetchedNumY
}
