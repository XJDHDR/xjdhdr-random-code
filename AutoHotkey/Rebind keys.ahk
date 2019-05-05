SetTitleMatchMode, 1
SetKeyDelay, , 1,
SetKeyDelay, , 1, Play


GroupAdd, Games_To_Monitor, ahk_class CryENGINE ahk_exe armoredwarfare.exe			; Armored Warfare
GroupAdd, Games_To_Monitor, ahk_class Valve001 ahk_exe csgo.exe						; Counter-Strike: Global Offensive
GroupAdd, Games_To_Monitor, ahk_class Skyrim Special Edition ahk_exe SkyrimSE.exe	; Skyrim Special Edition


#IfWinActive ahk_group	Games_To_Monitor
F13::Send \
F14::Send ]
F15::Send {Del}
F16::Send {End}
F17::Send {PgDn}
F18::Send {Ins}
F19::Send {Home}
F20::Send {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Event
F13::SendEvent \
F14::SendEvent ]
F15::SendEvent {Del}
F16::SendEvent {End}
F17::SendEvent {PgDn}
F18::SendEvent {Ins}
F19::SendEvent {Home}
F20::SendEvent {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Input
F13::SendInput \
F14::SendInput ]
F15::SendInput {Del}
F16::SendInput {End}
F17::SendInput {PgDn}
F18::SendInput {Ins}
F19::SendInput {Home}
F20::SendInput {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Play
F13::SendPlay \
F14::SendPlay ]
F15::SendPlay {Del}
F16::SendPlay {End}
F17::SendPlay {PgDn}
F18::SendPlay {Ins}
F19::SendPlay {Home}
F20::SendPlay {PgUp}


#UseHook On
#IfWinActive ahk_group	Games_To_Monitor_Hook
F13::Send \
F14::Send ]
F15::Send {Del}
F16::Send {End}
F17::Send {PgDn}
F18::Send {Ins}
F19::Send {Home}
F20::Send {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Event_Hook
F13::SendEvent \
F14::SendEvent ]
F15::SendEvent {Del}
F16::SendEvent {End}
F17::SendEvent {PgDn}
F18::SendEvent {Ins}
F19::SendEvent {Home}
F20::SendEvent {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Input_Hook
F13::SendInput \
F14::SendInput ]
F15::SendInput {Del}
F16::SendInput {End}
F17::SendInput {PgDn}
F18::SendInput {Ins}
F19::SendInput {Home}
F20::SendInput {PgUp}

#IfWinActive ahk_group	Games_To_Monitor_Play_Hook
F13::SendPlay \
F14::SendPlay ]
F15::SendPlay {Del}
F16::SendPlay {End}
F17::SendPlay {PgDn}
F18::SendPlay {Ins}
F19::SendPlay {Home}
F20::SendPlay {PgUp}


; Special rebinds
#IfWinActive ahk_class Canvas ahk_exe SporeApp.exe
XButton1::NumpadSub
F14::NumpadAdd
