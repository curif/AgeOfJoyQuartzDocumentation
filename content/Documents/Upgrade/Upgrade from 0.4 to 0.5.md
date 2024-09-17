## Installation process:

Before to proceed check if the latest version of Age of Joy, specifically version `0.5`, is available on the [Ithcio page](https://curifab.itch.io/age-of-joy). If not, stay tunned because it will be released soon.

> 
> Just install the APK using [[Sidequest]] or your preferred installation method.

**Backup**: Before proceeding with the installation, it's recommended to save all your game settings and progress (cabinets positions, cabinets, [[ROM]]s, [[MAME]] configurations, etc.) because it could be affected by the new version. You can do this by copying the entire folder `/sdcard/Android/data/com.curif.AgeOfJoy/` to your computer (using [[Sidequest]] for example). 

## News

### Improvements

Massive graphics, sound, NPCs and ambient improvements thanks to @Geometrizer.

Game performance improved a lot, again, thanks @Geometrizer.

Expanded emulation library! We've added more machine emulators (cores) and given you the ability to add your own. Be aware that some user-added cores may not work. @**Emashzed**

The game environment now dynamically responds to player movements, enhancing overall performance. Updates include optimizations in how cabinets load and unload, as well as improvements in playing attraction videos.

We've significantly improved NPCs with diverse styles and lifelike animations. @Geometrizer

This update is all about giving players more control over the game using AGEBasic. You can now use AGEBasic to set up things like movie posters and lights, and even make AGEBasic programs run automatically when you enter a new room. 

Sharp quality increase in audio fidelity in most cores. Vulkan specific tweaks.
#### Cabinets

A new event system, combined with the introduction of physical parts, empowers [[Cabinet Artist]]s to create more dynamic and interactive environments. Artists can now define whether specific cabinet parts should respond to environmental factors like gravity or player interaction by marking them as "physical." When used with the new **AGEBasic** event system, this unlocks a wide range of creative possibilities, enabling cabinets to react to the player's actions or changes in the environment, resulting in more immersive experiences.

Now it is possible to change the player position in reaction to some events. The typical use case is when the player inserts a coin and an *AGEBasic program* changes the player to look at the screen in an appropriate position.

Also it is possible to change the color, transparency level and set the emission color and material using AGEBasic.

Another important enhancement is the possibility of design which part of a cabinet the player can pass through and which should be solid. Very useful for, for example, cockpit cabinets. Also for cabinets the [[Cabinet Artist]]s now can distribute [[MAME]] files easily in the [[Cabinet Asset]].

It's possible to select cores: [[Cores]]
## 0.4 -> 0.5 Change log

- Player behavior was changed to improve the performance:
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
- Release candidate 5:
	- New `CRT` and `Projector` Shader: [[CDL the Cabinet Description Language#CRT shader]] @geometrizer
	- If needed you can save your ROM for different cores using this pattern:  `/sdcard/Android/data/com.curif.AgeOfJoy/downloads/<core>/` to separate your [[ROM]]s in different cores. For example: `/sdcard/Android/data/com.curif.AgeOfJoy/downloads/fbneo/myrom.zip` @emashzed
	- New `control-scheme` to repeat the same control scheme configuration for a cabinet. @emashzed
	- New sliding doors. @geometrizer
	- `insert-coin-on-startup`: in CDL to do not start the game when you insert a coin. @emashzed
	- CRT Ratio: to change the scale ratio of a CRT in CDL. @emashzed
	- Device detection (Q2/Q3): @emashzed
	- Adapted emulation cores to support VULKAN hardware interface: @emashzed
	- Foveated rendering: optimize performance by concentrating rendering resources on the area of the display where the user is looking. @emashzed
	- User core selection: [[Cores]] @emashzed
	- Boost the resolution of the eye texture during gameplay. @emashzed
	- Cache for GLB, parts and images has been improved (repeated GLB files are not stored multiple times). @emashzed
	- [[ASTC textures]] to improve cabinets performance. @emashzed
	- Added new `CRT` types: [[CDL the Cabinet Description Language#Monitor (CRT) Configuration]] @geometrizer
	- Default controller input changed: [[Quest Controllers#Exit emulation]]
	- Added new [[AGEBasic]] `CRT`: `19i-agebasic` a CRT type to only process [[AGEBasic]] programs. ```
				crt:
				  type: 19i-agebasic
				  orientation: horizontal
				  screen:
					    shader: CRT```
- Release candidate 6:
	- New physical system for cabinets parts: [[Cabinet physical parts manual]]
	- Posters and pictures remade.
	- New CRT models (read [[CDL the Cabinet Description Language#Monitor (CRT) Configuration]])
	- Strong cache system to avoid memory problems and speedup cabinet loading.
	- NPC refactoring and new actions/movements.
	- fbneo lightguns.
	- Multiple cores per cabinet.
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
	- Added `IIF()`, `AND()` and `OR()` functions.
	- `ControlHapticRumble(id, amplitude, duration)` to activate the haptic effect on a control.
	- New CDL keys to manage the emission of a cabinet part: `emmission` [[CDL the Cabinet Description Language#Emission]] includes capacity for color change and [[Emission file mask]].
- Release candidate 5:
	- Cabinet parts [[AGEBasic programing#Functions that only applies to a cabinet. In programs related with the cabinet, and packed inside a Cabinet Asset .]]
		- Colors:
			- `CabPartsGetTransparency()` and `CabPartsSetTransparency()` to get and change the transparency level of a cabinet part. 
			- `CabPartsSetColor()` to change the cabinet part's material color.
			- `CabPartsSetEmission()` to activate and deactivate the emission of a part (a button for example)
			- `CabPartsSetEmissionColor()` to set the color of the emission.
		- Rotation and translation of cabinet parts:
			- `CabPartsGetRotation(idx, axis)`: To get the rotation in degrees of the cabinet part. Axis must to be X,Y or Z.
			- `CabPartsSetRotation(idx, axis, angle)` to change the ange of rotation of a cabinet part counting from the origin.
			- `CabPartsGetCoordinate(idx, axis)`: to get the position in the [[3D space]]. Axis must to be X,Y,Z or H. (H is the height from the floor)
			- `CabPartsSetCoordinate(idx, axis, coord)`: to get the position in the [[3D space]]. Axis must to be X,Y, Z or H. Coord is the new coordinate value.
			- `DATA/READ/RESTORE` to add data to your programs.
		- Jukebox/music AGEBasic functions: read the [[Jukebox]] manual: MusicPlay, MusicAdd, MusicRemove, MusicClear,  MusicLoop,  MusicAddList, MusicPrevious and  MusicNext
		- `ControlActive()` accepts the port as parameter.
		- Screen:   `ScreenWidth()` and `ScreenHeight()`
		- String lists management:  `IsMember()`, `IndexMember()`, `AddMember()` and `RemoveMember()`
		- Play lists: cycle through games with Left Trigger + Left thumb click while playing.
- Release candidate 6:
	- New [[AGEBasic event system]]
	- It's possible to change the CPU performance.
	- To work with a data collection the DATA/READ/RESTORE commands combination has been added.
	- `CabPartsRotate(idx, axis, angle)` to rotate a part from the actual position.
	- `VAL()` to coarse strings to numbers.
	- `PlayerTeleport()` to jump to a room.
	- `HEXTODEC()` to use hexadecimal numbers.
	- `FGCOLOR` and `BGCOLOR` commands to set colors depending on the type of screen. `RESETCOLOR` and `INVERTCOLOR` as variants. `SETCOLORSPACE` allows to simulate a computer type (like "c64")
- Release candidate 7:
	- `CabPartsList()` to get a list of cabinet parts.
		
#### Bug fixes

- fixed: `CabDBAssign()` function fails when the name of the cabinet is a number: ex: "1942".
- Release candidate 4:
	- fixed: The player couldn't walk close to a cabinet, the space occupied by the cabinet was miscalculated in the previous version.
	- fixed: Imported models (GLB) are cached even when uploaded to the workshop, so they do not show new changes applied to the model for testing.
- Release candidate 5:
	- Fixed sound bug regarding duplicated cabinets in the same room.
	- Fix color gamma from some shaders and image conversion @emashzed
- Release candidate 6.
	- Too many to count them...

# Cabinet artists recommendations

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

## Special thanks

- **To our amazing community:** Your ideas and bug reports are invaluable. They help us continuously improve Age of Joy.
- **To all the talented cabinet artists:** You bring Age of Joy to life with your stunning creations. Without you, it would be a pale imitation of its full potential.
- **A huge shout-out to @DangerMiaus:** Your tireless support, testing efforts, and dedication to the community are truly appreciated!
- **to @ramiroramos**: for the effort to create a MR version (not ready yet)
- **to @angellicide and @dmacell** for the cabinet database.
- Sorry if I forget someone.

Other honorable mentions to @VRCop for technical ideas. @WilsonVR for be there from the very start. @dedhead616, @flannelot...

**And to anyone else who has contributed:** If we've missed you here, please know that we deeply appreciate your involvement in Age of Joy!
