Main site:  [MAME](https://www.mamedev.org/) (Multiple Arcade Machine Emulator)

MAME (Multiple Arcade Machine Emulator) is an open-source software project that emulates the hardware and software of a wide range of arcade machines and gaming systems. It is designed to preserve the history of arcade games by accurately emulating their original hardware and allowing them to be played on modern computers.

MAME aims to recreate the original arcade gaming experience by emulating the behavior of the hardware components, such as the central processing unit (CPU), graphics and sound chips, input devices, and memory. It can emulate a vast number of arcade systems, including popular ones like Atari, Capcom, Konami, Sega, and many others. By using the original ROMs (Read-Only Memory) from the arcade machines, MAME allows users to play a vast library of classic arcade games.

The project began in 1997 and has since evolved with the contributions of a dedicated community of developers and enthusiasts. MAME supports various platforms, including Windows, macOS, Linux, and more, making it accessible to a wide range of users.

> [!warning] It's important to note that while MAME itself is a legal project, the use of ROMs may have legal implications. Distributing or downloading copyrighted ROMs without the proper ownership rights is generally illegal. It is recommended to only use ROMs for which you have the appropriate permissions or obtain them from legal sources, such as original arcade machine owners or authorized distributors.

## Cores

The core serves as the foundation of the emulator and handles tasks such as CPU emulation, memory management, graphics rendering, sound emulation, and input handling. It provides the necessary components and algorithms to accurately emulate the behavior of the original arcade hardware.

By using a MAME core, developers can create platform-specific versions of the MAME emulator that provide optimal performance and compatibility for a particular operating system. Users can then run the MAME core on their chosen platform and utilize it to play arcade games by providing the required ROM files.

AGE of Joy is compatible with [libretro-mame2003-plus](https://github.com/libretro/mame2003-plus-libretro).

## Sound Samples

Sound samples in MAME are extra sound files that certain games need to function properly . These samples are typically used to provide improved audio effects or to emulate sounds that the original system hardware was incapable of producing.

For instance, in games like [[galaga]] and [[pacman]], enhanced samples have been created to provide a better audio experience. These samples are usually placed in a specific directory within your MAME setup, and they are loaded by the emulator when the game is run.

Please note that not all games require these additional samples, and the usage can vary depending on the specific version of MAME you are using. If you’re unsure whether a game requires samples, it’s best to check the documentation or the game’s community resources.

You can find sound samples in the next sites. Just download the zip file and upload them to `/sdcard/Android/data/com.curif.AgeOfJoy/system/samples` using [[Sidequest]] (or your preferred application to manage files in Quest). Don't decompress the file.

[Twisty's MAME Samples Collection (mameworld.info)](https://samples.mameworld.info/)

[Archive.org](https://archive.org/details/mamesamples)