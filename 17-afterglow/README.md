# 17 · 🎟️ Afterglow

A full landing page for a one-night festival or event, in one file: a huge poster-style hero with a striped sunset glow drawn on canvas, a live countdown, a scrolling ticker, a typographic lineup poster, a timetable with stage tabs, ticket tiers with a quantity stepper and a "Get tickets" confirmation that prints your ticket with a QR-style code, an FAQ accordion, a venue block with an animated map and a footer. Scroll reveals and every animation run from one loop. One HTML file, no libraries.

**Live demo:** https://sicscod.github.io/drops/17-afterglow/

https://github.com/Sicscod/drops/raw/main/17-afterglow/demo.mp4

## Change it without coding
```
https://sicscod.github.io/drops/17-afterglow/?name=Night%20Shift&date=2026-12-31T21:00&city=Berlin&hue=340
```
- `name`: the event name (split over two lines in the hero, a space picks where it breaks)
- `date`: doors open, ISO date and time, drives the countdown (if it's in the past, a demo timer runs)
- `city`: the city in the hero, ticket and footer
- `hue`: the sun colour, e.g. `18` orange, `0` red, `340` pink, `190` teal

## Make it yours
1. Open [`index.html`](index.html) → **Download raw file** (it's the whole project, one file)
2. Edit the `CONFIG` block: lineup tiers, stages and set times, ticket prices, FAQ, venue
3. Publish for free: **Settings → Pages → main** (or drop the folder on Vercel)

---
More free code every day → **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)** on Instagram & TikTok

← [All drops](https://sicscod.github.io/drops/)
