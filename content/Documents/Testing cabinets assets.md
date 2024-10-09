
Once your cabinet is complete, you can begin testing it. Normally, it should not work; some adjustments may be required, this happens a lot.

## The workshop

There are a special room *the workshop* where you can see and test the new cabinet. To deploy the cabinet there name it `test.zip` and copy to the `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets` folder (as usual, but with that special name). AGE of Joy will reload the cabinet immediately (this only happens in the workshop with that cabinet, but not in the rest of the rooms). Repeat the process until you are confident with the result.

At the end, rename the final cabinet with a unique name, two different cabinets can't have the same name. As a rule, I use the name of the ROM as the name of the cabinet, so your cabinet will be unique in the gallery and in the cabinet assets universe too.

You can, of course, publish your cabinet.

Read the [[CDL troubleshooting guide]] for a more detailed information about how to check a cabinet issue.

## Step by step

This is a step by step guide to craft a new cabinet for a ROM.

In this example, we will use the Galaga cabinet to craft a new Galaxian cabinet for the Galaxian ROM


### 1- Check the ROM

In theory any ROM that works in Libretro MAME 2003+ should work, BUT there are some
issues that must be managed in AGE of Joy to use some ROMs. One of them, for example, is the image format because 
not all ROMS uses the same image format, and if you ROM uses one that is not supported, then
the game don't run or may be it shows weird colors, or loss frames, etc.

Tested ROMs are registered in this site and a lot of them in the [[Discord server]]

if your ROM is not in the list, the only way is to craft a new cabinet for that ROM and test it in the game.

### 2- Craft a new cabinet for testing purposes

This method uses a previously saved model (bundled in the game) and reuse it. Starting with a cabinet asset and modifying it. A good start point is the Galaga cabinet, in this example we will modify the cabinet and we will create a new one.

#### 2.1 Decompress an existing cabinet asset in your PC

- Create a new folder in your PC with the name of the cabinet you want to create, for example `galaxian`
- Copy a _cabinet asset_ to your PC, for example `galaga.zip` and extract all the files to your new folder `galaxian`. Warning: its easy to confuse a cabinet asset with a ROM, usually the have the same file name.
- Now you should have a lot of files, some pngs, a mkv, and the most important `description.yaml` in the recently created `galaxian` folder 

#### 2.2 change the description file

- With a text editor open the `description.yaml` file
- Edit the cabinet name and rom filename:

Previously:
```
name: galaga
rom: galaga.zip
```
After your changes:
```
name: galaxian
rom: galaxian.zip
```

- Save the file.

#### 2.3 Compress to a new zip file

Depending on you operative system there are diferent ways to compress files. This example is for ubuntu. 

- Select all files in the `galaxian` folder
- Mouse right button opens a menu, then `Compress...`
- Create a new zip file with the name `test.zip` in any place in your disk.

![[sidequest screen file list.png]]

![[Sidequest create archive.png]]

The `test.zip` file is a *special cabinet asset* name for testing purposes only.

### 3- Test the cabinet

To test the cabinet you need to copy the `test.zip` cabinet asset to the headset, using [[Sidequest]] for example.
Remember: `test.zip` is for testing purposes, we should rename the zip file later after the testing phase.

- Follow [[How to get and deploy cabinets assets]] instructions to know how to copy the `test.zip` file to the `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets` folder.
- Copy the ROM file to `/sdcard/Android/data/com.curif.AgeOfJoy/downloads`, in this example our ROM file name is 'galaxian.zip'.
- Go to the workshop in the game (the door at your left with the wet floor sign in front), if all is ok the new cabinet should _spawn_ in the middle of the Room. If not, or shows something weird like a _mutant_ cabinet, or one cabinet inside the other, then something failed. 
- Walk to the cabinet, insert a coin and look what is happening.

If the game didn't start or the cabinet didn't spawn correctly, check the description.yaml file in search of errors. But if you didn't find any issue, then probably you ROM is not compatible. Ask for help in forums and GitHub.

If you find the issue (may be a typo) repeat all from the step 2.3. The corrected cabinet will replace the actual without need to restart AGE of Joy. Also read the [[CDL Debug mode]] information

### 4- Deploy the new cabinet

If your game is running without any noticeable issue, then you can deploy the new cabinet:

- Rename the file in your PC from `test.zip` to a file name that represents the game in the cabinet, in our example should be `galaxian.zip` 
- Copy the file to the `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets` folder.
- Start AGE of Joy again, the program will find the new cabinet and move it to the [[Cabinets database storage]]. The game will delete the original zip file from `/sdcard/Android/data/com.curif.AgeOfJoy/cabinets`
- After register the new cabinet, it will be deployed in an empty slot inside a Room in the game, replacing an "out of order" cabinet.

Enjoy your new cabinet!

#cabinet/artists 