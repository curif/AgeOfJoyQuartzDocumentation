The AGEBasic event system is a new engine available starting at version 0.6.
The system allows program execution when a event arise.
# Events

Events are triggered by specific actions in [[Age of Joy]]. While not all actions produce events, key interactions do, and developers will continue to introduce new ones in the future. Each event can execute an [[AGEBasic]] program when activated.

The system is initiated when a player inserts a coin in the cabinet. From that point, the event system operates in a continuous loop, starting with the coin insertion and concluding when the game ends on the cabinet. This event system is exclusive to cabinets and cannot run in rooms.

Currently, the following events are available:

- `on-always`: The AGEBasic program runs continuously. Once it finishes, it immediately starts again in the next loop.
- `on-timer`: This event can be configured to execute at set intervals, such as every second.
- `on-control-active-pressed/held/released`: Activated when the player interacts with a control, such as pressing/holding/releasing a button or moving a joystick.
- `on-insert-coin`: Triggered when a player inserts a coin into the cabinet.
- `on-custom`: A custom event that can be triggered from AGEBasic using the `EventTrigger()` function.
- `on-lightgun-enter`: Activated when the light gun points at a specific cabinet part.
- `on-lightgun-stay`: Activated when the light gun continues pointing at a specific cabinet part.
- `on-lightgun-exit`: Activated when the light gun doesn't points anymore at a specific cabinet part.
- `on-collision-start/stay/end`: Triggered when a cabinet part begins colliding with another part, maintain collision or end.
- `on-touch-start/end`: Activated when the player touches a cabinet part.

> [!important] 
> - only one program can execute at the same time. The event loop will wait for a program to finish to evaluate the next event.
> - The event system evaluate the triggers in order in a loop, when the last one is evaluated the loops restart.
> - These events require a part name to work: "on-collision-start", "on-collision-stay", "on-collision-end", "on-touch-start", "on-grab-start", "on-touch-end" and "on-grab-end"
> - Parts that interact with the player, [[Light guns]] or with other parts must to be `physical`. Read the [[Cabinet physical parts manual]] for details.

# Event syntax


```yaml
agebasic:
  debug: false
  after-load: onload.bas
  after-leave: onleave.bas
  after-insert-coin: oninsertcoin.bas
  events:
    - event: on-always
      name: my event name
      program: move.bas
      goto: 400
      delay: 0.001
      when:
        variable: myvar
        value: 1
```

- `events`: event list, is evaluated in order.
	- `name`: of the event (see `on-custom`). Optional.
	- `program`: [[AGEBasic]] program file to execute. Required.
	- `goto`: line number to start program execution. Optional, if it is missing the program will start at the first line.
	- `delay`: an optional interval to delay the evaluation between executions.
	- `when`: conditions the event's evaluation. Optional.
# Event types description

## `on-always`

This event executes the program `move.bas` on each loop. It is triggered always.

```yaml
agebasic:
  debug: false
  after-load: onload.bas
  after-leave: onleave.bas
  after-insert-coin: oninsertcoin.bas
  events:
    - event: on-always
      program: move.bas
      goto: 400
      #delay: 0.001
```

## `on-timer`

The event is triggered after a time delay in seconds (with decimals).
In the example the program is executed approximately once per second.

```yaml
  events:
    - event: on-timer
      program: move.bas
      delay: 1
```

## `on-control-active-pressed/held/release`

This event is triggered when a player interacts with a control (like a button or joystick) in the game. The event can handle different states of the control such as when it's pressed, held, or released.

### Example

```yaml
- event: on-control-active-pressed
      control: &keybupwall
        libretro-id: JOYPAD-A
        port: 0
      variables: &wall2vars
        - name: wall
          type: string
          value: wall2
      program: controlpress.bas
    - event: on-control-active-held
      control: *keybupwall
      variables: *wall2vars
      program: controlheld.bas
    - event: on-control-active-released
      control: *keybupwall
      variables: *wall2vars
      program: controlrelease.bas
```

### Explanation

1. **`on-control-active-pressed` Event:**
   - **Trigger:** When the player presses the `JOYPAD-A` button (on port 0).
   - **Action:** Runs the `controlpress.bas` program.

2. **`on-control-active-held` Event:**
   - **Trigger:** When the player continues to hold down the `JOYPAD-A` button.
   - **Action:** Runs the `controlheld.bas` program.

3. **`on-control-active-released` Event:**
   - **Trigger:** When the player releases the `JOYPAD-A` button.
   - **Action:** Runs the `controlrelease.bas` program.

### Additional Details:

- The default value for `port` is `0`, so it’s optional to include it in the configuration unless you need to specify a different port.

Read the manual for [[Controller configuration]] to understand how controls are mapped. Also read the [[Default controllers configuration mapping]].

## `on-insert-coin`

This event is triggered any time the player insert a coin in the cabinet but not the first time. If you want to perform an action when the player insert a coin for first time in the cabinet (to activate the game) use the `after-insert-coin` program.

## `on-custom`

The event is triggered by the execution of `EventTrigger(event name string)` function in AGEBasic.

```yaml
    - event: on-custom
      name: my-custom-event
      program: dosomething.bas
```

In any AGEBasic program you could call the `EventTrigger` function to execute the event and call the program `dosomenthing.bas`.

```vb
10 CALL EventTrigger("my-custom-event")
```
## `on-collision-start/stay/end`

These events are triggered when a part in your game collides with another object, and they are useful for detecting when an object begins, continues, or ends a collision with another part.

### Example

```yaml
    - event: on-collision-start
      part: wall1
      impact-parts: 
        - sphere
        - cube
      program: oncollision.bas
```

### Explanation

1. **`on-collision-start` Event:**
   - **Trigger:** Activated the moment a collision begins between `wall1` and any of the specified parts, such as `sphere` or `cube`.
   - **Action:** Runs the `oncollision.bas` program.
   - **Example Scenario:** If either the sphere or cube (both parts of the cabinet) makes contact with `wall1` for the first time, this event is triggered.

2. **`on-collision-stay` Event:**
   - **Trigger:** Activated as long as the collision between `wall1` and the specified parts (`sphere` or `cube`) continues after the initial contact.
   - **Action:** This event allows you to trigger continuous behaviors while the objects remain in contact.
   - **Example Scenario:** If the sphere or cube stays in contact with `wall1` for an extended period, this event remains active, running the corresponding program until the objects separate.

3. **`on-collision-end` Event:**
   - **Trigger:** Activated when the collision between `wall1` and the specified parts (`sphere` or `cube`) ends, meaning the objects move apart and are no longer touching.
   - **Action:** Triggers actions when objects separate after a collision.
   - **Example Scenario:** If the sphere or cube stops touching `wall1` (e.g., by moving away), this event will fire, signaling that the collision has ended.

### Summary of Collision Events:

- **`on-collision-start`:** Triggered when the collision **begins**.
- **`on-collision-stay`:** Triggered **while** the collision persists.
- **`on-collision-end`:** Triggered when the collision **ends**.

These events allow you to detect and respond to different stages of a collision between parts, enabling more dynamic interactions in your game.
## `on-touch-start/end`

This event is triggered when the player interacts by touching a specific cabinet part.

To enable touch detection on a part, you must mark it as touchable in the part’s configuration:

```yaml
parts:
  - name: mysphere
    physical:
	  shape: sphere
    player-interaction:
      can-touch: true
```

### Example

In [[AGEBasic]] events:

```yaml
    - event: on-touch-start
      part: mysphere
      program: touchwall2.bas
    - event: on-touch-end
      part: mysphere
      program: untouchwall2.bas
```

### Explanation
- **`on-touch-start`:** This event is triggered when the player starts touching the `wall2` part, executing the `touchwall2.bas` program.
- **`on-touch-end`:** This event is triggered when the player stops touching the `wall2` part, executing the `untouchwall2.bas` program.

In this example, when the player begins touching the part, the `touchwall2.bas` program runs, and when the touch ends, the `untouchwall2.bas` program is executed.

---

# Variables

You can assign variables to AGEBasic programs directly from an event. When the event triggers the system ingest variables and values to your program. You can use the variables as usual.

**Variables:**

* **`variables` (list of objects):**
    * Defines variables accessible to all AGEBasic programs.
    * Each object specifies:
        * **`name` (string):** Unique variable name following [[AGEBasic programing#Variables]] conventions.
        * **`type` (string):** Data type (`string` or `number`).
        * **`value` (string):** Initial value (converted to specified type).

Example:

```yaml
  events:
    - event: on-always
      program: move.bas
      variables:
        - name: velocity
          type: number
          value: 10
```

---

# Conditionals

You can execute or not an event based on a conditional. If the condition doesn't accomplish the event is not evaluated and isn't executed.

A conditional could contain constant values and variables in the comparison. `and` and `or` is also available.

Example:

```yaml
    - event: on-control-active-pressed
      name: Loop on/off
      control:
        libretro-id: JOYPAD_B
      program: menu.bas
      goto: 400
      when: 
        and: 
          - variable: menuType
            value: 1
          - variable: option
            comparison: "greater than"
            value: 4
          - variable: volume
	        comparison: ">"
	        compare-to: minDB
```

- `when`: Optional. The condition must accomplish to evaluate the event.
	- `and`: contains a list of conditions. All of them should evaluate to true.
	- `or`: At least one of them should evaluate to true.
	- `variable`: [[AGEBasic]] variable to compare.
	- `value`: constant to compare
	- `compare-to`: a variable to compare in place of `value`.
	- `comparison`: options: `equals`, `=`, `greater than`, `>`, `less than`, `<`, `greater than or equals`, `>=`, `less than or equals`, `<=`, `not equals`, `<>` or `!=`. Defaults to `=` if missing.

A conditional could be as complex as needed:

```yaml
	when: 
        and: 
          - variable: menuType
            value: 1
          - variable: option
            comparison: "greater than"
            value: 4
          - variable: volume
	        comparison: ">"
	        compare-to: minDB
	      - or:
			  - variable myvar2
				value: 30
			  - variable myvar3
				condition: greater than
				value: 30
			      
```

> [!warning]
> It is not possible to mix `and`, `or` and `variable` at same level.

Erroneous construction:

```yaml
    when:
        and: 
          - variable: menuType
            value: 1
          - variable: option
            comparison: "greater than"
            value: 4
	    variable: volume
		value: 0
```