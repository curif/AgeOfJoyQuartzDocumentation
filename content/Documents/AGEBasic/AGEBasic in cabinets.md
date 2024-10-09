#agebasic 
### How to execute AGEBasic programs in response to events related to a specific cabinet.

[[Age of Joy]] can be configured to execute AGEBasic programs when the player produces actions on a cabinet, or in events related to a cabinet. You can find the AGEBasic subdocument specification in the [[CDL the Cabinet Description Language]]

All [[AGEBasic]] programs that run in a cabinet preserve the same variable's space, that means, you can set a variable in a program and read its value in another program. The variable's space is initialized when the cabinet loads.

To better understand how AGEBasic works please refer to [[AGEBasic programing]] specification.

> AGEBasic cabinet programs are packaged within the same file as all the other cabinet assets, such as images or models.

### Insert coin event

AGE will execute the program when the player insert a coin in the cabinet for first time (to start a game)

Eg: this program will insert five extra coins after the player insert the first one:

`myinsertcoins.bas`

```vb
10 for i = 1 to 5
20   let result = cabInsertCoin()
30   if result = -1 then goto 1000
40 next i
50 end

1000 call DebugMode(1)
1020 let ERROR = "error insert coin. coin #" + str(i)
```

- The `cabInsertCoin()` is called five times to insert five coins after the player insert the first one.

To execute this program you should insert this subdocument in the Cabinet's `description.yaml` file:

```yaml
agebasic:
  active: true
  debug: true
  after-insert-coin: myinsertcoins.bas
```

### On Load event

Execute a program when the cabinet is fully loaded.

E.g.: this program will hide (disable) some parts of the cabinet after load

```vb
  
100 let PartNumber = cabPartsPosition("joystick") 
110 gosub 400 
120 let PartNumber = cabPartsPosition("front") 
130 gosub 400 
140 let PartNumber = cabPartsPosition("marquee") 
150 gosub 400 
200 end 

400 if PartNumber = -1 then goto 1000 
410 call cabPartsEnable(PartNumber, 0) ' disable 
420 return

1000 call DebugMode(1) 'activate debug mode to see the "error" variable in the insertcoin.bas.debug file. 
1010 let error = "part not found"
```

The program will find the joystick, front and marquee parts to disable them.

Eg: save all the parts in a variable string to see it on debug mode.

```vb
10 let list = ""
20 let count = CabPartsCount()
30 for i = 0 to count - 1
40   let list = list + CabPartsName(i) + " - "
50 next i
60 call DebugMode(1)
70 end
```

Read about Debug Mode in [[AGEBasic programing]]
