ScriptName XjMbarFirstInstallThreadMasterScript Extends Quest
; Most recent edits made: 04 February 2019

; This script was adapted from Chesko's Callback multi-threading tutorial:
; https://www.creationkit.com/index.php?title=Creating_Multithreaded_Skyrim_Mods_Part_3_-_Callbacks#Playing_the_Example_Plugin


;The 'public-facing' function that our Function script will interact with.
Function StartThreadedTasks(FormList frmlstPassedReadBooksList)
	((Self As Quest) as XjMbarFirstInstallThread01Script).PrepareThread(0x000C2D3B,   0, 150, "Skyrim.esm",      1)	; QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread02Script).PrepareThread(0x000C2D3B, 150, 300, "Skyrim.esm",      2)	; QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread03Script).PrepareThread(0x000C2D3B, 300, 450, "Skyrim.esm",      3)	; QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread04Script).PrepareThread(0x000C2D3B, 300, 450, "Skyrim.esm",      4)	; QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread05Script).PrepareThread(0x000C2D3B, 450, 610, "Skyrim.esm",      5)	; QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread06Script).PrepareThread(0x000C2CD9,   0,  93, "Skyrim.esm",      6)	; QASpellTomeContainer
	((Self As Quest) as XjMbarFirstInstallThread07Script).PrepareThread(0x0010D9FF,   0,  90, "Skyrim.esm",      7)	; QASkillBookContainer
	((Self As Quest) as XjMbarFirstInstallThread08Script).PrepareThread(0x0000CAB7,   0,  90, "Dawnguard.esm",   8)	; DLC01QAAllItems
	((Self As Quest) as XjMbarFirstInstallThread09Script).PrepareThread(0x00026B67,   0,  90, "Dragonborn.esm",  9)	; DLC02QABooksContainer
	((Self As Quest) as XjMbarFirstInstallThread10Script).PrepareThread(0x00026B69,   0,  90, "Dragonborn.esm", 10)	; DLC02QASpellTomeContainer
	
	RegisterForModEvent("XjMbarRunThreadedPreInstallCode", "OnRunThreadedPreInstallCode")
	Int iModEventHandle = ModEvent.Create("XjMbarRunThreadedPreInstallCode")
	ModEvent.PushForm(iModEventHandle, frmlstPassedReadBooksList)									; Read Books Form List
	ModEvent.PushForm(iModEventHandle, Game.GetFormFromFile(0x0000080E, "Mark Books as Read.esp"))	; Container Spawn Marker
	ModEvent.Send(iModEventHandle)
	UnregisterForAllModEvents()
EndFunction

