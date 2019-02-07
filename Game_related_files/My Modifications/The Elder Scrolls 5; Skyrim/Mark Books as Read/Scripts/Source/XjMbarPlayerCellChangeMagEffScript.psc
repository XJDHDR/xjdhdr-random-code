ScriptName XjMbarPlayerCellChangeMagEffScript Extends ActiveMagicEffect
; Most recent edits made: 21 January 2019
; Ability that will be activated when player is not in the same cell as XjMBARTrackPlayerCellChangeObjectReference


Event OnEffectStart(Actor actPlayerRefSpellTarget, Actor actNotApplicableCaster)
	Utility.Wait(0.1)	; Required! Aliases don't fill unless this is here.
	(Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript).RestartAliasQuestFunc()
EndEvent
