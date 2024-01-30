
#agebasic 
# Configure room lighting

You can configure lights color and intensity. 

Using `GetLights()` you can get all the lights on the active rooms in a string with the structure: `"<light name>|<ligth name>|..."`. Where the light name have the format `"<room>:<lightname>"`.

Read more in the [[AGEBasic programing]] manual, light section.
## Show actual room lights

```vb
10 REM List Lights
15 CLS
20 LET lights = GetLights()
30 LET count = CountMembers(lights, "|")
40 PRINT 0, 0, "Room ID"
50 PRINT 10, 0, "Light Name"
60 PRINT 30, 0, "Intensity"

70 FOR i = 0 TO count - 1
80   LET lightInfo = GetMember(lights, i, "|")
90   LET roomID = GetMember(lightInfo, 0, ":")
100  LET lightName = GetMember(lightInfo, 1, ":")
110  LET intensity = GetLightIntensity(lightInfo)

120  PRINT 0, i + 2, roomID
130  PRINT 10, i + 2, lightName
140  PRINT 30, i + 2, intensity
150 NEXT i

160 SHOW

10010 print 0, 24, "PRESS B to end", 1
10050 IF ControlActive("JOYPAD_B") THEN END
10060 goto 10050
```

#### Result

![[Pasted image 20240105104436.png]]

## Change lights intensity

This code increase the lights intensity in a 30%. Be careful, the results couldn't be as expected because the way Unity manage the illumination. 

```vb
10 REM Increase Light Intensity
20 LET lights = GetLights()
30 LET count = CountMembers(lights, "|")

40 FOR i = 0 TO count - 1
50   LET lightInfo = GetMember(lights, i, "|")
60   LET intensity = GetLightIntensity(lightInfo)

70   REM Increase intensity by 30%
80   LET newIntensity = intensity + (intensity * 0.3)

90   REM Ensure the intensity doesn't exceed 10 (maximum intensity)
100  IF newIntensity > 10 THEN LET newIntensity = 10

110  REM Set the new intensity
120  call SetLightIntensity(lightInfo, newIntensity)
130 NEXT i

140 SHOW
150 END

```

## Change light color

This program changes all the lights to blue.

![[Pasted image 20240109090047.png]]

```vb
10  CALL DebugMode(1) 'activate the debug mode
15  CLS

20  LET lights = GetLights()
30  REM Check if lights are present
40  IF LEN(lights) > 0 THEN GOTO 100

50  REM No lights available, end program
60  PRINT 0, 0, "No lights in the room", 0
70  END

80  REM Lights are present, proceed to change color
100 LET numLights = CountMembers(lights, "|")
110 FOR i = 0 TO numLights - 1
120     LET light = GetMember(lights, i, "|")
140     IF NOT(SetLightColor(light, 0, 0, 1)) THEN GOTO 180
150 NEXT i

160 PRINT 0, 23, "Lights changed to blue", 0
170 GOTO 10010

180 PRINT 0, 23, "ERROR setting light color #" + STR(i) + " " + light
190 goto 10010

10010 PRINT 0, 24, "PRESS B to end", 1
10050 IF ControlActive("JOYPAD_B") THEN END
10060 GOTO 10050

```

