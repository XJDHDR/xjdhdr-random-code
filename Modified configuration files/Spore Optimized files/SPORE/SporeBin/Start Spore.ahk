; Recommended settings for performance
#NoEnv
SetBatchLines -1
ListLines Off

; Execute Spore with Above-normal CPU priority and affinity set to 1 core
Run, %Comspec% /c start /abovenormal /affinity 1 "" SporeApp.exe, 

; Wait for Spore to start
WinWaitActive, ahk_exe SporeApp.exe, , 30

; Wait 10 seconds so that Spore can reach the main menu
Sleep, 10000

; Type in the High Resolution Textures cheat
Send, {Enter} ; Sorry, but I need to close all message boxes (e.g. Login errors) to type in cheats
Sleep, 200
Send, ^+c
Sleep, 200
Send, highresTextureLevel high{Enter}
Sleep, 1500
Send, ^+c
; If you don't see the cheat window open, press Ctrl+Shift+C to check if the cheat was typed in.

; Close the script since we no longer need it.
Sleep, 1000
ExitApp
