#agebasic #examples 
### Show some text on the screen

```vb
10 CLS

20 LET x = 0
30 LET y = 0
35 LET inverted = 0

40 PRINT x, y, "test: "+STR(y), inverted
50 LET y = y+1
55 LET inverted = MOD(y, 2)

60 IF y < 10 THEN GOTO 40

70 PRINT 0, y, "END"
```

Showing text in the [[AGEBasic]] screen (in the [[Configuration control cabinet]] for example) slows down the program, but you can print all you need and show it in one instruction at the end of your program:

```vb
5  cls
10 for y = 0 to 10
20    print 0,y, "line #" + str(i), 0, 0
30 next y
40 show
```

In the line `20`, you are printing with the parameter `show` in false (the last one). And in the line `40` you show all the line printed at the same time. This way you get a better performance.