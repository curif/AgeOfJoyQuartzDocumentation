# Update from 0.3 to 0.4

> [!warning] This version `0.4` isn't compatible with  `0.3`, you need to follow a process to install it. 
> During the installation you will need to uninstall the previous version and all your game data will be deleted (cabinets, positions, etc), please follow the installation process to avoid issues.


## Installation process:

Only if it isn't your first install.
Before to proceed check if the latest version of Age of Joy, specifically version `0.4`, is available on the [Ithcio page](https://curifab.itch.io/age-of-joy). If not, stay tunned because it will be released soon.

1. Backup: Before proceeding with the installation, it's recommended to save all your game settings and progress (cabinets positions, cabinets, roms, [[MAME]] configurations, etc.) because it will be deleted in the uninstallation process. You can do this by copying the entire folder `/sdcard/Android/data/com.curif.AgeOfJoy/` to your computer (using [[Sidequest]] for example). Alternatively, you can rename the folder to something else to keep it safe (but it was not tested).
2. Uninstall [[Age of Joy]]: On your Quest device, find the Age of Joy game and uninstall it. This step ensures that you're starting fresh with the new version. All your data will be deleted.
3. Install the new version:  If the new version is available, download and install it on your Quest device. 
4. Restore your backup: Finally, after installing the new version, copy the contents of the backup you created earlier back to the `/sdcard/Android/data/com.curif.AgeOfJoy/` location on your Quest device. This will restore all your previous configurations, including cabinet positions, cabinets, roms, and MAME settings.

## 0.3 -> 0.4 Changelog

### News

The [[Discord server]] community exceeded 400 cabinets!

* New [[Visual configuration]]:
	* Follow the [[Visual configuration manual]] to fully understand how it works.
	* Additionally, the configuration settings that were previously available in the [[AGE configuration using files]]  can now also be accessed and modified through the new Visual configuration too.
* [[AGEBasic]] to control in-game behavior using the BASIC programming language. You can write your own programs to change the game as you wish. There are examples about how to mix cabinets for example.
* External controls: The game now supports gamepad and compatible controls. You can connect and use a gamepad, as well as other compatible control devices like Bluetooth controllers. USB controllers have not undergone testing yet; however, they are expected to be compatible and function properly.
* Users said that AOJ works in Quest 3, but isn't fully tested yet.
* Controller configuration: There are two ways to configure controls. The first method is via CDL ([[CDL the Cabinet Description Language]]), which is a language used by the cabinet modeler artist to set up controls. The second method is using the Visual Configuration, which provides a more user-friendly interface for configuring controls.
* Rooms: Rooms now have some new features. 
	* Each room has a name assigned to it, making it easy to identify and refer to specific rooms. You can find the name and code of a room in the [[Configuration control cabinet]].
	* There are also "thematic" rooms available. The first one is inspired by the Dungeons & Dragons style, designed to create a more fantasy-like atmosphere for retro-medieval-fantasy games. More room styles are planned to be added in the future. 
	* The are six more rooms than in the previous version, counting 13 rooms at the moment of write this document.
	* In certain situations, the use of stairs is required to access specific rooms within the Gallery. This is because the Gallery now features multiple levels, resulting in a layout with varying elevations. To reach certain rooms, you will need to navigate and ascend or descend using the stairs provided. The introduction of multiple levels adds depth and dimension to the Gallery, creating a more dynamic and immersive environment.
* Cabinets:
	*  The placement of cabinets within rooms can now be customized using the new Visual configuration enhancement.
	* On the floor in front of each cabinet, there is a sticker that displays the cabinet's number. This sticker serves as a visual identifier for the cabinet, making it easier to locate and replace the cabinet with another game. The number on the sticker helps users accurately identify and keep track of each cabinet, facilitating the process of cabinet replacement.
	* There are functions in [[AGEBasic]] to control a cabinet.
	* New [[Configuration control cabinet]], you can find one on each room.
* Player (you):
	* Your height could be configured using visual/file configuration. Useful to play seated too.
	* Walk velocity and rotation configuration.
* Teleportation:
	* In room teleportation: the user now can jump to specific places (like a door o to the front of a cabinet) to avoid sickness motion effect, read more in [[In Room Teleportation]].
	* Room teleportation: now you can teleport to any room using the menu in the [[Configuration control cabinet]]
* When a coin is inserted into a cabinet, the visual representation of the hands in the virtual environment changes to that of a controller. This alteration serves as a visual indicator to signify that the user has entered game mode. Some cabinets might change that visual representation, e.g. for a weapon in light guns games.
* Light guns: Light guns let you play games where you point and shoot at the screen. E.g.: duck hunt
* New Movie Pictures from the 90s.
* New real Pictures added.
* New textured hands.
* Extensive documentation: [[Index]]

## Tech stuff

* Moved from OVR SDK to OpenXR
* Moved `cabinetsdb/registry.json` to a [[YAML]] format (but if you copy a `registry.json` file it will be used)
* Moved to the last LTS Unity version.
* Packages upgrade to the last version.
* Removed experimental packages.
* New NPC navigation system.

### Bug fixes

- Performance issues:
	- The loading of cabinets has been improved compared to the previous version.
	- Several rooms that were previously causing performance problems have been fixed. You should notice smoother performance in those rooms now.
- The positioning of cabinets on the floor has been fixed. Previously, some cabinets were incorrectly placed on the floor, causing them to appear shorter than their actual height. This issue has been resolved, and the cabinets should now be correctly positioned and visually accurate in terms of height.
- Memory and file corruption issues solved.
- A lot of minor bug fixes, most of them registered in the issues section in GitHub.

### known bugs

- Save states are disabled, which breaks most of the games.
- Hangs are expected.

#v0_4 