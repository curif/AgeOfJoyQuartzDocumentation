#agebasic #examples 
### Calculate the sum of cabinets assigned in all rooms
```vb
10 REM Program to calculate the sum of cabinets assigned in all rooms
20 LET totalRooms = RoomCount()
30 LET sumOfCabinets = 0

40 FOR roomIndex = 0 TO totalRooms - 1
50     LET roomNameFromIndex = RoomGetName(roomIndex)
60     LET assignedCabinetsInRoom = CabDBCountInRoom(roomNameFromIndex)
70     LET sumOfCabinets = sumOfCabinets + assignedCabinetsInRoom
80 NEXT roomIndex

90 PRINT 0,0, "Sum of Cabinets Assigned: " + STR(sumOfCabinets)
100 END
```

### Replace each cabinet in all rooms with a random cabinet
```vb
5 call DebugMode(1)
10 REM Replace each cabinet in all rooms with a random cabinet
20 LET totalRooms = RoomCount()
30 LET totalCabinetsDB = CabDbCount()
35 LET cont = 0
37 LET playerRoom = RoomName()

40 REM Loop through each room
50 FOR roomIndex = 0 TO totalRooms - 1
60     LET currentRoomName = RoomGetName(roomIndex)
65     LET countReplaced = 0
70     gosub 500

80     REM there is no way to know how many cabinets can hold a room, so it assumes 60 max.
81     rem obviously it will assing more than the room capacity.
90     FOR cabinetIndex = 0 TO 59
95         print 20,3, "#" + str(cabinetIndex)

100        REM is a cabinet assigned? we need one to proceed to change it.
110        if CabDBGetAssigned(currentRoomName, cabinetIndex) = "" then goto 170

120        LET randomIndex = INT(RND(1, totalCabinetsDB)) - 1
121        LET newCabinetName = CabDbGetName(randomIndex)
122        if newCabinetName = "" then goto 170

130        rem change the database by assigning the cabinet to the old position
140        if CabDBAssign(currentRoomName, cabinetIndex, newCabinetName) = 0 then goto 990

145        LET countReplaced = countReplaced + 1
146        print 0, 4 + MOD(countReplaced, 10), "#" + str(cabinetIndex) + " by DB #" + str(randomIndex) + ": " + str(newCabinetName) + "        "

149        rem change in current Room if it is the same to see it inmediatly
150        if playerRoom = currentRoomName then call CabRoomReplace(cabinetIndex, newCabinetName)

160        let cont=cont+1

170    NEXT cabinetIndex
180 NEXT roomIndex

190 CALL CabDBSave()
200 goto 10000

500 REM show main info
510 CLS
520 print 0,1, "Rooms: " + str(totalRooms), 0, 0
530 print 0,2, "Cabinets in DB:" + str(totalCabinetsDB), 0, 0
540 print 0,3, "room:" + currentRoomName, 1, 0
550 show
560 return

990 print 0,19, "assignment error", 1
995 print 0,20, "room:" + currentRoomName + "#" + str(cabinetIndex) + "cab:" + newCabinetName

10000 print 0, 23, "replaced: " + str(cont)
10010 print 0, 24, "PRESS B to end", 1
10050 IF ControlActive("JOYPAD_B") THEN END
10060 goto 10050

```

### Randomize two cabinets in a room
```vb
10 REM Cabinet Randomizer
20 LET numCabinets = CabRoomCount()
30 IF (numCabinets < 2) THEN GOTO 70  
40 LET index1 = INT(RND(0, numCabinets))
50 LET index2 = INT(RND(0, numCabinets))
60 IF (index1 = index2) THEN GOTO 40
70 LET cabinet1 = CabRoomGetName(index1)
80 LET cabinet2 = CabRoomGetName(index2)
90 CALL CabRoomReplace(index1, cabinet2)
100 CALL CabRoomReplace(index2, cabinet1)
110 END
```
