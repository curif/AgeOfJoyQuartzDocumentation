
A cab's `description.yaml` can be enriched with a control-scheme setting. 

If set, this specifies a controller `yaml` configuration file to apply to this cab. Control schemes are located in `/configuration/controllers/schemes` (this directory is auto-created) 

Example: `/configuration/controllers/schemes/6-buttons.yaml`  

```yaml
control-scheme: 6-buttons
```

> [!note] 
> NOTE: If the `description.yaml` specifies a control map, it takes precedence and the control scheme is functionally ignored.  Priority goes : description.yaml map > user game map > scheme map > global map

You should read the [[Controller configuration]] manual to fully understand how to map controllers and how the mapping merges with the rest of the configuration.

Example: `keyboard.yaml`

```yaml title="keyboard.yaml"
---
maps:
  - libretro-id: JOYPAD_UP
    behavior: button
    maps-to:
    - control: keyboard-w
  - libretro-id: JOYPAD_DOWN
    behavior: button
    maps-to:
    - control: keyboard-s  
  - libretro-id: JOYPAD_RIGHT
    behavior: button
    maps-to:
    - control: keyboard-d
  - libretro-id: JOYPAD_LEFT
    behavior: button
    maps-to:
    - control: keyboard-a
  - libretro-id: JOYPAD_B
    behavior: button
    maps-to:
    - control: keyboard-enter
  - libretro-id: JOYPAD_Y
    behavior: button
    maps-to:
    - control: keyboard-y
      path: <Keyboard>/#(y)
  - libretro-id: JOYPAD_A
    behavior: button
    maps-to:
    - control: keyboard-space
```

#CDL 