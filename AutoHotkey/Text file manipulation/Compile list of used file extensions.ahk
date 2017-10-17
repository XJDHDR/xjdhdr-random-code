

Loop, Read, Dragon Unpacker.reg, Dragon Unpacker - new.reg
{
	If ( ReadNextLine = 1 )
	{
		ReadNextLine = 0
		AddToEndOfFile := AddToEndOfFile . SubStr(A_LoopReadLine, 2)
	}
	IfInString, A_LoopReadLine, [HKEY_CLASSES_ROOT\.
	{
		AddToEndOfFile := AddToEndOfFile . "`r`n""" . SubStr(A_LoopReadLine, 20, -1) . """="
		ReadNextLine = 1
	}
	FileAppend, %A_LoopReadLine%`r`n
}
FileAppend, %AddToEndOfFile%, Dragon Unpacker - new.reg,