# 48 · 🤖 Love Captcha

A verification check for your person. Tick "I'm not a robot" and the challenge drops open: "Select all squares with the person you love". The grid has a cat, a pizza, a laptop, a coffee, a bed, a phone, a dog, "my ex" (with a tiny skull) and one drawn portrait of Delly. Pick Delly and hit verify. It isn't enough: "please also select…" and the grid flips over, so now all nine squares are Delly in different poses (wink, heart sunglasses, laughing, a bow, heart eyes, a crown…). Tap all nine, and every tap pops a heart. Verify again and the checkbox flies into the card and turns into a beating heart: "verified: definitely not a robot. just in love with Delly ♥", with confetti hearts. One HTML file, no libraries, everything drawn on a canvas (no images).

**Live demo:** https://sicscod.github.io/drops/48-love-captcha/?name=Delly

https://github.com/Sicscod/drops/raw/main/48-love-captcha/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/48-love-captcha/?name=Delly&msg=just%20in%20love%20with%20Delly%20%E2%99%A5&hue=345
```
- `name`: whose face fills the squares (it also shows up in the tile labels and the last line)
- `msg`: the last line on the "verified" card (default "just in love with {name} ♥")
- `hue`: the colour of the header, the hearts and the button, 0–360 (e.g. `?hue=0` red, `?hue=280` purple, `?hue=200` blue)
- `auto=1`: a cursor plays the whole thing by itself (good for screen recordings)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the nine round-one tiles (label, emoji, colour), the poses in round two, every line of text (the question, "please also select", the wrong-answer lines, the final score line), the heartbeat speed, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
