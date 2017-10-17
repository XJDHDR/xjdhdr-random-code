#SingleInstance Force
#Persistent
#NoEnv
SetBatchLines, -1


Loop, read, Notepad++ - Edit text file.reg,
{
	IfInString, A_LoopReadLine , \EditWithNPP]
	{
		StringTrimRight, LineContents, A_LoopReadLine, 8
		StringTrimLeft, LineContents, LineContents, 1
		FileContents = %FileContents%`n[-%LineContents%]`n%A_LoopReadLine%`n
	}
	Else
		FileContents = %FileContents%%A_LoopReadLine%`n
}

FileAppend, %FileContents%, Notepad++ - Edit text file - new.reg,

ExitApp