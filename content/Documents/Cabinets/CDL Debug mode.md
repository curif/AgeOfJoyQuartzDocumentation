Debugging a cabinet is a big part of the action of create one new cabinet.

Please read [[Testing cabinets assets#3- Test the cabinet]] before.
## How to activate the debug mode

Just set to `true` the debug-mode key in the `description.yaml`:

```yaml title="description.yaml"
debug-mode: true
```

> [!tip] 
> Remove the `debug-mode` key or set it to `false` before distribute your cabinet. 

## Test environment

The `debug-mode` is automatically activated for the cabinet tested in the workshop.
## Debug information 

[[Age of Joy]] will save a debug `log` file in the folder `/debug` of your installation.

#### Example

```txt title="alien3.log"
CABINET: alien3
Cabinet: OK
Part #1: Object_3 ART: OK
Part #1: Object_3 MATERIAL: OK
Part #1: Object_3 MATERIAL/ART: OK
Part #2: machinegun ART: OK
Part #2: machinegun MATERIAL: OK
Part #2: machinegun MATERIAL/ART: OK
Part #3: machinegun.001 ART: OK
Part #3: machinegun.001 MATERIAL: OK
Part #3: machinegun.001 MATERIAL/ART: OK
Part #4: gunbase decal ART: OK
Part #4: gunbase decal MATERIAL: OK
Part #4: gunbase decal MATERIAL/ART: OK
...
Part #12: front MATERIAL: OK
Part #12: front MATERIAL/ART: OK
Part #13: joystick ART: OK
Part #13: joystick MATERIAL: OK
Part #13: joystick MATERIAL/ART: OK
Part #14: button-blue ART: OK
Part #14: button-blue MATERIAL: OK
Part #14: button-blue MATERIAL/ART: OK
Part #15: button-yellow ART: OK
Part #15: button-yellow MATERIAL: OK
Part #15: button-yellow MATERIAL/ART: OK
Part #16: bezel ART: OK
Part #16: bezel MATERIAL: OK
Part #16: bezel MATERIAL/ART: OK
Part #17: marquee ART: System.IO.FileNotFoundException: C:\Users\curif\cabs\cabinetsdb/test/marquee.pngxxxxdxx
Part #17: marquee MATERIAL: OK
Part #17: marquee MATERIAL/ART: OK
Year: System.ArgumentException: Year out of range
Style: OK
Coin Slot: OK
CRT: OK
lightgun: System.Exception: file M41A.glbxxxx doesn't exists. ]
video: System.ArgumentException: video undeclared or file [alien3.mkvxxxxxxxxxxxxx] doesn't exists
--------------------------------------------------
```

In this example the art's part #17 refers to a non existent file (the name is wrong). The [[Light guns]]'s  model and the video file are also wrong and the year is out of range.


[[Age of Joy]] will check some inconsistences during the load process of the cabinet, but some errors should appear during other instances. For example, if the light gun file is present but corrupt, the error will not be registered on the log file as it depends of the light gun load when the player insert the coin.

There are some keys that if they aren't present in the `description.yaml` a default value will be assigned. For example, if you miss completely the `crt` key or the `coinslot` there is not error, because a default value will be assigned to the part.

A default value for some keys are assigned in the `description.yaml` automatically if the [[Cabinet Artist]] don't assign a value. For example, if the `crt` key is missing or the `coinslot` there is not error, because a default value will be assigned to that parts.

[[AGEBasic]] programs will be parsed/compiled when the game needs them and not when the cabinet loads. In order to check them you should look for the [[AGEBasic programing#Debug mode]]

#CDL #agebasic 