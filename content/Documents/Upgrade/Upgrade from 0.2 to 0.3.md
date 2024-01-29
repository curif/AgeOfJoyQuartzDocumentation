# V 0.3 Changelog

* Cabinets now loads when the player is close. This enhances the whole experience when you enter a new room.
* You can change the global and room configuration (right now using configuration files). In future versions it could be done by interacting with the environment. Read this [wiki page](https://github.com/curif/AgeOfJoy-2022.1/wiki/Game-Configuration:-configuration-files) to know how to change configurations, like sound and NPC behavior.
* Sound improvements: 3D sound, volume configuration and game sounds.
* Two new rooms were added.
* Compatibility with _vector graphics_ games added (for games like tempest or asteroids).
* MAME performance improved.
* Shaders: a new _clean shader_ with four _damages_ (cabinets artists can configure shaders as usual). Old _damage_ shader has been improved with more levels. Read the details in the [[CDL the Cabinet Description Language#Configuring the monitor (CRT)]]
* Control panel boxes: you could use these control panel boxes to configure the room in future versions. Right now the control boxes just have the room name in a card, useful for knowing which configuration file you need to change to modify the behavior of the room. 
* Better player - NPC relationship
* Call MAME menu via [libretro](https://docs.libretro.com/library/mame2003_plus/) using `right-grip` and `right-joystick-click` (at same time), use the `A` button to enter to each option menu. You can remap controls if the default don't suit your needs for each game (this is a libretro core feature).

### Known errors

- Donkey Kong and other similar games do not function properly; they are unusable.
- Save states are disabled, which breaks most of the games.
- Hangs are expected.
