; This script was copied from here:
; https://autohotkey.com/board/topic/1458-compile-multiple-files-at-once/

compile_app = "C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe"
icondir=%A_ScriptDir%\pics


; if the shift key is held down, then fresh recompile no matter what
shouldcompileall=no
GetKeyState __shift, Shift
if __shift = D
	shouldcompileall=yes

; ==============================================

Loop, Files, %A_ScriptDir%\Send keys\*.ahk, F
{
	infile=%A_ScriptDir%\Send keys\%A_LoopFileName%
	sFileName := StrReplace(A_LoopFileName, "." . A_LoopFileExt)
	outfile=%A_ScriptDir%\Send keys\%sFileName%.exe
	GoSub CompileFile
}

Return

; ==============================================

CompileFile:

	If infile=
	{
		MsgBox No infile specified!
		return
	}
	If outfile=
	{
		MsgBox No outfile specified!
		return
	}

	IfNotExist %infile%
	{
		MsgBox %infile% does not exist!
		return
	}

	; --------------------------------------------------------------
	; conditions for recompilation

	; Detect whether files have changed
	; Only compiled changed files to speed up process

	shouldcompile=no

	; if the output file was somehow deleted
	IfNotExist %outfile%
		shouldcompile=yes

	; the archive-bit is set for the file attributes
	FileGetAttrib, attribs, %infile%
	IfInString attribs, A
		shouldcompile=yes	

	if shouldcompileall=yes
		shouldcompile=yes

	; --------------------------------------------------------------
	; perform the compile
	
	if shouldcompile=yes
	{
		FileSetAttrib,-A, %infile% 
		if outfile=
			runme = %compile_app% /in "%infile%"
		else
			runme = %compile_app% /in "%infile%" /out "%outfile%"
		RunWait %runme%
	}
	return