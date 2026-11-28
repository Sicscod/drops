# 55 · 📦 npm install

`node_modules`, but it's a cardboard box with feelings. Run `npm install` and packages start flying in from both sides (`left-pad`, `is-odd`, `is-even`, `lodash`…), the box gulps every one, bulges, sweats, cracks the floor, and the size counter climbs from a few KB to **4.7 GB · heavier than the sun**. The terminal says "added 1,337 packages, found 0 vulnerabilities" and then, quietly, "(87 high severity)". Hit **rm -rf node_modules** and the box deflates like a balloon, flying around the room spraying confetti until it lands back at 12 KB: "much better." Then you run `npm install` again, obviously. One HTML file, no libraries, everything drawn on a canvas (no images).

**Live demo:** https://sicscod.github.io/drops/55-npm-install/

https://github.com/Sicscod/drops/raw/main/55-npm-install/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/55-npm-install/?project=my-app&size=4.7&hue=30
```
- `project`: the folder name in the terminal prompt
- `size`: how big node_modules gets, in GB (default 4.7)
- `hue`: the colour of the box, 0–360 (e.g. `?hue=200` blue, `?hue=330` pink)
- `auto=1`: a cursor plays the whole thing by itself (good for screen recordings)

Tap the button (or press Enter) to `rm -rf` it, and again to install it all back.

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the package names that fly in, the package count, the install time, all the terminal lines, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
