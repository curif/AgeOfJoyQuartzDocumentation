### How the cabinet building system works

**Warning**: tech talk. Read this if you want to create your own cabinets, if not, just download the cabinets assets packs.

Cabinets have two parts:

* **Cabinet Model**: Consider a piece of wood furniture that is unpainted and has the shape and components of an arcade cabinet.
* **Cabinet assets**: is a zip file that contains the side art stickers, bezels, marquees, and so on, as well as a description file that describes how to paint, how to place the stickers, marquee color light, tv (crt) position, the video to play on the screen when nobody is playing, etc.

The **models** of the cabinets, such as Galaga and Xevious, are included in the game, developed by an graphic artist, in a way that its design allows you to *reskin* them. New versions of the game should include new models.

![[Cabinet Assets.png]]

Without any special knowledge, it is possible to reuse a cabinet model, personalize it, zip the files, and copy it to the headset. Because all cabinets are made in this manner, the game does not include any cabinets assets bundled on it; however, you can create your own or download them starting with a base design. In fact, you can use a "galaga" design and change the side art, bezel, marquee, and so on. And then make a new one.

Obviously, you can download all the cabinets that you want because their are distributed as *game assets*

> Note: You don’t need to be a programmer or a graphics designer to make new cabinets assets starting of a base model.

### Creating new cabinets

Creating new cabinets is a trial-and-error process. There is a special room in the game called the *Workshop* where you can test your own cabinets. 

You can upload the cabinet you're working on as many times as you want to the workshop. When you are satisfied with the outcome, you can place the cabinet in the game. The cabinet will be automatically installed in a room by the game.

![[Workshop.png]]
The best way to make a new cabinet asset for a game is to copy an existing one, decompressing ```galaga.zip``` for example, and replace each file for the one that correspond to the game. It's important to use the same characteristic for each file, for example the width and eight for the side art graphics and the same rotation.

The special file ```description.yaml``` describes the parts of the cabinet.

Detailed instructions at the end of this post.

### The Cabinet Description Language

This is an example of the Cabinet Description Language (CDL) in the ```description.yaml``` in ```galaxian.zip```, a text file describing a cabinet in a computer language known as [[YAML]] (this is the simplest way to communicate with a computer system). 


```yaml
name: galaxian
rom: galaxian.zip
crt:
  type: 19i
  orientation: vertical
  screen:
    damage: low
    invertx: false
    inverty: true
style: galaga
material: black
year: 1979
coinslot: coin-slot-double
timetoload: 5
video:
  file: video.mkv
parts:
  - name: left
    art: 
      file: left.png
  - name: right
    art: 
      file: right.png
  - name: joystick
    art: 
      file: joystick.png
      inverty: true
  - name: joystick-down
    art: 
      file: joystick-down.png
  - name: front
    art: 
      file: front.png
  - name: bezel
    type: bezel
    art:
      file: bezel.png
  - name: marquee
    type: marquee
    art:
      file: marquee.png
    color:
      r: 238
      g: 232
      b: 176
      intensity: -2
```

You can use `CDL` to describe all of the design details of each part of a cabinet model simply by using a text editor on your computer. 

Once you understand the language, it's easy to develop new cabinets: [[CDL the Cabinet Description Language]]

## Testing cabinets assets

Once your cabinet is complete, you can begin testing it. Normally, it should not work; some adjustments may be required, this happens a lot.

Read [[Testing cabinets assets]] to continue.