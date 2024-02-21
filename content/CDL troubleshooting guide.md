If you as a [[Cabinet Artist]] have issues with your new created cabinet please follow this rules in order to fix it.

## Recommended readings

- [[CDL the Cabinet Description Language]]
- [[CDL Debug mode]]
- [[Cabinet building best practices]]
- [[AGEBasic programing#Debug mode]]

## Upload a test cabinet

The test cabinet is your newly created cabinet, but you need to rename it as `test.zip`. You should rename it again after it is tested and ready to publish it. 

Run the game first and upload  it to the `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets` folder.

> [!note] 
> The cabinet will reload if you are in the workshop area and you upload a new version.
## Troubleshooting

It's recommended to activate the [[CDL Debug mode]] to troubleshoot a cabinet.

After dropping in your 'test' cab, you see this-

![[Pasted image 20240221121725.png]]
WTF, No cab?

This almost always indicates a `description.yaml` that has the wrong formatting. As such, your cab never loads because AOJ can't read the yaml.  Go back and double check the yaml for formatting errors, read the [[CDL Debug mode]] information too.  This step is CRITICAL.  EVEN. ONE. SINGLE. FORMATTING. ERROR. IS. TOO. MANY!  Another cause could be your cab model is missing required parts or the required parts are mis-named.  Go back and check.  Now that the `description.yaml` and/or cab model is fixed, zip all the files up again, restart AOJ and load it in.  Moving on…

### Incorrect parts

**Now you see something similar to this…**

![[Pasted image 20240221121911.png]]

Well, here's the good news, AOJ can read your `description.yaml`  This monstrosity usually indicates that you have a part named in the yaml, but not named in the cab model, or named incorrectly.  Another very likely cause is a spelling error between the cab model part and the yaml named part.  A cab model part named joystikc is not the same as the yaml part named joystick.  The names are case sensitive also.  Double check the parts named in the yaml are present in the cab glb, and spelled the same in each case.  Another possible cause is your model.glb name is not the same as the model name listed in the yaml.  If you change anything in the cab glb model, AOJ must be restarted, or the old, incorrect cab model will still be in memory and display.  Good practice says to restart AOJ after any changes in the yaml or cab model.  Zip up the corrected files, restart AOJ, and load up.  Now that the part names and spelling are sorted out…

### Parts are rotated…

![[Pasted image 20240221122012.png]]
This is a relatively easy fix.  Go check the 'crt' and 'coin-slot' section in the yaml, and look for the section called 'geometry'.  These settings affect the rotation of these parts.

```yaml file="description.yaml"
crt:
  type: 19i
  orientation: horizontal   Set to vertical for vertical screen games
  screen:
    shader: clean
    damage: none
    inverty: true
  geometry:		The rotation around the X axis.  Try setting this to zero first or 
    rotation:                   if missing, copy and paste these settings.
      x: -90			

coinslot: coin-slot-double  
coinslotgeometry:	The rotation around the X axis.  Try setting this to zero first or 
  rotation:                     if missing, copy and paste these settings.
    x: -90	
```

Zip, restart, and load.  Now that the screen and coin-slot are fixed, let's start a game by dropping in a quarter.

### The game screen is upside-down

![[Pasted image 20240221122216.png]]

Another easy fix.  Go to the 'crt' section, the game screen section, and look here:

These settings control the orientation of the GAME screen.

```yaml file="description.yaml"
crt:
  type: 19i
  orientation: horizontal           Set to vertical for vertical screen games
  screen:
    shader: clean
    damage: none
    inverty: true			Invert the game screen on the Y axis, true or false
    invertx: false		Same for X axis. Change one or both to orient the game screen
  geometry:
    rotation:
      x: -90

```

### Attract video upside down…

![[Pasted image 20240221122318.png]]

The attract video file screen is separate from the game screen.
Another easy fix.  go to the 'video' section of the yaml:

```yaml file="description.yaml"
video: 
  file: galaga.mp4
  invertx: true		The video screen is separate from the game screen.  Add or adjust these
  inverty: true              settings true or false to correct the video screen along the X and/or Y axis.

```

## Complete, working cab…


![[Pasted image 20240221122422.png]]

Congratulations, your first cab!

This guide is by no means comprehensive, but serves as a starting point to troubleshoot common problems when loading a cab for the first time.

---
Author: @Geometrizer

#CDL 