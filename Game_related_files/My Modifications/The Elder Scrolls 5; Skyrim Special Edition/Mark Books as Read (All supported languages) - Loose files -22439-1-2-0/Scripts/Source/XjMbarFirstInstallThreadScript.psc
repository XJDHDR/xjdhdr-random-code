ScriptName XjMbarFirstInstallThreadScript Extends Quest Hidden
; Most recent edits made: 04 February 2019

; This script was adapted from Chesko's Callback multi-threading tutorial:
; https://www.creationkit.com/index.php?title=Creating_Multithreaded_Skyrim_Mods_Part_3_-_Callbacks#Playing_the_Example_Plugin


;Variables you need to get things done go here 
Int iContainerFormID
Int iEndContainerEntry
Int iFirstContainerEntry
Int iThreadNumber
String sModName


;Thread queuing and set-up
Function PrepareThread(Int iPassedContainerFormID, Int iPassedFirstContainerEntry, Int iPassedEndContainerEntry, String sPassedModName, Int iPassedThreadNumber)
    ;Store our passed-in parameters to member variables
	iContainerFormID = iPassedContainerFormID
	iFirstContainerEntry = iPassedFirstContainerEntry
	iEndContainerEntry = iPassedEndContainerEntry
	sModName = sPassedModName
	iThreadNumber = iPassedThreadNumber
EndFunction


;The actual set of code we want to multithread.
Event OnRunThreadedPreInstallCode(Form frmPassedFormlistAsForm, Form frmPassedContainerSpawnMarkerAsForm)
	If Game.GetModByName(sModName) != 255
		ObjectReference objrefContainerWithBooks = (frmPassedContainerSpawnMarkerAsForm As ObjectReference).PlaceAtMe(Game.GetFormFromFile(iContainerFormID, sModName))
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
					FormList frmlstXjMbarReadBooksList = frmPassedFormlistAsForm As FormList
					If frmlstXjMbarReadBooksList.HasForm(bkCurrentlySelectedBook) == False
						frmlstXjMbarReadBooksList.AddForm(bkCurrentlySelectedBook)
					EndIf
				EndIf
			EndIf
		EndWhile
		frmCurrentlySelectedContainerItem = None
		bkCurrentlySelectedBook = None
		objrefContainerWithBooks.DisableNoWait()
		objrefContainerWithBooks.Delete()
		objrefContainerWithBooks = None
	EndIf
	
	; OK, we're done - tell Func Script that we're finished
	((Self As Quest) As XjMbarFuncScript).AddMarkToAllReadBooksBeforeInstallThreadDoneFunc()
	
	; Set all variables back to default
	ClearThreadVariables()
EndEvent


Function ClearThreadVariables()
	;Reset all thread variables to default state
	iContainerFormID = 0
	iFirstContainerEntry = 0
	iEndContainerEntry = 0
	sModName = ""
	iThreadNumber = 0
EndFunction
