A "core" typically refers to the emulation engine responsible for emulating the hardware of a specific arcade system or gaming platform. Each core is tailored to emulate the hardware of a particular arcade machine or gaming system accurately.

## Available cores

Read the [[CDL the Cabinet Description Language#Cores]] to learn how to specify a cabinet core.

| Core      | Page                                               | Status   | Licence                                                                   |
| --------- | -------------------------------------------------- | -------- | ------------------------------------------------------------------------- |
| mame2003+ | https://github.com/libretro/mame2003-plus-libretro | stable   | https://github.com/libretro/mame2003-plus-libretro/blob/master/LICENSE.md |
| mame2010  | https://github.com/libretro/mame2010-libretro      | untested | https://github.com/libretro/mame2010-libretro/blob/master/docs/mame.txt   |
| fbneo     | https://github.com/finalburnneo/FBNeo              | untested | https://github.com/finalburnneo/FBNeo/blob/master/src/license.txt         |
last update: 2024-03-05

## User cores

Starting in the v0.5 release candidate 5, users could add emulation cores if they want.
### User defined core configuration

The user can change the core configuration properties using config files. The [[Cabinet Artist]] could configure the core in CDL too.

- **Users:** Can modify core settings through `yaml` config files
- [[Cabinet Artist]] : Have access to configure the core in CDL for more advanced configuration.

User defined core configuration is in `/configuration/cores/<core.yaml>`

```yaml
environment:
   prefix: beetle_saturn
   properties:
     virtuagun_input: Lightgun
     virtuagun_crosshair: Off
```

Prefix is optional.
Cab environment takes precedence over core environment (merges)

[[User cores configuration collection]]

### Core paths

Users should upload emulation cores to the `/sdcard/Android/data/com.curif.AgeOfJoy/cores` folder.

#CDL #cores 
