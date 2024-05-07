#agebasic 

![[Pasted image 20240507085430.png]]

You can escape character map codes in a string to get the desired character printed in the screen.

For example, `let str = "this is an horizontal rule: \64"` the `\64` refers to the character # 64 in the character map (starting in zero).

You need to escape codes *only to get "special" characters*, the usual ones are mapped to the correspondent character map, like `A` or `%`

E.g.

```vb
140 PRINT 0,0, ("\64" * 15) + " JUKEBOX " + ("\64" * 15), 1, 0
```

Result:

![[jukebox.png]]

> [!warning]
> 1. String operations doesn't work correctly with escaped characters. E.g. `len("a\233")` results to `5` , not to the expected `2`
> 2. The `inverted` parameter in the string doesn't work for special characters (like you can see in the previous example)
> 

