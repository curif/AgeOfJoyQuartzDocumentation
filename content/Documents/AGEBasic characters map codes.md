#agebasic 

You can escape character map codes in a string to get the desired character printed in the screen.

# C64 skin style character map

![[Pasted image 20240610112149.png]]


For example, `let str = "this is an horizontal rule: \64"` the `\64` refers to the character # 64 in the character map (starting in zero).

You need to escape codes *only to get "special" characters*, the usual ones are mapped to the correspondent character map, like `A` or `%`

E.g.

```vb
140 PRINT 0,0, ("\64" * 15) + " JUKEBOX " + ("\64" * 15), 1, 0
```

Result for c64 charmap:

![[jukebox.png]]

> [!warning]
> 1. String operations doesn't work correctly with escaped characters. E.g. `len("a\233")` results to `5` , not to the expected `2`
> 2. The `inverted` parameter in the string doesn't work for special characters (like you can see in the previous example)
> 

This program prints the character map on screen:

```vb
10 CLS
20 LET charnum = 0
30 FOR row = 0 to ScreenHeight() - 1
40   PRINT 0, row, str(charnum)
50   FOR col = 4 to 16+4
60     LET strcharnum = str(charnum)
70     PRINT col, row, "\" + strcharnum
80     LET charnum = charnum + 1
90     IF charnum > 255 THEN GOTO 500
100   NEXT col
110   PRINT col + 2, row, str(charnum - 1)
120 NEXT row

500 PRINT col + 2, row, str(charnum - 1)
510 END
```

### ZX Charmap
![[Pasted image 20240610123326.png]]
### C64 charmap
![[Pasted image 20240610123441.png]]


> [!note]
> You can change the `system-skin` for the configuration cabinet using the [[AGE configuration using files]] to get access to a different character map.
> 


