# 46 · 📶 Heart Wi-Fi

A Wi-Fi list for your person. It's already scanning when it opens and the networks around you are not helping: "FBI van #4", "no free wifi", "your wifi is slow lol", "my ex's hotspot (weak)" flickering down to zero bars. One network glows pink with a lock: Delly ♥. Tap it and it asks for the password. password123? The field shakes: "wrong. try what you feel." Type ♥ instead and it's accepted, the other networks fall off the screen, the Wi-Fi bars bend into a heart that fills up to 100% and the final card says "connected to Delly ♥ · signal: 100% · strong forever" while tiny hearts float up. One HTML file, no libraries, all drawn on a canvas.

**Live demo:** https://sicscod.github.io/drops/46-heart-wifi/?name=Delly

https://github.com/Sicscod/drops/raw/main/46-heart-wifi/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/46-heart-wifi/?name=Delly&pass=%E2%99%A5&msg=auto-join%3A%20on.%20forever.&hue=340
```
- `name`: whose Wi-Fi glows pink
- `pass`: the secret password, shown as the hint (default ♥; "you" and "<3" also work)
- `msg`: the last line on the "connected" card
- `hue`: the colour of the glow and the heart, 0–360 (e.g. `?hue=0` red, `?hue=280` purple, `?hue=200` blue)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the network list (names, bars, when they show up), the suggestion chips, the wrong-password lines, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
