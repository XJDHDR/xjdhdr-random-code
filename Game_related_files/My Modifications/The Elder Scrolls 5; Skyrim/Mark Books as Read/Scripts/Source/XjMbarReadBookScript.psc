ScriptName XjMbarReadBookScript Extends ReferenceAlias
; Most recent edits made: 05 February 2019


Bool bActivationAlreadyBlocked
Bool bCrosshairRefInvalid
Int iMessageBoxButtonPressed

Actor actPlayer
ObjectReference objrefBookAliasAttachedTo


Event OnInit()
	If GetOwningQuest().IsRunning() == False	; This is to workaround a quirk in Skyrim where the OnInit event runs twice on Quests and Aliases. 
		Return									; Throw out the first OnInit that runs when the game starts.
	EndIf
	GoToState("InitializationStarted")
	actPlayer = Game.GetPlayer()
	objrefBookAliasAttachedTo = GetReference()
	If objrefBookAliasAttachedTo != None
		RegisterForControl("Activate")
	EndIf
EndEvent


Event OnActivate(ObjectReference objrefActivator)
	If objrefActivator == actPlayer
		If objrefBookAliasAttachedTo.IsOffLimits() == True
			iMessageBoxButtonPressed = (Game.GetFormFromFile(0x00000810, "Mark Books as Read.esp") As Message).Show()
			If iMessageBoxButtonPressed == 0
				objrefBookAliasAttachedTo.SendStealAlarm(actPlayer)
				actPlayer.AddItem(objrefBookAliasAttachedTo, 1, True)
			ElseIf iMessageBoxButtonPressed == 1
				objrefBookAliasAttachedTo.Activate(actPlayer, True)
			EndIf
		Else
			iMessageBoxButtonPressed = (Game.GetFormFromFile(0x00000811, "Mark Books as Read.esp") As Message).Show()
			If iMessageBoxButtonPressed == 0
				actPlayer.AddItem(objrefBookAliasAttachedTo, 1, True)
			ElseIf iMessageBoxButtonPressed == 1
				objrefBookAliasAttachedTo.Activate(actPlayer, True)
			EndIf
		EndIf
	EndIf
EndEvent


Event OnControlDown(String sControlWeKnowIsActivate)
	If Game.GetCurrentCrosshairRef() != objrefBookAliasAttachedTo
		bCrosshairRefInvalid = True
		Return
	ElseIf objrefBookAliasAttachedTo.IsActivationBlocked() == True
		bActivationAlreadyBlocked == True
		Return
	Else
		objrefBookAliasAttachedTo.BlockActivation(True)
	EndIf
EndEvent


Event OnControlUp(String sControlWeKnowIsActivate, Float fUnneededTimeHeldDown)
	If bCrosshairRefInvalid == True
		bCrosshairRefInvalid = False
		Return
	ElseIf bActivationAlreadyBlocked == True
		bActivationAlreadyBlocked == False
		Return
	Else
		objrefBookAliasAttachedTo.BlockActivation(False)
	EndIf
EndEvent


Event OnRead()
	XjMbarFuncScript XjMbarFunctionsQuest = Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript
	XjMbarFunctionsQuest.MarkCurrentBookRuntimeFunc(objrefBookAliasAttachedTo.GetBaseObject())

	; These next two commands force Skyrim to update the UI.
	Game.DisablePlayerControls(False, False, False, False, False, False, True)
	Game.EnablePlayerControls(False, False, False, False, False, False, True)

	; Restart the alias quest. If another copy of the book just read is in the world near the player, we need to remove the alias from it.
	XjMbarFunctionsQuest.RestartAliasQuestFunc()
	XjMbarFunctionsQuest = None
	GoToState("DetatchmentRequired")
EndEvent


Event OnContainerChanged(ObjectReference objrefNewContainer, ObjectReference objrefUnneededOldContainerRef)
	If objrefNewContainer == actPlayer
		GoToState("DetatchmentRequired")
	EndIf
EndEvent


State DetatchmentRequired
	Event OnBeginState()
		UnregisterForAllControls()
		Clear()
	EndEvent

	Event OnInit()
	EndEvent
EndState


State InitializationStarted
	Event OnInit()
	EndEvent
EndState
