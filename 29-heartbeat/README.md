# 29 · ❤️ Heartbeat

A heart monitor for your person: a glowing ECG trace with phosphor afterglow sweeps across a dark screen at 72 bpm, "thinking about Delly". Press and hold (or drag your finger) and the pulse races past 140, the trace goes wild and the whole screen starts to glow red. Then the line flatlines for a beat and redraws itself as her name in one continuous cursive heartbeat stroke, ending in a heart-shaped beat, and "you do this to me" fades in underneath. Real monitor beeps that speed up with the pulse. Change the name in the link and send it to your person. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/29-heartbeat/?name=Delly

https://github.com/Sicscod/drops/raw/main/29-heartbeat/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/29-heartbeat/?name=Delly&msg=you%20do%20this%20to%20me&hue=150
```
- `name`: the name the heartbeat writes (and "thinking about …" on the monitor)
- `msg`: the line under the name, e.g. `?msg=only%20you`
- `hue`: colour of the calm trace (0-360), e.g. `?hue=190` for a cyan monitor; it always turns red when the heart races

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Open `index.html` and edit the `CONFIG` block: name, message, colours, resting and peak BPM, how long to hold, how fast the name is written, the script font, beeps on/off
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
