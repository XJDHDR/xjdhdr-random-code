Name: Mark Books as Read
Version: 1.2.1
Category: Gameplay Effects and Changes
Author: XJDHDR
Download locations: Nexus Mods (SE):		Direct Link: https://www.nexusmods.com/skyrimspecialedition/mods/22439
											Ad-supported interstitial link: http://dapalan.com/3050662/mark-books-as-read---nexus-mods-se
											
					Bethesda.net:			Direct Link: https://bethesda.net/en/mods/skyrim/mod-detail/4091993
											Ad-supported interstitial link: http://dapalan.com/3050662/mark-books-as-read---bethesda-net

					Nexus Mods (Oldrim):	Direct Link: https://www.nexusmods.com/skyrim/mods/20910
											Ad-supported interstitial link: http://simizer.com/3050662/mark-books-as-read---nexus-mods

					Steam Workshop:			Direct Link: http://steamcommunity.com/sharedfiles/filedetails/?id=84244648
											Ad-supported interstitial link: http://twineer.com/3050662/mark-books-as-read---steam-workshop


Table of Contents:
==================
Description
Details
Translations
Future plans
Requirements
Install
Update
Uninstall
Complimentary mods
Incompatibilities
Known issues or Bugs
Crashes and performance issues
History
Contact info
Donations
Credits
Tools used
Licensing/Legal


Description
===========
Places a mark on books after you have read them.


Details
=======
When you open a book in the game, the text "~(Read)" is added to the front of the book's name. This does two things. 
First, it tells you which books you have already read. 
Second, all books you have read will be sorted to the bottom of your inventory. 

Q: What effect does this mod have on quest books?
A: The book will have "~(Read)" added to the front of the name after you read it. Otherwise, the book will behave exactly as it is supposed to.

Q: How about spell tomes?
A: Spell tomes will be marked as read when you click on and get the spell from them. This can help you know which spells you've already learned.

Q: Skill books?
A: The book will be marked and you will acquire the skill point from that book.

Q: And books from other mods?
A: This mod will treat them in the same way as books in the base game. They will be marked as read and other effects of that book will still happen as noted above. This includes books added by any of Bethesda's DLC.

Q: Does this mod mark books that I've already read before installing?
A: From version 1.2.0, it will but only the first time after a clean save or loading a save that didn't have the mod.

Q: Can this mod be flagged as an ESL?
A: Yes, and that is exactly what I've done so you don't have to.

Q: Can you port this mod to the PS4 or XBOne?
A: Porting to the PS4 is impossible due to Sony's restrictions on mods. As for the XBOne, it doesn't have SKSE available which my mod heavily depends on. If I do port to the XBOne, it would have to be a heavily cut-down version which I can't promise I will make the effort to create.


Translations
============
My mod has the following languages integrated and will select the correct one based on the game's language:
- English
- French
- German
- Italian
- Russian
- Spanish

If you are interested in helping or simply want this mod in other languages, please send me a message. Please note that I only understand English and so please try to use English if possible in your communications with me.


Future plans
============
I am planning on adding integration with MCM that will add some configuration options for my mod. I have no timeline for this feature though.


Requirements
============
-Skyrim Script Extender (SKSE) v2.0.12 or later - http://skse.silverlock.org/


Install
=======
First, installing mods without using a mod manager is highly discouraged as it can lead to bugs and crashes in your game depending on how many mods you have installed and how they interact with each other. Hence, I can't provide support if you choose to install this mod manually. 

As for using a mod manager, I can't recommend any particular manager as everyone has their own personal preferences in this area. I would say that Wrye Bash ( https://github.com/wrye-bash/wrye-bash ) is a solid choice in this area though there are good reasons to use something else.

Prerequisites
---------------
First, make sure you have installed SKSE and checked that it works properly. Consult it's documentation or ask for help on the Bethesda forums if you have problems.

Second, if you have made any modifications to Papyrus related settings in Skyrim's INI files, please remove them. It is very easy to damage your Skyrim installation by tweaking these values and the defaults are usually good enough. I have also received a few bug reports which I highly suspect were caused by the user changing these values. This reddit post provides a great explanation of these settings: https://reddit.com/r/skyrimmods/comments/2gwvwl/guide_papyrus_ini_settings_and_why_you_shouldnt/

As a result, I have implemented scripting in my mod which will warn you if any of these dangerous tweaks have been made to Skyrim.ini.
If you want to improve your game's scripting performance, the only recommendation I can give is that you need to either improve the game's performance (by buying faster hardware or reducing the graphics settings) or uninstall/optimize any script-heavy mods you have.

Third, I highly recommend setting up SKSE to clear invalid references from your saves. There are two ways you can do this:
 - Easy way:
 -- Download this file and extract the contents into the folder you installed Skyrim and SKSE (by default, C:\Program Files (x86)\Steam\Steamapps\Common\skyrim): https://www.nexusmods.com/skyrimspecialedition/mods/1651/
 - Manual way:
 -- Navigate to the folder you installed Skyrim and SKSE (by default, C:\Program Files (x86)\Steam\Steamapps\Common\skyrim)
 -- Open the Data folder.
 -- Look for a folder called "SKSE". If it exists, open it. If not, create the folder then open it.
 -- Look for a file called "SKSE.ini". If it exists, open it. If not, open Notepad or your favourite text editor.
 -- Add the below text to the file. If [General] already exists, only add the second line below [General]. If "ClearInvalidRegistrations=1" is already present, you don't need to do anything else and can ignore the remaining instructions. If "ClearInvalidRegistrations=0" is already present, change the "0" into a "1".

[General]
ClearInvalidRegistrations=1

 -- Save the changes you made. If you're asked where to save the file, select the SKSE folder mentioned above. Make sure you name the file "SKSE.ini" and change "Save as type" to "All Files (*.*)","All Types (*.*)" or similar.

Fourth, I highly recommend installing the Unofficial Skyrim Special Edition Patch (USSEP). This fixes a huge number of bugs and crashes in the game:
Bethesda.net 		- https://bethesda.net/en/mods/skyrim/mod-detail/2947658
Nexus Mods         	- https://www.nexusmods.com/skyrimspecialedition/mods/266


Bethesda.net
--------------------
Either:
1. Just click on the "Add to Library" button on my mod's webpage then launch Skyrim SE. After that, click on "Mods" in the main menu and log-in. My mod will appear under "My Library".
2. From Skyrim's main menu, click on "Mods". After logging in click on "Search" or press X. Type in this mod's name.
After one of the two above, click on my mod's entry then click on "Download".

Other download source
------------------------
Download the file onto your PC then install it using your favourite mod manager. This is a standard mod containing a plugin and BSA so no special instructions are required to install. Please consult your mod manager's documentation or contact the mod manager's developer(s) if you need help installing mods.


Update
======
Bethesda.net
--------------
(Note: These instructions are a guess because I haven't found any information on how this works). From Skyrim's main menu, click on "Mods" and log-in. Select my mod then click on "Update". Either that or the mod updates itself automatically.

Nexus Mod Manager
-----------------
You will be prompted to download and install the update the next time you start the NMM.

Other download source
------------------------
Download the updated file, install it then uninstall the old version.

A clean save is not required to update this mod. The latest version should cleanly replace any old versions you are using. However, if you are having trouble updating this mod and following the prerequisites above don't help, you can try to do a clean save and see if that helps. This is the procedure:
1. Deactivate "Mark Books as Read.esp" in either Skyrim's launcher or your favourite mod manager.
2. Load the save you want to update.
3. Save your game in a new slot.
4. Repeat 2 and 3 for each save you want to update.
5. Install the latest version of this mod.
6. Reactivate "Mark Books as Read.esp" .


Uninstall
=========
This is a standard mod containing a plugin, BSA and supplementary files so no special instructions are required to uninstall. Please consult your mod manager's documentation or contact it's developer(s) if you need help uninstalling mods.


Complimentary mods
==================
- "Unread Books Glow" by Duggelz: https://www.nexusmods.com/skyrimspecialedition/mods/20679
	Duggelz and others have claimed that UBG is incompatible with my mod. However, I have tested and found that it is perfectly okay to use both mods together. UBG can be used to further help you locate books that you haven't read.
- "Book Covers Skyrim" by DanielCoffey and doccdr: https://www.nexusmods.com/skyrimspecialedition/mods/901
	Massive improvement to the textures used by books and other readables in Skyrim. It improves the resolution of the textures as well as adding unique textures to various special books.
- Any improved bookshelf mod.


Incompatibilities
=================
- "Deja Vu - I Already Read It" by Sagittarius22 - Does pretty much the same thing as this mod. I can't guarantee that your game will work properly if you use both of our mods together.

If you know of any other incompatibilities, please let me know.


Known Issues or Bugs
====================
- Do not save your game immeditately after reading a book. Otherwise, bad things can happen. Just wait 2 or 3 seconds first.
- In the following rare circumstances, a book on the ground might not be marked when you read them. The three possible solutions if this happens is to: 1. Pick up the book then read it from your inventory. 2. Leave the area containing the book then re-enter it. 3. Open the console and type "StopQuest XjMbarBookAliasQuest" then "StartQuest XjMbarBookAliasQuest"
	- An NPC drops a book on the ground.
	- A script spawns a book on the ground.
	- Rarely after you drop a book during or after intensive inventory management. Unfortunately, the current alternative to this point is the increased possibility of Stack Dumps.


Crashes and performance issues
==============================
I've seen a few reports of performance issues when this mod is installed and/or game crashes after uninstalling. Unfortunately, I've never had either of these happen to me. Thus, this is especially difficult to debug.

I believe the crashes are caused by scripts added by my mod becoming glued to your save game. When the mod is uninstalled, the scripts remain and can cause problems.

I have two suggestions for cleaning save games. Make sure you have backups just in case.
The first uses Skyrim Script Extender (SKSE) to clean your save game when you play the game:
	- Install SKSE v2.0.12 or later. You may download and install it from here:  http://skse.silverlock.org/
    - Create the SKSE.ini file that will tell SKSE to clean your save games. There are two ways you can do this:
		Easy:
		- Download this file and extract the contents where you installed Skyrim and SKSE (by default, C:\Program Files (x86)\Steam\Steamapps\Common\skyrim): https://www.nexusmods.com/skyrimspecialedition/mods/1651/

		Hard:
		- Navigate to where you installed Skyrim and SKSE (by default, C:\Program Files (x86)\Steam\Steamapps\Common\skyrim)
		- Open the Data folder.
		- Open the folder called "SKSE". If it doesn't exist, create it.
		- Open the file called "SKSE.ini". If it doesn't exist, open Notepad or your favourite text editor.
		- Add the text below to the file. If [General] already exists, only add the second line. If "ClearInvalidRegistrations=1" is already present, you don't need to do anything else.
		- Save the changes you made. If you're asked where to save the file, select the SKSE folder mentioned above. Make sure you name the file "SKSE.ini" and change "Save as type" to "All Files (*.*)","All Types (*.*)" or similar.
	[General]
	ClearInvalidRegistrations=1

If this doesn't help, my second suggestion is this tool: https://www.nexusmods.com/skyrimspecialedition/mods/5031/?. Again, backups are recommended. If this doesn't fix it either, send me a message and I will try to help.

As for slow performance, I believe this is caused by changing Papyrus related settings in Skyrim's INI files. My mod has scripting in it to detect major tweaks to these specific INI settings. If you see a warning from my mod about these tweaks, remove them.


History
=======
1.2.1 - 2019/02/06 - Added a workaround to fix the inventory screen not immediately updating itself after reading a book in your inventory.
					- Added a workaround to fix the UI not immediately updating itself after reading a book in the game's world.
					- Added a workaround to fix a quirk in Skyrim that causes OnInit events to be sent twice.
					- Added a messagebox to unread books in the game's world with various options. This message box will allow you to choose to read the book or pick it up without reading it.
					- Removed the option of not marking a book while sneaking. The message box addition above effectively removes the need for this feature.
					- Added a Russian and Italian translation.
					- Added a failsafe for message boxes that adds text to them if there is none present.
					- Fixed typos in new install script that caused the script to not work at all. Other small fixes also made to that code.
					- Added multithreading to new install script which massively shortens the time taken to complete.

1.2.0 - 2019/02/01 - Ported version 1.2.0 of this mod from Oldrim to Special Edition.
					- Flagged the plugin as an ESL.



Contact info
=======
You can find me at the following sites under the user 'XJDHDR':
	- Nexus Mods: http://www.nexusmods.com/skyrimspecialedition/users/625820/?
	- Bethesda.net: https://bethesda.net/community/user/xjdhdr
	- Github: https://github.com/XJDHDR
	

Donations
=========
While I don't expect reimbursement for creating or updating my mods and have no plans to charge for them, any donations will be greatly appreciated. If you would like to do so by looking at an advert instead of making a payment, you may use this adf.ly link that redirects to my mod's Nexus Mods webpage:
http://dapalan.com/3050662/mark-books-as-read---nexus-mods-se

Alternatively, donations may be made through PayPal (Nexus Mods account is not required):
http://www.nexusmods.com/skyrimspecialedition/users/donate/?id=625820


Credits
=======
My thanks goes to:

God for creating us all.
Bethesda Game Studios for creating the RPGs I love to play and mod.
Chesko, Hypno88 and H4vent on the Bethesda forums for helping me learn Papyrus and figure out how to make this mod work.
Dragonblood and B1gBadDaddy on the Bethesda forums for providing further help to me in refactoring and optimizing my mod's scripts: https://bethesda.net/community/topic/67647/assign-aliases-in-quest-to-contents-of-a-form-list-possible
Various members of Reddit for providing translations: https://www.reddit.com/r/translator/comments/6lks36/english_spanish_french_italian_and_german/
https://www.reddit.com/r/translator/comments/afpj2n/english_french_german_spanish_please_translate/
https://www.reddit.com/r/translator/comments/ag62ot/english_russian_italian_please_help_translate/
Nexus Mods and Steam Workshop for providing me with a place to host my work.
Wrye Bash team for Wrye Bash, one of my favourite mod managers.
The SKSE team. Without SKSE, this mod would not be possible. 
LHammonds for the Readme Generator this readme was created from.


Tools Used
==========
Creation Kit
7-Zip - http://7zip.org/
Skyrim Script Extender (SKSE) - http://skse.silverlock.org/
Readme Generator - http://lhammonds.game-host.org/obmm/tools_readme_generator1.asp (offline)
Notepad++ - https://notepad-plus-plus.org/
Paint.net - https://www.getpaint.net/
Wrye Bash - https://github.com/wrye-bash/wrye-bash


Licensing/Legal
===============
If you fix a bug or improve this mod in any way, please get in contact with me before uploading it. I will probably either grant permission for you to upload it or I will upload it myself while crediting you for the changes.
You are not allowed to sell this archive or any of it's contents for money or any form of remuneration.
If you want to upload this file somewhere else, please ask me for permission first. It's possible that I will upload it there myself.
