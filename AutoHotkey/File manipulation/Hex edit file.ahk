#NoEnv
ListLines, Off


Global bDoHashComparison := 0
Global sDesiredFileHash := "<CRC32Hash>"
Global bDoBackup := 0
Global sBackupFileSuffix := ".Original-No_Patches_Applied_by_XJDHDR"
Global sFileToEdit := "<file>"
Global sLogFileName := "<log name>"

Global sMessageForUnrecognizedFileHash := "The file that you want to patch is not the file which these patches have been tested with. While you can continue and apply these changes anyway, I can't guarantee that your game will work properly afterwards."
Global sMoreDetailedInfoAboutFile := "It will be in the location where <file name> is found."


If A_Args.Length() = 0
{
	FileDelete, %A_ScriptDir%\%sLogFileName%.log
	If FileExist(A_ScriptDir . "\" . sFileToEdit)
	{
		MsgBox, 3, %sFileToEdit% located in patcher's folder, %sFileToEdit% was found in the same place as this patcher. Is this the %sFileToEdit% you would like to patch (No will allow you to select the location of the one you want to patch)?,
		IfMsgBox, Cancel
			ExitApp
		IfMsgBox, Yes
		{
			If funcPerformHexEditing(A_ScriptDir . "\" . sFileToEdit) = False
				ExitApp
		}
		IfMsgBox, No
			funcSelectFileLocation()
	}
	Else
	{
		funcSelectFileLocation()
	}
}
Else
{
	FileDelete, %A_ScriptDir%\%sLogFileName%.log
	For n, sArrayParameter in A_Args
	{
		Loop Files, %sArrayParameter%, FD
		{
			objFileInArray := A_LoopFileFullPath
			If InStr(objFileInArray, "\" . sFileToEdit)
			{
				If funcPerformHexEditing(objFileInArray) = False
					Continue
				FileAppend, `n`n, %A_ScriptDir%\%sLogFileName%.log,
			}
			Else
				FileAppend, %sFileToEdit% not found in parameter: %objFileInArray%`n`n, %A_ScriptDir%\%sLogFileName%.log,
		}
	}
}

MsgBox, Patching has been completed.
ExitApp


funcSelectFileLocation()
{
	bWasFileFound := 0
	While bWasFileFound = 0
	{
		FileSelectFolder, sFolderContainingFileToBeEdited, ::{20d04fe0-3aea-1069-a2d8-08002b30309d}, 2, Please select the location of %sFileToEdit%. %sMoreDetailedInfoAboutFile%
		If %ErrorLevel% = 1
			ExitApp
		sFileToBeEditedPath := sFolderContainingFileToBeEdited . "\" . sFileToEdit
		bTestFilesLocationResult := funcTestFilesLocation(sFileToBeEditedPath)
		If bTestFilesLocationResult = 0
			Continue
		Else If bTestFilesLocationResult = 1
			bWasFileFound := 1
	}
	If funcPerformHexEditing(sFileToBeEditedPath) = False
		ExitApp
}


funcTestFilesLocation(sPassedFilePath)
{
	If Not FileExist(sPassedFilePath)
	{
		MsgBox, 21, %sFileToEdit% not found, %sFileToEdit% was not found in the specified location.`nPlease select the file's correct location.,
		IfMsgBox, Retry
			Return, False
		Else IfMsgBox, Cancel
			ExitApp
	}
	Return, True
}


funcPerformHexEditing(sPassedFileToHexEdit)
{
	FileSetAttrib, -R, %sPassedFileToHexEdit%
	If ErrorLevel > 0
	{
		MsgBox, The following file could not be opened and/or edited. Please ensure that this program has write permission to the location where the file is located, by either moving %sFileToEdit% to a location where you have write permission or running this program with admin privileges.`n%sPassedFileToHexEdit%
		Return, False
	}
	If FileExist(sPassedFileToHexEdit . sBackupFileSuffix)
	{
		FileSetAttrib, -R, %sPassedFileToHexEdit%%sBackupFileSuffix%
		If ErrorLevel > 0
		{
			MsgBox, The following file could not be opened and/or edited. Please ensure that this program has write permission to the location where the file is located, by either moving %sFileToEdit% to a location where you have write permission or running this program with admin privileges.`n%sPassedFileToHexEdit%%sBackupFileSuffix%
			Return, False
		}
		If bDoBackup = 1
		{
			FileDelete, %sPassedFileToHexEdit%
			If ErrorLevel > 0
			{
				MsgBox, The following file could not be opened and/or edited. Please ensure that this program has write permission to the location where the file is located, by either moving %sFileToEdit% to a location where you have write permission or running this program with admin privileges.`n%sPassedFileToHexEdit%
				Return, False
			}
			FileMove, %sPassedFileToHexEdit%%sBackupFileSuffix%, %sPassedFileToHexEdit%, 1
			If ErrorLevel > 0
			{
				MsgBox, The following file could not be opened and/or edited. Please ensure that this program has write permission to the location where the file is located, by either moving %sFileToEdit% to a location where you have write permission or running this program with admin privileges.`n%sPassedFileToHexEdit%
				Return, False
			}
		}
	}
	If bDoHashComparison = 1
	{
		sCalculatedFileHash := funcCalculateCRC32(sPassedFileToHexEdit)
		If Not sDesiredFileHash = sCalculatedFileHash
		{
			; Add your code for an unrecognised file hash here
			MsgBox, 49, , %sMessageForUnrecognizedFileHash%`nFile path: %sPassedFileToHexEdit%`nHash of file you selected: %sCalculatedFileHash%`nHash of file I've tested:     %sDesiredFileHash%,
			IfMsgBox, Cancel
				ExitApp
		}
	}

	If bDoBackup = 1
	{
		FileCopy, %sPassedFileToHexEdit%, %sPassedFileToHexEdit%%sBackupFileSuffix%, 1
	}
	
	objFile := FileOpen(sPassedFileToHexEdit, "rw -rwd")
	If Not IsObject(objFile)
	{
		MsgBox, The following file could not be opened and/or edited. Please ensure that this program has write permission to the location where the file is located, by either moving %sFileToEdit% to a location where you have write permission or running this program with admin privileges.`n%sPassedFileToHexEdit%
		objFile.Close()
		Return, False
	}
	
	FileCopy, %sPassedFileToHexEdit%, %sPassedFileToHexEdit%.%sBackupFileSuffix%, 1

	funcHexEditThenAddToLog(objFile, "n/a", "00", 5)

	objFile.Close()
	Return, True
}


; Many thanks to jNizM on GitHub and the AutoHotkey forum for this CRC32 calculation function that I copied from his/her HashCalc script:
; https://autohotkey.com/boards/viewtopic.php?t=87
; https://github.com/jNizM/HashCalc/blob/master/src/HashCalc.ahk
funcCalculateCRC32(sPassedFilePath := "")
{
    iNumberOfBytesRead := ""
	iHashSize := 2**22
    VarSetCapacity(int64FileSize, iHashSize, 0)
    handleOpenedFile := DllCall("Kernel32.dll\CreateFile", "Str", sPassedFilePath, "UInt", 0x80000000, "UInt", 3, "Int", 0, "UInt", 3, "UInt", 0, "Int", 0, "UInt")
	; https://docs.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea
	; 0x80000000 = GENERIC_READ only, first UInt 3 = shared read & write access, Int 0 = default security descriptor (n/a in this case) & no child process inheritance,
	; second UInt 3 = open only if file exists, UInt 0 = use only existing attribute flags, Int 0 = handle of template file (ignored in this case)
    If (handleOpenedFile < 1)
    {
        Return handleOpenedFile
    }
    handleLoadedLibrary := DllCall("Kernel32.dll\LoadLibrary", "Str", "Ntdll.dll")
    hexGeneratedCRC := 0
    DllCall("Kernel32.dll\GetFileSizeEx", "UInt", handleOpenedFile, "Int64", &int64FileSize), iFileSize := NumGet(int64FileSize, 0, "Int64")
    Loop % (iFileSize // iHashSize + !!Mod(iFileSize, iHashSize))
    {
        DllCall("Kernel32.dll\ReadFile", "UInt", handleOpenedFile, "Ptr", &int64FileSize, "UInt", iHashSize, "UInt*", iNumberOfBytesRead, "UInt", 0)
        hexGeneratedCRC := DllCall("Ntdll.dll\RtlComputeCrc32", "UInt", hexGeneratedCRC, "UInt", &int64FileSize, "UInt", iNumberOfBytesRead, "UInt")
    }
    DllCall("Kernel32.dll\CloseHandle", "Ptr", handleOpenedFile)
    SetFormat, Integer, % SubStr((A_FI := A_FormatInteger) "H", 0)
    hexGeneratedCRC := SubStr(hexGeneratedCRC + 0x1000000000, -7)
    DllCall("User32.dll\CharLower", "Str", hexGeneratedCRC)
    SetFormat, Integer, %A_FI%
    Return hexGeneratedCRC, DllCall("Kernel32.dll\FreeLibrary", "Ptr", handleLoadedLibrary)
}


funcHexEditThenAddToLog(objPassedFile, sOldHexValues := "n/a", sNewHexValues := "00", iStartPosition := 1, bDontLog := 0)
{
	funcHexEdit(objPassedFile, sOldHexValues, sNewHexValues, iStartPosition)
	If sOldHexValues not in n/a
		FileAppend, %A_Tab%Debug:    Above should say %iStartPosition%: 0x%sOldHexValues% replaced with 0x%sNewHexValues%`n`n, %A_ScriptDir%\%sLogFileName%.log,
	Else
		FileAppend, `n, %A_ScriptDir%\%sLogFileName%.log,
	Return
}


;	Many thanks to Wolf_II of the AutoHotkey forums for the HexEdit function below:
;	https://autohotkey.com/boards/viewtopic.php?t=20524
;-------------------------------------------------------------------------------
funcHexEdit(objPassedFile, sPassedOldHexValues := "n/a", sPassedNewHexValues := "00", iPassedStartPosition := 1, bPassedDontLog := 0) { ; write sPassedNewHexValues at pos
;-------------------------------------------------------------------------------
    ; Unacceptable sPassedNewHexValues will be rejected.
    ; If iPassedStartPosition is larger than file length
    ;   objPassedFile's length will be adjusted accordingly.
    ;   all undefined bytes in the file will be set to zero.
    ;---------------------------------------------------------------------------
    ; returns 1 if successful, 0 otherwise.
    ;---------------------------------------------------------------------------
	objPassedFile.Seek(iPassedStartPosition)
	sOldCharacters := SubStr("00" . funcConvertDecimalToBase(objPassedFile.ReadChar(StrLen(sPassedOldHexValues)), 16),-1)
	objPassedFile.Seek(iPassedStartPosition)
	
	sOriginalNibblesVal := sPassedNewHexValues
    While sPassedNewHexValues != ""
        objPassedFile.WriteChar("0x" SubStr(sPassedNewHexValues, 1, 2))
        , sPassedNewHexValues := SubStr(sPassedNewHexValues, 3)
	If bPassedDontLog = 0
		FileAppend, Patch: Data written to address %iPassedStartPosition%: 0x%sOldCharacters% replaced with 0x%sOriginalNibblesVal%`n, %A_ScriptDir%\%sLogFileName%.log,

    Return, True
}


funcConvertDecimalToBase(n, Base)
{
	Static U := A_IsUnicode ? "w" : "a"
	VarSetCapacity(S,65,0)
	DllCall("msvcrt\_i64to" U, "Int64",n, "Str",S, "Int",Base)
	Return, S
}
