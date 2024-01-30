#agebasic 
## Audio test example

```vb
10 let volGame = AudioGameGetVolume()
20 let volAmbience = AudioAmbienceGetVolume()

25 ' this is not noticeable, you cant ear it.
30 for vol = 1 to 5
40   call AudioAmbienceSetVolume(volAmbience + vol)
50 next vol

60 REM back to previous 
70 call AudioAmbienceSetVolume(volAmbience)

80 REM mute ambience audio
90 call AudioAmbienceSetVolume(-80)
100 if AudioAmbienceGetVolume() != -80 then let error = "ambience not muted"
```

## Change a game sound volume

To change the sound volume of a game you should use [[CDL the Cabinet Description Language]] to setup witch programs must to run for each event. We will use the `after-insert-coin` event to setup the game volume, and `after-leave` to back the game volume to the original.

#### AGEBasic property in the cabinet's `description.yaml`

```yaml
agebasic:
  after-insert-coin: insertcoin.bas
  after-leave: leave.bas
```

[[Age of Joy]] will load both programs when the cabinet loads. `insertcoin.bas` gets the actual global game volume and storage it in the `originalVolume` variable. Then it changes the game audio to `5 dB`.
When the player leaves the game, [[Age of Joy]] will run the `leave.bas` program and restore the game volume to the original.
#### insertcoin.bas

```vb
5 rem preserve the original volume to restore it in leave.bas
10 let originalVolume = AudioGameGetVolume()
20 call AudioGameSetVolume(5) '5 dB
```

#### leave.bas

```vb
5 rem originalVolume was loaded in insertcoin.bas
10 call AudioAmbienceSetVolume(originalVolume)
```

