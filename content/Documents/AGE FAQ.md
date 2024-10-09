# AGE of Joy 
## What is AGE of Joy?
AGE of Joy (`AGE` in short) is an experience/game/simulation. This experience is an attempt to preserve the arcade galleries of the old days, that feeling, in a virtual world where anyone with a VR headset can experiment with it.

## Ok, I want to download it.
Go [here](https://curifab.itch.io/age-of-joy).
## Can I play it on a PC?
As of the time this document was written, the game can only be played on Meta Quest 2 and is not compatible with PCs.
## How much it cost?
The game is available for download and enjoyment without any strict cost requirements. While you have the option to make a donation to support the developer, it is not mandatory. Feel free to download the game and experience it at no financial obligation.
## How to install AGE? 
* Download from this [itchio page](https://curifab.itch.io/age-of-joy) (you can download release candidates from GitHub too, but they are less stable).
* Backup the previous version (from the Quest to your PC) if you already install it.
* Install the game using [Sidequest](https://sidequestvr.com/) (follow [[Sidequest]] instructions to install it): [Instructions](https://learn.adafruit.com/sideloading-on-oculus-quest/install-and-use-sidequest)
Note that you need to enable the developer mode to sideload programs. It's the way that developers run applications: [Enable developer mode](https://learn.adafruit.com/sideloading-on-oculus-quest/enable-developer-mode)
**Important**: If you are upgrading to a new version please read this document: [[How to upgrade to a new version]].
## I install it but I only see black ugly cabinets! what is wrong?
It is completely normal to see black cabinets when you first install AGE. This is the expected appearance as the initial installation does not include any cabinets. To populate the rooms with cabinets, you will need to upload cabinet files. Additionally, if you want to play games, you will also need to obtain ROMs for the specific games you wish to play.
## I have problems when play, what can I do?
Please keep in mind that AGE is still in active development and may encounter errors or issues. If you experience any problems while playing, it is recommended to read the documentation first. The documentation provides valuable information and troubleshooting tips that might help resolve the issue.

If you are unable to find a solution in the documentation, it is advisable to seek further assistance in the [[Discord server]] community. The Discord community is a helpful resource where you can ask questions and receive support from other AGE users and developers.

By referring to the documentation and seeking assistance in the Discord community, you increase your chances of resolving any gameplay-related issues you may encounter.
## Can I configure the game, like to quit the NPCs or the sound?
Yes you can do it by changing the game configuration files, read how to do it here: [[AGE configuration using files]] 
## Can I configure the game being in the game? I don't like to change files.
Yes, with the [[Visual configuration]] if you are in the `0.4` version


# ROMS
## What is a rom?
A [[ROM]] is a file that represents a retro game (non techie response). Usually they have a filename ending with `.zip` like `galaga.zip`.

You need a [[ROM]] and an emulator like MAME to play old games.
## What is MAME?
[[MAME]] is the arcade machine emulator.
## What is an emulator?
An emulator is a software that emulates another software or hardware. In our case MAME emulate old arcade machines.
## Can I play AGE of Joy without ROMs?
You can get into the game and relive the experience of being in an arcade, but you can't play any arcade game without ROMs. In that case you can put the coin but nothing happens
## Why AGE of Joy don't have ROMS in the game?
It's illegal to distribute any copyrighted material without permission.
## It is legal to possess a ROM?
ROMs are copyrighted material, so be careful to not violate the intellectual property. 
## Where can I find them?
On internet. You can make a simply search like [MAME 2003-Plus Reference: Full Non-Merged Romsets](https://www.google.com/search?q=MAME+2003-Plus+Reference%3A+Full+Non-Merged+Romsets&sourceid=chrome&ie=UTF-8)
## I have a ROM, can I play it in AGE of Joy?
Not all ROMs are available to play, inconsistencies, bugs and incompatibilities exists. Usually if you can find a cabinet for a game then the [[ROM]] exists and is playable.
## I need a cabinet file to play with a ROM?
Yes, you need it, as in the old days, each cabinet had mainly one set. Read the cabinet section in this document. 
## MD5 checksum
### What is a md5 checksum/token?
The [[md5 checksum]] is a token that is useful to validate if your [[ROM]] is the correct. An md5 looks like `56a6c44c2d6678bdc085b8780bc51819`
### How can I check if my [[ROM]] is the correct using an MD5?
First you need the md5 of the tested rom, you can get it in the `description.yaml` file inside the cabinet file. Or you can get it by looking the page of each game in this site. Then compare it with the md5 of your own ROM, you can get your md5 here: [MD5 Hash Calculator](https://curif.github.io/AgeOfJoy-ROMCRC/index.html). Compare both md5, if they are exactly the same then you have the correct ROM.
## Where to upload the ROM?
Copy the [[ROM]] to `/sdcard/Android/data/com.curif.AgeOfJoy/downloads` using [[Sidequest]].
## So I have to decompress the zip file, right?
NO, just copy the zip file to the folder.
## I can't find the folder!
You must run AGE at least once to create the folders.


# Playing games
## How can I play an emulated game?

If you have a cabinet and a [[ROM]] you can play the game. Just put a coin on it: [video](https://youtu.be/MYOKp9lI_7o).

Also read the [controller documentation](https://curifab.itch.io/age-of-joy/devlog/457164/age-of-joy-quest-2-controls).
## I'm playing now, how to leave?

Press the grip button in your left control for some seconds.
## Can I insert a coin when I'm playing?

Yes you can do it.
## Can I change the buttons distribution and actions?

Yes you can, but you have to know that this is a MAME function, not is something related with AGE. To control the MAME emulation press the trigger and the joystick at same time in your right control when you are in game mode, a menu appears inside the game.
## I want to play sited, can I?

Yes, you need to configure the Quest Accessibility Options. By doing so, you will see the world of virtual reality as if you were standing upright.

# Cabinets
## What is a cabinet?
Old games comes in its own [[Cabinets]]. So to play a game you need to download a cabinet and upload it to your Quest.
## Where can I download cabinets?
You need to "hunt" them on internet. The best place to start is this site.
There a lot of cabinets made by the community, get those in [Discord](https://discord.gg/b83ykCM9Xp)
## how to install cabinets in AGE?
Read  [[How to get and deploy cabinets assets]]
## I have a cabinet asset, how to upload it?
Copy the zip file to `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets`
## So I have to decompress the zip file, right?
**NO**, just copy the zip file to the folder.
## I can't find the folder!
You must run AGE at least once to create the folders
## I'm confused, the cabinet file and the [[ROM]] file have the same name...
Yes, it is not strictly necessary but it is a convention. We can know that the cabinet is for a certain game that way.
## I want to make my own cabinets, can I?
Yes you can, but first check it if someone didn't made it. Then you please read the [[Short guide to make cabinets]]. If you are good enough, you can considered yourself as an [[Cabinet Artist]].
## I made my first cabinet! I want to share it with the world!
You can sell it or ask for donations on itchio. Or you can just share it with the community by posting it on the [[Discord server]]. Don't keep the cabinets for yourself, share them somehow!
## I have the cabinet, but the game don't runs, what can I do?
Read the ROM section in this document.
## I upload a cabinet, but I can see it.
The game deploy the cabinet in a free place, search for it.
If you can't find it, be sure you have enough space in the gallery to add new cabinets.
## My gallery is full of cabinets, what I can do?
Just wait for the next version, new versions comes with new rooms.

# Rooms
## What is a room?
The place where you can see the cabinets are called "rooms".
## What is the workshop?
A special room. If you are a cabinet artist or developer is the place where you test the cabinets.
## Can I configure the rooms?
Yes, you can change a little the room, read the configuration documentation: [[AGE configuration using files]] and [[Visual configuration]]. More configurations to come with new versions in the future.
## How I move from a room to another?
Just walk to the black door and wait for the next room to deploy.
You can teleport to a room with the [[Teleportation]] functionality.
## You can make that all the rooms are available at the same time? it is weird to wait.
Quest can't process all the rooms with all cabinets and introduction videos at the same time, so it's a way to have a big arcade gallery without problems.
## I can't enter a room!
Usually AGE comes with doors to rooms that would exist in future versions. You can't enter there because the room don't exists yet.
## I have to walk a lot to reach a game, can I just jump to it?
Yes, using the [[In Room Teleportation]].




