# How to add new emulation cores to Age of Joy (AoJ).

We'll use as an example the SwanStation core, which is an _amazing_ Sony Playstation core which runs fantastically in AoJ.

## Basic core installation

The first (and mandatory) step is to add the emulation core itself to the AoJ filesystem.
AoJ uses Libretro core binaries targeting the `arm64-v8a` architecture, which can be found here: https://buildbot.libretro.com/nightly/android/latest/arm64-v8a/

This repository features the latest "nightly" builds used in RetroArch, and is exhaustive and always up to date.

So, the installation procedure is :
- Download `swanstation_libretro_android.so.zip`
- Unzip
- Copy `swanstation_libretro_android.so` to the `\cores\` directory of AoJ.

_The `\cores\` folder is where libretro core binaries reside._

It is important _not_ to rename the .so file and use the original filename.
The core name is derived from the filename and will be set to the string portion preceding "_libretro_android.so". In our example, the core name that will be used further will therefore be "swanstation".
If we were using core `mednafen_saturn_libretro_android.so` the core name would be "mednafen_saturn"...

Once you have added a core to `\data\` it will be autodetected by AoJ on startup and you can reference it in you cabinets:

`description.yaml`:
``` yaml
core: swanstation
```

AoJ will also automatically create a subdirectory named after the core in the `\download\` folder for your games for you to keep things nice and tidy.

Note that you can actually update internal AoJ cores (like `fbneo`) by specifying a more up to date binary for that core. It will take precedence over the bundled one.


## Getting familiar with the core

While some cores work great out of the box, some others need extra steps to function.
It's therefore a good idea to get familiar with the core's documentation.

Three good resources are:

- The official libretro documentation which shows basic info for many cores: https://docs.libretro.com/guides/arcade-getting-started/
- The documentation from Recalbox, a distribution of Libretro for Raspberry Pi etc: https://wiki.recalbox.com/fr/emulators/consoles/playstation-1/libretro-swanstation  The website is in french, but it's the most exhaustive documentation around and well worth the look.
- The source code for the core. This is the ultimate source of truth, but it's for advanced users, not the faint of heart :) https://github.com/libretro/swanstation

The important information you'll want to spot are mainly :

- The file format support for the core (does it support zip files ? does it support chd files ? what are some specific file extensions used by the core ?...)
- The need for specific system files (BIOS requirements, name of the files and where to put them...)
- Core configuration options (discussed later)


## System files

Some cores will _not_ work without specific system files. 

In the case of SwanStation, as the RecalBox website informs up, the following files are needed: `scph5500.bin`, `scph5501.bin`, `scph5502.bin`. 
You'll need to obtain these files one way or another (don't ask me how or where to find them) and copy them to the `\system\` folder in AoJ.

_The `\system\` folder is where libretro core system files reside._


## Core configuration

You may want to customize the core by specifying environment configuration.

In the case of SwanStation for example, memory card support is not enabled by default. A look at the core documentation tells us enabling memory card support is done thru the `swanstation_MemoryCards_Card1Type`setting.

We can act on the core configuration by adding, and tweaking a yaml configuration file in the `\configuration\cores\` folder.

_The `\configuration\cores\` folder is where libretro core configuration files reside._


In our example, we'd drop a file named `swanstation.yaml`  in the `\configuration\cores\` folder:

```yaml
environment:
   properties:
     swanstation_MemoryCards_Card1Type: PerGameTitle
```

Some cores will work without a configuration file. Others will need tinkering and use of specific options.

For example, the mamearcade core will not work in AoJ without setting `mame_media_type: rom`

Core configuration is handy to customize the experience to your likings.
For example, you may want to set settings such as these to tweak the `fbneo` core:

```yaml
environment:
   properties:
     fbneo-force-60hz: enabled
     fbneo-samplerate: 48000
     fbneo-sample-interpolation: 4-point 3rd order
     fbneo-fm-interpolation: 4-point 3rd order
     fbneo-lowpass-filter: enabled
     fbneo-neogeo-mode: UNIBIOS
```


## Using an installed core in your cabinets

Using a core in a cabinet is very simple, you simply have to specify the core name in the `description.yaml` file.

`description.yaml`:
``` yaml
core: swanstation
```

You may also specify core configuration settings directly in the `description.yaml` for your specific cabinet (for a light gun game, for instance).

The syntax is exactly the same as global core configuration files

```yaml
environment:
   properties:
     swanstation_MemoryCards_Card1Type: PerGameTitle
```

#cores #CDL 