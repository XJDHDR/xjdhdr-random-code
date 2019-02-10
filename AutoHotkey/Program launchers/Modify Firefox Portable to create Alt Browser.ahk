#NoEnv
;ListLines, Off


; Update Resource Hacker's script
Loop, Read, %A_ScriptDir%\zzIcon_Replacement\ResHack-Script.txt, %A_ScriptDir%\zzIcon_Replacement\ResHack-Script-edited.txt
{
	If A_Index = 2
		FileAppend, Open="%A_ScriptDir%\firefox.exe"`n
	Else If A_Index = 3
		FileAppend, Save="%A_ScriptDir%\firefox.exe"`n
	Else If A_Index = 6
		FileAppend,   -modify "%A_ScriptDir%\zzIcon_Replacement\Logo-FullIcon-16-32-48-256.ico"`, ICONGROUP`, 1`n
	Else If A_Index = 7
		FileAppend,   -modify "%A_ScriptDir%\zzIcon_Replacement\Logo-FullIcon-16-32-48-256.ico"`, ICONGROUP`, 32512`n
	Else
		FileAppend, %A_LoopReadLine%`n
}
FileMove, %A_ScriptDir%\zzIcon_Replacement\ResHack-Script-edited.txt, %A_ScriptDir%\zzIcon_Replacement\ResHack-Script.txt, 1

; Fix Firefox x86
FileCopy, %A_ScriptDir%\App\Firefox\firefox.exe, %A_ScriptDir%\firefox.exe, 1
RunWait, "%A_ScriptDir%\..\ResourceHackerPortable\ResourceHackerPortable.exe" -script "%A_ScriptDir%\zzIcon_Replacement\ResHack-Script.txt",
FileMove, %A_ScriptDir%\firefox.exe, %A_ScriptDir%\App\Firefox\firefox-alt.exe, 1

; Fix Firefox x64
FileCopy, %A_ScriptDir%\App\Firefox64\firefox.exe, %A_ScriptDir%\firefox.exe, 1
RunWait, "%A_ScriptDir%\..\ResourceHackerPortable\ResourceHackerPortable.exe" -script "%A_ScriptDir%\zzIcon_Replacement\ResHack-Script.txt",
FileMove, %A_ScriptDir%\firefox.exe, %A_ScriptDir%\App\Firefox64\firefox-alt.exe, 1

; Fix PortableApps Launcher
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-FullIcon-16-32-48-256.ico, %A_ScriptDir%\App\AppInfo\appicon.ico, 1
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-256.png, %A_ScriptDir%\App\AppInfo\appicon_256.png, 1
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-128.png, %A_ScriptDir%\App\AppInfo\appicon_128.png, 1
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-75.png, %A_ScriptDir%\App\AppInfo\appicon_75.png, 1
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-32.png, %A_ScriptDir%\App\AppInfo\appicon_32.png, 1
FileCopy, %A_ScriptDir%\zzIcon_Replacement\Logo-16.png, %A_ScriptDir%\App\AppInfo\appicon_16.png, 1
FileCopy, %A_ScriptDir%\Other\Source\FirefoxPortable.jpg, %A_ScriptDir%\Other\Source\FirefoxAltPortable.jpg, 1

IniWrite, Mozilla Firefox Alt`, Portable Edition, 			%A_ScriptDir%\App\AppInfo\appinfo.ini, Details, Name
IniWrite, FirefoxAltPortable, 								%A_ScriptDir%\App\AppInfo\appinfo.ini, Details, AppID
IniWrite, %BASELAUNCHERPATH%\App\Firefox\firefox-alt.exe, 	%A_ScriptDir%\App\AppInfo\appinfo.ini, Control, BaseAppID
IniWrite, %BASELAUNCHERPATH%\App\Firefox64\firefox-alt.exe, %A_ScriptDir%\App\AppInfo\appinfo.ini, Control, BaseAppID64
IniWrite, FirefoxAltPortable.exe, 							%A_ScriptDir%\App\AppInfo\appinfo.ini, Control, Start

IniWrite, firefox-alt.exe, %A_ScriptDir%\Other\Source\FirefoxPortable.ini, FirefoxPortable, FirefoxExecutable
FileCopy, %A_ScriptDir%\Other\Source\FirefoxPortable.ini, %A_ScriptDir%\Other\Source\FirefoxAltPortable.ini, 1


FileRead, sTextFileContents, %A_ScriptDir%\Other\Source\FirefoxPortableU.nsi
sTextFileContents2 := StrReplace(sTextFileContents, "firefox.exe", "firefox-alt.exe", Unneeded, -1)
sTextFileContents3 := StrReplace(sTextFileContents2, "FirefoxPortable", "FirefoxAltPortable", Unneeded, -1)
FileDelete, %A_ScriptDir%\Other\Source\FirefoxPortableU.nsi
FileAppend, %sTextFileContents3%, %A_ScriptDir%\Other\Source\FirefoxPortableU.nsi

RunWait, "D:\Portable\PortableApps.com\PortableApps\NSISPortable\NSISPortable.exe" "%A_ScriptDir%\Other\Source\FirefoxPortableU.nsi",
FileDelete, %A_ScriptDir%\FirefoxPortable.exe
