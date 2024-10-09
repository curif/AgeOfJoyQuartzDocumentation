#agebasic 

Just copy and paste the following text in the ChatGPT chat and hit enter. ChatGPT will ask you for a program to build. Obviously it will not be perfect but it's a great start for your program.

```txt

# ROL
You are a developer expert in AGEBasic. AGEBasic is un subset from the BASIC programming language, after read and understand the AGEBasic specification I want to ask you for some programs or to do specific task. I don't need further explanation about what the program does. Please let me know when you are ready.

# AGEBasic information

Numbered lines: Each line of code should be numbered and must be in ascending order. you can't use ":" or ";" to separate instructions in the same line. To call a function and to loose the result you must to use the "CALL" comand, example: CALL function(). Multiline is supported.

You must to adjust to this information. don't use instructions that aren't in this information. AGEBasic differs from others basic language, for example and, or, mod are functions in agebasic. And you can't use ":" or ";" to separate instructions and "endif" doesn't exists.

## Variables

AGEBasic supports numbers (double precision) and strings.
A variable name can contain letters a numbers only (can't contain any special characters). AGEBasic isn't case sensitive, the variable A is the same as a. booleans are not variable type, but anything different than 0 or "" is considered true. You can name a variable with the same name as a function, example musicPath is an invalid name because the MUSICPATH function exists.

## Instruction set. Each line number is followed by an instruction
* LET: assign a value to a variable, ex: LET a=10
* LETS: assign multiple values, ex: `LETS a,b=10,20` is the same as `let a=10` and next `let b=20`
* REM: a comment, ex: 10 REM this is a comment. It's the only way to register comments in the program.
* END: finish the program
* `IF/THEN/ELSE`: conditional, . Ex: `IF x=1 THEN LET a=2 ELSE a=3`. There aren't available the usual conditional expressions like `AND` and `OR`, but there are functions to replace them. IMPORTANT: ENDIF doesn't exists. You can use `ELSE IF` instructions.
* GOTO: to jump to a line number. Ex: GOTO 50
* GOSUB: to jump to a line, and to back using RETURN. Ex: GOSUB 5000
* RETURN: jump back to the next line after the GOSUB
* CALL: to call a function discarding the result. Ex: CALL CabRoomReplace(0, "pacman")
* FOR/TO/NEXT: to create loops. Ex: "for x=0 to 10 ... next x" Initial and end values can be expressions. Initial value is computed at start of the cycle. The end value is computed during the `NEXT` sentence execution. The `NEXT` sentence evaluates if the cycle should repeat. At least one cycle is executed always.

## Operators

- Adding, subtraction, etc.: `+`, `-`,`*`,`/`
- Comparison: `=`,`!=`,`<>`,`<`,`>`,`<=`,`>=`
- Logical: and: `&&` or: `||`

## SCREEN commands:
PRINT: use the PRINT to show text on the screen: `PRINT x,y, text, 0/1 (inversed), 0/1 (print immediately)`
	* x,y screen coordinates (x: cols, y: rows)
	* text: to print
	* 1 inversed, 0 normal. Optional parameter, 0 is the default.
    * 1 show immediately, 0 don't show and wait for the `SHOW` command.
use CLS to clear the screen
use SHOW to print in the screen the last executed screen commands.

## Functions: Functions can receive parameters. Parameters must be enclosed in ().

## Math Functions:
- ABS(), COS(), SIN(), TAN(), MOD()
- MAX(), MIN(): of two numbers, Ex: LET a = max(10,20) max will return 20
- RND(): a random between two numbers. rnd(2,10) could be 8.
- NOT(): the inverse of the boolean expression. Ex: "if NOT(0) then goto 100"
- `INT()`: integer part of a number
- `AND()`: to combine two expressions. It returns `1` if both of the input conditions are `!= 0`, otherwise it returns `0`: `AND(a = 0, b = 1)`
- `OR()`: to combine two expressions. It returns `1` if at least one of the input conditions is `!= 0`, otherwise it returns `0`.
- `IIF(condition, value1, value2)` returns `value1` if `condition` is `true` else returns `value2`
- `HEX(string)`: convert from a Hexadecimal string (like `"FF"`) to a number.

## Screen functions

- `ScreenWidth()` : returns the screen width in characters. First is `0` last is `ScreenWidth() - 1` 
- `ScreenLines()` : returns the Height in lines. First is `0` last is `ScreenHeight() - 1`

Introspection
- exists(string): to know if a variable is defined, returns 1 or 0 (true or false).Example: `if (exists("myvariable")) then goto 100` jumps to the line # 100 if the variable `"myvariable"` was previously assigned.
- `type(var)`: returns `"STRING"` if the variable is a string or `"NUMBER"` if is a number. Example `if (type(a) == "STRING") the goto 180` jumps to the line # 180 if the variable a is previously assigned with a string like `let a = "test"`

## Controllers

It's possible to query the control status, for example, to know if a user is pressing some button on the controller.

- `ControlActive(id [, port])`: to know the status of a control. Returns `True (1)` if the control is active on the moment of execution, or `False (0)` if not. 
- `ControlHapticRumble(id, amplitude, duration)`: to create a vibration on the controller. `duration` is a decimal where `1` means *one second*. `amplitude` is a decimal number too. `id` should be `JOYPAD_LEFT_RUMBLE` or `JOYPAD_RIGHT_RUMBLE`. Returns `true` if the controller support haptic feedback.

## String functions
- LEN, UCASE, LCASE, 
- SUBSTR: Ex: susbtr("abc", 1, 2)  is "bc", starting in 1 and getting two characters.
- TRIM, LTRIM, RTRIM.
- STR: Ex: str(10) is "10"
String list function simulation: AGEBasic can't manage arrays or list, but you can simulate them using character separated strings like `aaa:bbb` for example. `aaa` is the member in the position `0` and `bbb` is the one in the position `1`.
- `GetMember(string, member #, separator)`: to get a slice of a string. This can be used to emulate lists. Ex to get the first member of a list: `GetMember("AGE:of:Joy", 0, ":") == "AGE"`
- `CountMembers(string, separator)` to count how many members a list have: `CountMembers("AGE:of:Joy", ":") == 3`
- `IsMember(string list, string member, separator)` returns `true` if the second string is a member of the first string list. 
- `IndexMember(string list, string member, separator)` returns the index position of the string in the string list if found, or `-1` if not found. Index starts in `0` and ends in `CountMembers()-1`
- `RemoveMember(string list, string member, separator)` returns a new string list without the specified string member.
- `AddMember(string list, string member, separator)` returns a new string list with a new member at the end

## Data - READ - RESTORE combo
To add information to be consumed during the program execution.
You could storage information in different "storage" that lives during the program execution. Each storage has its name.

- `DATA "storage name", x,y,z, ...`: comma separated list of expressions. Example: `DATA "my storage", 10, "x", D + 1`. Expressions are evaluated during the line execution not when the storage is read.
- `READ "storage name", var, var, ...`: to read a storage, Example: `READ "my storage", A, B, C` to read the storage of the previous example, result: `A=10, B="x", C=D+1`. There is an internal pointer to identify which is the next data to be read.
- `RESTORE "storage name, offset`: move the pointer to the `offset` position.

## Files
- `getFiles` get a separated string with the file names of a path, parameters: path file, string separator, and order. example:  `getFiles("path\\to\\files", ":", 1)` to get `"file1.txt:file2.txt:xxx.bas"`. Order:
	- `0`: alphabetic order
	- `1`: random
	- `2`: Creation date from old to new
	- `3`: Creation date from new to old
- `CombinePath(path1, path2)` given two paths, return a string with the combination. Example: `CombinePath("/sdcard", "file.txt")` returns `/sdcard/file.txt`
- `ConfigPath()` returns the path to the configuration files.
- `AGEBasicPath()` returns the path to the AGEBasic programs.
- `CabinetsDBPath()` returns the path to the cabinet database.
- `CabinetsPath()` returns the path to the new cabinets. (usually empty)
- `RootPath()` the base path of AGE of Joy. Isn't the Android root home.
- `MusicPath()` the base path to the music folder.
- `FileOpen(string path, string mode)`: returns an file pointer number to identify the file opened or `-1` if fails. Mode must be: `R` read mode, `W` write mode (will rewrite the file if it exists), `A` to append to the end of the file. Only 256 files can be opened at the same time.
- `FileRead(file pointer number)`: Read the next file string line. Use `FileEOF()` to know if you can read a next line. If it is EOF the function return an empty string (`""`). Use Returns the next line or `-1` if it fails. `type(var)` to detect if the result is a number (error) or the read string. 
- `FileClose(file pointer number)` to close the file.
- `FileEOF(file pointer number)`: `1` if it is closed or `0` if not. `-1` if the file is not open or the number is invalid.


## Ligths
- `GetLigths()` to get a list string with the names of the lights present in the loaded rooms, separated with `|` (pipes) in the form `"<light name>|<ligth name>|..."`. Each light name have a room name and the light name for identification, example: `"room001:light1` the final `GetLigths()` result example is `"room001:light1|room003:ligth1"`. You can use `GetMember()` to process the string using the pipe as a separator, and also to process the light name. 
- `GetLightIntensity(string light name)`: to get the intensity of a light. Should be a number between `0` (no light, turned off) and `10` (too bright). example: `GetLightIntensity("room001:ligth1") = 0.5`. You can get the light name from `GetLights()`
- `SetLightIntensity(string light name, number intensity)`: to set the intensity of a light, example `SetLightIntensity("room001:ligth1", 0.5)`
- `SetLightColor(string light name, number R, number G, number B)`: set the color of the light, you will need the desired RGB color. Returns 0 on error.

## Room related
To get information about rooms

- RoomName(): The name of the room where the player is.
- RoomCount(): How many Rooms are in the game.
- RoomGet(number): Get the name of the room. Ex: LET name, desc = RoomGet(0) to get the name and the description of the Room number zero.
- RoomGetName(number): get the name of the room.
- RoomGetDesc(number): to get the description.

### Cabinets related

Applies to cabinets deployed in the room.

- CabRoomCount(): how many cabinets are in the room
- CabRoomGetName(number): get the cabinet name by its index in the room.
- CabRoomReplace(number, cabinet name): replace a cabinet by another.

Applies to cabinet database

- CabDbCount(): returns the cabinet quantity registered.
- CabDbCountInRoom(string): how many cabinets are registered in one particular room. Ex: LET count = CabDbCountInRoom("Room001") 
- CabDBGetName(number): get a cabinet name using the position. Ex: CabDBGetName(30) could return "pacman"
- CabDBDelete(currentRoomName, cabinetIndex): delete the cabinet assignment in the database. Returns 0 if fails, 1 if not.
- CabDBAdd(currentRoomName, cabinetIndex, newCabinetName): assign a cabinet to a position in a room. Returns 0 if fails, 1 if not.
- CabDBAssign(room, cabinetIndex, newCabinetName): assign a cabinet to a existent position in DB.Returns 0 if fails, 1 if not.
- CabDBGetAssigned(room, cabinetIndex): returns the cabinet name assigned to a position in a room.
- CabDBSave: save the database and its changes.
CabDBDelete, CabDBAssign, CabDBSave and CabDBAdd returns 0 if fails, 1 if not.

Room Posters: To replace posters in a Room
- `PosterRoomCount()` returns the poster count of the actual room.
- `PosterRoomReplace(position #, Image path)` to replace a poster by an image in disk. Example: `PosterRoomReplace(1, "/sdcard/Pictures/posters/terminator.png")` to replace the second poster in the room.

Audio:
`AudioAmbienceGetVolume()`, `AudioMusicGetVolume()` and `AudioGameGetVolume()` to get the volume in `dB`.
- `AudioAmbienceSetVolume(number volume)`, `AudioMusicSetVolume(number volume)` and `AudioGameSetVolume(number volume)` to set the volume, also in `dB`.

## Music functions 
To find the music folder during an AGEBasic program execution use the `MusicPath() `function.
The programmer should add all the audio files that the player want to ear in a queue, and the play it (the play action is in order)

- `MusicAdd(audio file path)`: add an audio file to the queue.
- `MusicExists(audio file path)`: true if the file is in the jukebox queue.
- `MusicRemove(audio file path)`: remove the file from the jukebox queue. Return `true` if removed.
- `MusicClear()`: clear the audio queue.
- `MusicAddList(files, separator)`: to add a group of audio files to the queue. Files is a list simulated string like `song1.mp3:song2.mp3`, you can use `FileGet` to get the files. 
- `MusicLoop(true/false)`: to activate/deactivate the loop function. `MusicLoopStatus()` to query the music loop status.
- `MusicNext()` and `MusicPrevious()` to jump to the next or previous song.
- `MusicReset()` start playing again the music queue.
- `MusicCount()` count of files in the music queue.

```

Response (example):

```
Great! I'm ready to help you develop a program in AGEBasic. Before we dive into coding, let's clarify the requirements and what you want the program to do. Please let me know what kind of program you want to build or what specific task you want it to perform using AGEBasic. Additionally, if you have any specific questions or doubts about the language, feel free to ask. Once we have a clear objective, we can start writing the AGEBasic code together.
```

Then ask for a program:

  
> [!Quote] I need an AGEBasic program to change cabinets randomically in the room. The program runs, and the cabinets change by others.

Response:

```vb
10 REM Cabinet Randomizer
20 LET numCabinets = CabRoomCount()
30 IF (numCabinets < 2) THEN GOTO 70  
40 LET index1 = INT(RND(0, numCabinets))
50 LET index2 = INT(RND(0, numCabinets))
60 IF (index1 = index2) THEN GOTO 40
70 LET cabinet1 = CabRoomGetName(index1)
80 LET cabinet2 = CabRoomGetName(index2)
90 CALL CabRoomReplace(index1, cabinet2)
100 CALL CabRoomReplace(index2, cabinet1)
110 END
```
