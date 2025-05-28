To configure the lighting for a specific room using AGEBasic, you need to designate a program to run when that room is loaded. For instance, to set a program for "room001", you would modify the `configuration/room001.yaml` file.

Read [[AGE configuration using files#Files types]]
### Example `room001.yaml` Configuration

YAML

```yaml
agebasic:
  after-load: changelights.bas
  active: true
  debug: false
```

In this configuration:

- `after-load`: Specifies the AGEBasic program (`changelights.bas`) to be executed immediately after "room001" is loaded.
- `active`: Indicates whether AGEBasic programs are enabled for this room.
- `debug`: Sets the debugging mode for AGEBasic execution in this room.

### `changelights.bas` Examples

Below are examples of AGEBasic programs that can be used to manipulate the global lighting when a room is loaded:

**Example 1: Setting a red and luminous ambient light.**


```vb
10 CALL SetGlobalLight(255, 0, 0, 1.5)
```

This simple program directly calls the `SetGlobalLight` function to set the red color component to its maximum (255), the green and blue components to zero, and the light intensity to 1.5, resulting in a bright red ambient light.

**Example 2: Increasing the intensity of the current global light.**

```vb
10 LET s = GetGlobalLight("|")
20 LET r, g, b = GetMember(s, 0, "|"), GetMember(s, 1, "|"), GetMember(s, 2, "|")
30 CALL SetGlobalLight(VAL(r), VAL(g), VAL(b), 2)
```

This program first retrieves the current global light configuration as a string using `GetGlobalLight("|")`, where "|" acts as the separator. Then, it extracts the red, green, and blue color components using the `GetMember` function, parsing the string based on the "|" delimiter. Finally, it uses the `SetGlobalLight` function to apply the same color values but increases the intensity to 2, effectively "turning on" or brightening the existing light color.