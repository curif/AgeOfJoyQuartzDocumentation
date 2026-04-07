# AGEBasic LED Interface

Starting with version 0.6, [[AGEBasic]] can react to LED signals emitted by arcade game ROMs during emulation. Real arcade PCBs drove physical lamps — Player 1/2 Start buttons, coin counters, attract-mode flashers — via dedicated output lines. The LibRetro `LED interface` exposes those same signals to the frontend, and Age of Joy forwards them to AGEBasic.

> [!note] MAMEHooker users
> If you have used **MAMEHooker** to drive external LED hardware from MAME output signals, this is the same concept. The LED indices in Age of Joy correspond to the same output signals that MAMEHooker reads (e.g. `lamp0`, `lamp1`, …). Instead of wiring to physical hardware, you use AGEBasic to react to those signals inside the VR cabinet.

## How it works

When a compatible core loads a game that drives LEDs, it calls the LED interface callback once per video frame for each LED that changes state. Age of Joy captures those changes and makes them available as `on-led-change` events and as the `LEDSTATE()` function.

LED states are binary: **0** (off) or **1** (on). Each LED is addressed by an index (0–7).

> [!important]
> This feature depends on the emulation core implementing the LibRetro LED interface. Currently only **mame2003-plus** implements it. mame2010 and fbneo do not. If the core does not call the interface, the events self-disable silently after the first poll — there is no error and no CPU cost.

## Core and game compatibility

### Games with LEDs (mame2003-plus)

| ROM | Notes |
|-----|-------|
| `starwars.zip` | 3 LEDs (Player 1 Start, Player 2 Start, coin counter) |
| `missile.zip` | Start button lamps |
| `berzerk.zip` | Lamp outputs |
| `ajax.zip` | Lamp outputs |
| `battles.zip` | Lamp outputs |

### Games without LEDs

| ROM | Notes |
|-----|-------|
| `junofrst.zip` | No LED outputs — events self-disable |

> [!note]
> LED semantics are game-specific. Index 0 in Star Wars is not the same signal as index 0 in Missile Command. You need to discover which index corresponds to which lamp by observing the log during gameplay (search for `[OnLedChange] TRIGGER`).

## Discovering LEDs in a game

Add a diagnostic snippet to an `on-always` program or a temporary hook file:

```vb
10 FOR I = 0 TO 7
20   LET S = LEDSTATE(I)
30   IF S >= 0 THEN PRINT "LED "; I; " = "; S
40 NEXT I
50 END
```

Run the game and watch the [[Configuration Room]] log. Lines like:

```
[OnLedChange] TRIGGER led=0 1 → 0 → jumping to line 1000
```

confirm which indices are active.

---

## `on-led-change` event

The `on-led-change` event fires whenever a specific LED changes state (off→on or on→off). It is edge-triggered — it does not fire repeatedly while the LED is steady.

### YAML syntax

```yaml
agebasic:
  events:
    - event: on-led-change
      led: 0
      var: LED0
      program: hooks.bas
      goto: 1000
```

| Field | Type | Description |
|-------|------|-------------|
| `event` | string | Must be `on-led-change` |
| `led` | number | LED index to watch (0–7) |
| `var` | string | AGEBasic variable that receives the new state (0 or 1) |
| `program` | string | AGEBasic file to execute |
| `goto` | number | Line number to jump to inside the program |

You can register multiple events in the same program file using different `goto` targets:

```yaml
agebasic:
  events:
    - event: on-led-change
      led: 0
      var: LED0
      program: starwars-hooks.bas
      goto: 1000
    - event: on-led-change
      led: 1
      var: LED1
      program: starwars-hooks.bas
      goto: 2000
    - event: on-led-change
      led: 2
      var: LED2
      program: starwars-hooks.bas
      goto: 3000
```

---

## AGEBasic functions

### `LEDSTATE(index)`

Returns the current state of the LED at `index`.

| Return value | Meaning |
|---|---|
| `1` | LED is on |
| `0` | LED is off |
| `-1` | LED unavailable or game not loaded |

```vb
10 LET S = LEDSTATE(0)
20 IF S < 0 THEN GOTO 200
30 IF S = 1 THEN CALL CABPARTSEMISSION("button1", 1)
40 IF S = 0 THEN CALL CABPARTSEMISSION("button1", 0)
50 END
```

### `ONLED(index, "varName")` (used with `ONEVENT`)

Registers an `on-led-change` handler from inside a running AGEBasic program instead of from YAML. Returns a config-event descriptor consumed by `ONEVENT`.

```vb
10 ONEVENT ONLED(0, "P1_LAMP") GOTO 1000
20 ONEVENT ONLED(1, "P2_LAMP") GOTO 2000
30 END

1000 IF P1_LAMP = 1 THEN CALL CABPARTSEMISSION("p1start", 1)
1010 IF P1_LAMP = 0 THEN CALL CABPARTSEMISSION("p1start", 0)
1020 END

2000 IF P2_LAMP = 1 THEN CALL CABPARTSEMISSION("p2start", 1)
2010 IF P2_LAMP = 0 THEN CALL CABPARTSEMISSION("p2start", 0)
2020 END
```

---

## Star Wars cabinet example

The Star Wars cabinet uses three `on-led-change` events to drive emission color on the `back` panel. Each LED maps to a different color — blue for Player 1, red for Player 2, yellow for the coin counter.

**`description.yaml` (excerpt):**

```yaml
agebasic:
  events:
    - event: on-led-change
      led: 0
      var: LED0
      program: starwars-hooks.bas
      goto: 1000
    - event: on-led-change
      led: 1
      var: LED1
      program: starwars-hooks.bas
      goto: 2000
    - event: on-led-change
      led: 2
      var: LED2
      program: starwars-hooks.bas
      goto: 3000
```

**`starwars-hooks.bas`:**

```vb
10  REM starwars-hooks.bas
20  REM Reacts to Star Wars LED state changes (indices 0, 1, 2).
30  REM LED0, LED1, LED2 are injected by the on-led-change events.
50  END

1000 REM ---- LED 0 (Player 1 Start — blue) ----
1010 IF LED0 = 1 THEN CALL CABPARTSEMISSION("back", 1) : CALL CabPartsSetEmissionColor("back", 100, 180, 255)
1030 IF LED0 = 0 THEN CALL CABPARTSEMISSION("back", 0) : CALL CabPartsSetEmissionColor("back", 0, 0, 0)
1050 END

2000 REM ---- LED 1 (Player 2 Start — red) ----
2010 IF LED1 = 1 THEN CALL CABPARTSEMISSION("back", 1) : CALL CabPartsSetEmissionColor("back", 255, 80, 80)
2030 IF LED1 = 0 THEN CALL CABPARTSEMISSION("back", 0) : CALL CabPartsSetEmissionColor("back", 0, 0, 0)
2050 END

3000 REM ---- LED 2 (Coin counter — yellow) ----
3010 IF LED2 = 1 THEN CALL CABPARTSEMISSION("back", 1) : CALL CabPartsSetEmissionColor("back", 255, 220, 80)
3030 IF LED2 = 0 THEN CALL CABPARTSEMISSION("back", 0) : CALL CabPartsSetEmissionColor("back", 0, 0, 0)
3050 END
```

> [!note]
> The marquee part does not respond to emission changes. Use `back`, `bezel`, or other panel parts. `CabPartsSetEmissionColor` changes the emitted light color; `CABPARTSEMISSION` toggles emission on/off.

---

## Limitations

- **Edge-triggered only.** The event fires once per state change, not continuously. If you need the current state at any time, call `LEDSTATE()`.
- **Game-specific indices.** There is no standard mapping — LED 0 in one game is unrelated to LED 0 in another.
- **mame2003-plus only.** Other cores (mame2010, fbneo) do not call the LibRetro LED interface.
- **Starts after coin insert.** Like all cabinet events, the `on-led-change` loop is active only while a game session is running (between coin insert and game exit).

---

## See also

- [[AGEBasic cabinet event system]] — full event system reference
- [[AGEBasic in cabinets]] — how AGEBasic integrates with cabinets
- [[Cabinet physical parts manual]] — cabinet part names and types
