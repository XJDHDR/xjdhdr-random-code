ScriptName XjMbarFillInvFilterFormListScript Extends ReferenceAlias
; Most recent edits made: 05 Februuary 2019

Bool bBusyAddingItemsStateAdditionsRunning
Bool bFirstAddingItemsRunning
Int iNumItemsInPlayerInventory
String sMarkBooksAsReadVersion
String sVersionTest

Actor actPlayerRef
FormList frmlstXjMbarPermanentlyBlankFormList
XjMbarFuncScript XjMbarFunctionsQuest


Event OnInit()
	If GetOwningQuest().IsRunning() == False	; This is to workaround a quirk in Skyrim where the OnInit event runs twice on Quests and Aliases. 
		GetOwningQuest().Start()				; Use the first OnInit to start this quest then use second to do the real work.
	Else
		GotoState("StartInitializationCode")
	EndIf
EndEvent


Event OnPlayerLoadGame()
	GotoState("StartInitializationCode")
EndEvent


Event OnItemAdded(Form frmBaseItem, Int UnneededItemCount, ObjectReference UnneededItemReference, ObjectReference UnneededSourceContainer)
	GoToState("BusyAddingItems")
	bFirstAddingItemsRunning = True
	XjMBARFunctionsQuest.AddBookToInventoryEventFilterFormList(frmBaseItem)
	bFirstAddingItemsRunning = False
	If bBusyAddingItemsStateAdditionsRunning == False
		GoToState("")
	EndIf
EndEvent


; This code block requires SKSE
Event OnMenuOpen(String sUnneededMenuName)
	AddInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
	iNumItemsInPlayerInventory = actPlayerRef.GetNumItems()
EndEvent


Event OnMenuClose(String sUnneededMenuName)
	If iNumItemsInPlayerInventory != actPlayerRef.GetNumItems()
		XjMBARFunctionsQuest.IterateThroughPlayerInventoryForBooks()
	EndIf
	RemoveInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
EndEvent
; End of block that requires SKSE


State BusyAddingItems
	Event OnItemAdded(Form frmBaseItem, Int UnneededItemCount, ObjectReference UnneededItemReference, ObjectReference UnneededSourceContainer)
		AddInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
		bBusyAddingItemsStateAdditionsRunning == True
		Utility.Wait(10.0)
		XjMBARFunctionsQuest.IterateThroughPlayerInventoryForBooks()		; Requires SKSE
		RemoveInventoryEventFilter(frmlstXjMbarPermanentlyBlankFormList)
		bBusyAddingItemsStateAdditionsRunning = False
		If bFirstAddingItemsRunning == False
			GoToState("")
		EndIf
	EndEvent
EndState

State StartInitializationCode
	Event OnBeginState()
		GotoState("InitializationCodeRunning")
		sMarkBooksAsReadVersion = "1.2.1"

		If sVersionTest != sMarkBooksAsReadVersion
			XjMbarFunctionsQuest = Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript
			actPlayerRef = GetActorReference()
			frmlstXjMbarPermanentlyBlankFormList = Game.GetFormFromFile(0x0000080C, "Mark Books as Read.esp") As FormList
			UnregisterForAllMenus()					; Requires SKSE
			RegisterForMenu("BarterMenu")			; Requires SKSE
			RegisterForMenu("ContainerMenu")		; Requires SKSE
			RegisterForMenu("GiftMenu")				; Requires SKSE
			RegisterForMenu("InventoryMenu")		; Requires SKSE
			sVersionTest = sMarkBooksAsReadVersion
		EndIf
		GotoState("")
	EndEvent

	Event OnInit()
	EndEvent
	
	Event OnPlayerLoadGame()
	EndEvent
EndState
