ScriptName XjMbarPlayerAliasScript Extends ReferenceAlias
; Most recent edits made: 03 February 2019


Bool bGameLoaded
String sMarkBooksAsReadVersion
String sVersionTest

Actor actPlayerRef
Book bookXjMbarEmptyBookToForceInventoryUpdate
FormList frmlstXjMbarInventoryEventFilterFormList
FormList frmlstXjMbarPermanentlyBlankFormList
FormList frmlstXjMbarReadBooksList
XjMbarFuncScript XjMbarFunctionsQuest


Event OnInit()
	If GetOwningQuest().IsRunning() == False	; This is to workaround a quirk in Skyrim where the OnInit event runs twice on Quests and Aliases. 
		GetOwningQuest().Start()				; Use the first OnInit to start this quest then use second to do the real work.
	Else
		bGameLoaded = 0
		GotoState("StartInitializationCode")
	EndIf
EndEvent


Event OnPlayerLoadGame()
	bGameLoaded = 1
	GotoState("StartInitializationCode")
EndEvent


Event OnCellLoad()
	XjMbarFunctionsQuest.RestartAliasQuestFunc()
EndEvent


Event OnItemRemoved(Form frmRemovedItemBase, Int UnneededCount, ObjectReference refRemovedItemRef, ObjectReference refRemovedItemDest)
	AddInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
	If frmRemovedItemBase As Book			; Is it a book?
		If frmlstXjMbarReadBooksList.HasForm(frmRemovedItemBase) == 0
			XjMbarFunctionsQuest.RestartAliasQuestFunc()
		EndIf
	EndIf
	RemoveInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
EndEvent


Event OnObjectEquipped(Form EquippedObjectBase, ObjectReference UnneededReference)
	If EquippedObjectBase As Book		; Is it a book?
		If frmlstXjMbarReadBooksList.HasForm(EquippedObjectBase) == 0
			XjMbarFunctionsQuest.MarkCurrentBookRuntimeFunc(EquippedObjectBase)
			
			; These two commands force Skyrim to update the inventory menu.
			actPlayerRef.AddItem(bookXjMbarEmptyBookToForceInventoryUpdate, 1, true)
			actPlayerRef.RemoveItem(bookXjMbarEmptyBookToForceInventoryUpdate, 1, true)
			
			; Restart the alias quest. If another copy of the book just read is in the world near the player, we need to remove the alias from it.
			XjMbarFunctionsQuest.RestartAliasQuestFunc()
		EndIf
	EndIf
EndEvent


State StartInitializationCode
	Event OnBeginState()
		GotoState("InitializationCodeRunning")
		sMarkBooksAsReadVersion = "1.2.1"

		If sVersionTest != sMarkBooksAsReadVersion
			actPlayerRef = GetActorReference()		; This script is attached to a Player Alias. GetReference will grab the reference filled by that alias.
			XjMbarFunctionsQuest = Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript
			frmlstXjMbarReadBooksList = Game.GetFormFromFile(0x00000800, "Mark Books as Read.esp") As FormList
			frmlstXjMbarPermanentlyBlankFormList = Game.GetFormFromFile(0x0000080C, "Mark Books as Read.esp") As FormList
			frmlstXjMbarInventoryEventFilterFormList = Game.GetFormFromFile(0x0000080B, "Mark Books as Read.esp") As FormList
			bookXjMbarEmptyBookToForceInventoryUpdate = Game.GetFormFromFile(0x00000812, "Mark Books as Read.esp") As Book
			RemoveInventoryEventFilter(frmlstXjMbarInventoryEventFilterFormList)
			AddInventoryEventFilter(frmlstXjMbarInventoryEventFilterFormList)
			sVersionTest = sMarkBooksAsReadVersion
		EndIf
		XjMbarFunctionsQuest.ModStartupFunc(frmlstXjMbarInventoryEventFilterFormList, frmlstXjMbarReadBooksList, actPlayerRef)
		If bGameLoaded == 0
			XjMbarFunctionsQuest.AddMarkToAllReadBooksBeforeInstallFunc()
		EndIf
		bGameLoaded = 0
		XjMbarFunctionsQuest.MarkBooksOnGameLoadFunc()
		XjMbarFunctionsQuest.RestartAliasQuestFunc()
		XjMBARFunctionsQuest.IterateThroughPlayerInventoryForBooks()		; Requires SKSE
		GotoState("")
	EndEvent
	
	Event OnInit()
	EndEvent
	
	Event OnPlayerLoadGame()
	EndEvent
EndState
