#agebasic #video

> [!important] Available from version **0.5.0-RC19**

AGEBasic cabinets of type `19i-agebasic` can control video playback entirely from scripts. This page is the complete reference for every video command and function.

For a general introduction see [[AGEBasic programing#Video Player]].

---

## Requirements

- The cabinet must declare `crt: type: 19i-agebasic` in its `description.yaml`.
- Video files must be placed in the video folder on the device. Use `VIDEOPATH()` to get the path — never hardcode it.

---

## How the screen works

The cabinet has two display modes that are mutually exclusive:

- **Video mode** — active after `VIDEOPLAY`. The video fills the screen. `PRINT` and `SHOW` have no visible effect while in this mode.
- **CRT mode** — active after `VIDEOPAUSE` or `VIDEOSTOP`. The normal AGEBasic drawing surface is visible. Use this to show a HUD, control menu, or any other on-screen text.

There is no way to draw text on top of a playing video.

---

## Commands

### `VIDEOLOAD`

```vb
VIDEOLOAD path [, invertX [, invertY]]
```

Loads a video file and prepares it for playback. `invertX` and `invertY` flip the image horizontally or vertically (pass `1` to enable, `0` or omit to disable).

This command does not start playback. Call `VIDEOPLAY` after loading.

```vb
10 LET FPATH = COMBINEPATH(VIDEOPATH(), "myvideo.mp4")
20 VIDEOLOAD FPATH
30 VIDEOPLAY
```

---

### `VIDEOPLAY`

```vb
VIDEOPLAY
```

Starts or resumes playback of the currently loaded video. Switches the screen to video mode.

If the video has not finished preparing yet, playback starts automatically as soon as it is ready — you do not need to poll or retry.

Calling `VIDEOPLAY` on a paused video resumes from the paused position.

---

### `VIDEOPAUSE`

```vb
VIDEOPAUSE
```

Pauses playback at the current position. Switches the screen back to CRT mode so you can draw a HUD or control menu.

Calling `VIDEOPLAY` after a pause resumes from the same position.

```vb
100 VIDEOPAUSE
110 CLS
120 PRINT 0, 8, "  [ PAUSED ]"
130 SHOW
140 END
```

---

### `VIDEOSTOP`

```vb
VIDEOSTOP
```

Stops playback and rewinds to the beginning. Switches the screen back to CRT mode.

```vb
200 VIDEOSTOP
210 CLS
220 PRINT 0, 8, "  [ STOPPED ]"
230 SHOW
240 END
```

---

### `VIDEOSEEK`

```vb
VIDEOSEEK seconds
```

Jumps to the given position in seconds. The video must already be playing or paused (prepared) for this to have any effect.

```vb
REM Fast-forward 10 seconds
310 VIDEOSEEK VIDEOTIME() + 10
320 END

REM Rewind 10 seconds (clamp to 0)
410 VIDEOSEEK MAX(0, VIDEOTIME() - 10)
420 END
```

---

### `VIDEOLOOP`

```vb
VIDEOLOOP 1
VIDEOLOOP 0
```

Enables (`1`) or disables (`0`) looping. When looping is on, the video repeats automatically when it reaches the end. Looping is **on by default**.

```vb
REM Toggle loop on/off
710 VIDEOLOOP IIF(VIDEOLOOPSTATUS() = 1, 0, 1)
720 END
```

---

### `VIDEOLOADURL`

```vb
VIDEOLOADURL url [, invertX [, invertY]]
```

Loads a video from an HTTP or HTTPS URL instead of a local file. Prepares it for playback without starting it — call `VIDEOPLAY` after loading.

Supported sources:
- Direct video links (`.mp4`, `.mkv`, etc.)
- HLS adaptive streams (`.m3u8`) served by Jellyfin, Plex, or any DLNA server with an HTTP endpoint
- Jellyfin `/Items/<id>/Download?api_key=<token>` direct download URLs

Only `http://` and `https://` schemes are accepted. Streams requiring custom HTTP headers, auth tokens embedded in headers, or DRM protection are not supported.

> [!warning] HTTP streams and cleartext traffic
> Android blocks unencrypted `http://` connections by default. Age of Joy explicitly allows cleartext traffic so `VIDEOLOADURL` can reach local and internet media servers over plain HTTP. Be aware that `http://` streams — including auth tokens embedded in the URL (e.g. `?api_key=...`) — are transmitted unencrypted. Use `https://` whenever your server supports it.

`invertX` and `invertY` flip the image horizontally or vertically (pass `1` to enable, omit or pass `0` to disable).

After loading, all other video commands (`VIDEOPLAY`, `VIDEOPAUSE`, `VIDEOSTOP`, `VIDEOSEEK`, `VIDEOTIME()`, etc.) work exactly the same as with local files.

```vb
10 VIDEOLOADURL "http://192.168.1.10:8096/Items/abc123/Download?api_key=mytoken"
20 VIDEOPLAY
```

---

## Functions

### `VIDEOPATH()`

Returns the path of the folder where video files are stored on the device.

```vb
10 PRINT 0, 5, VIDEOPATH()
```

Use `COMBINEPATH()` to build a full path to a specific file:

```vb
10 LET FPATH = COMBINEPATH(VIDEOPATH(), "intro.mp4")
```

---

### `VIDEOSTATUS()`

Returns the current state of the video player as a number:

| Value | Meaning |
| :---: | :--- |
| `0` | Not loaded or not ready |
| `1` | Stopped / ready (no video is playing) |
| `2` | Playing |
| `3` | Paused |

Use this in timer events to decide whether to redraw the HUD:

```vb
10 LET S = VIDEOSTATUS()
20 IF AND(S <> 1, S <> 3) THEN END
30 REM draw HUD here...
```

---

### `VIDEOTIME()`

Returns the current playback position in seconds as a number.

```vb
10 PRINT 0, 10, "Time: " + STR(INT(VIDEOTIME())) + "s"
```

---

### `VIDEODURATION()`

Returns the total duration of the loaded video in seconds.

```vb
10 PRINT 0, 11, "Duration: " + STR(INT(VIDEODURATION())) + "s"
```

---

### `VIDEOLOOPSTATUS()`

Returns `1` if looping is currently enabled, `0` if it is off.

```vb
10 PRINT 0, 12, "Loop: " + IIF(VIDEOLOOPSTATUS() = 1, "ON", "OFF")
```

---

### `READM3UARRAY(path)`

Reads an M3U or M3U8 playlist file and returns its entries as an array. Lines starting with `#` (M3U directives and comments) and blank lines are skipped. Each remaining line — whether a URL or a file path — becomes one element of the returned array.

Returns an empty string if the file has no entries or cannot be read.

```vb
10 DIM PLAYLIST[200]
20 PLAYLIST = READM3UARRAY(COMBINEPATH(VIDEOPATH(), "channels.m3u8"))
30 VIDEOLOADURL PLAYLIST[0]
40 VIDEOPLAY
```

Iterating a full playlist:

```vb
10 DIM LIST[200]
20 LIST = READM3UARRAY(COMBINEPATH(VIDEOPATH(), "movies.m3u"))
30 LET IDX = 0
40 LET TOTAL = LEN(LIST)
50 IF IDX >= TOTAL THEN END
60 VIDEOLOADURL LIST[IDX]
70 VIDEOPLAY
80 LET IDX = IDX + 1
90 GOTO 50
```

The videoplayer cabinet automatically detects `.m3u` / `.m3u8` files in `VIDEOPATH()` and expands them at startup — you get a single unified playlist mixing local files and network URLs, navigated with the same up/down controls.

---

## Complete example: multi-file player

This example shows a complete video player cabinet with all four files: `description.yaml`, `after_load.bas`, `insert_coin.bas`, `player.bas`, and `hud.bas`.

---

### `description.yaml`

This is the cabinet configuration file. The critical field is `crt: type: 19i-agebasic` — without it the video commands are not available.

```yaml
---
name: videoplayer
year: 2024
style: galaga
material: black

agebasic:
  active: true
  system-skin: c64
  after-load: after_load.bas         # runs once when the cabinet loads (before coin)
  after-insert-coin: insert_coin.bas # runs every time the player inserts a coin

  variables:
    - name: CURR_FILE   # index of the file currently loaded (0-based)
      type: number
      value: "0"
    - name: FILE_COUNT  # total number of video files found
      type: number
      value: "0"
    # CURR_FILE and FILE_COUNT are declared here so that the `when:` guards
    # on button events can check FILE_COUNT before insert_coin.bas has run.
    # FILES is not declared here because it is populated dynamically by
    # GETFILESARRAY() inside insert_coin.bas.

  events:

    # Timer: refresh the HUD every 2 seconds.
    # hud.bas checks VIDEOSTATUS() itself and exits early if the video is playing.
    - event: on-timer
      name: hud update
      program: hud.bas
      delay: 2

    # B — Play / Pause toggle.
    # `when:` prevents the button from firing before any files are loaded.
    - event: on-control-active-released
      name: play pause
      control:
        libretro-id: JOYPAD_B
      program: player.bas
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # Y — Stop. Jumps to line 100 inside player.bas.
    - event: on-control-active-released
      name: stop
      control:
        libretro-id: JOYPAD_Y
      program: player.bas
      goto: 100
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # D-pad Right — Fast-forward 10 s (line 300 in player.bas).
    - event: on-control-active-released
      name: fast forward
      control:
        libretro-id: JOYPAD_RIGHT
      program: player.bas
      goto: 300
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # D-pad Left — Rewind 10 s (line 400 in player.bas).
    - event: on-control-active-released
      name: rewind
      control:
        libretro-id: JOYPAD_LEFT
      program: player.bas
      goto: 400
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # D-pad Down — Next file (line 500 in player.bas).
    - event: on-control-active-released
      name: next file
      control:
        libretro-id: JOYPAD_DOWN
      program: player.bas
      goto: 500
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # D-pad Up — Previous file (line 600 in player.bas).
    - event: on-control-active-released
      name: prev file
      control:
        libretro-id: JOYPAD_UP
      program: player.bas
      goto: 600
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # A — Toggle loop on/off (line 700 in player.bas).
    - event: on-control-active-released
      name: toggle loop
      control:
        libretro-id: JOYPAD_A
      program: player.bas
      goto: 700
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

    # X — Restart from the beginning (line 800 in player.bas).
    - event: on-control-active-released
      name: restart
      control:
        libretro-id: JOYPAD_X
      program: player.bas
      goto: 800
      when:
        variable: FILE_COUNT
        comparison: ">"
        value: 0

coinslot: coin-slot-small

parts:
  - name: marquee
    type: marquee
    art:
      file: marquee.png

crt:
  type: 19i-agebasic      # REQUIRED — enables video commands in AGEBasic
  orientation: horizontal
  screen:
    shader: crt
    damage: low
    inverty: false
```

**Key points about the YAML:**

- `goto:` sends execution directly to a line number inside the program, so one file (`player.bas`) can handle all button actions — each section starts at its own line number.
- `when:` guards prevent button events from firing before `insert_coin.bas` has run and populated `FILE_COUNT`.
- `variables:` pre-creates `CURR_FILE` and `FILE_COUNT` at cabinet load time. The `FILES` array is created at runtime inside `insert_coin.bas`.
- `after-load:` runs once when the room loads (attraction screen). `after-insert-coin:` runs every time a coin is inserted.

---

### `after_load.bas`

Shown on the screen while waiting for a coin. No video is playing yet.

```vb
10 CLS
20 FGCOLOR "cyan"
30 PRINTCENTERED 8, "AGE OF JOY VIDEO PLAYER", 0
40 RESETCOLOR
50 PRINTCENTERED 11, "Insert coin to start", 0
60 PRINTCENTERED 13, "Place videos in:", 0
70 PRINTCENTERED 14, VIDEOPATH(), 0
80 SHOW
90 END
```

---

**`insert_coin.bas`** — runs when the player inserts a coin:

```vb
10 LET FILES = GETFILESARRAY(VIDEOPATH(), 0)
20 LET FILE_COUNT = LEN(FILES)
30 IF FILE_COUNT = 0 THEN GOTO 100
40 LET CURR_FILE = 0
50 VIDEOLOAD COMBINEPATH(VIDEOPATH(), FILES[CURR_FILE])
60 VIDEOPLAY
70 END
100 CLS
110 PRINTCENTERED 8, "NO VIDEO FILES FOUND", 0
120 PRINTCENTERED 11, VIDEOPATH(), 0
130 SHOW
140 END
```

**`player.bas`** — handles all button events via `goto:` in `description.yaml`:

```vb
10 REM B — Play / Pause
20 IF VIDEOSTATUS() = 2 THEN VIDEOPAUSE : END
30 IF VIDEOSTATUS() = 3 THEN VIDEOPLAY : END
40 VIDEOLOAD COMBINEPATH(VIDEOPATH(), FILES[CURR_FILE])
50 VIDEOPLAY
60 END

100 REM Y — Stop
110 VIDEOSTOP
120 CLS : PRINT 0, 8, "  [ STOPPED ]" : SHOW
130 END

300 REM Right — Fast-forward 10 s
310 VIDEOSEEK VIDEOTIME() + 10
320 END

400 REM Left — Rewind 10 s
410 VIDEOSEEK MAX(0, VIDEOTIME() - 10)
420 END

500 REM Down — Next file
510 LET CURR_FILE = MOD(CURR_FILE + 1, FILE_COUNT)
520 VIDEOLOAD COMBINEPATH(VIDEOPATH(), FILES[CURR_FILE])
530 VIDEOPLAY
540 END

600 REM Up — Previous file
610 LET CURR_FILE = MOD(CURR_FILE - 1 + FILE_COUNT, FILE_COUNT)
620 VIDEOLOAD COMBINEPATH(VIDEOPATH(), FILES[CURR_FILE])
630 VIDEOPLAY
640 END

700 REM A — Toggle loop
710 VIDEOLOOP IIF(VIDEOLOOPSTATUS() = 1, 0, 1)
720 END
```

**`hud.bas`** — timer event, redraws control menu every 2 seconds when stopped or paused:

```vb
10 IF FILE_COUNT = 0 THEN END
20 LET S = VIDEOSTATUS()
30 IF AND(S <> 1, S <> 3) THEN END
40 CLS
50 PRINTCENTERED 1, "VIDEO PLAYER", 0
60 IF S = 1 THEN PRINT 0, 4, "  [ STOPPED ]"
70 IF S = 3 THEN PRINT 0, 4, "  [ PAUSED  ]"
80 PRINT 0, 6, "  [B] Play/Pause   [Y] Stop"
90 PRINT 0, 7, "  [<] Rewind 10s   [>] Forward 10s"
100 PRINT 0, 8, "  [^] Prev file    [v] Next file"
110 SHOW
120 END
```

---

## Tips

- Use `GETFILESARRAY(VIDEOPATH(), 0)` to get the list of all files in the video folder. The files are returned in filesystem order — prefix filenames with numbers (`01-intro.mp4`, `02-main.mp4`) to control the order.
- The `FILES` array and `FILE_COUNT`/`CURR_FILE` variables are shared across all event programs in the same cabinet session. Declare `CURR_FILE` and `FILE_COUNT` in `description.yaml` under `variables` so they are available before the coin is inserted (needed for `when:` guards on button events).
- A timer event with `delay: 2` is a good way to keep the HUD refreshed without running too often. Always check `VIDEOSTATUS()` at the top and exit early if the video is playing.
- **Mixing local files and network streams**: place `.m3u` or `.m3u8` playlist files alongside your `.mp4`/`.mkv` files in `VIDEOPATH()`. Use `READM3UARRAY()` at startup to expand them into a single `PLAYLIST` array, then decide at play-time whether to call `VIDEOLOAD` (local) or `VIDEOLOADURL` (network) by checking if the entry starts with `http`.
- **Jellyfin / Plex URLs**: use the `/Items/<id>/Download?api_key=<token>` endpoint for direct file delivery. The `/stream` endpoint also works and supports on-the-fly transcoding, but `static=true` (`/stream?static=true&...`) skips transcoding for best quality over a local network.
- **M3U file format**: one URL or path per line. Lines starting with `#` are ignored. Save the file with a `.m3u` or `.m3u8` extension and place it in `VIDEOPATH()`.
