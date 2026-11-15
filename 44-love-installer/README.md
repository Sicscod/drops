# 44 · 💾 love.exe

A retro installer that installs love for your person. The progress bar races through a very honest install log ("copying butterflies…", "deleting ex.dll…" flying straight into the recycle bin, "overthinking.sys removed"), then gets stuck at 99% with an error: missing file you.png. Drag the little you.png icon from the desktop into the window (or just tap it), the bar hits 100%, the whole window shatters into pixels that rebuild themselves into a beating pink heart, hearts burst out and "love.exe installed for Delly" pops up with a Run button. Press it. One HTML file, no libraries, all drawn on a canvas.

**Live demo:** https://sicscod.github.io/drops/44-love-installer/?name=Delly

https://github.com/Sicscod/drops/raw/main/44-love-installer/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/44-love-installer/?name=Delly&msg=no%20uninstaller%20included.&hue=340
```
- `name`: who love gets installed for
- `msg`: the little notification balloon after pressing Run
- `hue`: the colour of the heart and title bars, 0–360 (e.g. `?hue=0` red, `?hue=280` purple, `?hue=200` blue)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the install log lines, the missing file name, how fast the bar races, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
