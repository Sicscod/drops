# 15 · 🌊 Ripples

A dark, glossy water surface over a glowing neon word. Drag your finger and real ripples spread out, bend the light and catch highlights; tap to drop a droplet and watch the rings bounce off the pool walls. It's a real 2D wave simulation on a small grid, drawn with one WebGL shader, so it stays smooth on phones. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/15-ripples/

https://github.com/Sicscod/drops/raw/main/15-ripples/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/15-ripples/?text=hi%20Delly&hue=330
```
- `text`: the neon word under the water (it wraps and fits itself)
- `hue`: a fixed colour from 0 to 360 (e.g. `190` aqua, `330` pink, `45` gold), or `cycle` (default) to drift slowly through colours
- `floor`: the small print on the pool floor, empty `?floor=` hides it
- `hint`: the hint at the bottom

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: text, colour, damping (how long rings last), refraction, gloss, droplet size
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
