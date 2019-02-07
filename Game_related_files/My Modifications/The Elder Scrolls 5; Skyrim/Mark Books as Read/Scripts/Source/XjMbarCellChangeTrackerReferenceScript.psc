ScriptName XjMbarCellChangeTrackerReferenceScript Extends ObjectReference
; Most recent edits made: 21 January 2019


Event OnCellDetach()
	Utility.Wait(0.1)	; Required! Aliases don't fill unless this is here.
	(Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript).RestartAliasQuestFunc()
EndEvent
