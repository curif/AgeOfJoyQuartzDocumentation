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


```yaml file="flycast.yaml"
environment:
   prefix: reicast
   properties:
     allow_service_buttons: disabled
     alpha_sorting: per-triangle (normal)
     analog_stick_deadzone: 15%
     anisotropic_filtering: 4
     auto_skip_frame: disabled
     boot_to_bios: disabled
     broadcast: NTSC
     cable_type: TV (Composite)
     custom_textures: disabled
     dc_32mb_mod: disabled
     delay_frame_swapping: disabled
     detect_vsync_swap_interval: disabled
     digital_triggers: disabled
     dump_textures: disabled
     emulate_bba: disabled
     emulate_framebuffer: disabled
     enable_dsp: enabled
     enable_rttb: disabled
     fix_upscale_bleeding_edge: enabled
     fog: enabled
     force_freeplay: enabled
     frame_skipping: disabled
     gdrom_fast_loading: disabled
     hle_bios: disabled
     internal_resolution: 640x480
     language: English
     lightgun_crosshair_size_scaling: 100%
     lightgun1_crosshair: disabled
     lightgun2_crosshair: disabled
     lightgun3_crosshair: disabled
     lightgun4_crosshair: disabled
     mipmapping: enabled
     native_depth_interpolation: disabled
     network_output: disabled
     oit_abuffer_size: 512MB
     oit_layers: 32
     per_content_vmus: disabled
     pvr2_filtering: disabled
     region: USA
     screen_rotation: horizontal
     sh4clock: 200
     texture_filtering: 0
     texupscale_max_filtered_texture_size: 256
     texupscale: 1
     threaded_rendering: enabled
     trigger_deadzone: 0%
     upnp: enabled
     vmu_sound: disabled
     vmu1_pixel_off_color: DEFAULT_OFF 01
     vmu1_pixel_on_color: DEFAULT_ON 00
     vmu1_screen_display: disabled
     vmu1_screen_opacity: 100%
     vmu1_screen_position: Upper Left
     vmu1_screen_size_mult: 1x
     vmu2_pixel_off_color: DEFAULT_OFF 01
     vmu2_pixel_on_color: DEFAULT_ON 00
     vmu2_screen_display: disabled
     vmu2_screen_opacity: 100%
     vmu2_screen_position: Upper Right
     vmu2_screen_size_mult: 1x
     vmu3_pixel_off_color: DEFAULT_OFF 01
     vmu3_pixel_on_color: DEFAULT_ON 00
     vmu3_screen_display: disabled
     vmu3_screen_opacity: 100%
     vmu3_screen_position: Lower Left
     vmu3_screen_size_mult: 1x
     vmu4_pixel_off_color: DEFAULT_OFF 01
     vmu4_pixel_on_color: DEFAULT_ON 00
     vmu4_screen_display: disabled
     vmu4_screen_opacity: 100%
     vmu4_screen_position: Lower Right
     vmu4_screen_size_mult: 1x
     volume_modifier_enable: enabled
     widescreen_cheats: disabled
     widescreen_hack: disabled
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

