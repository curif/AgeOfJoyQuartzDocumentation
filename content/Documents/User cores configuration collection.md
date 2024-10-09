Donated by @Emashzed

```yaml file="sameboy.yaml"
environment:
   prefix: sameboy
   properties:
     model: Auto
     auto_sgb_model: Super Game Boy
     rtc: sync to system clock
     mono_palette: greyscale
     color_correction_mode: emulate hardware
     light_temperature: 0
     border: Super Game Boy only
     high_pass_filter_mode: accurate
     audio_interference: 0
     rumble: rumble-enabled games
```

```yaml file="swanstation.yaml"
environment:
   prefix: swanstation
   properties:
     __Logging_LogLevel: Debug
     MemoryCards_Card1Type: PerGameTitle
     GPU_Renderer: Software
```

```yaml file="same_cdi.yaml"
environment:
   prefix: same_cdi
   properties:
     mouse_enable: true
     boot_from_cli: true
```

```yaml file="mamearcade.yaml"
environment:
   prefix: mame
   properties:
     media_type: rom
```

```yaml file="gambatte.yaml"
environment:
  prefix: gambatte
  properties:
    gb_bootloader: enabled
    gb_hwmode: Auto
    gbc_color_correction: GBC only
    gbc_color_correction_mode: accurate
    gbc_frontlight_position: central
    dark_filter_level: 0
    audio_resampler: sinc
    up_down_allowed: disabled
    turbo_period: 4
    rumble_level: 10
    mix_frames: lcd_ghosting
    gb_link_mode: Not Connected
    gb_link_network_port: 56400
    gb_link_network_server_ip_1: 0
    gb_link_network_server_ip_2: 0
    gb_link_network_server_ip_3: 0
    gb_link_network_server_ip_4: 0
    gb_link_network_server_ip_5: 0
    gb_link_network_server_ip_6: 0
    gb_link_network_server_ip_7: 0
    gb_link_network_server_ip_8: 0
    gb_link_network_server_ip_9: 0
    gb_link_network_server_ip_10: 0
    gb_link_network_server_ip_11: 0
    gb_link_network_server_ip_12: 0
    gb_colorization: auto
    gb_internal_palette: GB - DMG
```

```yaml file="fbneo.yaml"
environment:
   prefix: fbneo
   properties:
     force-60hz: enabled
     samplerate: 48000
     sample-interpolation: 4-point 3rd order
     fm-interpolation: 4-point 3rd order
     lowpass-filter: enabled
     neogeo-mode: UNIBIOS
```

```yaml file="dirksimple.yaml"
environment:
   prefix: dirksimple_lair
   properties:
     starting_lives: 5
     infinite_lives: false
     god_mode: false
     play_sounds: true
```

```yaml file="cap32.yaml"
environment:
   prefix: cap32
   properties:
     autorun: enabled
     scr_crop: enabled
     gfx_colors: 16bit
     model: 6128+ (experimental)
```

