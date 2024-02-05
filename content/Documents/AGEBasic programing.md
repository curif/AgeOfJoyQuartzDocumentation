#agebasic 

BASIC is a popular programming language known for its simplicity and ease of use. It has been used in various applications, especially in the early days of computing.

`AGEBasic` draws its inspiration from another programming language called [Tiny Basic](https://en.wikipedia.org/wiki/Tiny_BASIC) which is a minimalistic version of BASIC. However, AGEBasic does not strictly adhere to all the rules and limitations of Tiny Basic. Instead, it takes inspiration from Tiny Basic and extends or modifies certain features to better suit the requirements and capabilities designed specifically to be executed in [[Age of Joy]].

With AGEBasic the player can develop it's own functions to run in the simulation. Allows to control parts of the game that there aren't available from the [[YAML]] configuration or the [[Visual configuration]].


> [!warning] 
> The contents of this document applies to [[Age of Joy]] version 0.4-RC04 or superior.

## AGEBasic program storage

The main storage for [[Documents/AGEBasic]] programs is `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic` . AGEBasic programs must to end with the `.bas` prefix, like `mixcabinets.bas` or `changecontrols.bas`.

## Variables

AGEBasic supports `numbers` (double precision) and `strings`.
A variable name can contain letters a numbers only. AGEBasic isn't case sensitive, the variable `A` is the same as `a`. 
`booleans` are not variable type, but anything different than `0` is considered `true`.

## Numbered lines

Each line of code should be numbered and be in ascending order.

## Sentences

* `LET`: assign a value to a variable, ex: `LET a=10`
* `LETS`: assign multiple values, ex: `LETS a,b=10,20`
* `REM`: a comment, ex: `REM this is a comment`. It's the only way to register comments in the program.
* `END`: finish the program
* `IF/THEN`: conditional, ELSE and ENDIF are not allowed. Ex: `IF x=1 THEN LET a=2`
* `GOTO`: to jump to a line number. Ex: `GOTO 50`
* `GOSUB`: to jump to a line, and to back using `RETURN`. Ex: `GOSUB 5000`
* `RETURN`: jump back to the next line after the `GOSUB`
* `CALL`: to call a function discarding the result. Ex: `CALL CabRoomReplace(0, "pacman")`
* `FOR/TO/NEXT/STEP`: to create loops. Ex: `for x=0 to 10 step 2 ... next x`
	* Initial, end  and step values can be expressions.
	* Initial value is computed at start of the cycle.
	* The end value is computed during the `NEXT` sentence execution.
	* The `NEXT` sentence evaluates if the cycle should repeat. At least one cycle is executed always.

## Screen sentences

* `PRINT` to show text on the screen: `PRINT x,y, text [, 0/1]`
	* x,y screen coordinates (x: cols, y: rows)
	* text: to print
	* 1 inversed, 0 normal. Optional parameter, 0 is the default.
* `CLS` to clear the screen
* `SHOW`: to show the last executed screen commands.

## Functions


Functions can receive parameters. Parameters must be enclosed.

### Math

- `ABS`, `COS`, `SIN`, `TAN`, `MOD`
- `MAX`, `MIN`: of two numbers, Ex: `LET a = max(10,20)` then `a` is 20
- `RND`: a random between two numbers. `rnd(2,10)` could be `8`.
- `NOT`: The inverse of the boolean expression. Ex: `if NOT(0) then goto 100`

### Strings

- `LEN`, `UCASE`, `LCASE`, 
- `SUBSTR`: Ex: `susbtr("abc", 1, 2) ` is "bc", starting in 1 and getting two characters.
- `TRIM`, `LTRIM`, `RTRIM`.
- `STR`: Ex: `str(10)` is `"10"`
- `GetMember(string, member #, separator)`: to get a slice of a string. Can be used to emulate lists. Example to get the first member of a list: `GetMember("AGE:of:Joy", 0, ":") == "AGE"`
- `CountMembers(string, separator)` to count how many members a list have: `CountMembers("AGE:of:Joy", ":") == 3`

### File management

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

### Introspection

- `exists(string)`: to know if a variable is defined, returns 1 or 0 (true or false). Example: `if (exists("myvariable")) then goto 100` jumps to the line # 100 if the variable `"myvariable"` was previously assigned.
- `type(var)`: returns `"STRING"` if the variable is a string or `"NUMBER"` if is a number. Example `if (type(a) == "STRING") the goto 180` jumps to the line # 180 if the variable a is previously assigned with a string like `let a = "test"`

### Room related

To get information about rooms

- `RoomName()`: The name of the room where the player is.
- `RoomCount()`: How many Rooms are in the game.
- `RoomGet(number)`: Get the name of the room. Ex: `LET name, desc = RoomGet(0)` to get the name and the description of the Room number zero.
- `RoomGetName(number)`: get the name of the room.
- `RoomGetDesc(number)`: to get the description.

### Cabinets related

Applies to cabinets deployed in the room where the cabinet controller is loaded.

- `CabRoomCount()`: how many cabinets are in the room
- `CabRoomGetName(number)`: get the cabinet name by its index in the room.
- `CabRoomReplace(number, cabinet name)`: replace a cabinet by another.

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

Functions that only applies to a cabinet. In programs related with the cabinet, and packed inside a [[Cabinet Asset]].

- `CabPartsCount()`: return the cabinet's parts count. Returns -1 when error (for example if the programmer tries to use it in other place than in a cabinet's asset)
- `CabPartsName(idx)`: given a part number (starting in cero), return the name of the part, eg: "joystick". Returns `""` when error (not in a cabinet's asset, or the part number not exists)
- `CabPartsPosition(name)`: given the name of a part return it's position on the Cabinet parts list. Returns `-1` when error (not in a cabinet's asset, or a part doesn't exists with the provider name)
- `CabPartsEnable(idx, enable)`: given a part number and a boolean (remember booleans are numbers, `true` is anything different to cero), will disable or enable it. When a part is disabled you can't see it in VR. Returns `-1` on error.
- `CabPartsGetCoordinate(string coord, number idx)` to get the `coord` position in [[3D space]]. `coord` could be "X", "Y", "Z" or "H". In particular `H` refers to the position of the object starting on the cabinet's base. 

Read more about cabinet's programs in [[AGEBasic in cabinets]].

#### Room Posters
To replace posters in a Room
- `PosterRoomCount()` returns the poster count of the actual room.
- `PosterRoomReplace(position #, Image path)` to replace a poster by an image in disk. Example: `PosterRoomReplace(1, "/sdcard/Pictures/posters/terminator.png")` to replace the second poster in the room.


### Light configuration

- `GetLigths()` to get a list string with the names of the lights present in the loaded rooms, separated with `|` (pipes) in the form `"<light name>|<ligth name>|..."`. Each light name have a room name and the light name for identification, example: `"room001:light1` the final `GetLigths()` result example is `"room001:light1|room003:ligth1"`. You can use `GetMember()` to process the string using the pipe as a separator, and also to process the light name. 
- `GetLightIntensity(string light name)`: to get the intensity of a light. Should be a number between `0` (no light, turned off) and `10` (too bright). example: `GetLightIntensity("room001:ligth1") = 0.5`. You can get the light name from `GetLights()`
- `SetLightIntensity(string light name, number intensity)`: to set the intensity of a light, example `SetLightIntensity("room001:ligth1", 0.5)`
- `SetLightColor(string light name, number R, number G, number B)`: set the color of the light, you will need the desired RGB color.  Returns `0` on error.

## Audio

[[Age of Joy]] plays two type of sounds: *ambience* (noise in rooms) and *games* sound. The volume of the audio is expressed in `dB`: `0` is normal, `20` as loud max, and -`-80` as silent. These values affect all the rooms and all the games.

To mute a sound set its volume to `-80`, and to unmute it simply set it to the previous volume value.

If you write a script for a cabinet (read [[CDL the Cabinet Description Language]]) that changes the volume of a game (for example), remember to change it to its previous value in order to not affect other games.
### Get/Set Volume

- `AudioAmbienceGetVolume()` and `AudioGameGetVolume()` to get the volume in `dB`.
- `AudioAmbienceSetVolume(number volume)` and `AudioGameSetVolume(number volume)` to set the volume, also in `dB`.

## Player position manipulation

It's possible to change the position of the player in the [[3D space]]:

- `PlayerGetHeight()`, `PlayerSetHeight(number)`: to get and set the height of the player. It's recommended to get the height and changing it by adding or decrementing its value.
- `PlayerGetCoordinate(string coord)`, `PlayerSetCoordinate(string coord)`: to get and set the coordinates in the [[3D space]] (force the player to a new position). `coord` should bet "X" or "Z". "Y" cant be changed, use `PlayerSetHeight` instead.
- `PlayerLookAt(cabinet part number)`: to force the player to look at a part of the cabinet. For example the screen. Can be used only in [[AGEBasic in cabinets]] mode.

It's recommended to read the [[AGEBasic examples - player to look at a screen when insert coin]].

## Debug mode

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
