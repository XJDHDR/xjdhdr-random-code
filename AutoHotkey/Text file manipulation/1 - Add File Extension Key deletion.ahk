DesiredLine = -1

IniRead, FileToManipulate, 0 - File To Manipulate.ini, File, Value

Loop, Read, %FileToManipulate%,
{
	If Not ( RegExMatch(A_LoopReadLine, "\[HKEY_CLASSES_ROOT\\\.[^\\\]]+]$") ) ; This expression matches "[HKEY_CLASSES_ROOT\.<anything that isn't \ or ]>]"
		FileToWrite = %FileToWrite%`n%A_LoopReadLine%
	Else
	{
		FileReadLine, LineBefore, %FileToManipulate%, A_Index - 1
		IfInString, LineBefore, [-HKEY_CLASSES_ROOT\
			FileToWrite = %FileToWrite%`n%A_LoopReadLine%
		Else
		{
			RegExMatch(A_LoopReadLine, "\\\.[^\\\]]+]$", FileExtension, 1)	; This expression matches "\.<anything that isn't \ or ]>]"
			If ( SubStr(A_LoopReadLine, 1, 2) = ";[" )
				FileToWrite = %FileToWrite%`n`;[-HKEY_CLASSES_ROOT%FileExtension%`n%A_LoopReadLine%
			Else
				FileToWrite = %FileToWrite%`n[-HKEY_CLASSES_ROOT%FileExtension%`n%A_LoopReadLine%
		}
	}
}

StringTrimLeft, FileToWrite, FileToWrite, 1
FileAppend, %FileToWrite%, New-%FileToManipulate%,