# 50 · 🔋 Love Charger

A tired little battery for your person. It opens at 1%: blinking red, heavy eyelids, a sweat drop, a "Low battery" toast, and it keeps nodding off and jerking awake while "monday", "3 meetings" and "group chat · 247 unread" pop up and drain it even more. Drag the heart-shaped plug that says "Delly" into its port (or just tap the heart). It clicks in, the bolt turns into a heart, and the battery fills with bubbly pink liquid from 1% to 100% while its face goes from shocked to blushing to sparkly-eyed and tiny hearts fizz out of the top. At 100% it reads "100% · fully charged by Delly ♥" and does a happy little hop. Tap the battery to make it hop again, or tap the plug to unplug it and start over. One HTML file, no libraries, everything is drawn on a canvas (no images).

**Live demo:** https://sicscod.github.io/drops/50-love-charger/?name=Delly

https://github.com/Sicscod/drops/raw/main/50-love-charger/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/50-love-charger/?name=Delly&msg=100%25%20%C2%B7%20fully%20charged%20by%20Delly%20%E2%99%A5&hue=340
```
- `name`: the name on the heart plug (it also shows up in "connected to …" and the last line)
- `msg`: the line at 100% (default "100% · fully charged by {name} ♥")
- `hue`: the colour of the liquid, the plug and the hearts, 0–360 (e.g. `?hue=0` red, `?hue=280` purple, `?hue=200` blue)
- `auto=1`: a cursor plays the whole thing by itself (good for screen recordings)

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: the drain messages (text, how much they cost, when they pop), every line of text (the low-battery toast, "charging", the tag under the counter, battery health), how long the charge takes, sound
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
