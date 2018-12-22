This directory contains my efforts to reverse-engineer and modify various EXEs for the game "Emperor: Battle for Dune". 

Game.exe is the original EXE that ships with the game patched to version 1.09.
EMPEROR.EXE and SETUP.EXE come from the official "Install Fix" patch that can be found here: http://dune2k.com/Duniverse/Games/Emperor/Downloads/Patches


Here is the list of EXEs and their changes:
Emperor.exe:
- EMPEROR - 1 - Install Fix - No HKCU edits.exe
	This is the original EXE that comes from the official "Install Fix" patch.
	
- EMPEROR - 2 - HKLM to HKCU.exe
	Above EXE that has had all calls to RegCreateKeyExA and RegOpenKeyExA modified to read and write to the HKCU hive instead of HKLM.
	
	
Game.exe:
- Game - 1 - Original - No HKCU edits.exe
	This is the original EXE that comes from the official "version 1.9" patch.
	
- Game - 2 - HKLM to HKCU.exe
	Above EXE that has had all calls to RegCreateKeyExA and RegOpenKeyExA modified to read and write to the HKCU hive instead of HKLM.

	
Setup.exe: 
- SETUP - 1 - Install Fix version.exe
	This is the original EXE that comes from the official "Install Fix" patch.

- SETUP - 1 - Original.exe
	This is the original EXE that comes from the game's install CD (Disc 1).
	
- SETUP - 2 - Install Fix converted to HKCU (no Resource.cfg edit).exe
	The original EXE from "Install Fix" that has had all calls to RegCreateKeyExA and RegOpenKeyExA modified to read and write to the HKCU hive instead of HKLM.

- SETUP - 2 - Original converted to HKCU (no Resource.cfg edit).exe
	The original EXE from the CD that has had all calls to RegCreateKeyExA and RegOpenKeyExA modified to read and write to the HKCU hive instead of HKLM.

- SETUP - 3 - Install Fix converted to HKCU + Resource.cfg edit (no no-cd).exe
	The above #2 EXE from "Install Fix" that has been modified to not make changes to "Resource.cfg" after installing the game.

- SETUP - 4 - Install Fix converted to HKCU + Resource.cfg edit + no-cd (no manifest).exe
	The above #3 EXE that has been modified to bypass the requirement that the EXE be on a CD labelled "EMPEROR1".

- SETUP - 5 - Install Fix converted to HKCU + Resource.cfg edit + no-cd + Manifest (pre Windowed mode tweaks).exe
	The above #4 EXE that has had the manifest at the bottom of this readme appended. This causes the EXE to not trigger a UAC prompt as well as not apply Microsoft's DPI scaling.

- SETUP - 6 - Inst. Fix to HKCU + Resource.cfg edit + no-cd + Manifest + Correct style.exe
	The above #5 EXE that has had the window style changed from WS_POPUP to WS_CAPTION + WS_MINIMIZEBOX


- XJDHDR - Modify hex values - Setup.exe.ahk
	This AutoHotkey script will modify an unmodified Emperor Setup.exe to apply all of the changes that have been applied to EXEs #2 to #6.


- Emperor; Battle for Dune - Reverse Engineered files.arc
	An encrypted 7z archive (rename it to .7z) containing all the above EXEs. It is encrypted to ensure the EXEs don't get automatically deleted by overzealous malware scanners and the like.



<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
	<assemblyIdentity
		type="win32"
		name="XJDHDR.PersonalMods.EmperorBattleForDune.SetupExe"
		processorArchitecture="x86"
		version="1.0.0.0"
	/>

	<compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
		<application> 
			<!--This Id value indicates the application supports Windows Vista functionality -->
			<supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/>
			<!--This Id value indicates the application supports Windows 7 functionality-->
			<supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
		</application> 
	</compatibility>

	<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
		<security>
			<requestedPrivileges>
				<requestedExecutionLevel
					level="asInvoker"
					uiAccess="false"
				/>
			</requestedPrivileges>
		</security>
	</trustInfo>
	<application xmlns="urn:schemas-microsoft-com:asm.v3">
		<windowsSettings
			xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
			<dpiAware>True</dpiAware>
		</windowsSettings>
	</application>
</assembly>