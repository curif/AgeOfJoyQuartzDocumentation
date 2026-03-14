Is a `zip` file that contains all the necessary files to represent [[Cabinets]] in VR.

Usually the cabinet asset is named with the same name that the game's [[ROM]]. It's considered a *name convention*.

A cabinet asset is a zip file containing all the required files for a cabinet:

- `description.yaml`: Read [[CDL the Cabinet Description Language]]
- `*.glb`: cabinet's models for those cabinets that do not adhere to some of the standards.
- `*.mp3, *.ogg, *.wav`: for cabinet's speakers to play triggered sounds.
- `*.png, *.jpg`: for cabinet parts' textures.
- `*.bas`: [[AGEBasic]] programs.
- `*.mp3, *.ogg, *.wav`: music files (for jukeboxes).
- Any other core specific file: [[CDL the Cabinet Description Language#MAME files distribution]] for distribution.
- Image files for screen backgrounds.
- Metadata `yaml` files.
- Any other required files

User must to upload to the `/cabinets` folder the zip file (without decompression) and start the game in order to register the cabinet. 
## Related documentation

[[How to get and deploy cabinets assets]]
[[Short guide to make cabinets]]
