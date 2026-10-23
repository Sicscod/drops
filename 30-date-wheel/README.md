# 30 · 🎡 Date Wheel

A retro game-show prize wheel that settles the weekend: "what are we doing this weekend, Delly?" Sushi, movie night, arcade, sunset walk, karaoke, stay in. Drag or flick it and it spins with real physics: momentum, friction, and a red flap that clicks and bounces off every brass peg, slowing the wheel until it rocks to a stop. It lands, the banner says "SUSHI!", and then the wheel quietly creeps over one more peg. Every slice flips to "all of them", the hub says "with me", confetti cannons go off and you get an admit-two ticket stamped "100% rigged". Put her name and your plans in the link and send it to your person. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/30-date-wheel/?name=Delly

https://github.com/Sicscod/drops/raw/main/30-date-wheel/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/30-date-wheel/?name=Delly&options=sushi|movie%20night|arcade|sunset%20walk|karaoke|stay%20in&final=all%20of%20them,%20with%20me
```
- `name`: who the wheel is asking
- `options`: the slices, separated by `|` (or commas), e.g. `?options=tacos|bowling|museum|picnic`
- `final`: where it really lands. The part before the comma goes on every slice, the part after goes in the middle, e.g. `?final=everything,%20together`
- `when`: the small line on the ticket, e.g. `?when=valid%20saturday`

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: name, slices, the rigged answer, slice colours, friction, how hard you can flick it and how long it pretends the result is real
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
