:repeat
@..\..\aapython2\python compile.py

Rem - This section adds the mill bonus per month tweak to the compiled "simple_triggers.txt" file.
Rem - It will remain here until I figure out how to implement it in the Python code.
Echo 720.000000 3 6 3 1224979098644774912 648518346341351501 648518346341351591 541 3 1224979098644774912 131 1 1 3 936748722493063465 1224979098644774912 5 >> "..\export\simple_triggers.txt"
For /f "skip=1" %%G In (..\export\simple_triggers.txt) Do If Not Defined iNumberOfTriggers Set "iNumberOfTriggers=%%G"
Set iOldNumberOfTriggers=%iNumberOfTriggers%
Set /a iNumberOfTriggers=%iNumberOfTriggers%+1

:Variables
set InputFile=..\export\simple_triggers.txt
set OutputFile=..\export\simple_triggers-new.txt
set "_strFind=%iOldNumberOfTriggers%"
set "_strInsert=%iNumberOfTriggers%"

:Replace
>"%OutputFile%" (
  for /f "usebackq delims=" %%A in ("%InputFile%") do (
    if "%%A" equ "%_strFind%" (echo %_strInsert%) else (echo %%A)
  )
)
MOVE /Y "..\export\simple_triggers-new.txt" "..\export\simple_triggers.txt"
Rem - End of "simple_triggers.txt" addition section.

@echo Script processing has ended as of %TIME%
@pause
rem goto:repeat