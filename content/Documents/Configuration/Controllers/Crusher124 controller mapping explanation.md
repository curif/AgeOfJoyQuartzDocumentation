

This post explains what I've learned about yaml controller mapping, something I've spent some time on, setting up custom maps and resolving button conflicts.  

AOJ v0.4 yaml controller mapping The MAME core accepts four types of control inputs: Mouse, keyboard, gamepad, and lightgun. MAME recognizes a given input based on the libretro_id that has been assigned to that control button. AOJ is coded to pass Quest 2 and gamepad button presses, assigned to various libretro_ids, to the MAME core to control the game.
    
This table is the default MAME control assignments for the six primary control buttons: 
![[Pasted image 20231026091714.png]]
This table contains the first button conflict in AOJ. As you can see, Button 1 = B AND/OR Right Trigger, and Button 6 is also Right Trigger. If your game uses Button 1 and Button 6, like six button fighting games for example, pressing B, Button 1, is also pressing Button 6 at the same time. MAME is getting two inputs at the same time, it should only get one. This leads to unexpected game behavior
   
The default AOJ control assignments for the six primary control buttons are shown in this table:

![[Pasted image 20231026091749.png]]

If your game only uses one or two buttons and the joystick, really no problem. If the game has more control inputs, or you want to customize your controller button assignments, the solution is to assign each MAME default control type to your new custom button via the Libretro_ID. For example, you want to assign your B button as the game A button, and A to B.

MAME Default:
![[Pasted image 20231026091831.png]]

All these A Button libretro_id's must be re-mapped to the B Button: JOYPAD_A, MOUSE_RIGHT, and LIGHTGUN_AUX_A. All these B Button libretro_id's must be re-mapped to the A Button: JOYPAD_B, MOUSE_LEFT, and LIGHTGUN_TRIGGER.
I know this seems confusing, and it is. I will attach several of my yaml control maps as examples. If you need some help with a custom control map, post the game and the exact button assignments you want and I'll see what I can do. Remember you must be using AOJ v0.4. AOJ is essentially a single player VR frontend for MAME2003+, and multiplayer is not supported, at least not yet. Any yaml control mapping trying to 'force' multiplayer won't work. You can only play multiplayer against the CPU.

```YAML
maps:
- libretro-id: JOYPAD_B
  port: 0
  behavior: button
  maps-to:
  - control: quest-b
    path: <XRController>{RightHand}/secondaryButton
  - control: gamepad-b
    path: <Gamepad>/buttonEast
  - control: quest-right-trigger
    path: <OculusTouchController>{RightHand}/triggerPressed
  - control: keyboard-enter
    path: <keyboard>/enter
- libretro-id: JOYPAD_A
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-a
    path: <Gamepad>/buttonSouth
  - control: quest-a
    path: <XRController>{RightHand}/primaryButton
- libretro-id: JOYPAD_X
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-x
    path: <Gamepad>/buttonWest
  - control: quest-x
    path: <XRController>{LeftHand}/primaryButton
- libretro-id: JOYPAD_Y
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-y
    path: <Gamepad>/buttonNorth
  - control: quest-y
    path: <XRController>{LeftHand}/secondaryButton
- libretro-id: JOYPAD_START
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-start
    path: <Gamepad>/start
  - control: quest-start
    path: <OculusTouchController>/start
- libretro-id: JOYPAD_SELECT
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-select
    path: <Gamepad>/select
  - control: quest-select
    path: <XRController>{RightHand}/menuButton
- libretro-id: JOYPAD_UP
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: JOYPAD_DOWN
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: JOYPAD_LEFT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: JOYPAD_RIGHT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: JOYPAD_UP
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: JOYPAD_DOWN
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: JOYPAD_LEFT
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: JOYPAD_RIGHT
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: JOYPAD_L
  port: 0
  behavior: button
  maps-to:
  - control: quest-left-trigger
    path: <OculusTouchController>{LeftHand}/triggerPressed
  - control: gamepad-left-trigger
    path: <Gamepad>/leftTrigger
- libretro-id: JOYPAD_R
  port: 0
  behavior: button
  maps-to:
  - control: quest-right-trigger
    path: <OculusTouchController>{RightHand}/triggerPressed
  - control: gamepad-right-trigger
    path: <Gamepad>/rightTrigger
- libretro-id: JOYPAD_L2
  port: 0
  behavior: button
  maps-to:
  - control: quest-left-grip
    path: <XRController>{LeftHand}/gripButton
  - control: gamepad-left-bumper
    path: <Gamepad>/leftShoulder
- libretro-id: JOYPAD_R2
  port: 0
  behavior: button
  maps-to:
  - control: quest-right-grip
    path: <XRController>{RightHand}/gripButton
  - control: gamepad-right-bumper
    path: <Gamepad>/rightShoulder
- libretro-id: JOYPAD_R3
  port: 0
  behavior: button
  maps-to:
  - control: quest-right-thumbstick-press
    path: <XRController>{RightHand}/thumbstickClicked
  - control: gamepad-right-thumbstick-press
    path: <Gamepad>/rightStickPress
- libretro-id: EXIT
  port: 0
  behavior: button
  maps-to:
  - control: quest-left-grip
    path: <XRController>{LeftHand}/gripButton
  - control: gamepad-left-bumper
    path: <Gamepad>/leftShoulder
  - control: keyboard-esc
    path: <keyboard>/escape
- libretro-id: INSERT
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-select
    path: <Gamepad>/select
- libretro-id: MOUSE_X
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: MOUSE_Y
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: MOUSE_LEFT
  port: 0
  behavior: button
  maps-to:
  - control: quest-b
    path: <XRController>{RightHand}/secondaryButton
  - control: gamepad-b
    path: <Gamepad>/buttonEast
- libretro-id: MOUSE_RIGHT
  port: 0
  behavior: button
  maps-to:
  - control: quest-a
    path: <XRController>{RightHand}/primaryButton
  - control: gamepad-a
    path: <Gamepad>/buttonSouth
- libretro-id: MOUSE_MIDDLE
  port: 0
  behavior: button
  maps-to:
  - control: quest-x
    path: <XRController>{LeftHand}/primaryButton
  - control: gamepad-x
    path: <Gamepad>/buttonWest
- libretro-id: MOUSE_WHEELUP
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: MOUSE_WHEELDOWN
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: MOUSE_HORIZ_WHEELUP
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: MOUSE_HORIZ_WHEELDOWN
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: MOUSE_BUTTON_4
  port: 0
  behavior: button
  maps-to:
  - control: quest-left-thumbstick-press
    path: <XRController>{LeftHand}/thumbstickClicked
  - control: gamepad-left-thumbstick-press
    path: <Gamepad>/leftStickPress
- libretro-id: MOUSE_BUTTON_5
  port: 0
  behavior: button
  maps-to:
  - control: quest-right-thumbstick-press
    path: <XRController>{RightHand}/thumbstickClicked
  - control: gamepad-right-thumbstick-press
    path: <Gamepad>/rightStickPress
- libretro-id: LIGHTGUN_AUX_A
  port: 0
  behavior: button
  maps-to:
  - control: quest-a
    path: <XRController>{RightHand}/primaryButton
  - control: gamepad-a
    path: <Gamepad>/buttonSouth
- libretro-id: LIGHTGUN_AUX_B
  port: 0
  behavior: button
  maps-to:
  - control: quest-b
    path: <XRController>{RightHand}/secondaryButton
  - control: gamepad-b
    path: <Gamepad>/buttonEast
  - control: quest-right-trigger
    path: <OculusTouchController>{RightHand}/triggerPressed
  - control: keyboard-enter
    path: <keyboard>/enter
- libretro-id: LIGHTGUN_AUX_C
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-x
    path: <Gamepad>/buttonWest
  - control: quest-x
    path: <XRController>{LeftHand}/primaryButton
- libretro-id: LIGHTGUN_DPAD_UP
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: LIGHTGUN_DPAD_DOWN
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: LIGHTGUN_DPAD_LEFT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: LIGHTGUN_DPAD_RIGHT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-left-thumbstick
    path: <XRController>{LeftHand}/Primary2DAxis
  - control: gamepad-left-thumbstick
    path: <Gamepad>/leftStick
- libretro-id: LIGHTGUN_DPAD_UP
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: LIGHTGUN_DPAD_DOWN
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: LIGHTGUN_DPAD_LEFT
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: LIGHTGUN_DPAD_RIGHT
  port: 1
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
    path: <XRController>{RightHand}/Primary2DAxis
  - control: gamepad-right-thumbstick
    path: <Gamepad>/rightStick
- libretro-id: LIGHTGUN_START
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-start
    path: <Gamepad>/start
  - control: quest-start
    path: <OculusTouchController>/start
- libretro-id: LIGHTGUN_SELECT
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-select
    path: <Gamepad>/select
  - control: quest-select
    path: <XRController>{RightHand}/menuButton
- libretro-id: LIGHTGUN_TRIGGER
  port: 0
  behavior: button
  maps-to:
  - control: quest-right-trigger
    path: <OculusTouchController>{RightHand}/triggerPressed
  - control: gamepad-right-trigger
    path: <Gamepad>/rightTrigger
- libretro-id: LIGHTGUN_RELOAD
  port: 0
  behavior: button
  maps-to:
  - control: gamepad-start
    path: <Gamepad>/start
  - control: quest-start
    path: <OculusTouchController>/start
```
```yaml
# This is a generic 6-button fighting game control map
# that resolves many button conflicts. Games tested were MK, MK2, MK3,
# Street Fighter II, and Super Street Fighter II - The New Challengers.
# A gamepad is recommended, an XBOX Bluetooth gamepad was used for testing.
# The Quest 2 controllers are not recommended for 6-button fighting games.
# Copy and paste this file into your games' description.yaml file, then save.
# Developed by crusher124 for the AOJ Community.

controllers:
    maps:

    - libretro-id: JOYPAD_B
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-a
        path: <Gamepad>/buttonSouth
      - control: quest-a
        path: <XRController>{RightHand}/primaryButton

    - libretro-id: MOUSE_LEFT
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-a
        path: <Gamepad>/buttonSouth
      - control: quest-a
        path: <XRController>{RightHand}/primaryButton

    - libretro-id: JOYPAD_Y
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-x
        path: <Gamepad>/buttonWest
      - control: quest-x
        path: <XRController>{LeftHand}/primaryButton

    - libretro-id: LIGHTGUN_AUX_B
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-x
        path: <Gamepad>/buttonWest
      - control: quest-x
        path: <XRController>{LeftHand}/primaryButton

    - libretro-id: JOYPAD_A
      port: 0
      behavior: button
      maps-to:
      - control: quest-b
        path: <XRController>{RightHand}/secondaryButton
      - control: gamepad-b
        path: <Gamepad>/buttonEast

    - libretro-id: MOUSE_RIGHT
      port: 0
      behavior: button
      maps-to:
      - control: quest-b
        path: <XRController>{RightHand}/secondaryButton
      - control: gamepad-b
        path: <Gamepad>/buttonEast

    - libretro-id: LIGHTGUN_AUX_A
      port: 0
      behavior: button
      maps-to:
      - control: quest-b
        path: <XRController>{RightHand}/secondaryButton
      - control: gamepad-b
        path: <Gamepad>/buttonEast

    - libretro-id: JOYPAD_X
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-y
        path: <Gamepad>/buttonNorth
      - control: quest-y
        path: <XRController>{LeftHand}/secondaryButton

    - libretro-id: MOUSE_BUTTON_4
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-y
        path: <Gamepad>/buttonNorth
      - control: quest-y
        path: <XRController>{LeftHand}/secondaryButton

    - libretro-id: LIGHTGUN_AUX_C
      port: 0
      behavior: button
      maps-to:
      - control: gamepad-y
        path: <Gamepad>/buttonNorth
      - control: quest-y
        path: <XRController>{LeftHand}/secondaryButton
```

```yaml
controllers:
    maps:

    - libretro-id: JOYPAD_B
      port: 0
      behavior: button
      maps-to:
      - control: quest-y
        path: <XRController>{LeftHand}/secondaryButton
      - control: quest-left-trigger
        path: <OculusTouchController>{LeftHand}/triggerPressed
      - control: gamepad-left-trigger
        path: <Gamepad>/leftTrigger
      - control: gamepad-x
        path: <Gamepad>/buttonWest

    - libretro-id: LIGHTGUN_TRIGGER
      port: 0
      behavior: button
      maps-to:
      - control: quest-left-trigger
        path: <OculusTouchController>{LeftHand}/triggerPressed

    - libretro-id: MOUSE_LEFT
      port: 0
      behavior: button
      maps-to:
      - control: quest-y
        path: <XRController>{LeftHand}/secondaryButton

    - libretro-id: JOYPAD_A
      port: 0
      behavior: button
      maps-to:
      - control: quest-a
        path: <XRController>{RightHand}/primaryButton
      - control: quest-x
        path: <XRController>{LeftHand}/primaryButton
      - control: gamepad-a
        path: <Gamepad>/buttonSouth
      - control: gamepad-y
        path: <Gamepad>/buttonNorth

    - libretro-id: MOUSE_BUTTON_4
      port: 0              
      behavior: button
      maps-to:
      - control: quest-a
        path: <XRController>{RightHand}/primaryButton
      - control: quest-x
        path: <XRController>{LeftHand}/primaryButton

    - libretro-id: JOYPAD_Y
      port: 0
      behavior: button
      maps-to:
      - control: quest-right-trigger
        path: <OculusTouchController>{RightHand}/triggerPressed
      - control: quest-b
        path: <XRController>{RightHand}/secondaryButton
      - control: gamepad-b
        path: <Gamepad>/buttonEast
      - control: gamepad-right-trigger
        path: <Gamepad>/rightTrigger

    - libretro-id: MOUSE_MIDDLE
      port: 0
      behavior: button
      maps-to:
      - control: quest-b
        path: <XRController>{RightHand}/secondaryButton
```

---

Source (Discord) https://discord.com/channels/1066438667989696645/1068505292876288050/1160040219299549214


