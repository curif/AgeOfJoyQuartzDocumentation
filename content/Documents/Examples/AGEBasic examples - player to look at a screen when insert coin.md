> [!warning]
> Available only after version 0.5 release candidate 4

On some complex cabinets should be useful to position the player in a proper position to play a game. This example and guide will help you (as a [[Cabinet Artist]]) to position the player in a place to play a game when the game starts, and to recover the original position when it ends.

To do this, you will need to create three [[AGEBasic]] programs and register them in cabinet's `description.yaml` file.

```yaml title="description.yaml"
agebasic:
  active: true
  debug: true
  after-insert-coin: insertcoin.bas
  after-leave: onleave.bas
  after-load: onload.bas

```

> remember to delete the `debug` entry on cabinet distribution.


### Create a component to establish the player position

The idea is to use a component in the cabinet to design the player's position, could be made in [[Blender]]

![[Pasted image 20240205131038.png]]
 The cube in the image is located where the player head should be when the game starts.
 Name it as you wish, for example "head".

Export the model of your cabinet as `glb`.

#### On load

During the `onload` phase we will register the position of the *head* so we can use it later

> [!note] 
> Remember: all program's cabinets uses the same `variable` space. You can access a variable defined in another program.

```vb title="onload.bas"
10 rem Get cab part position and coordinates
20 let head = CabPartsPosition("head")
30 if head = -1 then goto 1000
40 let screen = CabPartsPosition("screen-mock-horizontal")
50 if screen = -1 then goto 1000

60 lets headX, headZ, headH = CabPartsGetCoordinate(head, "X"), CabPartsGetCoordinate(head, "Z"), CabPartsGetCoordinate(head, "H")
70 call CabPartsEnable(head, 0)
80 end

1000 let error = "some cabinets parts not found in cabinet"
1010 end
```

In lines 20 and 40 the program find the part number for the `head` and the `screen` components. In line 60 the program gets the head position in [[3D space]]. Both variables will be useful in the next programs.
The program disable the head (so the player can't see the head box).

#### Insert coin

The next stage is the insert coin, the program will run when the user insert a coin on the cabinet. The program will change the player height (previously it storage the actual value in the variable `playerH`) by the same height of the `head` component (`headH` on the `onload.bas`). After that in line 90 and 100 the program moves the player to the same `X` and `Z` coordinates than the `head` to position the player on the desired place.
In line 110 the program forces the player to look to the direction of the screen.

```vb title="insertcoin.bas"
10 rem get actual player position x and Z
20 lets playerX, playerZ = PlayerGetCoordinate("x"), PlayerGetCoordinate("z")
30 rem get the player height
40 let playerH = PlayerGetHeight()

50 rem change player height at the same of the head object. 
60 rem the head object height is the distance from the ground, like the player.
70 call PlayerSetHeight(headH)
80 rem move the player to the coordinates of the cabinets' head component.
90 call PlayerSetCoordinate("X", headX)
100 call PlayerSetCoordinate("Z", headZ)
110 call PlayerLookAt(screen)

```

#### On leave

When the player leaves the program will recover the player position and height stored during the insert coin event.

```vb title="onleave.bas"
10 rem return the player to its previous position
20 rem and height when the player leaves the game
30 call PlayerSetHeight(playerH)
40 call PlayerSetCoordinate("x", playerX)
50 call PlayerSetCoordinate("z", playerZ)
60 end
```

#agebasic #examples