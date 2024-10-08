
**Optimizing Audio Clips for Better Performance**

For optimal performance, consider using short audio clips that loop seamlessly without noticeable interruptions. This approach helps reduce memory consumption and ensures a smoother user experience.

To achieve this, it's essential to choose an audio clip that supports loop mode. When editing the video, extract only the desired audio track and shorten it to a length that can be effectively looped.

You can use mono channels to reduce the clip even more. Because we are using spatialization a stereo clip isn't necessary.

## Recommended audio properties

- channels: mono
- sample rate: 48000hz
- audio code: mp3

To get the audio clip you could upload the attraction video to a site like https://www.online-convert.com/ or https://cloudconvert.com/mkv-to-mp3.

A site like https://mp3cut.net/es/ could help to cut the audio file.

## Max player distance

Both `video` and `audio` yaml keys contains a `max-player-distance` property to set the distance from the cabinet to the player.

- `max-player-distance` in `video` means the video will play if the player is in the range from zero to max-player-distance mts measured from the cabinet to the player. Also the player should be looking at the cabinet. Else the video will stop. If the player is close to the cabinet and not looking at the cabinet the audio will sound, but if he is looking at the cabinet the video will play.
- `max-player-distance` in audio is the same, and logically it should be greater than `max-player-distance` in videos. The audio clip will play even if the player is not looking at the cabinet, or if he is looking at but far away the `max-player-distance` in the video. 

