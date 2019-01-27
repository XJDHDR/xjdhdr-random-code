ScriptName XjMbarFirstInstallThreadMasterScript Extends Quest
; Most recent edits made: 26 January 2019

; This script was adapted from Chesko's Callback multi-threading tutorial:
; https://www.creationkit.com/index.php?title=Creating_Multithreaded_Skyrim_Mods_Part_3_-_Callbacks#Playing_the_Example_Plugin


XjMbarFirstInstallThread01Script Thread01
XjMbarFirstInstallThread02Script Thread02
XjMbarFirstInstallThread03Script Thread03
XjMbarFirstInstallThread04Script Thread04
XjMbarFirstInstallThread05Script Thread05
XjMbarFirstInstallThread06Script Thread06
XjMbarFirstInstallThread07Script Thread07
XjMbarFirstInstallThread08Script Thread08
XjMbarFirstInstallThread09Script Thread09
XjMbarFirstInstallThread10Script Thread10


Function StartupThreadingMasterScript()
    ;Let's cast our threads to local variables so things are less cluttered in our code
	Quest qstXjMbarFunctionsQuest = Game.GetFormFromFile(0x00000801, "Mark Books as Read.esp") As XjMbarFuncScript
	Thread01 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread01Script
	Thread02 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread02Script
	Thread03 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread03Script
	Thread04 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread04Script
	Thread05 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread05Script
	Thread06 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread06Script
	Thread07 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread07Script
	Thread08 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread08Script
	Thread09 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread09Script
	Thread10 = qstXjMbarFunctionsQuest as XjMbarFirstInstallThread10Script
	qstXjMbarFunctionsQuest = None
EndFunction


;The 'public-facing' function that our Function script will interact with.
Function StartThreadedTasks(FormList frmlstPassedReadBooksList)
	Thread01.PrepareThread(0x000C2D3B,   0, 150, "Skyrim.esm",     frmlstPassedReadBooksList, 1)	; QABooksContainer
	Thread02.PrepareThread(0x000C2D3B, 150, 300, "Skyrim.esm",     frmlstPassedReadBooksList, 2)	; QABooksContainer
	Thread03.PrepareThread(0x000C2D3B, 300, 450, "Skyrim.esm",     frmlstPassedReadBooksList, 3)	; QABooksContainer
	Thread04.PrepareThread(0x000C2D3B, 300, 450, "Skyrim.esm",     frmlstPassedReadBooksList, 4)	; QABooksContainer
	Thread05.PrepareThread(0x000C2D3B, 450, 610, "Skyrim.esm",     frmlstPassedReadBooksList, 5)	; QABooksContainer
	Thread06.PrepareThread(0x000C2CD9,   0,  93, "Skyrim.esm",     frmlstPassedReadBooksList, 6)	; QASpellTomeContainer
	Thread07.PrepareThread(0x0010D9FF,   0,  90, "Skyrim.esm",     frmlstPassedReadBooksList, 7)	; QASkillBookContainer
	Thread08.PrepareThread(0x0000CAB7,   0,  90, "Dawnguard.esm",  frmlstPassedReadBooksList, 8)	; DLC01QAAllItems
	Thread09.PrepareThread(0x00026B67,   0,  90, "Dragonborn.esm", frmlstPassedReadBooksList, 9)	; DLC02QABooksContainer
	Thread10.PrepareThread(0x00026B69,   0,  90, "Dragonborn.esm", frmlstPassedReadBooksList, 10)	; DLC02QASpellTomeContainer
	
;	SendModEvent("XjMbarRunThreadedPreInstallCode")
	Int iModEventHandle = ModEvent.Create("XjMbarRunThreadedPreInstallCode")
	ModEvent.Send(iModEventHandle)
EndFunction

