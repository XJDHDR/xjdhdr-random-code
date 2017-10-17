; Recommended settings for performance
#NoEnv
ListLines, Off

Run, .\DOSBOX\dosbox.exe -conf dosbox.conf -noconsole -c "exit",
Sleep, 3000
WinGet, ConstructorGameEXEPID, PID, A, 
GroupAdd, ConstructorGameEXEGroup, ahk_PID %ConstructorGameEXEPID%, 
WinWaitClose, ahk_pid %ConstructorGameEXEPID%, 
ExitApp,

#IfWinActive, ahk_group ConstructorGameEXEGroup, 
RButton::
SendInput, m
Sleep, 50
SendInput, {LButton}
Return,

MButton::
SendInput, {RButton}
Return,
