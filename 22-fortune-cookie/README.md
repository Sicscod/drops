# 22 · 🥠 Fortune Cookie

A glossy fortune cookie sitting on a dark plate, painted entirely with canvas gradients. Tap it: it wobbles, cracks in two with crumbs bouncing across the plate, and a paper slip unrolls with a fortune. Tap again for a fresh cookie. The first ones are cute and silly, but cookie Nº 3 is rigged: "your next date is with Delly." Put your name in the link and send it to your person. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/22-fortune-cookie/?name=Delly

https://github.com/Sicscod/drops/raw/main/22-fortune-cookie/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/22-fortune-cookie/?name=Delly&rig=3
```
- `name`: your name, it goes into the rigged fortune
- `fortunes`: your own fortunes, separated by `|`, e.g. `?fortunes=you%20are%20cute|text%20me%20back`
- `last`: the rigged fortune itself, `{name}` gets replaced, e.g. `?last=dinner%20is%20on%20{name}%20tonight.`
- `rig`: which cookie gets the rigged fortune (default 3)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: name, the fortune list, the rigged line, which cookie is rigged
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
