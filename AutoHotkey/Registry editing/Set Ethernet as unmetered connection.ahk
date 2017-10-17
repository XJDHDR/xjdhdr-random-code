; Recommended settings for performance
#NoEnv
ListLines, Off

; This script will set Ethernet connections as either unmetered. To run this script, run the following command:
; "Location of Autohotkey.exe" [any switches accepted by Autohotkey.exe] "Location of this script" [metered/unmetered]
;
; This script works by modifying the "Ethernet" DWORD in the following registry key:
; HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost 
;
; Note that this script must either be run as the TrustedInstaller user or the above registry key must be modified to grant the 
; "Full Control" permission to whichever user this script will be run as. Instructions can be found here:
; http://www.eightforums.com/tutorials/2815-permissions-allow-deny-access-users-groups-windows-8-a.html#option2

RegWrite, REG_DWORD, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost , Ethernet, 1

ExitApp
