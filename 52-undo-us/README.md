# 52 · 💔 Ctrl+Z Us

A fight, saved as `us.txt`. The file opens already wrecked: the sweet line `i love you · we're okay` is struck through in red, and under it the argument piles up — `you never listen`, `whatever`, `fine.` — glitching, the title flashing "unsaved changes ●", a little broken heart cracked open in the corner. Then a cursor starts hammering **Ctrl+Z**. Each press rewinds one step with a reverse-swell whoosh: an angry line un-types itself character by character and collapses away, the mood heart heals one notch, and the music un-glitches a little more. The last undo brings the sweet line back from the dead — the red strike retracts, the words glow, a caret blinks, the broken heart snaps shut in a burst of confetti and the title finally reads "saved ✓ · Delly ♥" while hearts float up. One HTML file, no libraries, everything drawn on a canvas (no images).

**Live demo:** https://sicscod.github.io/drops/52-undo-us/?name=Delly

https://github.com/Sicscod/drops/raw/main/52-undo-us/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/52-undo-us/?name=Delly&msg=i%20love%20you%20%C2%B7%20we're%20okay&hue=340
```
- `name`: the name shown once it's saved ("saved ✓ · {name} ♥")
- `msg`: the sweet line that gets restored (default "i love you · we're okay")
- `hue`: the colour of the hearts and the glow, 0–360 (e.g. `?hue=0` red, `?hue=275` purple, `?hue=200` blue)
- `auto=1`: a cursor plays the whole thing by itself (good for screen recordings)

Tap the **Ctrl+Z** keys (or press Ctrl+Z on your keyboard) to rewind the fight one line at a time.

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the angry lines of the fight, the sweet line it restores, the file name, the unsaved/saved titles, the hint, the colour, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
