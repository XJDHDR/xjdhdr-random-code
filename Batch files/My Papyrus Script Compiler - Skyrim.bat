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
"%CompilerLocation%\PapyrusCompiler.exe" %1 -f="%OutputLocation%\Source\TESV_Papyrus_Flags.flg" -i="%OutputLocation%\Source;%OutputLocation%\Source\Dawnguard;%OutputLocation%\Source\Hearthfire;%OutputLocation%\Source\Dragonborn" -o="%OutputLocation%" -optimize
Shift
If Not "%~1"=="" GoTo Loop
Pause
