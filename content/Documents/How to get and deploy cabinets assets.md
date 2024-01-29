## Get and deploy cabinets assets

### Instructions to copy cabinets to your headset, you'll need a [[Sidequest]]  working installation with access to your Quest 2.

![[Steps to get and deploy cabinet assets.png]]

1. Download [[Cabinet Asset]]s from itch.io or another source and decompress the file in a folder in your computer, you should obtain some zip files like `galaga.zip`. Each zip file are the instructions to deploy a cabinet in the game.
2. Exit the game in the headset. Copy the zips files cabinets that you want to the  `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets` path using [[Sidequest]].
3. Run the game again, it should detect the new cabinets and deploys them in a room, search them.

Remember: cabinets have two parts,

* **Cabinet Model**: Consider a piece of wood furniture that is unpainted and has the shape and components of an arcade cabinet.
* **Cabinet assets**: is a zip file that contains the side art stickers, bezels, marquees, and so on, as well as a description file that describes how to paint, how to place the stickers, marquee color light, tv (crt) position, the video to play on the screen when nobody is playing, etc.


---

## ROMs

To play the games, you'll also need the [ROMs](https://en.wikipedia.org/wiki/ROM_image) compatible with [MAME](https://en.wikipedia.org/wiki/MAME). Copy them to `/sdcard/Android/data/com.curif.AgeOfJoy/downloads`. If not, you can still run the simulation but not play the games.

👮🏼‍♂️ Some ROMs are copyrighted material, check it on the internet.

There are a [MAME 2003-Plus Reference: Full Non-Merged Romsets](https://www.google.com/search?q=MAME+2003-Plus+Reference%3A+Full+Non-Merged+Romsets&sourceid=chrome&ie=UTF-8) on internet.

To verify that the ROM you possess is the correct version use [this tool](https://curif.github.io/AgeOfJoy-ROMCRC/index.html)to obtain the MD5 Hash. Compare the obtained hash to the registered hash in the database. If they match, you have the same ROM that was used for testing the game.