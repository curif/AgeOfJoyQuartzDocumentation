#agebasic 

BASIC is a popular programming language known for its simplicity and ease of use. It has been used in various applications, especially in the early days of computing.

`AGEBasic` draws its inspiration from another programming language called [Tiny Basic](https://en.wikipedia.org/wiki/Tiny_BASIC) which is a minimalistic version of BASIC. However, AGEBasic does not strictly adhere to all the rules and limitations of Tiny Basic. Instead, it takes inspiration from Tiny Basic and extends or modifies certain features to better suit the requirements and capabilities designed specifically to be executed in [[Age of Joy]].

With AGEBasic the player can develop it's own functions to run in the simulation. Allows to control parts of the game that there aren't available from the [[YAML]] configuration or the [[Visual configuration]].

> [!important] read about the new [[AGEBasic event system]] (version >= 0.6)


## AGEBasic program storage

The main storage for [[Documents/AGEBasic]] programs is `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic` . AGEBasic programs must to end with the `.bas` prefix, like `mixcabinets.bas` or `changecontrols.bas`.

## Variables

AGEBasic supports `numbers` (double precision), hexadecimal (preceded by a `&`) and `strings`.
A variable name can contain letters a numbers only. AGEBasic isn't case sensitive, the variable `A` is the same as `a`. 
`booleans` are not variable type, but anything different than `0` is considered `true`.

Examples:

```vb
10 LET A = 10 'a number 
20 LET A = 10.10 'a number
30 LET A = "AGE of Joy" 'a string
40 LET A = "10" 'a string
50 LET A = 0 'an hex number
```

## Numbered lines

Each line of code should be numbered and be in ascending order. Multiline is supported.

## Sentences

* `LET`: assign a value to a variable, ex: `LET a=10`
* `LETS`: assign multiple values, e.g.: `LETS a,b=10,20` is the same as `let a=10` and next `let b=20`
* `REM`: a comment, ex: `REM this is a comment`. It's the only way to register comments in the program.
* `END`: finish the program
* `IF/THEN/ELSE`: conditional, . Ex: `IF x=1 THEN LET a=2 ELSE a=3`. There aren't available the usual conditional expressions like `AND` and `OR`, but there are functions to replace them. IMPORTANT: ENDIF doesn't exists
* `GOTO`: to jump to a line number. Ex: `GOTO 50`
* `GOSUB`: to jump to a line, and to back using `RETURN`. Ex: `GOSUB 5000`
* `RETURN`: jump back to the next line after the `GOSUB`
* `CALL`: to call a function discarding the result. e.g.: `CALL CabRoomReplace(0, "pacman")`
* `FOR/TO/NEXT/STEP`: to create loops. Ex: `for x=0 to 10 step 2 ... next x`
	* Initial, end  and step values can be expressions.
	* Initial value is computed at start of the cycle.
	* The end value is computed during the `NEXT` sentence execution.
	* The `NEXT` sentence evaluates if the cycle should repeat. At least one cycle is executed always.
* `SLEEP` to sleep a number of seconds, doesn't work in programs executed in the control cabinet (has no sense). E.g.: `SLEEP 1` (sleeps the program during a second). `SLEEP 0.5` sleeps for half of a second. Values must be greater than `0.01`.

# Operators

- Adding, subtraction, etc.: `+`, `-`,`*`,`/`
- Comparison: `=`,`!=`,`<>`,`<`,`>`,`<=`,`>=`
- Logical: and: `&&` or: `||`

## General functions

AGEBasic Functions can receive parameters. Parameters must be enclosed.

### Math

- `ABS`, `COS`, `SIN`, `TAN`, `MOD`
- `INT`: integer part of a number
- `MAX`, `MIN`: of two numbers, Ex: `LET a = max(10,20)` then `a` is 20
- `RND`: a random between two numbers. `rnd(2,10)` could be `8`.
- `NOT`: The inverse of the boolean expression. Ex: `if NOT(0) then goto 100`
- `AND`: to combine two expressions. It returns `1` if both of the input conditions are `!= 0`, otherwise it returns `0`: `AND(a = 0, b = 1)`
- `OR`: to combine two expressions. It returns `1` if at least one of the input conditions is `!= 0`, otherwise it returns `0`.
- `IIF(condition, value1, value2)` returns `value1` if `condition` is `true` else returns `value2`
- `HEXTODEC(string)`: convert from a Hexadecimal string (like `"FF"`) to a number. Remember an hex number is represented by a `&` also. Example `HEXTODEC("FF") = &FF`
- `VAL(string)`: to coarse a string to a number, inversed of `STR(number)`. Example: `VAL("10.5") = 10.5`

### Strings

- `LEN`, `UCASE`, `LCASE`, 
- `SUBSTR`: Ex: `susbtr("abc", 1, 2) ` is "bc", starting in 1 and getting two characters.
- `TRIM`, `LTRIM`, `RTRIM`.
- `STR`: Ex: `str(10)` is `"10"`
#### List simulation

AGEBasic can't manage arrays or lists, but you can simulate them using character separated strings like `aaa:bbb` for example. `aaa` is the member in the position `0`, `bbb` is the one in the position `1` and the separator is `:`.

- `GetMember(string, member #, separator)`: to get a slice of a string. Can be used to emulate lists. Example to get the first member of a list: `GetMember("AGE:of:Joy", 0, ":") = "AGE"`
- `CountMembers(string, separator)` to count how many members a list have: `CountMembers("AGE:of:Joy", ":") = 3`
- `IsMember(string list, string member, separator)` returns `true` if the second string is a member of the first string list. 
- `IndexMember(string list, string member, separator)` returns the index position of the string in the string list if found, or `-1` if not found. Index starts in `0` and ends in `CountMembers()-1`
- `RemoveMember(string list, string member, separator)` returns a new string list without the specified string member.
- `AddMember(string list, string member, separator)` returns a new string list with a new member at the end

### Introspection

- `exists(string)`: to know if a variable is defined, returns 1 or 0 (true or false). Example: `if (exists("myvariable")) then goto 100` jumps to the line # 100 if the variable `"myvariable"` was previously assigned.
- `type(var)`: returns `"STRING"` if the variable is a string or `"NUMBER"` if is a number. Example `if (type(a) == "STRING") the goto 180` jumps to the line # 180 if the variable a is previously assigned with a string like `let a = "test"`

## Screen

* `PRINT` to show text on the screen: `PRINT x,y, text [, 0/1] [, 0/1]`
	* x,y screen coordinates (x: cols, y: rows)
	* text: to print
	* 1 inversed, 0 normal. Optional parameter, 0 is the default.
	* 1 show immediately, 0 don't show and wait for the `SHOW` command (recomended)
* `CLS` to clear the screen
* `SHOW`: to print in the screen the last executed screen commands.
* `FGCOLOR` and `BGCOLOR` commands to set colors depending on the type of screen. `RESETCOLOR` and `INVERTCOLOR` as variants. `SETCOLORSPACE` allows to simulate a computer type (like "c64"):
	* c64
	* ibmpc
	* amstrad
	* cpc
	* zx
	* apple2
	* cpc_mono
	* msx
	* msx_mono
	* to7

### Screen functions

- `ScreenWidth()` : returns the screen width in characters. First is `0` last is `ScreenWidth() - 1` 
- `ScreenLines()` : returns the Height in lines. First is `0` last is `ScreenHeight() - 1` 

### Special characters

You can escape [[AGEBasic characters map codes]] in a string only to print it. The rest of the string functions doesn't take in count the escaped characters, e.g. `STR("a\23") = 4`. 

# Room related

To get information about rooms

- `RoomName()`: The name of the room where the player is.
- `RoomCount()`: How many Rooms are in the game.
- `RoomGet(number)`: Get the name of the room. Ex: `LET name, desc = RoomGet(0)` to get the name and the description of the Room number zero.
- `RoomGetName(number)`: get the name of the room.
- `RoomGetDesc(number)`: to get the description.

# Cabinets related

## Functions for deployed cabinets in rooms

Applies to cabinets deployed in the room where the cabinet controller is loaded.

- `CabRoomCount()`: how many cabinets are in the room
- `CabRoomGetName(number)`: get the cabinet name by its index in the room.
- `CabRoomReplace(number, cabinet name)`: replace a cabinet by another.

## Functions for cabinets administration

Applies to cabinet database (`registry.yaml`) and the [[Cabinets database storage]]. 

- `CabDbCount()`: how many cabinets registered in the storage
- `CabDbCountInRoom(string)`: how many cabinets are *assigned* to one particular room. Ex: `LET count = CabDbCountInRoom("Room001")` 
- `CabDBGetName(number)`: get a cabinet name using the position in the storage. Ex: `CabDBGetName(30)` could return "pacman"
- `CabDBGetAssigned(room, cabinetIndex)`: returns the cabinet name assigned to a position in a room.
- `CabDBDelete(currentRoomName, cabinetIndex)`: delete the cabinet assignment to a room in the database (frees the position).
- `CabDBAdd(room, cabinetIndex, newCabinetName)`: to add a new room/position/cabinet in the database, if the position is taken the program will fail. 
- `CabDBAssign(room, cabinetIndex, newCabinetName)`: assign a cabinet to a existent position in DB. 
- `CabDBSave`: save the database and its changes.

`CabDBDelete`,`CabDBAssign`, `CabDBSave` and `CabDBAdd` returns 0 if fails, 1 if not.

## Functions that only applies to a cabinet. 

In programs related with the cabinet, and packed inside a [[Cabinet Asset]].

Cabinet's parts are named (see the [[CDL the Cabinet Description Language#Configuring cabinet parts]]) and are identified by its position too. You can use one or each other when you need to call a function who uses a cabinet part, an index is preferred if you will call more than one function for the same part (by performance considerations).

The program fail when you name a part incorrectly or when the index is incorrect. See [[AGEBasic programing#Debug mode]] to learn how to debug your program.

- `CabInsertCoin()`: insert a coin in the cabinet.
- `CabPartsCount()`: return the cabinet's parts count.
- `CabPartsName(idx)`: given a part number (starting in cero), return the name of the part, e.g.: `CabPartsName(7)` returns "joystick". 
- `CabPartsPosition(name)`: given the name of a part return it's position on the Cabinet parts list. 
- `CabPartsEnable(idx, enable)`: given a part number or a part name (`idx`),  and a Boolean (remember Booleans are numbers, a true value is anything different to cero), will disable or enable it. When a part is disabled you can't see it in VR. 
- Position in space: 
	- `CabPartsGetCoordinate(idx, string type)` to get the position in [[3D space]]. `type` could be "X", "Y" or "Z" . Refers to the position of the object starting on the cabinet's base (local coordinate). You can also use `CabPartsGetGlobalCoordinate()` to get the part coordinates in the Global 3D space.
	- `CabPartsSetCoordinate(idx, string type, number coord)`, like `CabPartsGetCoordinate` but to set the part's position relative to the cabinet. `CabPartsSetGlobalCoordinate()` is also available.
	- `CabPartsGetRotation(idx, string type)` and `CabPartsSetRotation(number part idx, string type, number angle)` to get and set the rotation of a cabinet part. **NOTE**: The `CabPartsRotate` could get better results.
	- `CabPartsRotate(idx, string type, number angle)` to rotate locally a part. Available in v0.6.
	- `CabPartsGetGlobalRotation()` and `CabPartsSetGlobalRotation()` to get set the global rotation. 
- `CabPartsGetTransparency(idx)`: returns the part's transparency percentage.
- `CabPartsSetTransparency(idx, percentage)`: set part's transparency to a percentage (0 to 100).
- `CabPartsSetEmission(idx, true/false)`: activate the emissive material on the part if it's possible. You should probable set an emission color too.
- `CabPartsSetEmissionColor(idx, r, g, b)` to set the *emission* color. The color will blend with the main texture, if any.
- `CabPartsSetColor(idx, r, g, b)` to set the color. The color will blend with the main texture, if any.

Examples:

```vb file="onload.bas"
10 let base = CabPartsPosition("joystick-base")
20 lets baseX, baseZ, baseH = CabPartsGetCoordinate(base, "X"), CabPartsGetCoordinate(base, "Z"), CabPartsGetCoordinate(base, "H")
30 let transp = CabPartsGetTransparency("bezel")
40 call CabPartsSetTransparency("bezel", transp + 10)

70 call CabPartsEmission("joystick-button", 1)
80 call CabPartsSetEmissionColor("joystick-button", 190, 20, 20)
90 call CabPartsSetColor("left", 200, 0, 0)
```

### Audio parts in cabinets

According to the yaml cabinet configuration you can set a `part` of a cabinet to be a _speaker_. You can also change some properties on AGEBasic:

- `CabPartsAudioPlay(name)`: Play the audio associated with the specified part. Given the name of a part, it triggers the audio playback. For example, `CabPartsAudioPlay("speaker")` will start playing the audio from the part named "speaker".
- `CabPartsAudioStop(name)`: Stop the audio associated with the specified part. Given the name of a part, it stops the audio playback. For example, `CabPartsAudioStop("speaker")` will stop the audio from the part named "speaker".
- `CabPartsAudioPause(name)`: Pause the audio associated with the specified part. Given the name of a part, it pauses the audio playback. For example, `CabPartsAudioPause("speaker")` will pause the audio from the part named "speaker".
- `CabPartsAudioVolume(name, volume)`: Set the audio volume for the specified part. Given the name of a part and a volume value (0.0 to 1.0), it adjusts the volume. For example, `CabPartsAudioVolume("speaker", 0.5)` will set the audio volume of the part named "speaker" to 50%.
- `CabPartsAudioDistance(name, minDistance, maxDistance)`: Set the minimum and maximum distance for 3D audio effects for the specified part. Given the name of a part and the min/max distances, it adjusts the 3D audio settings. For example, `CabPartsAudioDistance("speaker", 1.0, 5.0)` sets the 3D audio distance for the part named "speaker".
- `CabPartsAudioFile(name, filePath)`: Assign an audio file to the specified part. Given the name of a part and the file path, it loads the audio file into the part. For example, `CabPartsAudioFile("speaker", "gong.mp3")` assigns the "gong.mp3" file to the part named "speaker".
- `CabPartsAudioLoop(name, loop)`: Set the looping behavior for the specified part's audio. Given the name of a part and a boolean value (`true` or `false`), it enables or disables audio looping. For example, `CabPartsAudioLoop("speaker", true)` enables looping for the part named "speaker".

Read more about cabinet's programs in [[AGEBasic in cabinets]].
### Cabinet events

Functions that interacts with the [[AGEBasic event system]].

- `EventTrigger(event name string)`: activate an event.

# Room

Functions related with the loaded rooms.

## Room Posters

To replace posters in a Room
- `PosterRoomCount()` returns the poster count of the actual room.
- `PosterRoomReplace(position #, Image path)` to replace a poster by an image in disk. Example: `PosterRoomReplace(1, CombinePath(ConfigPath(), "posters/myposter.png"))` to replace the second poster in the room.


## Light configuration

- `GetLigths()` to get a list string with the names of the lights present in the loaded rooms, separated with `|` (pipes) in the form `"<light name>|<ligth name>|..."`. Each light name have a room name and the light name for identification, example: `"room001:light1` the final `GetLigths()` result example is `"room001:light1|room003:ligth1"`. You can use `GetMember()` to process the string using the pipe as a separator, and also to process the light name. 
- `GetLightIntensity(string light name)`: to get the intensity of a light. Should be a number between `0` (no light, turned off) and `10` (too bright). example: `GetLightIntensity("room001:ligth1") = 0.5`. You can get the light name from `GetLights()`
- `SetLightIntensity(string light name, number intensity)`: to set the intensity of a light, example `SetLightIntensity("room001:ligth1", 0.5)`
- `SetLightColor(string light name, number R, number G, number B)`: set the color of the light, you will need the desired RGB color.  Returns `0` on error.

# Audio

[[Age of Joy]] plays two type of sounds: *ambience* (noise in rooms) and *games* sound. The volume of the audio is expressed in `dB`: `0` is normal, `20` as loud max, and -`-80` as silent. These values affect all the rooms and all the games.

To mute a sound set its volume to `-80`, and to unmute it simply set it to the previous volume value.

If you write a script for a cabinet (read [[CDL the Cabinet Description Language]]) that changes the volume of a game (for example), remember to change it to its previous value in order to not affect other games.
## Get/Set Volume

- `AudioAmbienceGetVolume()`, `AudioMusicGetVolume()` and `AudioGameGetVolume()` to get the volume in `dB`.
- `AudioAmbienceSetVolume(number volume)`, `AudioMusicSetVolume(number volume)` and `AudioGameSetVolume(number volume)` to set the volume, also in `dB`.

## Music

To play music (Jukebox functions). 
All the audio files (like `mp3` or `ogg`) should be saved in the `/sdcard/Android/data/com.curif.AgeOfJoy/music` folder. To easily get that folder during an AGEBasic program execution use the `MusicPath() `function.
The programmer should add all the audio files that the player want to ear in a queue, and the play it (the play action is in order)
### Music functions

- `MusicAdd(audio file path)`: add an audio file to the queue.
- `MusicExists(audio file path)`: true if the file is in the jukebox queue.
- `MusicRemove(audio file path)`: remove the file from the jukebox queue. Return `true` if removed.
- `MusicClear()`: clear the audio queue.
- `MusicAddList(files, separator)`: to add a group of audio files to the queue. Files is a list simulated string like `song1.mp3:song2.mp3`, you can use `FileGet` to get the files. 
- `MusicLoop(true/false)`: to activate/deactivate the loop function. `MusicLoopStatus()` to query the music loop status.
- `MusicNext()` and `MusicPrevious()` to jump to the next or previous song.
- `MusicReset()` start playing again the music queue.
- `MusicCount()` count of files in the music queue.

# Player

It's possible to change the position of the player in the [[3D space]]:

- `PlayerGetHeight()`, `PlayerSetHeight(number)`: to get and set the height of the player. It's recommended to get the height and changing it by adding or decrementing its value.
- `PlayerGetCoordinate(string coord)`, `PlayerSetCoordinate(string coord, value)`: to get and set the coordinates in the [[3D space]] (force the player to a new position). `coord` should bet "X" or "Z". "Y" cant be changed, use `PlayerSetHeight` instead.
- `PlayerLookAt(cabinet part number)`: to force the player to look at a part of the cabinet. For example the screen. Can be used only in [[AGEBasic in cabinets]] mode.
- `PlayerTeleport(string room)`: to teleport the player to a room. The string is the room name (like "room001" for example.)

It's recommended to read the [[AGEBasic examples - player to look at a screen when insert coin]].

# Controllers

It's possible to query the control status, for example, to know if a user is pressing some button on the controller.

- `ControlActive(id [, port])`: to know the status of a control. Returns `True (1)` if the control is active on the moment of execution, or `False (0)` if not. The `id`s of the controls (like buttons) are in the table in the page: [[Default controllers configuration mapping]]. `[port]` is an optional port number (`0` is the default). `ControlActive` can be used in [[AGEBasic in cabinets]] or in programs to execute in the [[Configuration control cabinet]]. Note: `port` is available in the `0.5` version and superior.
- `ControlHapticRumble(id, amplitude, duration)`: to create a vibration on the controller. `duration` is a decimal where `1` means *one second*. `amplitude` is a decimal number too. `id` should be `JOYPAD_LEFT_RUMBLE` or `JOYPAD_RIGHT_RUMBLE`. Returns `true` if the controller support haptic feedback.

# Data manipulation
Sometimes you will need to storage and read information for your programs.

## Data - READ - RESTORE combo
To add information to be consumed during the program execution.
You could storage information in different "storage" that lives during the program execution. Each storage has its name.

- `DATA "storage name", x,y,z, ...`: comma separated list of expressions. Example: `DATA "my storage", 10, "x", D + 1`. Expressions are evaluated during the line execution not when the storage is read.
- `READ "storage name", var, var, ...`: to read a storage, Example: `READ "my storage", A, B, C` to read the storage of the previous example, result: `A=10, B="x", C=D+1`. There is an internal pointer to identify which is the next data to be read.
- `RESTORE "storage name", offset`: move the pointer to the `offset` position.

## File management

- `GetFiles(path, separator, order)` get a list string with the file names of a path, parameters: path to scan, string separator, and order. You could use `CountMembers()` and `GetMember()` to process the result. Order:
	- `0`: alphabetic order
	- `1`: random
	- `2`: Creation date from old to new
	- `3`: Creation date from new to old
		example:  `let f = getFiles("path\\to\\files", ":", 3)` to get `"file1.txt:file2.txt:xxx.bas"` then  `GetMember(f, 1) = "file2.txt"`
- `CombinePath(path1, path2)` given two paths, return a string with the combination. Example: `CombinePath("/sdcard", "file.txt")` returns `/sdcard/file.txt`
- `ConfigPath()` returns the path to the configuration files.
- `AGEBasicPath()` returns the path to the AGEBasic programs.
- `CabinetsDBPath()` returns the path to the cabinet database.
- `CabinetsPath()` returns the path to the new cabinets. (usually empty)
- `RootPath()` the base path of AGE of Joy. Isn't the Android root home.
- `MusicPath()` the base path to the music folder.

# CPU control

You can increase the CPU load, but take in consideration that it could affect the overall game performance. The use of CPU is administered internally by using delays in the program execution (interline execution).
- `GetCPU()`: obtain the actual CPU percentage used for program executions. 
- `SetCPU(percentage)` to set the maximum CPU percentage. `100` is the max value.

The default CPU percentage is `76%`

# Debug mode

The AGEBasic developer has the option to enable Debug Mode within a program or a setup, such as in a programming YAML subdocument within a cabinet's configuration.

Once DebugMode is activated (true), [[Age of Joy]] will generate a report upon completion, detailing the most recent error (both compilation and runtime errors), along with the final program status, encompassing variable specifics like names, types, and values.

- `DebugMode(true/false)`

Example:

```vb
1000 let i = 100
1010 call DebugMode(1) 'activate the debug mode
1020 let ERROR = "some error message to see in debug"
```

Result:

```txt
Program: myprogram.bas
PROGRAM STATUS ---
PROGRAM: myprogram.bas
Last line parsed: 1020 executed: 3
vars: 
I: 100 [Number]
ERROR: some error message to see in debug [string]
---
```

You can find the result file in the folder: `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic`

The name of the file sould be:  `myprogram.bas.debug` (the file name of the program with the `.debug` suffix)

---

If you want to use ChatGPT to ask for programs, just follow this [[AGEBasic prompt for ChatGPT]]

[[AGEBasic Examples]]
