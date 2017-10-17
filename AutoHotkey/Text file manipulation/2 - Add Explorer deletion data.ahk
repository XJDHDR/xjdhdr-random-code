CommentedLine = 0
DesiredLine = -1
LastLine = 0

IniRead, FileToManipulate, 0 - File To Manipulate.ini, File, Value

Loop, Read, %FileToManipulate%,
	LastLine += 1

Loop, Read, %FileToManipulate%,
{
	If ( DesiredLine = A_Index )
	{
		DesiredLine = -1
		If ( CommentedLine = 1 )
		{
			CommentedLine = 0
			FileToWrite = %FileToWrite%`n`;[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Roaming\OpenWith\FileExts%FileExtension%`n`;[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts%FileExtension%`n
		}
		Else
			FileToWrite = %FileToWrite%`n[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Roaming\OpenWith\FileExts%FileExtension%`n[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts%FileExtension%`n
	}
	Else If ( LastLine = A_Index ) And ( DesiredLine <> -1 )
	{
		If ( CommentedLine = 1 )
		{
			CommentedLine = 0
			FileToWrite = %FileToWrite%`n`n`;[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Roaming\OpenWith\FileExts%FileExtension%`n`;[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts%FileExtension%
		}
		Else
			FileToWrite = %FileToWrite%`n`n[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\Roaming\OpenWith\FileExts%FileExtension%`n[-HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FileExts%FileExtension%
	}
    
	If Not ( RegExMatch(A_LoopReadLine, "\[HKEY_CLASSES_ROOT\\\.[^\\\]]+]$") )	; This expression matches "[HKEY_CLASSES_ROOT\.<anything that isn't \ or ]>]"
		FileToWrite = %FileToWrite%`n%A_LoopReadLine%
	Else
	{
		FileToWrite = %FileToWrite%`n%A_LoopReadLine%
		DesiredLine := A_Index + 3
		RegExMatch(A_LoopReadLine, "\\\.[^\\\]]+]$", FileExtension, 1)	; This expression matches "\.<anything that isn't \ or ]>]"
		If ( SubStr(A_LoopReadLine, 1, 2) = ";[" )
			CommentedLine = 1
	}
}

StringTrimLeft, FileToWrite, FileToWrite, 1
FileAppend, %FileToWrite%, New-%FileToManipulate%,