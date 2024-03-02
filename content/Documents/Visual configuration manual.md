

The Arcade Owners stumbled upon a lot forgotten *Commodore 64* in a auction. They enclosed it each one in a custom cabinet and developed a program to control the gallery's configurations. This retro-meets-modern integration permits anyone with a coin to configure the Arcade Gallery functions.

Also you can continue configuring the game using the [[AGE configuration using files]] method as usual too.

## Capabilities

* Configure `global` and `individual` settings: This feature enables users to apply settings either to all rooms or to specific rooms individually.
* Locomotion: like the walk velocity/turn or activate and deactivate the [[In Room Teleportation]].
* player configuration: the player representation in the game. 
* [[Teleportation]] to any room: Users have the ability to teleport to any room within the virtual environment. This allows for easy and quick navigation, providing a seamless experience in exploring different areas.
* Controller configuration: allows the user to change the [[Controllers]] behavior (gamepad or Quest controls) for a game or for all the games.  The visual configuration allow the user to change the Controller configuration without the need to change the [[YAML]] config files. Read the [[Controller configuration]] for detailed information.
* Cabinet replacement: This feature grants users the freedom to place any cabinet in any position within a room. It enables customization and rearrangement of cabinets according to personal preference or desired room layout.
* NPC Behavior: Users have the ability to alter the behavior of non-playable characters (NPCs) within the virtual environment. This includes adjusting their actions or even disabling them if the user prefers to have a solitary experience in the rooms.
* Reset configuration to ground zero (actually excludes the cabinets positions and controllers configuration)

### Visual configuration Menu

![[ConfigurationMenu.png]]


---


### Global or Room setup

![[ConfigurationGlobalChange.png]]



The player has the ability to switch between two setup modes using the *Change Mode* option.

- Global mode: When the "working with Global" option is selected, any changes made will be applied to all rooms. This means that modifications or adjustments will have a universal impact and affect all rooms within the virtual environment. It provides a convenient way to make broad changes that are intended to be consistent across all rooms.

- Room mode: When the "working with Global" option is unselected, the changes made will only be applied to the specific room where the player is currently located. Each room has its own [[Configuration control cabinet]], which allows for individual customization and settings unique to that particular room. This mode provides a more localized and specific approach, allowing players to tailor their experience within each room according to their preferences.

By providing these setup modes, players have the flexibility to choose between making changes that have a global impact across all rooms or focusing on individual room customization using the dedicated Configuration control cabinet specific to each room.

The configuration menu changes depending on the option selected. 

---
### Player height

You can change the player height and age in the visual configuration too. And, if you set it to the tallest one, you can play seated if you want.

Follow these steps: [[Set player height using visual configuration]]

---
### NPC's Behavior setup

![[configurationNPC.png]]

---
### Audio Setup

![[ConfigurationAudio.png]]

---
### Locomotion setup

> [!note] available only in Global Configuration

![[locomotion.png]]

---
### Teleportation

This option allows the player to execute the [[Teleportation]] action. The player will travel to the selected room by selecting the "teleport" option.

The jump is executed immediately.

![[ConfigurationTeleportation.png]]

---
### Setup Controllers

![[ConfigurationControllers.png]]

The user can setup the controllers behavior for all games when is working in *Global mode*. If not, a game should be selected to remap controls for the game in the room

The player could map any control by selecting up to five different real controls to respond the mapping.

Each control should be allocated in a `Port`. A port is a virtual representation of a connector to a controller. Ports are numbered starting by zero.

![[Controller configuration#About Mapping]]

Read more about [[Controller configuration]].

---

### Cabinet replacement

![[ConfigurationReplaceCabinets.png]]

You can replace a cabinet in a room for other that you uploaded previously.


---

### Reset
![[ConfigurationReset.png]]
> [!warning] Use this option with caution.

Select this option to reset the setup and start from ground zero. 

Basically, deletes de global or room configuration [[YAML]] file.

Excludes:
- cabinets positions
- controller configuration
---

### AGEBasic programs

This section shows how to control the [[Documents/AGEBasic]] programs execution.


![[ConfigurationAGEBasic.png]]

To known more about AGEBasic please read the [[AGEBasic programing]] section in this documentation. 

#### Options:
- Program: to select the program to run. The list will contain all programs in the AGEBasic path that don't end with compilation errors. The [[Configuration control cabinet]] compiles all the programs when you enter into the AGEBasic section in the menu.
- Run: to run the selected program. 
- Compile all files again: if you upload a new program (developed by you or by any user), the program should be compiled before run. Just run this option if you change anything.
- Show last runtime/compilation error: to show the results of the compilation or the result of a running program.

> Programs could run for a long period of time, but only one program can run at same time. The system will alert you if you are trying to run a program when other is running.

> A program could or couldn't show anything in the screen. We recommend that your programs shows information about what they are doing.

At the end of the screen the system shows the folder where you should upload your programs.

![[Pasted image 20230731132539.png]]
Example of a program running.


---

[[Index]]

