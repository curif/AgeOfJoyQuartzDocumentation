#agebasic 

BASIC is a popular programming language known for its simplicity and ease of use. It has been used in various applications, especially in the early days of computing.

`AGEBasic` draws its inspiration from another programming language called [Tiny Basic](https://en.wikipedia.org/wiki/Tiny_BASIC) which is a minimalistic version of BASIC. However, AGEBasic does not strictly adhere to all the rules and limitations of Tiny Basic. Instead, it takes inspiration from Tiny Basic and extends or modifies certain features to better suit the requirements and capabilities designed specifically to be executed in [[Age of Joy]].

With AGEBasic the player can develop it's own functions to run in the simulation. Allows to control parts of the game that there aren't available from the [[YAML]] configuration or the [[Visual configuration]].

> [!important] read about the new [[AGEBasic cabinet event system]] (version >= 0.6)

## AGEBasic program storage

The main storage for [[AGEBasic]] programs is `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic`. AGEBasic programs must to end with the `.bas` prefix, like `mixcabinets.bas` or `changecontrols.bas`.
## Variables

### Understanding Variables: Your Program's Memory Boxes

Imagine you're writing a recipe. Instead of always writing "add 2 cups of sugar," you might say "add sugarAmount cups of sugar," and then somewhere else define sugarAmount = 2. If you later decide to use 3 cups, you only change it in one place!

In programming, a **variable** is very similar. It's essentially a **named storage location** in your computer's memory that holds a piece of information, or "data." Think of it like a labeled container or a box where you can store values.

**Why do we use variables?**

- **To store data:** From numbers to text, variables remember information your program needs.    
- **To make code flexible:** Instead of hardcoding values directly into your commands, you can use variables. If the value changes, you only update the variable, not every instance where it's used.
- **To improve readability:** Giving meaningful names to your data (playerScore instead of just 100) makes your code much easier to understand.
    
#### Naming Your Variables: The Rules of the Label

Just like you give a box a clear label so you know what's inside, variables need names. These names have specific rules to follow:

- **Allowed Characters:** A variable name can contain only **letters** (A-Z, a-z), **numbers** (0-9), and the **underscore character** (`_`).
- **Starting Character:** A variable name **must start with a letter**. You can't start a variable name with a number or an underscore.
- **No Special Characters:** You cannot use special characters (like $, @, %, ! etc.) in a variable name.
- **No Reserved Words:** You can't name a variable with the same name as a function or command that already exists in the programming language. These are called "reserved words." For example, in AGEBasic, `musicPath` would be an invalid variable name because the MUSICPATH function already exists.
#### Types of Data Variables Can Hold (in AGEBasic)

Variables aren't just empty boxes; they're designed to hold different types of information. In AGEBasic, your variables can contain:

- **Numbers:** These are stored as **double precision** values, meaning they can hold both whole numbers (integers) and numbers with decimal points very accurately. You can also represent numbers in **hexadecimal** format by preceding them with an & (e.g., &FF represents 255).
- **Strings:** These are sequences of text or characters, like a name, a sentence, or a file path.
- **Arrays:** These are special variables that can hold a collection of multiple values under a single name, like a list of numbers or a list of names.

> [!note] 
> **Booleans:** While "booleans" (which represent true or false values) aren't a distinct variable type in AGEBasic, the language interprets any numerical value **different from 0 as true**, and the number **0 itself as false**. A string variable not empty (`<>""`) is evaluated as `true`. A non empty array is also evaluated as `true`.

Examples:

 Correct:
 
```vb
10 LET A = 10 'a number 
20 LET A = 10.10 'a number
30 LET A = "AGE of Joy" 'a string
40 LET A = "10" 'a string
50 LET A = &0 'an hex number
60 LET MY_VARIABLE = &FF
```

Incorrect:

```vb
10 LET MYVARIABLE$ = 10
20 LET  = "text"
30 A = 10
```
# Sentences

Refers to a single, complete instruction or command that the program executes.
## Numbered lines

Each line of code should be numbered and be in ascending order. Multiline is supported.
A Command must be the first after a line number. Functions can be called using a `CALL` function

```vb
10 PRINT "Hello world"
```
## Line separation

One line number could contain two sentences using `:` as separator. 

```vb
10 LET a = 10 : REM value of a is 10
20 PRINTLN a : PRINTLN "Hello world"
```
## Multiline

It is possible to separate lines for clarity:

```vb
100 IF A = 1
    THEN LET A = 2
    ELSE LET A = 3 
```

> [!warning]
> This sentence will create an error because every new sentence starts with a number.

```vb
100 LET A = 
        200
```


## Commands

Each line must begin with a line number and a command. 
* `LET`: assign a value to a variable, ex: `LET a=10`
* `LETS`: assign multiple values, e.g.: `LETS a,b=10,20` is the same as `let a=10` and next `let b=20`
* `DIM`: create an array variable.
* `REM`: a comment, ex: `REM this is a comment`. It's the only way to register comments in the program.
* `END`: finish the program
* `IF/THEN/ELSE`: conditional, . Ex: `IF x=1 THEN LET a=2 ELSE a=3`. There aren't available the usual conditional expressions like `AND` and `OR`, but there are functions to replace them. IMPORTANT: ENDIF doesn't exists
* `GOTO`: to jump to a line number. Ex: `GOTO 50`
* `GOSUB`: to jump to a line, and to back using `RETURN`. Ex: `GOSUB 5000`
* `RETURN`: jump back to the next sentence after the `GOSUB`
* `CALL`: to call a function discarding the result. e.g.: `CALL CabRoomReplace(0, "pacman")`
* `FOR/TO/NEXT/STEP`: to create loops. Ex: `for x=0 to 10 step 2 ... next x`
	* Initial, end  and step values can be expressions.
	* Initial value is computed at start of the cycle.
	* The end value is computed during the `NEXT` sentence execution.
	* The `NEXT` sentence evaluates if the cycle should repeat. At least one cycle is executed always.
* `SLEEP` to sleep a number of seconds, doesn't work in programs executed in the control cabinet (has no sense). E.g.: `SLEEP 1` (sleeps the program during a second). `SLEEP 0.5` sleeps for half of a second. Values must be greater than `0.01`.
* Graphic sentences (DDRAW, DPSET, etc.)
* `RUN "path/to/my/myprogram.bas" [LINE 30]`: to run a program (optionally starting at specified line #). The main program will continue after the called program finish.

## Operators

- Adding, subtraction, etc.: `+`, `-`,`*`,`/`
- Comparison: `=`,`!=`,`<>`,`<`,`>`,`<=`,`>=`
- Logical: **and**: `&&` **or**: `||`

## Arrays
### 1. What is an Array?

At its core, an **array** is a structured collection of data items, all stored under a single variable name. Imagine a series of numbered compartments, where each compartment can hold a piece of data. Instead of creating many individual variables (e.g., `ITEM1`, `ITEM2`, `ITEM3`), an array allows you to store and access these related pieces of data using a single name followed by an **index** (or subscript) that indicates the specific position of the item you want to access.

This makes it incredibly efficient to store and process lists or tables of information, especially when the number of items is large or varies during program execution.

### 2. The Dimensional Concept of Arrays

Arrays can be designed with different "dimensions," which essentially refers to the number of indices required to pinpoint a specific element.

*   **One-Dimensional (1D) Arrays:**
    These are like a simple list or a single row of data. You need only one index to access an element.
    *Example:* `A[0]`, `A[1]`, `A[2]`, ...
    Think of it as a column of numbers:
    ```
    +-----+
    | A[0]|
    +-----+
    | A[1]|
    +-----+
    | A[2]|
    +-----+
    ```

*   **Two-Dimensional (2D) Arrays:**
    These are like a table or a grid (rows and columns). You need two indices to access an element: one for the row and one for the column.
    *Example:* `B[0,0]`, `B[0,1]`, `B[1,0]`, `B[1,1]`, ...
    Think of it as a spreadsheet:
    ```
    +----------+----------+----------+
    | B[0,0]   | B[0,1]   | B[0,2]   |
    +----------+----------+----------+
    | B[1,0]   | B[1,1]   | B[1,2]   |
    +----------+----------+----------+
    ```

*   **Multi-Dimensional Arrays (3D and beyond):**
    AGEBasic supports arrays with more than two dimensions. A three-dimensional array, for instance, can be visualized as a cube or a stack of tables. You would need three indices to access an element (e.g., `MULTI[F,G,X]`). While higher dimensions are supported, they become increasingly abstract to visualize but are extremely useful for complex data structures.

**Important Note on Indexing:**
AGEBasic arrays utilize **zero-based indexing**. This means the first element in any dimension is at index `0`, the second at `1`, and so on, up to `N-1` where `N` is the declared size for that dimension.

### 3. Declaring Arrays with `DIM`

Before you can use an array, you must declare it using the `DIM` (Dimension) statement. This tells AGEBasic the name of your array and how much space to reserve for it in memory by specifying the size of each dimension.

**Syntax:**
`DIM arrayName[size1 [, size2, ...]]`

*   `arrayName`: The name of your array. Follows standard variable naming rules (starts with a letter, contains only letters and numbers, not a reserved word).
*   `size1, size2, ...`: The size of each dimension. This number represents the *total count of elements* in that specific dimension. For example, `DIM A[5]` declares an array with 5 elements, accessible from `A[0]` to `A[4]`.

**Examples:**

*   **One-Dimensional Array:**
    ```vb
    10 DIM myNumbers[10] : REM Declares an array named 'myNumbers' with 10 elements (indices 0 to 9)
    ```

*   **Two-Dimensional Array:**
    ```vb
    20 DIM gridData[3, 5] : REM Declares a 2D array: 3 rows (indices 0-2), 5 columns (indices 0-4)
    ```

*   **Multi-Dimensional Array (e.g., 3D):**
    ```vb
    30 DIM cubeData[2, 3, 4] : REM Declares a 3D array with dimensions: (indices 0-1, 0-2, 0-3)
    ```

### 4. Accessing and Assigning Array Elements

Once an array is declared, you can access individual elements for reading or writing by specifying the array name followed by the appropriate indices enclosed in square brackets `[]`.

**Assigning Values:**
Use the `LET` command to assign a value to a specific array element.

**Syntax:**
`LET arrayName[index1 [, index2, ...]] = value`

**Example:**
```vb
10 DIM prices[5]
20 LET prices[0] = 10.50
30 LET prices[1] = 22.99
40 LET prices[4] = 5.00
50 DIM matrix[2,2]
60 LET matrix[0,0] = "Top-Left"
70 LET matrix[1,1] = "Bottom-Right"
```

**Dinamic array creation:**

You can create an array using the `ARRAY()` function:
```vb
10 LET RGB_BLUE = ARRAY(0,0,255)
20 PRINTLN "B:" = STR(RGB_BLUE[2])
```

**Retrieving Values:**
You can use array elements just like regular variables in expressions, `PRINT` statements, or other `LET` assignments.

**Syntax:**
`arrayName[index1 [, index2, ...]]`

**Example:**
```vb
100 DIM myValues[3]
110 LET myValues[0] = 100
120 LET myValues[1] = myValues[0] * 2 : REM myValues[1] becomes 200
130 PRINTLN "Value at index 0: " + STR(myValues[0])
140 PRINTLN "Value at index 1: " + STR(myValues[1])
```

### 5. Getting Array Length with `LEN()`

The `LEN()` function, traditionally used for string lengths, has been extended to provide the *total number of elements* in an array. This is particularly useful for certain iteration patterns or for determining the overall capacity of an array.

**Syntax:**
`LEN(arrayName)`

**Return Value:** A number representing the total count of elements in the array (product of all dimension sizes).

**Example:**
```vb
10 DIM singleDim[5]
20 LET totalElements1 = LEN(singleDim) : REM totalElements1 will be 5

30 DIM twoDim[2,3]
40 LET totalElements2 = LEN(twoDim) : REM totalElements2 will be 2 * 3 = 6

50 DIM multiDim[2,3,4]
60 LET totalElements3 = LEN(multiDim) : REM totalElements3 will be 2 * 3 * 4 = 24
```

### 6. Mixed-Type Arrays

Unlike some programming languages, AGEBasic arrays are **flexible in type**. This means a single array can store a mix of numbers (double precision, hexadecimal) and strings within its elements. The `TYPE()` function can be used to check the specific type of an element if needed during runtime.

**Example:**
```vb
10 DIM mixedData[2]
20 LET mixedData[0] = 123.45 : REM A number
30 LET mixedData[1] = "Hello, AGEBasic!" : REM A string

40 IF TYPE(mixedData[0]) = "NUMBER" THEN PRINTLN "Element 0 is a number."
50 IF TYPE(mixedData[1]) = "STRING" THEN PRINTLN "Element 1 is a string."
```


### 7. Sort an array

*   `SORT` to sort elements within an array: `SORT(array_variable, [descending_flag])`
    *   `array_variable`: The array to be sorted. Must be a `BasicValue` of type `Array`.
    *   `descending_flag`: Optional `BasicValue` of type `Number` (or convertible to boolean).
        *   `0` (or `false`): Sorts in ascending order (default).
        *   Non-`0` (e.g., `1` or `true`): Sorts in descending order.
    *   **Returns:** The `BasicValue` array after it has been sorted in-place.
    *   **Behavior:**
        *   Performs an in-place sort; the original `array_variable` is modified.
        *   Elements are compared using `BasicValue`'s intrinsic comparison rules for numbers and strings (lexicographical).
        *   Throws `InvalidOperationException` if array elements are `BasicValueType.Array` or `BasicValueType.empty`, or if mixed types cannot be implicitly converted for comparison (e.g., an unparseable string with a number).
### Short Example of Array Use

Here's a concise AGEBasic program demonstrating a one-dimensional array to store and print a list of scores.

```vb
10 REM Short Array Example: High Scores
20 CLS
30 DIM highScores[5] ' Declare an array to hold 5 scores

40 LET highScores[0] = 1000
50 LET highScores[1] = 750
60 LET highScores[2] = 900
70 LET highScores[3] = 500
80 LET highScores[4] = 1200

90 PRINTLN "--- High Scores ---", 0, 0
95 LET highScores = SORT(highScores, 1) : REM descending
100 FOR i = 0 TO 4
120  PRINTLN "Score " + STR(i+1) + ": " + STR(highScores[i]), 0, 0
130 NEXT i
140 SHOW
150 SLEEP 3 ' Wait for 3 seconds
160 END
```

**Explanation:**
This program first clears the screen. It then declares a one-dimensional array `highScores` capable of holding 5 numeric elements. It populates this array with example scores. A `FOR` loop then iterates from index 0 to 4 (the valid range for a 5-element array), printing each score along with its position.  Finally, `SHOW` updates the screen and the program pauses before ending.

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
- `ARRAY(val1, val2[, val3,...]`: Create an array with the specified values.

### Strings

- `LEN`, `UCASE`, `LCASE`, 
- `SUBSTR`: Ex: `susbtr("abc", 1, 2) ` is "bc", starting in 1 and getting two characters.
- `TRIM`, `LTRIM`, `RTRIM`.
- `STR`: Ex: `str(10)` is `"10"`
- `StringMatch(string val, string pattern)` checks if a substring (pattern) exists within a string (val), returning `1` if found and `0` if not. For example, `StringMatch("Hello, World!", "World")` returns `1`, while `StringMatch("Hello, World!", "Earth")` returns `0`.

#### List simulation

AGEBasic versions (previous to `0.5.0 RC15`) can't handle arrays or lists, but you can simulate them using character separated strings like `aaa:bbb` for example. `aaa` is the member in the position `0`, `bbb` is the one in the position `1` and the separator is `:`.

> [!warning]
> These functions are maintained for retro compatibility (programs before `0.5.0 RC15`. New programs should use `ARRAY`s

- `GetMember(string, member #, separator)`: to get a slice of a string. Can be used to emulate lists. Example to get the first member of a list: `GetMember("AGE:of:Joy", 0, ":") = "AGE"`
- `CountMembers(string, separator)` to count how many members a list have: `CountMembers("AGE:of:Joy", ":") = 3`
- `IsMember(string list, string member, separator)` returns `true` if the second string is a member of the first string list. 
- `IndexMember(string list, string member, separator)` returns the index position of the string in the string list if found, or `-1` if not found. Index starts in `0` and ends in `CountMembers()-1`
- `RemoveMember(string list, string member, separator)` returns a new string list without the specified string member.
- `AddMember(string list, string member, separator)` returns a new string list with a new member at the end
### Introspection

- `exists(string)`: to know if a variable is defined, returns 1 or 0 (true or false). Example: `if (exists("myvariable")) then goto 100` jumps to the line # 100 if the variable `"myvariable"` was previously assigned.
- `type(var)`: returns `"STRING"` if the variable is a string or `"NUMBER"` if is a number or "ARRAY". Example `if (type(a) == "STRING") the goto 180` jumps to the line # 180 if the variable a is previously assigned with a string like `let a = "test"`

## Screen

### Character functions

* `PRINT` to show text on the screen: `PRINT x,y, text [, 0/1 [, 0/1]]`
	* `x,y` screen coordinates (x: cols, y: rows) 
	* `text`: to print
	* `1` inversed, `0` normal. Optional parameter, 0 is the default.
	* `1` show immediately, `0` don't show and wait for the `SHOW` command (recommended)
* `PRINTLN` to show text on the screen with internal `x, y` control: `PRINTLN text [, 0/1 [, 0/1]`]
	* `text`: to print
	* `1` inversed, `0` normal. Optional parameter, 0 is the default.
	* `1` show immediately, `0` don't show and wait for the `SHOW` command (recommended)
* `CLS` to clear the screen
* `SHOW`: to print in the screen the last executed screen commands.
* `LOCATE X, Y`: Moves the text cursor to character column `X` and row `Y`.
    *   `X`: Horizontal character position. `0` (left) to `SCREENWIDTH() - 1` (right).
    *   `Y`: Vertical character line. `0` (top) to `SCREENHEIGHT() - 1` (bottom).
-   `GETX()`: Returns the current horizontal character column of the text cursor.
    *   Return value is a Number, from `0` (leftmost) to `SCREENWIDTH() - 1` (rightmost).
-   `GETY()`: Returns the current vertical character row (line) of the text cursor.
    *   Return value is a Number, from `0` (topmost) to `SCREENHEIGHT() - 1` (bottommost).
-   `PRINTCENTERED Y, TEXT [, INVERTED [, DRAW_FLAG]]`: Prints `TEXT` centered horizontally on character row `Y`.
    *   `Y` (Number): The character row (line) to print on. `0` is the top row.
    *   `TEXT` (String or Number): The text or number to print. Numbers will be converted to strings.
    *   `INVERTED` (Boolean, optional, default `0` or `FALSE`): If `1` (or `TRUE`), uses inverted foreground/background colors for this print.
    *   `DRAW_FLAG` (Boolean, optional, default `1` or `TRUE`): If `1` (or `TRUE`), the screen is updated immediately after printing. Set to `0` (or `FALSE`) to batch multiple drawing operations before calling `SHOW` or another command that draws.
* `FGCOLOR` and `BGCOLOR` commands to set colors depending on the type of screen. `RESETCOLOR` and `INVERTCOLOR` as variants. 
* `SCROLL N_LINES [, FILL_COLOR_SPEC [, DRAW_FLAG]]`: Scrolls the entire character display area vertically.
    *   `N_LINES` (Number): The number of character lines to scroll.
        *   Positive values scroll content **DOWN** (new blank space appears at the top).
        *   Negative values scroll content **UP** (new blank space appears at the bottom).
        *   A value of `0` results in no scroll.
    *   `FILL_COLOR_SPEC` (Color, optional): The color to fill the new blank lines created by scrolling.
        *   Can be a string color name (e.g., `"black"`, `"blue"`).
        *   Can be three numbers representing R, G, B values (e.g., `0,0,0` for black).
        *   If omitted, the current default background color .
    *   `DRAW_FLAG` (Boolean, optional, default `1` or `TRUE`): If `1` (or `TRUE`), the screen is updated immediately. Set to `0` (or `FALSE`) to defer the screen update.
-   `SCROLLRECT CX, CY, CW, CH, N_LINES [, FILL_COLOR_SPEC [, DRAW_FLAG]]`: Scrolls a rectangular sub-region of the character display vertically.
    *   `CX` (Number): The starting character column (X-coordinate) of the rectangle's top-left corner.
    *   `CY` (Number): The starting character row (Y-coordinate) of the rectangle's top-left corner.
    *   `CW` (Number): The width of the rectangle in characters. Must be greater than 0.
    *   `CH` (Number): The height of the rectangle in characters. Must be greater than 0.
    *   `N_LINES` (Number): The number of character lines to scroll within the specified rectangle.
        *   Positive values scroll content **DOWN** within the rectangle.
        *   Negative values scroll content **UP** within the rectangle.
        *   A value of `0` results in no scroll.
    *   `FILL_COLOR_SPEC` (Color, optional): The color to fill the new blank lines created by scrolling within the rectangle.
        *   Can be a string color name (e.g., `"black"`, `"blue"`).
        *   Can be three numbers representing R, G, B values (e.g., `0,0,0` for black).
        *   If omitted, the current default background color (`ScreenGenerator.charBackgroundColor`) is used.
    *   `DRAW_FLAG` (Boolean, optional, default `1` or `TRUE`): If `1` (or `TRUE`), the screen is updated immediately. Set to `0` (or `FALSE`) to defer the screen update.
* `SETCOLORSPACE` allows to simulate a computer type (like "c64"):
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
* `GETCOLOR(string)`: returns an `ARRAY` with (r, g, b). E.g. `LET A=GETCOLOR("blue") : PRINTLN A[3]` must print `255`.
- `SCREENWIDTH()` : returns the screen width in characters. First is `0` last is `ScreenWidth() - 1` 
- `SCREENHEIGHT()` : returns the Height in lines. First is `0` last is `ScreenHeight() - 1` 
- `SCREENSIZE()` : returns an array with two positions: Width and Height.]]
### Drawing functions

All of them starts with`D`.
Here is a markdown manual for the provided BASIC graphics commands:

---

## Graphics Commands

This section describes the graphics commands, which allow you to draw various shapes and retrieve screen information.

-   `DCHARPIXELX(CHAR_X, CHAR_Y)`: Returns the screen pixel X-coordinate of the top-left corner of the character cell specified by `CHAR_X` (column) and `CHAR_Y` (row).
    *   `CHAR_X` (Number): The character column. Typically ranges from `0` (leftmost) to `SCREENWIDTH() - 1` (rightmost character column).
    *   `CHAR_Y` (Number): The character row. Typically ranges from `0` (topmost) to `SCREENHEIGHT() - 1` (bottommost character row).
    *   Returns a `Number`. If character coordinates are invalid or out of bounds, may return `-1`.
-   `DCHARPIXELY(CHAR_X, CHAR_Y)`: Returns the screen pixel Y-coordinate of the top-left corner of the character cell specified by `CHAR_X` (column) and `CHAR_Y` (row).
    *   `CHAR_X` (Number): The character column. Typically ranges from `0` (leftmost) to `SCREENWIDTH() - 1` (rightmost character column).
    *   `CHAR_Y` (Number): The character row. Typically ranges from `0` (topmost) to `SCREENHEIGHT() - 1` (bottommost character row).
    *   Returns a `Number`. If character coordinates are invalid or out of bounds, may return `-1`.
-   `DCHARPIXEL(CHAR_X, CHAR_Y)`: Returns an array containing the screen pixel X and Y coordinates `[PX, PY]` of the top-left corner of the character cell specified by `CHAR_X` (column) and `CHAR_Y` (row).
    *   `CHAR_X` (Number): The character column. Typically ranges from `0` (leftmost) to `SCREENWIDTH() - 1` (rightmost character column).
    *   `CHAR_Y` (Number): The character row. Typically ranges from `0` (topmost) to `SCREENHEIGHT() - 1` (bottommost character row).
    *   Returns an `Array of Numbers` (`[PX, PY]`). If character coordinates are invalid or out of bounds, may return `[-1, -1]`.
-   `DPSET(PX, PY, COLOR_SPEC [, DRAW_FLAG])`: Draws a single pixel at the specified `(PX, PY)` pixel coordinates on the screen.
    *   `PX` (Number): The X-coordinate of the pixel.
    *   `PY` (Number): The Y-coordinate of the pixel.
    *   `COLOR_SPEC` (Color): The color to draw the pixel. This can be:
        *   A `String` representing a predefined color name (e.g., `"RED"`, `"BLUE"`).
        *   A `Number` representing an RGB color value (e.g., `&HFFFFFF` for white).
        *   An `Array of Numbers` `[R, G, B]` or `[R, G, B, A]`, where each component is an integer from `0` to `255`.
    *   `DRAW_FLAG` (Boolean, Optional): If `TRUE` (default), the screen is immediately updated and redrawn after the pixel is drawn. If `FALSE`, the pixel is drawn to an internal buffer and not immediately displayed, requiring a subsequent `DRAWSCREEN` (or similar update) command to show changes.
-   `DLINE(PXY1, PXY2, COLOR_SPEC [, DRAW_FLAG])`: Draws a line between two specified pixel coordinate pairs.
    *   `PXY1` (Array of Numbers): The starting pixel coordinates, specified as `[PX1, PY1]`.
    *   `PXY2` (Array of Numbers): The ending pixel coordinates, specified as `[PX2, PY2]`.
    *   `COLOR_SPEC` (Color): The color of the line. See `DPSET` for `COLOR_SPEC` format.
    *   `DRAW_FLAG` (Boolean, Optional): Controls immediate screen redraw. See `DPSET` for details.
-   `DOVAL(CORNER, PRADIUSX, PRADIUSY, BORDER_COLOR_SPEC [, FILL_FLAG [, FILL_COLOR_SPEC [, DRAW_FLAG]]])`: Draws an ellipse (oval).
    *   `CORNER` (Array of Numbers): The top-left pixel coordinates `[PX, PY]` of the bounding box that encloses the oval.
    *   `PRADIUSX` (Number): The horizontal radius of the oval. Must be a positive number.
    *   `PRADIUSY` (Number): The vertical radius of the oval. Must be a positive number.
    *   `BORDER_COLOR_SPEC` (Color): The color of the oval's border. See `DPSET` for `COLOR_SPEC` format.
    *   `FILL_FLAG` (Boolean, Optional): If `TRUE`, the oval will be filled. Defaults to `FALSE` (only border drawn).
    *   `FILL_COLOR_SPEC` (Color, Optional): The color to fill the oval with. Only applicable if `FILL_FLAG` is `TRUE`. If omitted, defaults to `BORDER_COLOR_SPEC`. See `DPSET` for `COLOR_SPEC` format.
    *   `DRAW_FLAG` (Boolean, Optional): Controls immediate screen redraw. See `DPSET` for details.
-   `DCIRCLE(CENTER, PRADIUS, BORDER_COLOR_SPEC [, FILL_FLAG [, FILL_COLOR_SPEC [, DRAW_FLAG]]])`: Draws a circle.
    *   `CENTER` (Array of Numbers): The pixel coordinates `[PX, PY]` of the center of the circle.
    *   `PRADIUS` (Number): The radius of the circle. Must be a positive number.
    *   `BORDER_COLOR_SPEC` (Color): The color of the circle's border. See `DPSET` for `COLOR_SPEC` format.
    *   `FILL_FLAG` (Boolean, Optional): If `TRUE`, the circle will be filled. Defaults to `FALSE` (only border drawn).
    *   `FILL_COLOR_SPEC` (Color, Optional): The color to fill the circle with. Only applicable if `FILL_FLAG` is `TRUE`. If omitted, defaults to `BORDER_COLOR_SPEC`. See `DPSET` for `COLOR_SPEC` format.
    *   `DRAW_FLAG` (Boolean, Optional): Controls immediate screen redraw. See `DPSET` for details.
-   `DBOX(CORNER, SIZE, BORDER_COLOR_SPEC [, FILL_FLAG [, FILL_COLOR_SPEC [, DRAW_FLAG]]])`: Draws a rectangle (box).
    *   `CORNER` (Array of Numbers): The top-left pixel coordinates `[PX, PY]` of the rectangle.
    *   `SIZE` (Array of Numbers): The width and height of the rectangle, specified as `[WIDTH, HEIGHT]`.
    *   `BORDER_COLOR_SPEC` (Color): The color of the rectangle's border. See `DPSET` for `COLOR_SPEC` format.
    *   `FILL_FLAG` (Boolean, Optional): If `TRUE`, the rectangle will be filled. Defaults to `FALSE` (only border drawn).
    *   `FILL_COLOR_SPEC` (Color, Optional): The color to fill the rectangle with. Only applicable if `FILL_FLAG` is `TRUE`. If omitted, defaults to `BORDER_COLOR_SPEC`. See `DPSET` for `COLOR_SPEC` format.
    *   `DRAW_FLAG` (Boolean, Optional): Controls immediate screen redraw. See `DPSET` for details.
* `DSCREENWIDTH()` : returns the screen width in pixels. First is `0` last is `DSCREENWIDTH() - 1` 
- `DSCREENHEIGHT()` : returns the Height in pixels. First is `0` last is `DSCREENHEIGHT() - 1` 
- `DSCREENSIZE()` : returns an array with two positions: Width and Height in pixels.

### Sprites

Sprites: sprites are graphics game components that can overlap one each other. Read the  [[Working with Sprites in AGEBasic]]

### Screen `SHOW` Command

```vb
100 SHOW
```

The `SHOW` command is responsible for updating the visible screen with any pending graphical changes. Many drawing and text manipulation commands make modifications to an internal screen buffer. These changes are not immediately visible on the screen until `SHOW` is called, or until a command with an implicit or explicit "draw immediately" flag is executed.

Think of it like an artist painting on a canvas hidden behind a curtain. The `SHOW` command pulls back the curtain to reveal all the changes made since the last time the curtain was pulled back.

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
- `CabDBGetInfo(cabinetName, path)`: reads a single field from a cabinet's `description.yaml`, given its DB name and a field `path`. The path is case-insensitive and can reach nested fields with `.` and list items with `[n]` or `.n`. Examples: `CabDBGetInfo("pacman", "year")`, `CabDBGetInfo("pacman", "crt.type")`, `CabDBGetInfo("pacman", "parts[3].art.file")`. A trailing `.count` segment returns a list's length, e.g. `CabDBGetInfo("pacman", "parts.count")`. Unlike the other `CabDB*` functions, an invalid cabinet name or path **doesn't stop your program**: the problem is written to the console log and the function returns `""`, so you can keep running and, for example, show a fallback value. A missing/empty list also returns `""` for `.count`, so check for `""` before comparing the result as a number. Note: `description.yaml` doesn't currently have an `author` or `description` field, so those aren't available through this function yet — only fields that already exist in the yaml (`name`, `year`, `style`, `core`, `crt.*`, `model.*`, `parts[n].*`, etc.) can be read this way.
- `CabDBSetInfo(cabinetName, path, value)`: writes `value` into a cabinet's `description.yaml` at the same `path` syntax as `CabDBGetInfo`. Missing intermediate objects (e.g. an absent `color:` block) are created automatically, and a list index equal to the list's current length appends a new element — e.g. `CabDBSetInfo("test", "parts[2].name", "newpart")` when the cabinet currently has 2 parts, or `CabDBSetInfo("test", "roms[1]", "pacman.zip")` to add a rom. Booleans accept `0`/`1` or `"true"`/`"false"`. Returns `1` on success, `0` on failure — like `CabDBGetInfo` it never stops your program; failures go to the console log. **Notes**: the whole yaml file is rewritten, so comments, the original key order, and any fields not recognized by AGE of Joy are lost, and fields left at their default value get written out explicitly; fields that are dictionaries (e.g. `crt.screen.properties.*`) aren't supported yet; and writing does **not** change the live 3D cabinet by itself — see `WorkshopReload()` below for the workshop's test cabinet.
- `CabDBSearch(string name, string separator)`: returns a _simulated list_ separated by `separator` of cabinets that starts with `name`. Example: `CabDBSearch("ju", "|")` could return `"junofst|jupiter"`. if `name` is `"#"` will return all the games starting with special characters.
- `CabDBSearchArray(string name)`: like `CabDBSearch` but returns an array.
- `CabDBGetAssigned(room, cabinetIndex)`: returns the cabinet name assigned to a position in a room.
- `CabDBDelete(currentRoomName, cabinetIndex)`: delete the cabinet assignment to a room in the database (frees the position).
- `CabDBAdd(room, cabinetIndex, newCabinetName)`: to add a new room/position/cabinet in the database, if the position is taken the program will fail. 
- `CabDBAssign(room, cabinetIndex, newCabinetName)`: assign a cabinet to a existent position in DB. 
- `CabDBSave`: save the database and its changes.

`CabDBDelete`,`CabDBAssign`, `CabDBSave` and `CabDBAdd` returns 0 if fails, 1 if not.

## Functions for the Workshop test cabinet

- `WorkshopReload()`: **only works in the Workshop room.** Redeploys the Workshop's test cabinet from the `cabinetsdb/test` folder on disk, without having to drop a new `test.zip` — this is the way to see the effect of a `CabDBSetInfo` edit on the test cabinet while building it. Returns `1` if the reload was requested (it happens within a couple of seconds), or `0` if there's no active test cabinet loader (e.g. you're not in the Workshop, or no test cabinet has been loaded yet). **Warning**: don't call this unconditionally from `debug.bas` — the Workshop's debug console reruns `debug.bas` every time its log file changes, and an unconditional `WorkshopReload()` there would trigger an endless reload loop.

## Functions that only applies to a cabinet. 

In programs related with the cabinet, and packed inside a [[Cabinet Asset]].

Cabinet's parts are named (see the [[CDL the Cabinet Description Language#Configuring cabinet parts]]) and are identified by its position too. You can use one or each other when you need to call a function who uses a cabinet part, an index is preferred if you will call more than one function for the same part (by performance considerations).

The program fail when you name a part incorrectly or when the index is incorrect. See [[AGEBasic programing#Debug mode]] to learn how to debug your program.

- `CabInsertCoin()`: insert a coin in the cabinet.
- `CabCoinSlotSound(enabled)`: enable (`1`) or silence (`0`) the coin-drop sound at runtime. Useful for NES cores where coin-insert acts as the select button and no sound is needed. Example: `CALL CabCoinSlotSound(0)` to silence, `CALL CabCoinSlotSound(1)` to restore.
- `CabPartsCount()`: return the cabinet's parts count.
- `CabPartsName(idx)`: given a part number (starting in cero), return the name of the part, e.g.: `CabPartsName(7)` returns "joystick". 
- `CabPartsPosition(name)`: given the name of a part return it's position on the Cabinet parts list. 
- `CabPartsEnable(idx, enable)`: given a part number or a part name (`idx`),  and a Boolean (remember Booleans are numbers, a true value is anything different to cero), will disable or enable it. When a part is disabled you can't see it in VR. 
- `CabPartsList(string separator)` return a string list of cabinet's part ordered by its position.
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
- `CabPartsSetTexture(idx, filename [, invertX [, invertY]])`: apply a PNG or JPG image from the cabinet folder to the part's main material texture. `filename` is relative to the cabinet folder — path traversal is not allowed. `invertX` and `invertY` are optional booleans (0/1, default 0). The texture load is asynchronous: the call returns immediately and the surface updates once the file is fetched from cache or disk.

Examples:

```vb file="onload.bas"
10 LET base = CABPARTSPOSITION("joystick-base")
20 LET baseX, baseZ, baseH = CABPARTSGETCOORDINATE(base, "X"), CABPARTSGETCOORDINATE(base, "Z"), CABPARTSGETCOORDINATE(base, "H")
30 LET transp = CABPARTSGETTRANSPARENCY("bezel")
40 CALL CABPARTSSETTRANSPARENCY("bezel", transp + 10)

70 CALL CABPARTSEMISSION("joystick-button", 1)
80 CALL CABPARTSSETEMISSIONCOLOR("joystick-button", 190, 20, 20)
90 CALL CABPARTSSETCOLOR("left", 200, 0, 0)

REM swap the display texture on a VCR part to show digit 3
100 CALL CABPARTSETTEXTURE("vcr-display", "digit_3.png")
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

Functions that interacts with the [[AGEBasic cabinet event system]].

- `EventTrigger(event name string)`: activate an event.

#### Memory-change interface ⚠ Experimental

React to byte-level memory changes in the emulated game, similar to how **MAMEhook** reads MAME output values. Addresses come from Pugsy's cheat XML files. See [[AGEBasic cabinet event system#on-memory-change]] for the full reference and the important disclaimer about core support.

- `ONMEMORY(address, region, "varName")`: Used with `ONEVENT`. Watches a raw memory address in the given region (`0`=SAVE_RAM, `2`=SYSTEM_RAM, etc.) and injects `varName` with the new byte value when it changes.
- `ONMEMORY("cheat description", "varName")`: Cheat-name form — looks up the address from the cabinet's `cheat.xml` file.

```vb
10 ONEVENT ONMEMORY(34944, 2, "LIVES") GOTO 1000
20 END

1000 PRINT "Lives changed to: "; LIVES
1010 END
```

> [!warning]
> This feature is **experimental and probably not working** with current cores. Prefer `on-led-change` / `ONLED` for cabinet light effects.

#### LED interface

React to arcade LED signals (Player Start lamps, coin counters, etc.) emitted by the emulated ROM. Requires a core that implements the LibRetro LED interface (mame2003-plus). See [[AGEBasic LED interface]] for the full reference.

- `LEDSTATE(index)`: Returns the current state of LED `index` (0–7). Returns `1` (on), `0` (off), or `-1` if unavailable or no game is loaded.
- `ONLED(index, "varName")`: Used with `ONEVENT` to register an `on-led-change` handler at runtime. Injects `varName` with the new LED state when the event fires.

```vb
10 ONEVENT ONLED(0, "P1_LAMP") GOTO 1000
20 END

1000 IF P1_LAMP = 1 THEN CALL CABPARTSEMISSION("back", 1)
1010 IF P1_LAMP = 0 THEN CALL CABPARTSEMISSION("back", 0)
1020 END
```

# Room

Functions related with the loaded rooms.

## Room Posters

To replace posters in a Room
- `PosterRoomCount()` returns the poster count of the actual room.
- `PosterRoomReplace(position #, Image path)` to replace a poster by an image in disk. Example: `PosterRoomReplace(1, CombinePath(ConfigPath(), "posters/myposter.png"))` to replace the second poster in the room.

## Room Light configuration


> [!WARNING] **Important:** Room-specific light configuration is now deprecated. Please use the Global Light Configuration for managing lights.

This section describes the legacy methods for interacting with individual room lights. While still functional, these methods are superseded by the global light system.

- **`GetLights()`:** Retrieves a string containing the names of all lights in the currently loaded rooms. The light names are concatenated using the pipe (`|`) character as a separator. Each individual light name follows the format `"roomName:lightName"` for easy identification.    
    **Example:** `"livingRoom:ceilingLight|bedroom01:nightLamp|kitchen:overhead"`
    To work with this string:
    1. Use a string processing function (like `GetMember()`, if available in your system) to split the string into individual light names using the `|` delimiter.
    2. Further process each individual light name string to separate the room name from the specific light name (e.g., using the `:` delimiter).
- **`GetLightIntensity(lightName)`:** Returns the current intensity of the specified light.
    - **Parameter:** `lightName` (string) - The unique identifier of the light (e.g., `"room001:light1"`), obtained from the `GetLights()` method.
    - **Return Value:** A number between `0` (off) and `10` (maximum brightness).
    - **Example:** `GetLightIntensity("study:deskLamp")` might return `7.2`.
- **`SetLightIntensity(lightName, intensity)`:** Sets the intensity of the specified light.
    - **Parameters:**
        - `lightName` (string) - The unique identifier of the light (e.g., `"room001:light1"`).
        - `intensity` (number) - The desired brightness level, ranging from `0` to `10`.
    - **Example:** `SetLightIntensity("bedroom02:readingLight", 5)` will set the reading light in bedroom 02 to a medium intensity.
- **`SetLightColor(lightName, R, G, B)`:** Sets the color of the specified light using RGB values.    
    - **Parameters:**
        - `lightName` (string) - The unique identifier of the light (e.g., `"room001:light1"`).
        - `R` (number) - The red color component (typically 0-255 or 0.0-1.0, depending on your system's color model).
        - `G` (number) - The green color component (typically 0-255 or 0.0-1.0).
        - `B` (number) - The blue color component (typically 0-255 or 0.0-1.0).
    - **Return Value:** `0` if an error occurred during the color setting process.
    - **Example:** `SetLightColor("livingRoom:ambientLight", 255, 165, 0)` would set the ambient light in the living room to orange (assuming 0-255 color range).

# Configuring Global/Room Lighting

This section details how to manage the global lighting system, the recommended method for controlling illumination within the gallery.

The global lighting system provides the flexibility to adjust the color tint and intensity of light either for individual rooms or uniformly across all spaces. 
To execute a program to change the light when a room is loaded utilize the AGEBasic entries in the configuration room yaml (like `room001.yaml`):
#### Example `room001.yaml`
```yaml
agebasic:
  after-load: changelights.bas
  active: true
  debug: false
```

#### Global lighting functions

Utilize the following functions to configure the gallery's ambiance:

- **`GetGlobalLight(separator)`:** Retrieves the current global light configuration as a string. The output follows the format `r|g|b|i`, where `r`, `g`, and `b` represent the red, green, and blue color components, respectively, and `i` denotes the light intensity. This format emulates an AGEBasic list.
    
- **`SetGlobalLight(r, g, b, intensity)`:** Modifies the intensity and color of the global light.
    - `r` (number): The red color value, ranging from 0 to 255.
    - `g` (number): The green color value, ranging from 0 to 255.
    - `b` (number): The blue color value, ranging from 0 to 255.
    - `intensity` (number): The desired light intensity level.
    - **Example:** Executing `SetGlobalLight(0, 0, 255, 1.7)` would set the global light to a blue hue with an intensity of 1.7 (assuming a 0-255 color range).
    
Read about light configuration in [[AGE configuration using files#Lights Configuration]]
# Audio

[[Age of Joy]] plays two type of sounds: *ambience* (noise in rooms) and *games* sound. The volume of the audio is expressed in `dB`: `0` is normal, `20` as loud max, and -`-80` as silent. These values affect all the rooms and all the games.

A SID (commodore 64 audio files) implementation has been added in version 0.5.0-RC19.

Read [[AGEBasic Audio Reference]]
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
- `ControlRumble(id, amplitude, duration)`: to create a vibration on the controller. `duration` is a decimal where `1` means *one second*. `amplitude` is a decimal number too. `id` should be `JOYPAD_LEFT_RUMBLE` or `JOYPAD_RIGHT_RUMBLE`. Returns `true` if the controller support haptic feedback.

# Data manipulation
Sometimes you will need to storage and read information for your programs.

## Data - READ - RESTORE combo
To add information to be consumed during the program execution.
You could storage information in different "storage" that lives during the program execution. Each storage has its name.

- `DATA "storage name", x[,y,z, ...]`: comma separated list of expressions. Example: `DATA "my storage", 10, "x", D + 1`. Expressions are evaluated during the line execution not when the storage is read.
- `READ "storage name", var[, var, ...]`: to read a storage, Example: `READ "my storage", A, B, C` to read the storage of the previous example, result: `A=10, B="x", C=D+1`. There is an internal pointer to identify which is the next data to be read.
- `RESTORE "storage name"[, offset]`: move the pointer to the `offset` position. Defaults to 0.

## File management

- `GetFiles(path, separator, order)` get a list string with the file names of a path, parameters: path to scan, string separator, and order. You could use `CountMembers()` and `GetMember()` to process the result. Order:
	- `0`: alphabetic order
	- `1`: random
	- `2`: Creation date from old to new
	- `3`: Creation date from new to old
		example:  `let f = getFiles("path\\to\\files", ":", 3)` to get `"file1.txt:file2.txt:xxx.bas"` then  `GetMember(f, 1) = "file2.txt"`
- Path management:
	- `CombinePath(path1, path2)` given two paths, return a string with the combination. Example: `CombinePath("/sdcard", "file.txt")` returns `/sdcard/file.txt`
	- `ConfigPath()` returns the path to the configuration files.
	- `AGEBasicPath()` returns the path to the AGEBasic programs.
	- `CabinetsDBPath()` returns the path to the cabinet database.
	- `CabinetsPath()` returns the path to the new cabinets. (usually empty)
	- `CabinetPath()` returns the path to the actual cabinet (only available in [[AGEBasic in cabinets]]).
	- `RootPath()` the base path of AGE of Joy. Isn't the Android root home.
	- `MusicPath()` the base path to the music folder.
- File management (v0.6 and sup)
	- `FileOpen(string path, string mode)`: returns an file pointer number to identify the file opened or `-1` if fails. Mode must be: `R` read mode, `W` write mode (will rewrite the file if it exists), `A` to append to the end of the file. Only 256 files can be opened at the same time.
	- `FileRead(file pointer number)`: Read the next file string line. Use `FileEOF()` to know if you can read a next line. If it is EOF the function return an empty string (`""`). Use Returns the next line or `-1` if it fails. `type(var)` to detect if the result is a number (error) or the read string. 
	- `FileClose(file pointer number)` to close the file.
	- `FileEOF(file pointer number)`: `1` if it is closed or `0` if not. `-1` if the file is not open or the number is invalid.
	- `FileWrite(file pointer number, string line)`: add the line to the file.
	- `FileDelete(path)`: to delete a file, returns `false` if fail.
	- `FileExists(path)`: returns `true` if the file exists.

# CPU control

You can increase the CPU load, but take in consideration that it could affect the overall game performance. You can control how many lines of BASIC code the interpreter attempts to execute in a single frame.

- `GetCPU()`: obtain the actual CPU multiplier used for program executions. 
- `SetCPU(multiplier)`: change multiplier,  it's positive number representing lines-per-frame.

The default CPU value is `1`.

Read [[Optimizing Performance with SETCPU in AGEBasic ]]

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

The name of the file should be:  `myprogram.bas.debug` (the file name of the program with the `.debug` suffix)

> [!warning]
> Don't distribute [[Cabinet Asset]]s with `DebugMode` active. [[Age of Joy]] will write a file every time a program ends. If you are using [[AGEBasic cabinet event system]] the situation is worse because some programs runs more than one time (like the ones attached to `on-allways` events).
> Use `DebugMode` only in your tests.

---

# Video Player

> [!important] Available from version **0.5.0-RC19**

AGEBasic cabinets of type `19i-agebasic` can control video playback directly from scripts. This lets you build a fully scriptable video player cabinet: load a file, play, pause, stop, seek forward or backward, navigate between files, and toggle looping — all driven by button events.

Video files are stored in a dedicated folder on the device. The `VIDEOPATH()` function returns its path so you never have to hardcode it.

During playback the video fills the screen. When you call `VIDEOPAUSE` or `VIDEOSTOP`, the CRT screen is restored and your `PRINT`/`SHOW` drawing commands become visible again — this is how you display a HUD or control menu to the player.

### Streaming from the network

Use `VIDEOLOADURL` to load a video from an HTTP or HTTPS URL instead of a local file. This supports direct media links (`.mp4`, `.mkv`) and HLS adaptive streams (`.m3u8`) served by media servers such as Jellyfin, Plex, or any DLNA server that exposes an HTTP endpoint. Only `http://` and `https://` schemes are accepted.

```vb
10 VIDEOLOADURL "http://192.168.1.10:8096/Videos/12345/stream.m3u8"
20 VIDEOPLAY
```

After `VIDEOLOADURL` all other video commands (`VIDEOPLAY`, `VIDEOPAUSE`, `VIDEOSTOP`, `VIDEOSEEK`, `VIDEOTIME()`, etc.) work exactly the same as with local files.

Limitations: streams requiring custom HTTP headers (auth tokens, cookies) or DRM protection are not supported.

### Reading M3U/M3U8 playlists

Use `READM3UARRAY(path)` to load a `.m3u` or `.m3u8` playlist file into an array. Lines beginning with `#` (M3U directives and comments) and blank lines are skipped; each remaining line (URL or file path) becomes one array element.

```vb
10 DIM PLAYLIST[200]
20 PLAYLIST = READM3UARRAY(COMBINEPATH(VIDEOPATH(), "channels.m3u8"))
30 VIDEOLOADURL PLAYLIST[0]
40 VIDEOPLAY
```

Combine with `READM3UARRAY` and `LEN` to iterate through a playlist:

```vb
10 DIM LIST[200]
20 LIST = READM3UARRAY(COMBINEPATH(VIDEOPATH(), "movies.m3u"))
30 LET IDX = 0
40 LET TOTAL = LEN(LIST)
50 IF IDX >= TOTAL THEN END
60 VIDEOLOADURL LIST[IDX]
70 VIDEOPLAY
80 LET IDX = IDX + 1
90 GOTO 50
```

Read the full reference: [[AGEBasic Video Player]]

---

If you want to use ChatGPT to ask for programs, just follow this [[AGEBasic prompt for AI assistants]]

[[AGEBasic Examples]]
