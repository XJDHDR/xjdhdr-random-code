@echo off
..\..\aapython2\python process_init.py
..\..\aapython2\python process_global_variables.py
..\..\aapython2\python process_strings.py
..\..\aapython2\python process_skills.py
..\..\aapython2\python process_music.py
..\..\aapython2\python process_animations.py
..\..\aapython2\python process_meshes.py
..\..\aapython2\python process_sounds.py
..\..\aapython2\python process_skins.py
..\..\aapython2\python process_map_icons.py
..\..\aapython2\python process_factions.py
..\..\aapython2\python process_items.py
..\..\aapython2\python process_scenes.py
..\..\aapython2\python process_troops.py
..\..\aapython2\python process_particle_sys.py
..\..\aapython2\python process_scene_props.py
..\..\aapython2\python process_tableau_materials.py
..\..\aapython2\python process_presentations.py
..\..\aapython2\python process_party_tmps.py
..\..\aapython2\python process_parties.py
..\..\aapython2\python process_quests.py
..\..\aapython2\python process_info_pages.py
..\..\aapython2\python process_scripts.py
..\..\aapython2\python process_mission_tmps.py
..\..\aapython2\python process_game_menus.py
..\..\aapython2\python process_simple_triggers.py
..\..\aapython2\python process_dialogs.py
..\..\aapython2\python process_global_variables_unused.py
..\..\aapython2\python process_postfx.py

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

@del *.pyc
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul