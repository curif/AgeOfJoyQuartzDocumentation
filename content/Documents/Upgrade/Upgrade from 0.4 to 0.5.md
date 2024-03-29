## Installation process:

Before to proceed check if the latest version of Age of Joy, specifically version `0.5`, is available on the [Ithcio page](https://curifab.itch.io/age-of-joy). If not, stay tunned because it will be released soon.

> 
> Just install the APK using [[Sidequest]] or your preferred installation method.

**Backup**: Before proceeding with the installation, it's recommended to save all your game settings and progress (cabinets positions, cabinets, [[ROM]]s, [[MAME]] configurations, etc.) because it could be affected by the new version. You can do this by copying the entire folder `/sdcard/Android/data/com.curif.AgeOfJoy/` to your computer (using [[Sidequest]] for example). 

## News

### Improvements

Massive graphics, sound and ambient improvements thanks to @Geometrizer.

Game performance improved a lot, again, thanks @Geometrizer.

The game environment now dynamically responds to player movements, enhancing overall performance. Updates include optimizations in how cabinets load and unload, as well as improvements in playing attraction videos.

This update is all about giving players more control over the game using AGEBasic. You can now use AGEBasic to set up things like movie posters and lights, and even make AGEBasic programs run automatically when you enter a new room. 

#### Cabinets

Now it is possible to change the player position in reaction to some events. The typical use case is when the player inserts a coin and an *AGEBasic program* changes its position to look at the screen in an appropriate position.

Also it is possible to change the color, transparency level and set the emission color and material using AGEBasic.

Another important enhancement is the possibility of design which part of a cabinet the player can pass through and which should be solid. Very useful for, for example, cockpit cabinets. Also for cabinets the [[Cabinet Artist]]s now can distribute [[MAME]] files easily in the [[Cabinet Asset]].

It's possible to select cores: [[Cores]]
## 0.4 -> 0.5 Change log

- Player behavior was change to improve the performance:
	- Cabinets loads only when the player is static in a position close to the cabinet's group. Cabinets don't load while the player is walking to do not interrupt the movement. But if the cabinet was loaded previously it pop up immediately.
	- Presentation videos loads when the player are close to the cabinet. A picture will take the place of the video when the player is away or looking from the distance.
- More rooms. Some of them are big, with capacity to accommodate more than 40 cabinets.
- Player can run a preconfigured [[AGEBasic]] program on Room load. Use this way to configure the Room (changing movie posters or lighting for example).
- Movie posters can be customized (change the image poster) using AGEBasic.
- Using AGEBasic the player can query, change intensity and colors of the light in the room.
- Rooms are darkest than the previous version.
- Sound samples tested and working. Check the [[MAME]] page for information.
- Release candidate 4:
	- A [[Cabinet Artist]] can change the game volume using [[AGEBasic]] in the [[Cabinet Asset]] 
	- New [[CDL Debug mode]] so [[Cabinet Artist]]s can find issues in its cabinets quickly. 
	- New *blocker type* part on [[CDL the Cabinet Description Language#Parts]]. Read how to use it in the [[Player Blockers]] manual page.
	- When a room loads, and there are cabinets not assigned, [[Age of Joy]] will assign a random cabinet to each free position.
	- [[Cabinet Artist]]s could deploy [[MAME]] files using the new key `mame-files` key in [[CDL the Cabinet Description Language#MAME files distribution]].
	- New CDL key for `space` metric on cabinets: [[Cabinet space sizes]]. [[Cabinet Artist]]s could flag bigger cabinets to fulfill specifics spaces in the [[Room]]s and to not interfere with the Player transit.
	- There aren't any *required* [[Cabinets]] parts in the new version. On previous ones [[Cabinet Artist]]s **must** include some specific parts. Those parts aren't required anymore, so, for example, it is possible to create a cabinet without a screen or even create piece of furniture in place of cabinets.
	- A new *Cocktail* standard cabinet style to select in yaml with the `style` key. 
	- New `visible` property to hide cabinets parts (like the player head representation).
	- Glass materials: A new `Layer Glass` material to create Bezels for games like Space Invaders (1979). Glass materials has been improved: [[CDL the Cabinet Description Language#Apply a material to parts#Material options]]
	- Player can activate the **Snap Turn Movement** in the [[Visual configuration]] or [[AGE configuration using files]]
	- MAME Core selection between `mame2003+`, `fbneo` and `mame2010`.

### AGEBasic change log

[[AGEBasic]] is the integrated programing language for [[Age of Joy]]. For more information read the [[AGEBasic programing]] documentation and [[AGEBasic Examples]]

- New `GetMember()` and `CountMembers()` functions to emulate `lists`. In AGEBasic an emulated list is an string separated by an special character.
- New `getFiles()` function to read files from a path.
- `PosterRoomCount()` and `PosterRoomReplace()` functions to replace a Movie Poster in a Room
- The user can execute an `after-load` AGEBasic program globally or for each Room. The program will execute after the room is loaded and allows the user to configure the room. For example, to change the Movie Posters on the walls. Read the [[AGE configuration using files]] document to learn how to activate the new feature.
- File management AGEBasic functions: `GetFiles()` and `CombinePath()`
	- Path functions: `ConfigPath()`,  `AGEBasicPath()`, `CabinetsDBPath()`, `CabinetsPath()` and `RootPath()`
- New introspection function `type(var)`
- Light configuration: `GetLigths()`, `GetLightIntensity()`, `SetLightIntensity()` and `SetLightColor()`
- Release candidate 4:
	- Functions to change the volume of the sound globally: `AudioAmbienceGetVolume()`, `AudioGameGetVolume()`, `AudioAmbienceSetVolume()` and `AudioGameSetVolume()`.
	- New AGEBasic functions to query files in the file system. To access the most common paths in the game (like the configuration path, cabinet's path, etc.) They are useful in AGEBasic programs.
	- Functions to query and set the player and cabinet parts in [[3D space]]: `PlayerGetHeight()`, `PlayerSetHeight()`, `PlayerGetCoordinate()`, `PlayerSetCoordinate()`, `PlayerLookAt()`. Check the [[AGEBasic examples - player to look at a screen when insert coin]] for a use case.
	- Added `AND()` and `OR()` functions.
	- `ControlHapticRumble(id, amplitude, duration)` to activate the haptic effect on a control.
	- New CDL keys to manage the emission of a cabinet part: `emmission` [[CDL the Cabinet Description Language#Emission]] includes capacity for color change and [[Emission file mask]].
	- Cabinet parts [[AGEBasic programing#Functions that only applies to a cabinet. In programs related with the cabinet, and packed inside a Cabinet Asset .]]
		- Colors:
			- `CabPartsGetTransparency()` and `CabPartsSetTransparency()` to get and change the transparency level of a cabinet part. 
			- `CabPartsSetColor()` to change the cabinet part's material color.
			- `CabPartsSetEmission()` to activate and deactivate the emission of a part (a button for example)
			- `CabPartsSetEmissionColor()` to set the color of the emission.
		- Rotation and translation of cabinet parts:
			- `CabPartsGetRotation(idx, axis)`: To get the rotation in degrees of the cabinet part. Axis must to be X,Y or Z.
			- `CabPartsSetRotation(idx, axis, angle)` to change the ange of rotation of a cabinet part.
			- `CabPartsGetCoordinate(idx, axis)`: to get the position in the [[3D space]]. Axis must to be X,Y,Z or H. (H is the height from the floor)
			- `CabPartsSetCoordinate(idx, axis, coord)`: to get the position in the [[3D space]]. Axis must to be X,Y, Z or H. Coord is the new coordinate value.
#### Bug fixes

- fixed: `CabDBAssign()` function fails when the name of the cabinet is a number: ex: "1942".
- Release candidate 4:
	- fixed: The player couldn't walk close to a cabinet, the space occupied by the cabinet was miscalculated in the previous version.
	- fixed: Imported models (GLB) are cached even when uploaded to the workshop, so they do not show new changes applied to the model for testing.

# Cabinet artists activities

This version 0.5 comes with many new features, this is a recommendation on what to do to best adapt the cabinets to the new version.

- Follow the [[Cabinet building best practices]] and fulfill the [[CDL best practices checklist]] to improve your cabinet performance.
- If your cabinet is not identified with the usual standard size, change your `description.yaml` according to [[Cabinet Space Sizes]].
- If you have hidden parts inside a model, go and delete them, they are no longer required to be there and consume resources.
- Add `blockers` to block some parts of the cabinet and to free others, so the player can walk through them. [[Player Blockers]]
- Activate and deactivate the [[CDL Debug mode]] to test if any issue appears on your cabinet so you can fix it.
- Check your cabinets, some of them miscalculate the size and [[Age of Joy]] could create some glitches when position it, like floating cabinets for example. To solve the issue add a [[Player Blockers]].
- Improvements you can add to your cabinet:
	- Emissive parts: [[Emission file mask]]
	- Change the player position for a better one on play: [[AGEBasic examples - player to look at a screen when insert coin]]
	- Move cabinet parts in reaction to player actions (like to move a virtual graphic joystick in reaction to the real one).
	- Add files to distribute when the cabinet is uploaded to the game, `mame-files` on [[CDL the Cabinet Description Language#MAME files distribution]]. 
	- Core selection: [[Cores]]

