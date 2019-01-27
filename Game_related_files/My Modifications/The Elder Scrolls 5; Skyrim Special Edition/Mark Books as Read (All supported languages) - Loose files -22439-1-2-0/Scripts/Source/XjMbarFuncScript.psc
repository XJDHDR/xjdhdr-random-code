ScriptName XjMBARFuncScript Extends Quest
; Most recent edits made: 26 January 2019


Import StringUtil

Int iModIDPlaceableStaticsHF
Int iModIDPlaceableStaticsOld
Int iModIDPlaceableStaticsSE
Int iThreadsProcessed

Actor actPlayerRef
FormList frmlstXjMbarInventoryEventFilterFormList		; Note to self: Books only need to be removed from this list after player has read them.
FormList frmlstXjMbarReadBooksList
ObjectReference objrefContainerSpawnMarker
ObjectReference objrefPlayerCellChangeTrackerObjectReference


Function ModStartupFunc(FormList PassedInventoryEventFilterFormList, FormList PassedReadBooksList, Actor actPassedPlayerRef)
	actPlayerRef = actPassedPlayerRef
	If actPlayerRef == None
		actPlayerRef = Game.GetPlayer()
	EndIf
	frmlstXjMbarInventoryEventFilterFormList = PassedInventoryEventFilterFormList
	frmlstXjMbarReadBooksList = PassedReadBooksList
	objrefPlayerCellChangeTrackerObjectReference = Game.GetFormFromFile(0x00000806, "Mark Books as Read.esp") As ObjectReference

	; This block of code requires SKSE
	CreateExcludedModIDsFunc()

	Int iSKSEVersion = SKSE.GetVersionRelease()
	If iSKSEVersion == 0
		Message msgXjMbarSKSENotFound = Game.GetFormFromFile(0x00000809, "Mark Books as Read.esp") As Message
		If msgXjMbarSKSENotFound.GetName() == ""
			msgXjMbarSKSENotFound.SetName("SKSE was not found")
		EndIf
		msgXjMbarSKSENotFound.Show()
		msgXjMbarSKSENotFound = None
	ElseIf iSKSEVersion < 61
		Message msgXjMbarSKSETooOld = Game.GetFormFromFile(0x0000080A, "Mark Books as Read.esp") As Message
		If msgXjMbarSKSETooOld.GetName() == ""
			msgXjMbarSKSETooOld.SetName("SKSE is too old")
		EndIf
		msgXjMbarSKSETooOld.Show()
		msgXjMbarSKSETooOld = None
	Else
		Float fINIUpdateBudgetMS = Utility.GetINIFloat("fUpdateBudgetMS:Papyrus")
		Float fINIExtraTaskletBudgetMS = Utility.GetINIFloat("fExtraTaskletBudgetMS:Papyrus")
		Int iINIMaxMemoryPageSize = Utility.GetINIInt("iMaxMemoryPageSize:Papyrus")
		Int iINIMaxAllocatedMemoryBytes = Utility.GetINIInt("iMaxAllocatedMemoryBytes:Papyrus")
	
		If fINIUpdateBudgetMS < 0.6 || \
		fINIUpdateBudgetMS > 2.4 || \
		fINIExtraTaskletBudgetMS < 0.6 || \
		fINIExtraTaskletBudgetMS > 2.4 || \
		Utility.GetINIInt("iMinMemoryPageSize:Papyrus") != 128 || \
		iINIMaxMemoryPageSize < 512 || \
		iINIMaxMemoryPageSize > 1024 || \
		iINIMaxAllocatedMemoryBytes < 76800 || \
		iINIMaxAllocatedMemoryBytes > 153600
			Message msgXjMbarImproperINISettings = Game.GetFormFromFile(0x00000808, "Mark Books as Read.esp") As Message
			If msgXjMbarImproperINISettings.GetName() == ""
				msgXjMbarImproperINISettings.SetName("Improper Skyrim.ini settings detected")
			EndIf
			msgXjMbarImproperINISettings.Show()
			msgXjMbarImproperINISettings = None
		EndIf
	EndIf
	; End of code that requires SKSE
EndFunction


Function RestartAliasQuestFunc()
	GotoState("AliasQuestRestarting")
	Quest qstXjMbarBookAliasQuest = Game.GetFormFromFile(0x00000815, "Mark Books as Read.esp") As Quest
	Int iCurrentlySelectedAlias = 100
	While iCurrentlySelectedAlias > 0
		iCurrentlySelectedAlias -= 1		; Deliberate! Alias IDs are from 0 to 99, not 1 to 100.
		(qstXjMbarBookAliasQuest.GetAlias(iCurrentlySelectedAlias) As ReferenceAlias).GoToState("DetatchmentRequired")
	EndWhile
	While (qstXjMbarBookAliasQuest.GetAlias(0) As ReferenceAlias).GetReference() != None
		Utility.Wait(0.01)
	EndWhile
	qstXjMbarBookAliasQuest.Stop()
	qstXjMbarBookAliasQuest.Start()
	qstXjMbarBookAliasQuest = None
	objrefPlayerCellChangeTrackerObjectReference.MoveTo(actPlayerRef)
	GotoState("")
EndFunction


Function IterateThroughPlayerInventoryForBooks()
	Int iCurrentlySelectedInventoryItem = actPlayerRef.GetNumItems()		; Requires SKSE
	While iCurrentlySelectedInventoryItem > 0
		iCurrentlySelectedInventoryItem -= 1
		AddBookToInventoryEventFilterFormList(actPlayerRef.GetNthForm(iCurrentlySelectedInventoryItem))		; Requires SKSE
	EndWhile
EndFunction


Function MarkBooksOnGameLoadFunc()
	Int iCurrentlySelectedBookInList = frmlstXjMbarReadBooksList.GetSize()
	While iCurrentlySelectedBookInList > 0
		iCurrentlySelectedBookInList -= 1
		MarkTheBookFunc(frmlstXjMbarReadBooksList.GetAt(iCurrentlySelectedBookInList))
	EndWhile
EndFunction


Function MarkCurrentBookRuntimeFunc(Form frmPassedBookBaseObject, Bool bPassedSneakingDetectionRequired = False)
	If ( bPassedSneakingDetectionRequired == False ) || ( actPlayerRef.IsSneaking() == 0 )
		If TestIfFormHasExcludedModIDFunc(frmPassedBookBaseObject) == True
			Return
		EndIf
	
		If frmlstXjMbarReadBooksList.HasForm(frmPassedBookBaseObject) == 0
			If MarkTheBookFunc(frmPassedBookBaseObject) == True
				Message msgXjMbarBookMarkedMessage = Game.GetFormFromFile(0x00000805, "Mark Books as Read.esp") As Message
				If msgXjMbarBookMarkedMessage.GetName() == ""
					msgXjMbarBookMarkedMessage.SetName("Book marked as read.")
				EndIf
				msgXjMbarBookMarkedMessage.Show()
				msgXjMbarBookMarkedMessage = None
			EndIf
			
			frmlstXjMbarReadBooksList.AddForm(frmPassedBookBaseObject)
			Int iNumberOfFormAdditionAttempts = 0
			While iNumberOfFormAdditionAttempts < 5
				If frmlstXjMbarReadBooksList.HasForm(frmPassedBookBaseObject) == True
					iNumberOfFormAdditionAttempts += 5
				Else
					iNumberOfFormAdditionAttempts += 1
					frmlstXjMbarReadBooksList.AddForm(frmPassedBookBaseObject)
				EndIf
			EndWhile
			Int iNumberOfFormRemovalAttempts = 0
			While iNumberOfFormRemovalAttempts < 5
				If frmlstXjMbarInventoryEventFilterFormList.HasForm(frmPassedBookBaseObject) == False
					Return
				Else
					iNumberOfFormRemovalAttempts += 1
					frmlstXjMbarInventoryEventFilterFormList.RemoveAddedForm(frmPassedBookBaseObject)
				EndIf
			EndWhile
		EndIf
	EndIf
EndFunction


Function AddBookToInventoryEventFilterFormList(Form frmPassedBookBaseObject)
	If frmPassedBookBaseObject As Book
		If frmlstXjMbarReadBooksList.HasForm(frmPassedBookBaseObject) == False
			If frmlstXjMbarInventoryEventFilterFormList.HasForm(frmPassedBookBaseObject) == False
				If TestIfFormHasExcludedModIDFunc(frmPassedBookBaseObject) == True
					Return
				EndIf
	
				Int iNumberOfFormAdditionAttempts = 0
				While iNumberOfFormAdditionAttempts < 5
					If frmlstXjMbarInventoryEventFilterFormList.HasForm(frmPassedBookBaseObject) == True
						Return
					Else
						iNumberOfFormAdditionAttempts += 1
						frmlstXjMbarInventoryEventFilterFormList.AddForm(frmPassedBookBaseObject)
					EndIf
				EndWhile
			EndIf
		EndIf
	EndIf
EndFunction


Bool Function MarkTheBookFunc(Form frmPassedBookBaseObject)
	; Most of this code requires SKSE
	String sBookName = frmPassedBookBaseObject.GetName()
	String sMarkToPlaceOnBook = (Game.GetFormFromFile(0x00000807, "Mark Books as Read.esp") As Message).GetName()
	If sMarkToPlaceOnBook == ""
		sMarkToPlaceOnBook = "~(Read)"
	EndIf
	If Substring(sBookName, 0, GetLength(sMarkToPlaceOnBook)) != sMarkToPlaceOnBook
		frmPassedBookBaseObject.SetName(sMarkToPlaceOnBook+" "+sBookName)
		Int iNumberOfChangeNameAttempts = 0
		While iNumberOfChangeNameAttempts < 5
			If frmPassedBookBaseObject.GetName() == sMarkToPlaceOnBook+" "+sBookName
				Return True
			Else
				iNumberOfChangeNameAttempts += 1
				frmPassedBookBaseObject.SetName(sMarkToPlaceOnBook+" "+sBookName)
			EndIf
		EndWhile
	EndIf
	Return False
EndFunction


Function AddMarkToAllReadBooksBeforeInstallFunc()
	Debug.Notification("Mark Books as Read: Started marking previously read books")
	
	If ( frmlstXjMbarReadBooksList.GetSize() == 0 ) && ( SKSE.GetVersionRelease() != 0 )
		If Game.GetModByName("Skyrim.esm") != 255		; Requires SKSE
			RegisterForModEvent("XjMbarSendThreadResults", "OnSendThreadResults")
			iThreadsProcessed = 0
			XjMbarFirstInstallThreadMasterScript XjMbarFunctionsQuest = Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFirstInstallThreadMasterScript
			XjMbarFunctionsQuest.StartupThreadingMasterScript()
			XjMbarFunctionsQuest.StartThreadedTasks(frmlstXjMbarReadBooksList)
			Book bkCurrentlySelectedBook = None
			If Game.GetModByName("HearthFires.esm") != 255		; Requires SKSE
				Int[] iBookFormIDArray = New Int[10]
				iBookFormIDArray[0] = 0x000008AE	; BYOHHouseBanditAttack2Note
				iBookFormIDArray[1] = 0x000030A1	; BYOHHouseJarlFriendLetter
				iBookFormIDArray[2] = 0x00003F78	; BYOHAdoptionStewardCourierNote
				iBookFormIDArray[3] = 0x00003F7C	; BYOHAdoptionConstanceLetter
				iBookFormIDArray[4] = 0x00010BEF	; BYOHHouseJarlFriendLetter2
				iBookFormIDArray[5] = 0x0001579F	; BYOHHouse1Deed
				iBookFormIDArray[6] = 0x000157A0	; BYOHHouse2Deed
				iBookFormIDArray[7] = 0x000157A1	; BYOHHouse3Deed
				iBookFormIDArray[8] = 0x00015D59	; BYOHHouseGuide
				iBookFormIDArray[9] = 0x00016130	; BYOHHouseJarlIntroLetter
	
				Int iCurrentArrayLength = 0
				While iCurrentArrayLength < 10
					bkCurrentlySelectedBook = Game.GetFormFromFile(iBookFormIDArray[iCurrentArrayLength], "HearthFires.esm") As Book
					If bkCurrentlySelectedBook.IsRead() == True
						If frmlstXjMbarReadBooksList.HasForm(bkCurrentlySelectedBook) == True
							frmlstXjMbarReadBooksList.AddForm(bkCurrentlySelectedBook)
						EndIf
					EndIf
					iCurrentArrayLength += 1
				EndWhile
				iCurrentArrayLength = 0
			EndIf

			While iThreadsProcessed < 10
				Utility.Wait(0.5)
			EndWhile
			XjMbarFunctionsQuest = None
			UnregisterForAllModEvents()
	
			iThreadsProcessed = 0
			bkCurrentlySelectedBook = None
		EndIf
	EndIf
	Debug.Notification("Mark Books as Read: Finished marking previously read books")
EndFunction

;Event OnSendThreadResults(String sUnneededModEventName, String sUnneededPassedString, Float fUnneededPassedFloat, Form frmUnneededSender)
Event OnSendThreadResults()
	RegisterForModEvent("XjMbarSendThreadResults", "OnSendThreadResults")
	iThreadsProcessed += 1
	Debug.Trace("Mbar: iThreadsProcessed = " + iThreadsProcessed)
EndEvent


Bool Function TestIfFormHasExcludedModIDFunc(Form frmPassedBookBaseObject)
	Int iCurrentFormID = frmPassedBookBaseObject.GetFormID()
	Int iCurrentFormModID = ( iCurrentFormID / 16777216 ) As Int	; 16777216 is the hexadecimal number 0x01000000 in decimal notation. This formula will convert the form's FormID into a ModID. "As Int" will chop off any decimals created by the maths.

	; NOTE: Can't currently detect mods that are ESL flagged using the GetModByName function. 

	; Do not mark the book if it comes from one of the following mods:
	If ( iCurrentFormModID == iModIDPlaceableStaticsSE )			; Placeable Statics - Special Edition version
		Return True
	ElseIf ( iCurrentFormModID == iModIDPlaceableStaticsOld )		; Placeable Statics - Oldrim version
		Return True
	ElseIf ( iCurrentFormModID == iModIDPlaceableStaticsHF )		; Placeable Statics - Oldrim's Hearthfire version
		Return True
	EndIf
	Return False
EndFunction


Function CreateExcludedModIDsFunc()
	; This whole function requires SKSE
	; This section detects the presence of any installed mods that have "books" which should not be marked under any circumstance

	; NOTE: Can't currently detect mods that are ESL flagged using the GetModByName function. 

	iModIDPlaceableStaticsSE = Game.GetModByName("AK - Placeable Statics SE.esp")					; Placeable Statics - Special Edition version
	If ( iModIDPlaceableStaticsSE == 0 ) || ( iModIDPlaceableStaticsSE == 255 )
		iModIDPlaceableStaticsSE = 500
		iModIDPlaceableStaticsOld = Game.GetModByName("AK -Placeable Statics.esp")					; Placeable Statics - Oldrim version
		If ( iModIDPlaceableStaticsOld == 0 ) || ( iModIDPlaceableStaticsOld == 255 )
			iModIDPlaceableStaticsOld = 500
			iModIDPlaceableStaticsHF = 500
		Else
			iModIDPlaceableStaticsHF = Game.GetModByName("AK - Placeable Statics - Hearthfire.esp")	; Placeable Statics - Oldrim's Hearthfire version
			If ( iModIDPlaceableStaticsHF == 0 ) || ( iModIDPlaceableStaticsHF == 255 )
				iModIDPlaceableStaticsHF = 500
			EndIf
		EndIf
	Else
		iModIDPlaceableStaticsOld = 500
		iModIDPlaceableStaticsHF = 500
	EndIf
EndFunction


State AliasQuestRestarting
	Function RestartAliasQuestFunc()
		objrefPlayerCellChangeTrackerObjectReference.MoveTo(actPlayerRef)
	EndFunction
EndState
