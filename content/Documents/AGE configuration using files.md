
To change a configuration file you will need to know the [[YAML]] language that is widely used by the game. Like in CDL, there are some rules to follow.

If you already know YAML or CDL you can jump the next section:

# YAML

CDL (Cabinet description language) is written in [[YAML]].

The special file ```description.yaml``` describes the parts of the cabinet.

## description.yaml

YAML is composed by `keys` and `values`:
```
key: value
```
The keys can only contain non-capital letters and no special characters.

Dependency are indicated using tabs. 

Values can be anything:
* integers
* floats (dot decimal delimited): 3.1416
* strings
* booleans: `true` or `false`.
* a *document* (a group of key/values) 
* a *list of values* (each element of a list starts with a `-`)

A `yaml` detailed tutorial: [YAML Tutorial: Everything You Need to Get Started in Minutes](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)

# Configuration files

You can find the files in the path `/sdcard/Android/data/com.curif.AgeOfJoy/configuration` in your Quest 2. If you don't have the folder, is because you didn't run the 0.3.0 version (or superior) yet; the first time it runs creates the folder and the default `configuration.yaml`. Once you have it you are ready to change it.

If you change the file when the game is running, then the game will react a seconds later. You don't need to restart the game.

You can change files on the Quest disk by copying or editing the file directly.

## Files types

You can have two o more types of files in the `configuration` folder:
- Global configuration: named `configuration.yaml` affects all the game.
- Room configuration: named `<room name>.yaml`. Example: `room001.yaml` or `roomintro.yaml`. Each room in the game has its own code, you can find the code in the [[Configuration control cabinet]] installed in each room; just add the `.yaml` extension to the name.

### Room configuration files

At start, only the `configuration.yaml` file exists, it is global and all the rooms respond to the configuration of that file. But, if you create a room configuration file, then the room will respond to the configuration of that file. _You don't need to repeat all the `keys` in all files, just change what you need_ in the room configuration file. For example, you can disable NPCs in the global configuration, but enable them in the `room004.yaml`. What you write in a room file affects only to that room and only the parameters that you write there, the others parameters responds to the global configuration file.

Both type of files share the same yaml structure.

## configuration.yaml elements

```yaml
npc:
  status: enabled
audio:
  background:
    volume-percent: 70	
    muted: false
  in-game-background:
    volume-percent: 20
    muted: false
locomotion:
  teleport-enabled: true
  speed: 2
  turn-speed: 80
  snap-turn-amout: 30
  snap-turn-active: false
player:
  height: 1.6
```

## `npc`

Non playing characters configuration.

`status` can be:
* `enabled`: the walk and play as usual.
* `static`: they will walk to a position in the room and stay there forever.
* `disabled`: to disable the NPC. They will left you alone in the room.

## `audio`
### `background` 
It's the background sound, you can change the volume or mute it.
* `volume-percent`: 0-100, 100 is loud
* `mute`: true/false. You can mute the background audio using this key.
### `in-game-background` 
It's the background sound when you play a game. The keys and values are the same. Maybe you want to mute the background sound when you are playing, or decrement to a 20% (like the example)

## Locomotion

Refers to the player's movement in the virtual space (walk, rotate, etc.)

* `teleport-enabled`: `true` or `false`. Activate/deactivate the [[In Room Teleportation]] 
* `speed`: is the translation velocity. The velocity used to walk.
* `turn-speed`: is the velocity that the player used when rotate.
* `snap-turn-active`: `true` or `false`. Activate/deactivate snap turn.
* `snap-turn-amount`: number of degrees to rotate.

## Player

To configure some aspects about the player:

- `height`: a decimal point number that represents the player's eye sight height. Values can vary from 1.35 to 1.85 max. 1.6 is an average height. The default (zero) is your real height.

#### Heights

Use `Calculated` (`height` zero) to use your real height in the game. 
The values are not exact but indicative.

| Option            | Height (aprox)    |
|----------------------|-----------|
| Pac-man (short)      | 1.35m     |
| Sonic                | 1.4m      |
| Pikachu              | 1.45m     |
| Mario                | 1.5m      |
| Luigi                | 1.55m     |
| Final Fantasy (avg)  | 1.6m      |
| Megaman              | 1.65m     |
| Street Fighter       | 1.7m      |
| Donkey Kong          | 1.75m     |
| Mega Boss            | 1.8m      |
| NBA Jam (tall)       | 1.85m     |

#### Example

```yaml
player:
  height: 1.6
```

# AGEBasic

[[AGEBasic]]  a special version of the BASIC programming language. To learn how to program in AGEBasic read the  [[AGEBasic programing]] document.

You can change the configuration of any the room using an AGEBasic program. The program will run after the room loads. If you want to run the same AGEBasic program globally for all the rooms, the best way is to set it in the `configuration.yaml` file. But if you want to run a different one for any room you can set it in the `<room name>.yaml` (room configuration file). You can set both, and if a room have a configuration file with an `agebasic` entry on it, the configuration cabinet will use the last one and discard the global one. This is the normal behavior for all configuration files (see the Merging section below)

The programs runs in the [[Configuration control cabinet]], and you can see the results in the screen.

As always you can set the `debug` entry and the configuration cabinet will save the errors (if any) in a file . Also you can set the Debug Mode with the AGEBasic funcion `DebugMode(1)` in your AGEBasic program. 
#### Example

`room001.yaml`
```yaml
agebasic:
  after-load: configroom1.bas
  active: true
  debug: false
```

This `configroom1.bas` will run after the room001 is loaded, because is configure in the `room001.yaml` file.
The `configroom1.bas` must exists in the `/sdcard/Android/data/com.curif.AgeOfJoy/AGEBasic` path. If not, you will receive an error like: 

![[Pasted image 20240102130617.png]]

If the program has some syntax error on it, you should check it again in the screen of the configuration cabinet:
![[Pasted image 20240102130838.png]]

Or if the program runs without any problem:

![[Pasted image 20240102131007.png]]


---

## Merging Example

In this example, you disabled all NPCs except those in room001.

`configuration.yaml`:
```yaml
npc:
  status: disabled
audio:
  background:
    volume-percent: 70	
    muted: false
  in-game-background:
    volume-percent: 20
    muted: false

```
`room001.yaml`
```yaml
npc:
  status: enabled
```
