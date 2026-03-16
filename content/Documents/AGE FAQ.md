Here is the corrected version of the document with improved grammar, punctuation, and syntax while maintaining your original markdown structure.

# AGE of Joy 

## What is AGE of Joy?
AGE of Joy (**AGE** for short) is an experience, game, and simulation. This project is an attempt to preserve the feeling of arcade galleries from the past in a virtual world where anyone with a VR headset can experience them.

## Okay, I want to download it.
You can download it [here](https://curifab.itch.io/age-of-joy).

## Can I play it on a PC?
As of the time this document was written, the game is only compatible with Meta Quest 2 and does not support PC play.

## How much does it cost?
The game is available for free. While you have the option to make a donation to support the developer, it is not mandatory. Feel free to download and enjoy the game with no financial obligation.

## How do I install AGE? 
* Download it from the [itch.io page](https://curifab.itch.io/age-of-joy). (You can also download release candidates from GitHub, but they are generally less stable).
* Back up the previous version (from your Quest to your PC) if you have already installed it.
* Install the game using [SideQuest](https://sidequestvr.com/) (follow the [SideQuest installation instructions](https://learn.adafruit.com/sideloading-on-oculus-quest/install-and-use-sidequest)).

**Note:** You must enable **Developer Mode** to sideload applications. This is the standard way developers run non-store applications: [How to enable Developer Mode](https://learn.adafruit.com/sideloading-on-oculus-quest/enable-developer-mode).

**Important:** If you are upgrading to a new version, please read this document: [[How to upgrade to a new version]].

## I installed it, but I only see ugly black cabinets! What is wrong?
It is completely normal to see black cabinets when you first install AGE. The initial installation does not include specific game assets. To populate the rooms, you must upload **cabinet files**. Additionally, to play the games, you will need to obtain the specific **ROMs** for the games you wish to play.

## I am having problems while playing; what can I do?
Please keep in mind that AGE is still in active development and may encounter bugs. If you experience issues, we recommend reading the documentation first. It provides valuable troubleshooting tips that may resolve your problem.

If you cannot find a solution in the documentation, please seek assistance in the [[Discord server]]. The community is a helpful resource where you can ask questions and receive support from other users and developers.

## Can I configure game settings, such as turning off NPCs or sound?
Yes, you can do this by modifying the game configuration files. Learn how here: [[AGE configuration using files]].

## Can I configure the game while I'm inside it? I don't like editing files.
Yes, you can use the [[Visual configuration]] menu if you are using version `0.4` or higher.

---

# ROMS

## What is a ROM?
A [[ROM]] is a file that represents a retro game (to put it simply). Usually, these filenames end in `.zip`, such as `galaga.zip`. You need both a ROM and an emulator (like MAME) to play these classic games.

## What is MAME?
[[MAME]] is the arcade machine emulator used within AGE of Joy.

## What is an emulator?
An emulator is software that mimics another piece of software or hardware. In this case, MAME emulates original arcade hardware.

## Can I play AGE of Joy without ROMs?
You can enter the game and relive the atmosphere of being in an arcade, but you cannot play the games themselves without ROMs. If you try to "insert a coin" without a ROM installed, nothing will happen.

## Why doesn't AGE of Joy include ROMs?
It is illegal to distribute copyrighted material without the owner's permission.

## Is it legal to possess a ROM?
ROMs are copyrighted material. Be careful not to violate intellectual property laws in your jurisdiction.

## Where can I find them?
On the internet. You can perform a simple search for something like: [MAME 2003-Plus Reference: Full Non-Merged Romsets](https://www.google.com/search?q=MAME+2003-Plus+Reference%3A+Full+Non-Merged+Romsets).

## I have a ROM; can I play it in AGE of Joy?
Not all ROMs are compatible due to version inconsistencies or bugs. Generally, if a cabinet exists for a specific game in the AGE community, the ROM is likely playable.

## Do I need a cabinet file to play a ROM?
Yes. Just like in the old days, every game needs its physical cabinet. See the **Cabinets** section below for more details.

## MD5 Checksum
### What is an MD5 checksum?
An [[MD5 checksum]] is a unique "fingerprint" or token used to validate that your ROM file is the correct version. An MD5 looks like this: `56a6c44c2d6678bdc085b8780bc51819`.

### How can I check if my ROM is correct using MD5?
First, find the MD5 of the "tested" ROM in the `description.yaml` file inside the cabinet zip, or by checking the game's page on this site. Then, compare it to your ROM's MD5 using a tool like this: [MD5 Hash Calculator](https://curif.github.io/AgeOfJoy-ROMCRC/index.html). If the strings match exactly, you have the correct ROM.

## Where do I upload the ROM?
Copy the [[ROM]] file to `/sdcard/Android/data/com.curif.AgeOfJoy/downloads` using [[SideQuest]].

## Do I need to decompress the ZIP file?
**NO.** Just copy the `.zip` file directly to the folder.

## I can't find the folder!
You must run AGE of Joy on your Quest at least once for the application to create the necessary folders.

---

# Playing Games

## How do I play an emulated game?
If you have both the cabinet and the [[ROM]] installed, you can play. Simply "insert a coin" to start. You can also refer to the [controller documentation](https://curifab.itch.io/age-of-joy/devlog/457164/age-of-joy-quest-2-controls) for specific inputs.

## I'm playing now; how do I leave the game?
Press and hold the **Grip button** on your **left controller** for a few seconds.

## Can I insert a coin while I'm already playing?
Yes, you can.

## Can I change the button layout or actions?
Yes. This is a function of MAME, not AGE itself. To access the MAME internal menu, press the **Trigger and the Joystick** at the same time on your **right controller** while in game mode.

## I want to play while seated; is that possible?
Yes. You may need to configure the Quest "Accessibility Options" (specifically "Adjust Height") to ensure the virtual world aligns correctly while you are seated.

---

# Cabinets

## What is a cabinet?
In the arcade world, games are housed in [[Cabinets]]. To see a game in AGE, you must download a cabinet asset and upload it to your Quest.

## Where can I download cabinets?
The best place to start is the [Discord server](https://discord.gg/b83ykCM9Xp), where the community shares many custom-made cabinets.

## How do I install cabinets in AGE?
Read the guide: [[How to get and deploy cabinet assets]].

## I have a cabinet asset; how do I upload it?
Copy the `.zip` file to `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets`.

## Do I need to decompress the ZIP file?
**NO.** Just copy the `.zip` file directly into the folder.

## I'm confused; the cabinet file and the ROM file have the same name...
This is a common convention to help users identify which cabinet belongs to which game, but it is not strictly required by the system.

## Can I make my own cabinets?
Yes! Please check if the cabinet has already been made by someone else first. If not, read the [[Short guide to make cabinets]]. If you create high-quality work, you may be recognized as a [[Cabinet Artist]].

## I made a cabinet and want to share it!
You can host it on [[itch.io]] or share it with the community on the [[Discord server]]. We encourage everyone to share their creations!

## I have the cabinet, but the game won't run.
Please refer to the **ROM section** of this document to ensure your ROM is the correct version and in the right folder.

## I uploaded a cabinet, but I can't see it in the game.
The game deploys cabinets in available open spaces; you may need to walk around to find it. Also, ensure you haven't reached the cabinet limit for your current room gallery.

## My gallery is full; what can I do?
New versions of AGE often include new rooms. Keep an eye out for updates to expand your arcade.

---

# Rooms

## What is a room?
The virtual environments where cabinets are placed are called "rooms."

## What is the Workshop?
The Workshop is a special room intended for cabinet artists and developers to test their assets.

## Can I configure the rooms?
Yes. You can make minor adjustments to the rooms. See [[AGE configuration using files]] and [[Visual configuration]].

## How do I move from one room to another?
Walk toward the black doors and wait for the next room to load. You can also use the [[Teleportation]] menu to move between rooms instantly.

## Can you make all rooms available at the same time? 
The Quest hardware cannot process all rooms, cabinets, and introduction videos simultaneously. Loading rooms individually ensures a smooth, high-performance experience.

## I can't enter a specific room!
AGE often includes "placeholder" doors for rooms intended for future versions. If a door doesn't open, that room likely hasn't been built yet.

## Can I jump directly to a specific game without walking?
Yes, you can use the [[In Room Teleportation]] feature to move quickly.