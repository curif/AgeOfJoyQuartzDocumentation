#agebasic #examples 

### Comments 

```vb
10 rem coment
20 ' comment
30 let a=10 'comment
40 end
```

### Debug


```vb
1000 let i = 100
1010 call DebugMode(1) 'activate the debug mode
1020 let ERROR = "some error message to see in debug"
```

Result file `"myprogram.bas.debug"` in the same folder than the `myprogram.bas` file.

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

### Variable types

You can take decisions using the type of a variable, it's useful for debugging.

```vb
10 let a = 10
20 if type(a) == "NUMBER" goto 100
30 if type(a) == "STRING" goto 200
40 print 0,0, "Variable a unknown"
50 end

100 print 0,0, "variable A is a number"
110 end

200 print 0,0 "varibble A is a string"
210 end

```

### Other example


```vb title="testInstrospection.bas"
5 call DebugMode(1)
10 REM Replace each cabinet in all rooms with a random cabinet
20 LET totalRooms = RoomCount()
30 LET totalCabinetsDB = CabDbCount()
35 LET cont = 0
37 LET playerRoom = RoomName()
100 if type(cont) != "NUMBER" then let error="cont is not a number"
```

#### Result

In the `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic` folder: 

```txt title="testInstrospection.bas.debug"
Program: testInstrospection.bas
---PROGRAM STATUS ---
PROGRAM: testInstrospection.bas
Last line parsed: 37
Next line to execute: 96
Executed lines counter: 4308
vars: 
TOTALROOMS: 20 [Number]
TOTALCABINETSDB: 164 [Number]
CONT: 0 [Number]
PLAYERROOM: roominit [String]

---

```