## Installation process:

Before to proceed check if the latest version of Age of Joy, specifically version `0.5`, is available on the [Ithcio page](https://curifab.itch.io/age-of-joy). If not, stay tunned because it will be released soon.

> Just install the APK using [[Sidequest]]

**Backup**: Before proceeding with the installation, it's recommended to save all your game settings and progress (cabinets positions, cabinets, roms, [[MAME]] configurations, etc.) because it could be affected by the new version. You can do this by copying the entire folder `/sdcard/Android/data/com.curif.AgeOfJoy/` to your computer (using [[Sidequest]] for example). 

### News

This latest iteration aims to empower users by expanding the capabilities of [[AGEBasic]], allowing for the customization of every facet of the game. Users can now configure Movie Posters and Lights using AGEBasic functionalities. They can run an AGEBasic program when a [[Room]] is loaded. 
## 0.4 -> 0.5 General change log

- Player behavior (performance):
	- Cabinets loads only when the player is static in a position close to the cabinet's group. Cabinets don't load while the player is walking to do not interrupt the movement.
	- Presentation videos loads when the player are close to the cabinet.
- More rooms. Some of them are big, with capacity to accommodate more than 30 cabinets.
- Player can run a preconfigured [[AGEBasic]] program on Room load. Use this way to configure the Room (changing movie posters for example).
- Movie posters can be customized (change the image poster) using AGEBasic.
- Using AGEBasic the player can query, change intensity and colors of the light in the room.
- Rooms are darkest than the previous version.
- Sound samples tested and working. Check the [[MAME]] page for information.
- A [[Cabinet Artist]] can change the game volume using [[AGEBasic]] in the [[Cabinet Asset]]
- New [[CDL Debug mode]] so [[Cabinet Artist]]s can find issues in its cabinets quickly.

### AGEBasic change log

[[AGEBasic]] is the integrated programing language for [[Age of Joy]]. For more information read the [[AGEBasic programing]] documentation and [[AGEBasic Examples]]

- New `GetMember()` and `CountMembers()` functions to emulate `lists`. In AGEBasic an emulated list is an string separated by an special character.
- New `getFiles()` function to read files from a path.
- `PosterRoomCount()` and `PosterRoomReplace()` functions to replace a Movie Poster in a Room
- The user can execute an `after-load` AGEBasic program globally or for each Room. The program will execute after the room is loaded and allows the user to configure the room. For example, to change the Movie Posters on the walls. Read the [[AGE configuration using files]] document to learn how to activate the new feature.
- File management functions: `GetFiles()` and `CombinePath()`
	- Path functions: `ConfigPath()`,  `AGEBasicPath()`, `CabinetsDBPath()`, `CabinetsPath()` and `RootPath()`
- New introspection function `type(var)`
- Light configuration function: `GetLigths()`, `GetLightIntensity()`, `SetLightIntensity()` and `SetLightColor()`
- Functions to change the volume of the sound globally: `AudioAmbienceGetVolume()`, `AudioGameGetVolume()`, `AudioAmbienceSetVolume()` and `AudioGameSetVolume()`.
- New AGEBasic functions to query files in the file system. To access the most common paths in the game (like the configuration path, cabinet's path, etc.) They are useful in AGEBasic programs.
#### Bug fixes

- `CabDBAssign()` function fails when the name of the cabinet is a number: ex: "1942"
