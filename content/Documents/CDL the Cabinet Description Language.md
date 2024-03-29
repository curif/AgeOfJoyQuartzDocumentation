# This document describes the CDL (Cabinet Description Language)

The term CDL refers to the characteristics of a cabinet for a specific game.

## Cabinet Asset structure

Cabinets contains two main components:

* **Cabinet Model**: Consider a piece of wood furniture that is unpainted and has the shape and components of an arcade cabinet.
* **Cabinet assets**: is a zip file that contains the side art stickers, bezels, marquees, and so on, as well as a description file that describes how to paint, how to place the stickers, marquee color light, tv (crt) position, the video to play on the screen when nobody is playing, etc.

The **models** of the cabinets, such as Galaga and Xevious, are included in the game, developed by an graphic artist, in a way that its design allows you to *re-skin* them. New versions of the game should include new models.

> Starting at version 0.2 models can be included in the cabinet asset too.

Without any special knowledge, it is possible to reuse a cabinet model, personalize it, zip the files, and copy it to the headset. Because all cabinets are made in this manner, the game does not include any cabinets assets bundled on it; however, you can create your own or download them starting with a base design. In fact, you can use a "galaga" design and change the side art, bezel, marquee, and so on. And then make a new one.

![[Cabinet Assets.png]]

> Note: You don’t need to be a programmer or a graphics designer to make new cabinets assets starting of a base model.

## YAML

CDL is written in [[YAML]]. 

The special file ```description.yaml``` describes the parts of the cabinet.

YAML is composed by `keys` and `values` in the form:
```yaml
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

A detailed tutorial: [YAML Tutorial: Everything You Need to Get Started in Minutes](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started).

# description.yaml file
## description.yaml elements

A [[YAML]] document usually starts with `---`

```yaml
---
name: xevious
year: 1982
author: curif
comments: is a vertically scrolling shooter arcade video game developed and published by Namco in 1982. It was released in Japan by Namco and in North America by Atari, Inc. Controlling the Solvalou starship, the player attacks Xevious forces before they destroy all of mankind. The Solvalou has two weapons at its disposal: a zapper to destroy flying craft, and a blaster to bomb ground installations and enemies. It runs on the Namco Galaga arcade system.

rom: xevious.zip
timetoload: 18
md5sum: fe6e9e3d5d1faaab2f53d97fed83c562

enablesavestate: false
statefile: state.nv
space: 1x1x2

material: black
```

* `name`: name of the cabinet, usually the same name of the ROM. if the ROM is `dkong.zip`, then the cabinet asset file name is `dkong.zip` too and the name of the cabinet is `dkong`. Please don't confuse files, that usually happens because cabinet assets and ROMs have the same file name, but, by using this way, it's easy to know witch cabinet asset is made for each [[ROM]], just store those files in different folders. 
* `year`: game distribution year[^1]
* `rom`: file name of the [[ROM]] file.
* `timetoload`: (optional) Time to load is the time that the engine wait after load the game. It tells MAME to load the game, wait N timetoload seconds, and then tells it to insert a coin. There isn't any way to know when MAME finished the boot phase, then the only way is to wait. Obviously not all games take the same, and because of that we need to configure `timetoload`. To obtain a `timetoload` just counts the seconds that the boot phase take.
* `md5sum`: MD5 can be used as a [checksum](https://en.wikipedia.org/wiki/Checksum) to verify [data integrity](https://en.wikipedia.org/wiki/Data_integrity) against unintentional corruption ([Wikipedia](https://en.wikipedia.org/wiki/MD5)). To verify if your ROM is the same that the one we tested, go to [this page](https://curif.github.io/AgeOfJoy-ROMCRC/index.html) and get the MD5 of your ROM, compare it with the registered, must be the same.
* ~~`enablesavestate`: Enable it (true) if AGE of Joy should save the state after the `timetoload` period. This key is optional, defaults to false. [^2]~~
* ~~`statefile`: file name of the state file. This key is optional, defaults to `state.nv`. [^2]~~
* `material`: (optional) a material to use for all parts of the cabinet. materials are explained below.
* `space`: Short of *Occupied Space*. Space in units that the cabinet will fill in the Room: [[Cabinet space sizes]]

#### Optional keys:

- `author`: cabinet author Nik name.
- `comments`: any extra relevant information

### The `enablesavestate` key

> [!warning] 
> states isn't working and was  deprecated.


Each game has its own boot process, which is initiated when the arcade gallery owner powers on the cabinet. Bypassing the boot process is a desirable feature that allows the player to skip the boot process every time he or she wants to play.

To avoid this process, AGE of Joy saves the game's state (memory, CPU states, etc.) after the 'timetoload' period of time has passed. The game will re-start at that point the next time it is run, skipping the boot load phase and arriving at the point where the game is ready to accept the first coin. It's similar to how a computer goes and back from hibernation.

### Cabinet models reference

```yaml
style: xevious
```
* `style`: is the name of the *Cabinet Model*. The most common cabinets are bundled in the game and can be reused. Members of the AGE of Joy community frequently reuse cabinet models to create a new one.
	* Available styles:  timeplt,  galaga, pacmancabaret, frogger, defender, donkeykong, xevious, 1942, stargate, junofrst, digdug, tron, joust, cocktail
	

```yaml
model:
  file: NeoGeo.glb
  style: mslug
```

* `model`: a document to describe the cabinet model to use when the model is bundled in a cabinet asset (not inside the game). The model key and the style key are mutually exclusive and cannot exists in the same `description.yaml` file at the same time. 
* `file`: Is the file name of the model. These models files are in `glb` (gLTF) binary format. The cabinet asset must contain the file unless a `style` key exists.
* `style`: part of the model document, refers to a previous uploaded cabinet asset model. In the example, the `mslug.zip` file cabinet asset must contain a `NeoGeo.glb` model. This key is optional, defaults to the actual model.

## Cores

[[Age of Joy]] has bundled [[Cores]] for your selection. Options:
- `mame2003+`
- `mame2010`

```title="description.yaml"
core: mame2003+
```
## Attraction videos

Every game runs it's own introduction when nobody is playing, showing the game play or instructions. Because of the limited power of some devices, not all games can be emulated at the same time to display these screens. To solve this problem and to obtain the more accurate experience possible an introduction video is playing when the player is not in game mode (playing the game). These videos are typically obtained using RetroArch (by running the game and recording the introduction part), the result is a `.mkv` file that can be included in the cabinet asset.

```yaml
video: 
  file: video12.mkv
    inverty: true
    invertx: true
```
* `video`: optional, a document describing the video to play.
* `file`: file name of the video, must be included in the cabinet asset.
* `invertx`: flip the video by the x axis (optional).
* `inverty`: flip the video by the y axis (optional).

## Configuring cabinet parts

tips:

* A part is a component of the model, like the left wall, the bezel or the marquee.
* Each part of the cabinet can be configured.
* Not all cabinet models use the same parts.

### Parts
```yaml
parts:
  - name: left
    type: default
    art: 
      file: left.png
      invertx: true
      inverty: true
  - name: right
    art: 
      file: right.png
```
* `parts`: optional. A list of documents describing the parts of the model. If is missing, the engine will configure all the parts using the `material` key in the root of the document. Each `part` document describes the way the part is skinned: can be a `material`, a `color` or an `art`.
* `name`: name of the part to be configured. Each part that is not described in the list is configured according the `material` key (root). Each part registered in 'description.yaml' must have a component in the cabinet model (the name of the object in [[Blender]])
* type: can be `bezel`, `marquee`, `blocker` or `default`. Optional key, defaults to `default` if missing.

![[Pasted image 20240202085322.png]]

(parts in blender)

#### `type` parts:

[[Age of Joy]] reacts to the `type` key offering special characteristics and functions for each one.

* `default`: For a common component, like the left wood.
* `bezel`: to apply to a component that will show an image with transparency. Usually for a bezel.
* `marquee`: to show images with background lights. Typically for the marquee, but some cabinets (such as xevious or tron) have more than one.
* `blocker`: a component to limit the player movement on it. If you don't add a `blocker` part Age of Joy will create one around the cabinet. The player cannot cross the `blocker` area. Read the [[Player Blockers]] page to understand how to use it.

### Coloring parts

The [RGB color](https://en.wikipedia.org/wiki/RGB_color_model) to apply to the cabinet component.
Example:
```yaml
    color:
      r: 238
      g: 232
      b: 176
      intensity: 1
```
* color: the color document
	* r: red color component (integer 0-255)
	* g: green color component (integer 0-255)
	* b: blue color component (integer 0-255)
	* intensity: intensity multiplier, integer, can be negative to obtain darker variants of the color.

### Apply a material to parts

A material is a pre-configured color, may be skinned (with textures) or not. They are included in the game.

Example:

```yaml
  - name: bordercrt
    material: plastic
```

* `material`: the name of one included material in the game.

#### Material options:
* `black`: black wood cabinet
* `base`: base material to modify (colors for example)
* wood:
	* `lightwood`
	* `darkwood`
* `plastic`
* glass:
	* `dirty glass`: a dirty one.
	* `clean glass:` a clean reflective glass.
	* `layer glass`: allows transparency on pictures (like 1979 Space Invaders' screen layer)

### "Art" parts

The Art document describes how the part is textured. The cabinet developer must provide images based on the requirements of each part.
Example:
```yaml
    art: 
      file: left.png
      inverty: true
      invertx: true
```
* `art`: the art document.
* `file`: file name of the image used as a texture for the part. The file must be included in the cabinet asset.
* `invertx`: flip the image by the x axis (optional).
* `inverty`: flip the image by the y axis (optional).

### Emission

A default part could be emissive: 

```yaml
- name: bulb
	material: base
	emission:
		emissive: true
		color: 
		  r: 238
	      g: 232
	      b: 176
	
```

This example should simulate bulbs lights. Also you can turn on/off using [[AGEBasic]].

Read the [[Emission file mask]] example.

### Visibility

The `visible` key allows  [[Cabinet Artist]]s to hide cabinet parts. Useful for example to set cabinets parts that acts like marks in the [[3D space]], the most usual use case is the player head position used to set the player in a specific position when inserts a coin (using [[AGEBasic]]). This is the started visibility, you can change it with the function `CabPartsEnable()`, read [[AGEBasic in cabinets]].

Default: `true`

```
visible: false
```
### Marquee

There are exclusive keys for marquees:
Example:
```yaml
  - name: marquee
    type: marquee
    art: 
      file: left.png
      inverty: true
      invertx: true
    marquee:
      illumination-type: two-lamps
    color:
      r: 238
      g: 232
      b: 176
      intensity: -2
```
The Marquee in CDL is made up of not only the glass where the `art` image is stuck, but also the illumination system inside the cabinet. The illumination is composed by one or two lamps or tubes, and it's possible to avoid the illumination too.

You should use the `color` configuration to change the color of the lamps inside the marquee. Prefer a color that is close to yellow because incandescent lamps in the 1980s produce a warm color in that tone. Instead, choose a white color for fluorescent tubes.

`illumination-type` options: `none`, `one-lamp`, `two-lamps`, `one-tube` and `two-tubes`. Any other value fallbacks to the default: `one-lamp`. 

### Combinations

Starting on v0.5 it is possible to combine materials with colors, transparency, etc. Some keys works better with specific materials, for example, `layer glass` material with `transparency`.

Example 1: a glass with a colored layer and a bezel on top of it.

```yaml
 - name: bezel
    material: layer glass
    art:
      file: LayerBezel.png
    transparency: 70
    color:
      r: 200
      g: 100
      b: 100
```

Example 2: a tinted red wood.

```yaml
  - name: right
    material: lightwood
    color:
      r: 255
      g: 0
      b: 0
```
## Configuring the monitor (CRT)

A cathode-ray tube (CRT) is a [vacuum tube](https://en.wikipedia.org/wiki/Vacuum_tube) containing one or more [electron guns](https://en.wikipedia.org/wiki/Electron_gun), which emit [electron](https://en.wikipedia.org/wiki/Electron) beams that are manipulated to display images on a [phosphorescent](https://en.wikipedia.org/wiki/Phosphorescence) screen ([Wikipedia](https://en.wikipedia.org/wiki/Cathode-ray_tube))

In short: is the screen.

The most used screen for cabinets was the 19i. AGE of Joy comes with that model included in the game, other models could be included in the future.

The crt document comes in two parts: the root for a tube element configuration (orientation, geometry, etc) and the screen to configure how 
the game and video looks when play.
```yaml
crt:
  type: 19i
  orientation: horizontal
  screen:
    damage: low
    inverty: true
    invertx: true
    gamma: 0.5
    brightness: 1.0
  geometry:
    rotation: 
      x: -90
```
* `crt`: the crt model document (optional)
* `type`: 19i (optional) [^3]
* `orientation`: horizontal or vertical.
* `screen`: screen description sub-document.
* `geometry`: geometry description sub-document.
* `gamma`: adjust game color gamma palette. Optional, defaults to 0.5
* `brightness`: adjust game brightness
### Values by core
| Property | core | values |
| ---- | ---- | ---- |
| **brightness** | mame2010 | default, +1%, +2%, +3%, +4%, +5%, +6%, +7%, +8%, +9%, +10%, +11%, +12%, +13%, +14%, +15%, +16%, +17%, +18%, +19%, +20%, -20%, -19%, -18%, -17%, -16%, -15%, -14%, -13%, -12%, -11%, -10%, -9%, -8%, -7%, -6%, -5%, -4%, -3%, -2%, -1% |
|  | mame2003+ | 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0 |
| **Gamma** | mame2010 | default, +1%, +2%, +3%, +4%, +5%, +6%, +7%, +8%, +9%, +10%, +11%, +12%, +13%, +14%, +15%, +16%, +17%, +18%, +19%, +20%, -20%, -19%, -18%, -17%, -16%, -15%, -14%, -13%, -12%, -11%, -10%, -9%, -8%, -7%, -6%, -5%, -4%, -3%, -2%, -1% |
|  | mame2003+ | 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0 |

### Screen sub-document

```yaml
  screen:
    shader: damage
    damage: low
    inverty: true
    invertx: true
```
* `screen`: optional document.
* `damage`: those old CRTs in the arcade galleries works for long periods of time, some of them 24/7. They usually fail and it's not uncommon to see the defects during the game play. games uses _shaders_ to simulate effects like the CRT damage. 

* `invertx`: flip the game image by the x axis (optional).
* `inverty`: flip the game image by the y axis (optional).

#### Damage shader

```yaml
  screen:
    shader: damage
    damage: low
```
This shader simulate a faulty TV. The grade of damage is regulated with the damage key and can be:

* `low`: some noise in the screen, it is the default (you can avoid the key)
* `medium`: noise and scanlines
* `high`: noise, scanlines and color slide. The game is hard to play with a screen with high damage.

The damage shader is the default.

In the v0.2 the only option is `low`.
In the v0.3 you can use `medium` and `high` too.

#### Clean shader
It's available starting in the 0.3 version.

The clean shader interferes with the screen less than the damage shader. Use this one if you want to use a TV like if the TV is brand new. 

If you want, you can add some damage to the clean shader too.

```yaml
  screen:
    shader: clean
    damage: none
```
The grade of damage is regulated with the `damage` key and can be:

* `none`: without any interference, it is the default (you can avoid the key)
* `low`: some scanlines
* `medium`: more scanlines than low
* `high`: more scanlines than medium and some bright in the center and obscurity in the borders.

This shader is recommended for Vector Games.

### CRT geometry
If necessary, adjust the size and rotation of the CRT.
```yaml
  geometry:
    rotation: 
      x: -90
      y: 0
      z: 0
    scalepercentage: 100
```
* `geometry`: optional geometry CRT sub-document.
* `rotation`: to configure the rotation optional sub-document. Its possible to configure a rotation for each axis. The value is in degrees, the example rotates the screen -90 degrees in `x` axis. Optional, all axis optional too, defaults to 0.
* `scalepercentage`: increase or decrease the size of the element by a percentage. Optional, default to 100%. Integer, can be negative.

## Coin slot configuration
The place where to drop coins to start games.
The coin slot position is configured in the model.
```yaml
coinslot: coin-slot-double
coinslotgeometry:
  rotation:
    x: -90
```
* `coinslot`: coin slot model to apply: `coin-slot-double` or `coin-slot-small`
* `coinslotgeometry`: the same `geometry` sub-document than in CRT.

## Controllers

Some games needs a specific controller configuration to be playable.
Available starting at 0.4 version.

Example: 
```yaml
controllers:
	maps:
	- libretro-id: JOYPAD_B
	  maps-to:
	  - control: quest-b
	  - control: gamepad-b
	  - control: quest-right-trigger
```

You need to read the [[Controller configuration]] manual to fully understand how to map controllers and how the mapping merges with the rest of the configuration.

## Light guns cabinet configuration

![[Light guns#Light guns]]

#### Minimal configuration to activate:

```yaml
light-gun:
  active: true
```

- `light-gun`: light gun configuration section
	- `active`: to activate the light gun. (`true`/`false`). Defaults to `false`.
	- `model`: a `.glb` file with a model that represents the light gun. [[Age of Joy]] will change the right controller model by the model after load it. Remember: the load file operation is CPU intensive (even in async mode), you should use low poly models with little or not texture in order to not freeze the game for a long period of time. The model file must to be present in the [[Cabinet Asset]].
		- The model metrics is in meters, [[Age of Joy]] makes none adjustment to the size or rotation. But if it is inverted you can use the `invert-pointer` property.
		- If you download a model from internet, don't forget to give the credit to the author. You can write a file with the license in the [[Cabinet Asset]].
	- `gun`: about the gun representation in VR
		- `invert-pointer`: some meshes are inverted (they shoot to the opposite part of the gun)
		- `adjust-sight`: allows you to adjust the point where the "bullet" will hit the screen in relation to the light gun. This property allows cabinets developers to adjust the sight point in the screen to the gun model. Start testing with a little value like 2 or 3.
			- `horizontal`: measured in cms (centimeters), moves the gun up or down (without noticeable real movement of the gun) to adjust the shoot. Can be negative to move the sight down.
			- `vertical`: same as horizontal. A negative value moves to sight to the left.
	- `debug`:
		- `active`: to activate a mark where the gun hit the screen. Activate only when you are working in the cabinet development.
	- `crt`: to adapt the light gun behavior's to the CRT measurement. Don't touch it, is loaded by default, unless the CRT changes.
		- `mesh-factor-scale-x`: Screen mesh scale factor to adjust in width. 0.01 by default
		- `mesh-factor-scale-y`: idem previous. 0.01 by default
		- `border-size-x`: CRT border size left to exclude.  1.5 by default
		- `border-size-y`: idem previous. 1.0 by default
		- `invertx`: Invert to negative/positive the x point where the gun shoot the screen, true by default.
		- `inverty`: idem previous. true by default.
#### Example:

```yaml
light-gun:
  active: true
  gun:
    invert-pointer: true
    adjust-sight:
      horizontal: 0
      vertical: 2
  debug:
    active: true
```

Light guns controllers are configurable using the [[Controller configuration]]. Read the [[Default controllers configuration mapping]] too, focus on LIGHTGUN_* entries in the table.


## MAME files distribution

> [!warning]
> Available on version >= 0.5 RC4
>  It's important to note that while MAME itself is a legal project, the use of ROMs may have legal implications. Distributing or downloading copyrighted ROMs or related files without the proper ownership rights is generally illegal. It is recommended to only use ROMs and files for which you have the appropriate permissions or obtain them from legal sources, such as original arcade machine owners or authorized distributors.

In addition to the art files, various other files such as configuration files, RAM files, and more are integral components of the [[MAME]] engine. At times, these files are essential for playing a game or complementing its functionality. Sound samples serve as a prime example; while the game may run, certain sounds may be absent.

To streamline the installation process for players, [[Cabinet Artist]]s could consider including these files in the cabinet asset zip file. Furthermore, they could describe in CDL the method by which [[Age of Joy]] will distribute the files, enabling MAME to locate and utilize them seamlessly.

| File Type   | Description                                     |
|-------------|-------------------------------------------------|
| config      | Configuration files for MAME emulator settings  |
| disk-image  | Disk images       |
| sample      | Sample files containing audio for certain games |
| nvram       | NVRAM files storing non-volatile memory data    |

#### Describe the file distribution in the description.yaml file


```yaml title="description.yaml"
mame-files:
  - file: isachd.chd
    type: disk-image
  - file: isasample.wav
    type: sample
  - file: isaconfig.cfg
    type: config
  - file: isaconfig2.cfg
    type: config
  - file: isanvram.nv
    type: nvram
```

In this example:

- `mame-files`: This indicates a list of files that MAME utilizes.
	- `file`: Specifies the name of each file (must be in the zip file).
	- `type`: Indicates the type of file (e.g., disk-image, sample, config, nvram).

By including such information in the `description.yaml` file, it provides clear instructions for [[Age of Joy]] on where each file is located and its corresponding type, facilitating efficient file management and distribution.
## AGE Basic

You can run [[AGEBasic]] programs designed for a specific cabinet. [[Age of Joy]] has the ability to execute programs in response to predefined events, like when a user inserts a coin for the first time.

AGEBasic programs must be included in the [[Cabinet Asset]].

```yaml
agebasic:
  active: true
  debug: true
  after-insert-coin: start_game.bas  # Run this program when a coin is inserted
  after-load: initialize.bas     # Run this program on cabinet startup
  after-leave: save_data.bas     # Run this program when the player leaves
  variables:
	  - name: myvar
	    type: string
	    value: This is a test
```
This document details the `agebasic` configuration section within your arcade cabinet, controlling AGEBasic program behavior.

**General Settings:**

* **`active` (boolean):**
    * **Enabled (true):** AGEBasic programs run normally (default).
    * **Disabled (false):** All programs are inactive, useful for troubleshooting.
* **`debug` (boolean):**
    * **Enabled (true):** Creates debug files for each executed program.
    * **Disabled (false):** No debug files generated.

**Program Execution Triggers:**

* **`after-insert-coin` (string):**
    * Filename of the program that runs **once** when a coin is inserted to start the game.
* **`after-load` (string):**
    * Filename of the program that runs **once** after the cabinet fully loads (startup).
* **`after-leave` (string):**
    * Filename of the program that runs **once** when the player leaves the game.

**Variables:**

* **`variables` (list of objects):**
    * Defines variables accessible to all AGEBasic programs.
    * Each object specifies:
        * **`name` (string):** Unique variable name following [[AGEBasic programing#Variables]] conventions.
        * **`type` (string):** Data type (`string` or `number`).
        * **`value` (string):** Initial value (converted to specified type).

**Example Configuration:**

Read this document to fully understand how AGEBasic programs works in the cabinet's environment: [[AGEBasic in cabinets]].

## Debug

It easy to fail the task of writing a `yaml` file, It's common to introduce syntax or semantic error. [[Cabinet Artist]]s should analyze debug information about the cabinet they are making.

### Activate the debug mode

Just set to `true` the debug-mode key in the `description.yaml`:

```yaml title="description.yaml"
debug-mode: true
```

Recommended information in the [[CDL Debug mode]] page.

## Further reading

[[Cabinet building best practices]] To learn how to create a great cabinet that works smoothly in the virtual reality environment.
[[CDL best practices checklist]]

## References

[^1]: only for information, don't affect the game.
[^2]: ignored in v0.2
[^3]: the only available option.
 
---
#CDL #cabinet/artists 