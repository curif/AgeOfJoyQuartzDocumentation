There are [[Controllers]] of any type/model/brand/etc and it's impossible to map all of them in a single game.

This document explains how to map your controller to any retro game, but it's not guaranteed that any control could be mapped.

> [!note] this document apply to AGE of Joy version >= 0.4

## Visual configuration

You can use the [[Visual configuration]] if you don't want to setup the controllers behavior by modifying files.

## About Mapping

>  Refers to the action to map the [[MAME]] emulated  [[Controllers]] to the real ones.

The emulator knows anything about the controller that the player is using, then he uses a "generic controller" that must be mapped to a real one. The emulator just ask something like *"is the player pressing the `B` button?"* and AGE respond by analyzing if the player have pressed the `B` button in the Quest controller (for example). 

Each MAME frontend (like Retroarch) maps controllers using its own way. AGE uses configuration [[YAML]] files to map controllers.

## Configuration types

There are different types of controller configuration related to how the configuration is applied to a cabinet/game:

1. Global configuration: is the control configuration that apply to all cabinets.
2. Default configuration: is the configuration that apply when no other configuration exists.
3. Cabinet configuration: is the controller configuration registered within the cabinet. The cabinet builder write it in the `description.yaml`. Read about [[CDL the Cabinet Description Language]]
4. Game User configuration: is a configuration that the player wants to apply to a cabinet to modify the behavior.

### Configuration hierarchy

Refers to how AGE will merge the different mappings to get a complete one.

![[Controllers jerarquia.png]]

When a game starts:

1. AGE analyze in the  [[CDL the Cabinet Description Language]] to see if there is a section that describe the mapping, if not, it fallback to the User Cabinet Configuration.
2. AGE uses the user cabinet configuration yaml if the file exists, if not, it uses the Global Configuration.
3. Again, if the file doesn't exists, AGE will uses the global configuration.
4. If all others are missing AGE will use the default configuration.

### Merge

AGE will merge the controller mapping configuration in the hierarchy order. That means, if a Cabinet Control or user configuration exists, it will be merged with the Global and then with the Default.

For example, suppose the user maps the `B` button in the user configuration, but that button is configured in the Cabinet, then the cabinet configuration will remains. But the only configuration is the `B` button, and the user configure the `X` and `Y` in the Global configuration then all will be merged. After the merge, the `B` (cabinet configuration) and `X` and `Y` (global) are configured. The rest of the mapping is merged with the default to get a full controller mapping working.

### Configuration files

The controller configuration YAML files are in the path: `/sdcard/Android/data/com.curif.AgeOfJoy/configuration/controllers`.

- Global configuration file: `global.yaml`
- User cabinet configuration file: combines the cabinet name with the `.yaml` extension, example: `galaga.yaml`, complete path: `/sdcard/Android/data/com.curif.AgeOfJoy/configuration/controllers/galaga.yaml`

if you want to change the controller behavior for all the games, then create a `global.yaml`. And if you want to change something specific for a game, then create a configuration for the cabinet, like `galaga.yaml`. Both will be merged, and then merged with the default.

# Controller description YAML

Read [[Quest controller controls]] to know the meaning of the control codes like `quest-b`
Also read [[Gamepad controller controls]] for control codes starting with `gamepad`.

## Example

```yaml
maps:
- libretro-id: JOYPAD_B
  port: 0
  maps-to:
  - control: quest-b
  - control: gamepad-b
  - control: quest-right-trigger
- libretro-id: JOYPAD_X
  port: 0
  maps-to:
  - control: gamepad-x
  - control: quest-x
- libretro-id: JOYPAD_START
  port: 0
  maps-to:
  - control: gamepad-start
  - control: quest-start
- libretro-id: JOYPAD_RIGHT
  behavior: axis
  port: 0
  maps-to:
  - control: quest-left-thumbstick
  - control: gamepad-left-thumbstick
```

This yaml file shows how to create a map list that maps the libretro (MAME) controls to the real ones.
- `maps`: is the map list
	- `libretro-id`: refers to the MAME control to be mapped, read the list in [[MAME controller standard table]].
	- `port`: MAME support many ports. A port represent a virtual connection to a controller device. Ports starts in 0, and some games uses the 0 and the 1 at same time for control of a single character (like Robotron). Zero is the default and the key can be omitted.
	- `behavior`: is the way that the control works. Only two are available: `button` and `axis`. You can omit the key when is a button. 
	- `maps-to`: is the list of real controllers and controls (buttons for example) to check when MAME wants to know if the control is pressed.
		- `control`: is the real control to check, explained below. Can be more than one, AGE will check all of them.

### Behavior of the control

- `button`: just a button, like `X`, `Y`, `L2`, etc. 
- `axis`: refers to an axis controller (Joystick) like the `quest-left-thumbstick`. In the example, `JOYPAD_RIGHT` is mapped to the thumbstick in the left quest controller, then AGE will check if the user is moving the thumbstick to the right part of the joystick to respond when MAME ask if the joypad right is active.

> [!warning] you can't mix an `button` control (like the B button) with an `axis` (like the left thumbstick) in the same mapping.

### Merge

When AGE merge configurations it just replace or add mappings to get a most complete one. The merge is at `libretro-id` level. That means AGE will not merge the controls but replace all the mapping of the `libretro-id`.

Example:

your `global.yaml`:

```yaml
maps:
- libretro-id: JOYPAD_B
  maps-to:
  - control: quest-y
- libretro-id: JOYPAD_X
  maps-to:
  - control: gamepad-x
  - control: quest-x
```

`galaga.yaml`:

```yaml
maps:
- libretro-id: JOYPAD_B
  maps-to:
  - control: quest-b
  - control: gamepad-b
  - control: quest-right-trigger

```

Merged for galaga cabinet:

```yaml
maps:
- libretro-id: JOYPAD_B
  maps-to:
  - control: quest-b
  - control: gamepad-b
  - control: quest-right-trigger
- libretro-id: JOYPAD_X
  maps-to:
  - control: gamepad-x
  - control: quest-x
```

As you can see `JOYPAD_B` is replaced and `JOYPAD_X` is added. The final one will contains the remaining configuration in the [[Default controllers configuration mapping]].

### Paths

The mapping works with known controllers and its parts registered in AGE's internal tables. There is a big probability that your controller works out of the box, or may be you need to touch a configuration file to add controls because your controller is not fully compatible. But are some situations where unknown incompatible controllers aren't registered in the internal tables, for them the `path` key exists.

In [[Unity]] controllers and controls are reached using a path. A path looks like: `<XRController>{LeftHand}/primaryButton`. AGE internal processing uses the Unity paths to know if the control is active. Users could register a path too if they need it.

Example:

```yaml
maps:
- libretro-id: JOYPAD_B
  behavior: button
  maps-to:
  - control: my-unique-controller-b
    path: <an-unknown-controller>{RightHand}/secondaryButton
  - control: quest-b
  - control: gamepad-b
  - control: quest-right-trigger
```

In this example a user maps an unknown controller using its path. The user should know about unity development to understand how to get that path.

Don't try this example it will not work. It's just to illustrate how the `path` works.

## The default configuration

Most controllers should work out of the box because AGE have an internal mapping configuration that match with common used controllers in the market (the default mapping). If you can connect your controller to the headset (using Bluetooth for example) there is a great possibility that it works out of the box.

[[Default controllers configuration mapping]]

Remember that the default controller configuration will be merged with your configuration.

# Crusher124 controller mapping explanation

[[Crusher124 controller mapping explanation]]

## Using ChatGPT

[[Creating maps for controllers using LLMs like ChatGPT]]


#v0_4 