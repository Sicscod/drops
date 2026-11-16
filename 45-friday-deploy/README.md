# 45 · 🔥 Friday Deploy

A big glossy "Deploy to prod" button, and the clock in the corner says Fri 16:59. Move the cursor near it and it panics: it sweats, wobbles and dodges you once. Click it anyway and the confirm dialogs start stacking up ("are you sure?", "it's friday.", "your weekend will remember this", "ok but don't say we didn't warn you"). Say yes four times and the deploy starts: the progress bar crawls, a tiny pixel server rack starts smoking, the logs go red, cartoon flames dance on the log panel and the coffee mug sweats. Then at 99% everything stops, and it actually passes. "✓ deployed. 0 errors." Everything freezes, the clock flips to 17:00, the button puts on a tiny party hat, one confetti pop, and the mug asks "...wait, it worked?". One HTML file, no libraries, all drawn on a canvas.

**Live demo:** https://sicscod.github.io/drops/45-friday-deploy/

https://github.com/Sicscod/drops/raw/main/45-friday-deploy/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/45-friday-deploy/?day=fri&time=16:59&hue=152
```
- `day`: the day on the clock, e.g. `?day=mon` (it also shows up in the second dialog)
- `time`: the time on the clock, e.g. `?time=23:59` (it flips one minute forward when the deploy passes)
- `hue`: the button colour, 0–360, e.g. `?hue=0` for red or `?hue=210` for blue
- `auto=1`: a cursor plays the whole thing by itself (good for screen recordings)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the button label, the project name, the confirm dialogs (title, text, yes/no buttons, icon), the deploy log lines and when they appear, how long the deploy takes, the final lines, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
