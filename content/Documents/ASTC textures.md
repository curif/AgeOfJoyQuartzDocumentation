Support for ASTC textures for cabinets.

The `ASTC` file type for the cabinet's images could improve the overall game performance. 

These need to have the `.astc` extension and be produced with [astcencode](https://github.com/ARM-software/astc-encoder](https://github.com/ARM-software/astc-encoder) with the following settings:

```shell
astcenc-avx2.exe -cl "texture.png" "texture.astc" 6x6 -exhaustive -yflip
```

Then all that's left is referencing the `.astc` file instead of the `.png` in the `description.yaml` manifest.

#CDL 