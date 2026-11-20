# 49 · 🥊 Merge Conflict

Your merge stops with a conflict, and the two versions of the line are not taking it quietly. HEAD is a blue blob, feature is an orange blob, each wearing its line of code as a sumo belt, and they shove each other around a ring drawn by the `=======` marker while "ROUND 1" flashes and the code around them shakes. Hover Accept Current and the blue one gets smug while the orange one bawls; hover Accept Incoming and they swap. Click Accept Both: they stop, look at each other, hug and squish into one purple blob, its belt flies into the code as a single clean line, the conflict markers fall off the screen, "✓ merged · tests passing", confetti, thumbs up. One HTML file, no libraries, all drawn on a canvas.

**Live demo:** https://sicscod.github.io/drops/49-merge-conflict/

https://github.com/Sicscod/drops/raw/main/49-merge-conflict/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/49-merge-conflict/?a=140&b=330
```
- `a`: the HEAD blob's colour, 0–360, e.g. `?a=140` for a green one (default 212, blue)
- `b`: the incoming blob's colour, e.g. `?b=330` for pink (default 26, orange)
- `m`: the merged blob's colour (by default it's halfway between the two)
- `auto=1`: a cursor plays the whole fight by itself (good for screen recordings)

Tap a blob to make it shove. Tap Accept Current or Accept Incoming and the winner throws the other one out of the ring.

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the code around the conflict, the two fighting lines and the merged one, the branch names, the button labels, "ROUND 1", every quip, the success text, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
