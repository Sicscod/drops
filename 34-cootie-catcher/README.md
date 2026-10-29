# 34 · 📝 Cootie Catcher

The paper fortune teller from school, sitting on a wooden desk in soft window light: real folds and creases, coloured-pencil scribbles, colour names and numbers, a little star and heart doodle, and a shadow that moves with it. Tap a colour and it spells it out, snapping open and shut in alternating directions in 3D with a paper flick on every fold. Pick a number and the flap lifts up, the fortune is written under it, and a pen writes it out on the notebook page. The first two are cute ("you'll get boba today"). The third one is rigged: "you're going on a date with me, Delly ♥". Change the name in the link and send it to your person. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/34-cootie-catcher/?name=Delly

https://github.com/Sicscod/drops/raw/main/34-cootie-catcher/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/34-cootie-catcher/?name=Delly&fortunes=you'll%20get%20boba%20today|someone%20can't%20stop%20thinking%20about%20you&last=you're%20going%20on%20a%20date%20with%20me%2C%20%7Bname%7D%20%E2%99%A5
```
- `name`: who the rigged fortune is about (it fills `{name}` in `last`)
- `fortunes`: the honest fortunes, separated by `|`
- `last`: the rigged fortune; a `♥` is drawn as a red pen heart
- `rig`: which round gets the rigged fortune, e.g. `?rig=2` (default 3)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: name, fortunes, the rigged line, which round is rigged, the four colours and their names, paper colour, pen inks, how fast it snaps, camera tilt, sound on/off
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
