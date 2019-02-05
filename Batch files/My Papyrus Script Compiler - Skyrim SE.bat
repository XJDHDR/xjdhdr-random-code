Echo Off
SetLocal EnableDelayedExpansion

cd %~dp0
cd ..\..\..\Papyrus Compiler
Set CompilerLocation=%cd%
cd %~dp0
cd ..\
Set OutputLocation=%cd%
cd %~dp0

:Loop
"%CompilerLocation%\PapyrusCompiler.exe" %1 -f="%CompilerLocation%\Papyrus Source\TESV_Papyrus_Flags.flg" -i="%OutputLocation%\Source;%CompilerLocation%\Papyrus Source;%CompilerLocation%\Papyrus Source\Dawnguard;%CompilerLocation%\Papyrus Source\Hearthfire;%CompilerLocation%\Papyrus Source\Dragonborn" -o="%OutputLocation%" -optimize
Shift
If Not "%~1"=="" GoTo Loop
Pause
