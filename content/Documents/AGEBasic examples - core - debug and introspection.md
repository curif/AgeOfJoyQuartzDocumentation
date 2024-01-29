Examples related to the basic programming in [[AGEBasic]]

### Comments 

```Basic
10 rem coment
20 ' comment
30 let a=10 'comment
40 end
```

### Debug


```basic
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

### Variable type

You can take decisions using the type of a variable, it's useful for debugging.

```BASIC
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
