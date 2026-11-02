<h1 align="center">FH2 Mouse &amp; Keyboard</h1>

A mouse cursor and keyboard controls for **Forza Horizon 2** on PC (Azimuth). Drive with the keyboard, point at things in the menus and click them, drag the map, turn the garage camera, place decals with the keyboard, and fly the photo mode camera, all without picking up a controller. The controller keeps working as before, and you can switch between the two at any time.

FH2 Mouse & Keyboard (FH2Mouse) is a mod for the [FH2 Mod Platform](https://github.com/Trinculo54/fh2-mod-platform).

## Controls

**Everywhere in the menus**

| Mouse | Does |
|---|---|
| Move | Selects the button, tile, list row, slider or option under the cursor |
| Left click | A on what's under the cursor: opens a tile, picks a car, switches a tab |
| Left click on a slider or option | Changes it: left of the value lowers it, right of the value raises it (hold to repeat) |
| Right click | B (back) |
| Wheel | Up / down in lists, left / right in lists that scroll sideways (car lists, Jump to Manufacturer) |
| Side buttons | LB / RB |
| Middle click | Right stick click |
| Help bar at the bottom | Click an entry ("Ⓧ Return to garage", "Ⓨ Stamp", …) to press that button |

On screens with nothing to point at (the title screen, videos, the wheelspin), a left click anywhere is A.

**Map:** drag to move the map, click a spot to select the icon there or set a waypoint, wheel to zoom.

**Garage and design editor:** drag on empty space to turn the camera, wheel to zoom. In *Design editor → Edit layer*, **W A S D** move the layer (and size, spin or skew it on those tabs).

**Photo mode:** left drag to turn the camera, **W A S D** to move it, **Q / E** down / up, wheel to zoom, right click to exit.

The cursor hides by itself a few seconds after you stop moving the mouse, and comes back when you move it.

**Keyboard**

| Key | While driving | In the menus |
|---|---|---|
| W / S | Gas / brake (and reverse) | |
| ← / → | Steer | Left / right |
| ↑ / ↓ | | Up / down (hold to repeat) |
| Space | Handbrake | |
| A / Z | Shift up / down (manual transmission) | |
| Left Alt | Clutch | |
| C | Change camera | |
| Right Ctrl | Look back | |
| R | Rewind | |
| M | Map | |
| P | Photo mode | |
| , / . | Previous / next radio station | |
| Left Ctrl | Nitro, with the [FnFNitro](https://github.com/qiangqiang101/NitroSystem) mod installed | |
| Esc | Pause | B (back) |
| Enter | Enter garage (and the HUD's other prompts) | A (select) |
| Page Up / Page Down | | Previous / next tab (LB / RB) |
| X / Y | | X / Y (what the help bar offers on them: "Return to garage", "Stamp", …) |
| Tab | | View ("Setup manager", "Jump to manufacturer", "Hide UI", "Save") |
| Z / C | | LT / RT ("Select / Unselect Layer") |
| F / V | | Left / right stick click ("Advanced camera") |

While you play with the keyboard, the help bar and the HUD's prompts show the keys instead of the controller's buttons: "Enter Select", "Esc Back", "PgUp" / "PgDn" for the tabs. Press a button on the controller and its buttons come back; press a key and the keys do. The pictures show the keys you've set, so they follow your changes. A button with no key (moving the sticks, or one you set to None) keeps the controller's picture.

The driving keys go straight to the game's own controls, not through a pretend controller, and only while you're driving, so a key can do one thing while driving and another in the menus. W in photo mode still moves the photo camera. The menu keys, Esc's pause and the radio keys hold the pad's own buttons for the game, so the menus take them exactly as they take a pad's. No controller needs to be plugged in: Enter on the title screen signs you in without one. If a controller goes (unplugged, or its batteries run out) the keyboard plays on: no "Controller disconnected" message and no pause. Plug a pad back in and the game asks for its A, as usual, to pair it again. Look left / right can have keys too. With FnFNitro installed, Left Ctrl presses its nitro button (whichever its `NitroButton` is) for it alone: the game doesn't see it, and no controller is needed.

Every key can be changed in the game, in **Pause > Settings > MODS**: each action has a "Key:" row, and left / right picks its key. The change takes effect at once. "Keyboard controls" there turns the keys off, and "Keyboard icons" keeps the controller's buttons in the help bar. The same keys are in the ini's `[Keyboard]` section, which takes any key and more than one per action.

## Installing

You need Azimuth and the FH2 Mod Platform, which every platform mod ships. Extract the release zip into your Azimuth folder (the one with `azimuth.exe`), so you end up with:

```
DWrite.dll                 the FH2 Mod Platform
fh2-mods\FH2Mouse.dll      this mod
```

The zip ships the platform as `DWrite.dll` only, since Azimuth 1.0.3 no longer loads `d3dcompiler_47.dll`. If you have a `d3dcompiler_47.dll` from an older mod, it can stay; it's simply not used.

> [!IMPORTANT]
> `FH2Mouse.dll` goes in the **`fh2-mods`** folder, the FH2 Mod Platform's. Don't put it in **`mods`**: that folder belongs to Extra Options and holds its plugins, and the mod won't load from there.

Start the game and move the mouse. The first launch creates `FH2Mouse\FH2Mouse.ini` next to `azimuth.exe`.

To remove it, delete `fh2-mods\FH2Mouse.dll` and the `FH2Mouse` folder.

## Settings

`FH2Mouse\FH2Mouse.ini` (read when the game starts):

| Setting | Default | Meaning |
|---|---|---|
| `Enabled` | `1` | `0` turns the mod off |
| `HoverSelects` | `1` | Moving over something selects it. With `0`, only clicks do |
| `HideAfterSeconds` | `3` | Hide the cursor after this long without moving the mouse (`0` = never) |
| `FrameRate` | `0` | The game's frame rate: `0` measures it (`platform.log` says what it found). Set it (`30`, `60`, `120`, `144`...) only if photo mode or the garage camera turns too fast or too slow |
| `Debug` | `0` | Log what's under the cursor and every click to `fh2-mods\platform.log` |

The `[Keyboard]` section (added to an older ini the first time this version starts) gives each action one or more keys, separated by spaces: `Gas=W Up`, `LookLeft=Q`, `Map=None`. Keys are letters, digits, `F1`-`F24`, `Num0`-`Num9` (with Num Lock on), `Left` `Right` `Up` `Down`, `Space`, `Enter`, `Escape`, `Tab`, `Backspace`, `Insert`, `Delete`, `Home`, `End`, `PageUp`, `PageDown`, `Shift`/`LShift`/`RShift`, `Ctrl`/`LCtrl`/`RCtrl`, `Alt`/`LAlt`/`RAlt`, `Comma`, `Period`, `Minus`, `Equals`, `Semicolon`, `Slash`, `Grave`, `LBracket`, `Backslash`, `RBracket`, `Quote`, or a virtual-key code (`0xNN`). The actions are `Gas`, `Brake`, `SteerLeft`, `SteerRight`, `Handbrake`, `ShiftUp`, `ShiftDown`, `Clutch`, `Camera`, `LookBack`, `LookLeft`, `LookRight`, `Rewind`, `Map`, `PhotoMode`, `RadioPrevious`, `RadioNext`, `Interact`, `Nitro` and `Pause` while driving, and `Accept`, `Back`, `Up`, `Down`, `Left`, `Right`, `PreviousTab`, `NextTab`, `ButtonX`, `ButtonY`, `ButtonView`, `ButtonLT`, `ButtonRT`, `ButtonLS` and `ButtonRS` in the menus. The MODS page offers the usual keys; one set in the ini that isn't among them shows there as it is. `Enabled=0` turns the keys off. `KeyIcons=0` keeps the controller's buttons in the help bar while you play with the keyboard.

The key pictures are built into `FH2Mouse.dll`: one PNG per key, named as the ini names keys (`Enter.png`, `Escape.png`, `PageUp.png`, `A.png`; `UpDown.png` and `LeftRight.png` for the d-pad's both-ways pictures). A key without one, like a key the ini sets that the MODS page doesn't offer, is drawn. To use a picture of your own, put a PNG with that name in `FH2Mouse\KeyIcons` (any size, with transparency); the game shows it from its next start, and deleting it brings back the built-in one. A picture can be up to four times as wide as it is high, like the built-in Enter, Space and Shift: the help bar makes room for it, and where a page only has a square for the button (the title screen's PRESS (A) TO START, the HUD's prompts, the tab strips' LB / RB) it's shrunk to fit the square. The game's copies are made from them each start, in `mediaoverride\UI\textures\data_bound\FH2MouseKeys`, so don't edit those.

The keys' rows need FH2 Mod Platform 2.8.0 or later (the one in the release zip); with an older one the keys work, set in the ini.

## Known limits

- **"Ⓨ Change time"** in the pause menu comes from the *Extra Options – Weather Control* plugin, which reads the controller directly, so clicking it does nothing. Give the plugin a keyboard key (`ChangeTimeKeyboard` in its `EO_WeatherControl.ini`) to change the time without a controller.
- The design editor's *Advanced camera* (right stick click) can't be held with the mouse.
- Only the 24 November 2015 build of the game that everyone plays is supported. On anything else the mod checks the game's code, finds it different, and stays off (it says so in `platform.log`).

## When something doesn't work

Look in `fh2-mods\platform.log` for the lines starting with `[FH2 Mouse & Keyboard]`. If something's wrong, set `Debug=1` in the ini, reproduce it, and attach the log to an issue, together with which screen you were on.

## How it works

The game's UI library still contains a mouse system, but the Xbox build never feeds it and its hit testing finds nothing. FH2Mouse finds the control under the cursor itself, from the menus' visual tree (including the 9° perspective tilt most menus are drawn with), moves the focus there, and sends the same key presses the controller sends. Pages then behave exactly as they would with a pad. The map, the garage and photo mode cameras, and the decal editor read their inputs through a few small hooks, all made through the platform. Every hook checks the game's code first and is skipped if it isn't as expected.

## Building

FH2Mouse builds with [llvm-mingw](https://github.com/mstorsjo/llvm-mingw/releases) and CMake, with the platform as a git submodule:

```bash
git clone --recursive https://github.com/qiangqiang101/FH2Mouse
cmake -S . -B build -G Ninja -DCMAKE_C_COMPILER=x86_64-w64-mingw32-clang -DCMAKE_CXX_COMPILER=x86_64-w64-mingw32-clang++ -DCMAKE_RC_COMPILER=x86_64-w64-mingw32-windres
cmake --build build
```

This gives `build/FH2Mouse.dll`, and the platform as `build/platform/DWrite.dll`. The key pictures are `keyicons/*.png`, embedded by `src/keyicons.rc` (add a line there for a new one). The art keys without one are drawn from is in `src/key_art.h`, made by `tools/make_key_art.py` from Forza Horizon 6's `KeyboardIcons.zip` (extracted); the build doesn't need it again. Releases are built by `.github/workflows/build.yml` when a release is published (or on demand from the Actions tab), which attaches `FH2Mouse-<tag>.zip` to the release. `tools/` holds the static-analysis and test scripts used while writing it (`fh2re.py` reads the game's exe; `drive.py` moves the mouse and takes screenshots).

## License

MIT, see [LICENSE](LICENSE).

## Disclaimer

Unofficial fan-made software. Not affiliated with, endorsed by, or connected to Playground Games, Turn 10 Studios, Xbox Game Studios, Microsoft, or the Azimuth developers. Use at your own risk.
