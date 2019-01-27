scriptname XjMbarFirstInstallThreadScript extends Quest Hidden
; Most recent edits made: 26 January 2019

; This script was adapted from Chesko's Callback multi-threading tutorial:
; https://www.creationkit.com/index.php?title=Creating_Multithreaded_Skyrim_Mods_Part_3_-_Callbacks#Playing_the_Example_Plugin


;Variables you need to get things done go here 
Int iContainerFormID
Int iEndContainerEntry
Int iFirstContainerEntry
Int iThreadNumber
String sModName

FormList frmlstXjMbarReadBooksList


;Thread queuing and set-up
Function PrepareThread(Int iPassedContainerFormID, Int iPassedFirstContainerEntry, Int iPassedEndContainerEntry, String sPassedModName, FormList frmlstPassedReadBooksList, Int iPassedThreadNumber)
	RegisterForModEvent("XjMbarRunThreadedPreInstallCode", "OnRunThreadedPreInstallCode")
    ;Store our passed-in parameters to member variables
	iContainerFormID = iPassedContainerFormID
	iFirstContainerEntry = iPassedFirstContainerEntry
	iEndContainerEntry = iPassedEndContainerEntry
	sModName = sPassedModName
	frmlstXjMbarReadBooksList = frmlstPassedReadBooksList
	iThreadNumber = iPassedThreadNumber
EndFunction


;The actual set of code we want to multithread.
;Event OnRunThreadedPreInstallCode(String sUnneededModEventName, String sUnneededPassedString, Float fUnneededPassedFloat, Form frmPossiblyUnneededSender)
Event OnRunThreadedPreInstallCode()
;	Debug.Trace("Mbar: Thread info " + iThreadNumber + "  " +  iContainerFormID + "  " +  iFirstContainerEntry + "  " +  iEndContainerEntry + "  " +  sModName)
	ObjectReference objrefContainerSpawnMarker = Game.GetFormFromFile(0x0000080E, "Mark Books as Read.esp") As ObjectReference
	ObjectReference objrefContainerWithBooks = objrefContainerSpawnMarker.PlaceAtMe(Game.GetFormFromFile(iContainerFormID, sModName))
	objrefContainerSpawnMarker = None
	If (iFirstContainerEntry == 450) || (sModName != "Skyrim.esm") || (iContainerFormID == 0x000C2CD9) || (iContainerFormID == 0x0010D9FF)
		iEndContainerEntry = objrefContainerWithBooks.GetNumItems()				; Requires SKSE
	EndIf
	
	Book bkCurrentlySelectedBook = None
	Form frmCurrentlySelectedContainerItem = None
	While iEndContainerEntry > iFirstContainerEntry
		iEndContainerEntry -= 1
		frmCurrentlySelectedContainerItem = objrefContainerWithBooks.GetNthForm(iEndContainerEntry)		; Requires SKSE
		If frmCurrentlySelectedContainerItem As Book
			bkCurrentlySelectedBook = frmCurrentlySelectedContainerItem As Book
			If bkCurrentlySelectedBook.IsRead() == True
				If frmlstXjMbarReadBooksList.HasForm(bkCurrentlySelectedBook) == False
					frmlstXjMbarReadBooksList.AddForm(bkCurrentlySelectedBook)
				EndIf
			EndIf
		EndIf
	EndWhile
	objrefContainerWithBooks.DisableNoWait()
	objrefContainerWithBooks.Delete()
	objrefContainerWithBooks = None
	
	; OK, we're done - raise event to return results
;	SendModEvent("XjMbarSendThreadResults")
	Debug.Trace("Mbar: Thread complete " + iThreadNumber)
	Int iModEventHandle = ModEvent.Create("XjMbarSendThreadResults")
	ModEvent.Send(iModEventHandle)
	
	; Set all variables back to default
	ClearThreadVariables()
EndEvent


Function ClearThreadVariables()
	;Reset all thread variables to default state
	iContainerFormID = 0
	iFirstContainerEntry = 0
	iEndContainerEntry = 0
	sModName = ""
	frmlstXjMbarReadBooksList = None
	iThreadNumber = 0
	UnregisterForAllModEvents()
EndFunction
