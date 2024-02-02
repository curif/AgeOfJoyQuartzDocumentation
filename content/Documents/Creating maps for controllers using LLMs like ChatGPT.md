
Mapping controls using [[YAML]] can be a time-consuming endeavor. Instead of spending valuable time on it, why not seek a little assistance from our trusted ally, ChatGPT?

To accomplish the task we need a *context prompt* that explain how to do it, so we can start asking for yaml code later.

### Instructions:

- open the [ChatGPT](https://chat.openai.com/) (free version is OK for this task)
- copy and paste the `context prompt`, hit enter.
- ask for [[YAML]] code as you wish
- be critic, analyze the result before use it. LLMs like ChatGPT can fail.

> [!note] 
> Is easiest to create small code blocks and compose them in a big yaml file than ask for all the maps in one prompt.  

# Context Prompt

```
background: AGE is a videogame in which the player can play other emulated games in a emulator called libretro. Libretro have two sets of controls: JOYPADs and MOUSE. To control a game the player uses real controls like JOYPADs, MOUSE and GAMEPADs that represents controllers in the reality. The controls must be mapped, so when libretro requires the status of an action (like the status of a joypad button), AGE must to respond with the status of the real player controller button. To create a map a language based on YAML is used.

This is the structure of the yaml document:

maps:
- libretro-id: JOYPAD_B
  port: 0
  behavior: axis
  maps-to:
  - control: quest-b
  - control: gamepad-b
  - control: quest-right-trigger

where maps is the list of maps, libretro-id is the action code, port is the controller conection (can be 0 to 10) and the default is 0 (can be omitted). The behavior can be axis or button, an axis can map movements to left, right, up and down with the same control. 
maps-to is a list of actions in the real controller. 

This is the list of libretro-id used for the emulated game to ask for the status of the "maps-to control" for Joypads: JOYPAD_A, JOYPAD_B, JOYPAD_X, JOYPAD_Y, JOYPAD_SELECT, JOYPAD_START, JOYPAD_UP, JOYPAD_DOWN, JOYPAD_LEFT, JOYPAD_RIGHT, JOYPAD_L, JOYPAD_R, JOYPAD_R2, JOYPAD_L2, JOYPAD_R3, JOYPAD_L3.
This is the list of libretro-id used for MOUSE axis movement: MOUSE_X (moves in x coordinate), MOUSE_Y (moves in the Y coordinates), MOUSE_WHEELUP (mouse wheel), MOUSE_WHEELDOWN, MOUSE_HORIZ_WHEELUP, MOUSE_HORIZ_WHEELDOWN. These are for buttons: MOUSE_LEFT (left button), MOUSE_RIGHT, MOUSE_MIDDLE, MOUSE_BUTTON_4 and MOUSE_BUTTON_5.

List of maps-to buttons in the joypad left: 
quest-x, quest-y, quest-start, quest-left-grip, quest-left-trigger and quest-left-thumbstick-press. 
List of maps-to buttons in the joypad right controller: quest-a, quest-b, quest-select, quest-right-grip, quest-right-trigger, quest-right-thumbstick-press. 
The maps-to axis in the joypad left is quest-left-thumbstick, and in the right one is quest-right-thumbstick. 
List of maps-to for buttons in a gamepad: gamepad-a, gamepad-b, gamepad-x, gamepad-y, gamepad-x, gamepad-select, gamepad-start, gamepad-start, gamepad-left-bumper, gamepad-right-bumper, gamepad-left-trigger, gamepad-right-trigger, gamepad-left-thumbstick-press, gamepad-right-thumbstick-press.
List of maps-to for axis in a gamepad: gamepad-left-thumbstick and gamepad-right-thumbstick.

Say ok if you understand and can help me to create the yaml documents. Remember to map only the controls that I ask for.
```

# Example questions

> [!quote] map the buton b to the button b in the quest and gamepad.

### Response

```yaml
maps:
- libretro-id: JOYPAD_B
  port: 0
  behavior: button
  maps-to:
  - control: quest-b
  - control: gamepad-b
```

****

> [!quote] maps the up, down, left, right in the port 0 to the right axis in the quest and gamepad.

### Response

```yaml
maps:
- libretro-id: JOYPAD_UP
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
  - control: gamepad-right-thumbstick

- libretro-id: JOYPAD_DOWN
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
  - control: gamepad-right-thumbstick

- libretro-id: JOYPAD_LEFT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
  - control: gamepad-right-thumbstick

- libretro-id: JOYPAD_RIGHT
  port: 0
  behavior: axis
  maps-to:
  - control: quest-right-thumbstick
  - control: gamepad-right-thumbstick

```

#v0_4 