# 01 · ✨ Particle Portfolio

A one-file portfolio where **your name is made of particles** that scatter when you move your cursor (or touch the screen on mobile).

**Live demo:** https://sicscod.github.io/drops/01-particle-portfolio/

## Features
- 🎇 Interactive particle name: mouse and touch
- 📱 Fully responsive, works great on phones
- ⚡ One `index.html`, no build step, no frameworks
- 🎨 Change colors in one place (`:root` in the CSS)
- ♿ Respects "reduce motion", keyboard friendly

## Make it yours (2 minutes)
1. Click **Use this template** (or download the ZIP).
2. Open `index.html` and edit the `CONFIG` block at the bottom:
   ```js
   const CONFIG = {
     name: "Your Name",
     role: 'Designer who makes <em>things people love.</em>',
     email: "you@mail.com",
     projects: [ { title: "...", text: "...", tags: ["JS"], url: "https://..." } ],
     ...
   };
   ```
3. Want other colors? Change `--accent` and `--accent-2` at the top of the `<style>`, and `particles.colors` in `CONFIG`.

## Publish for free
**GitHub Pages:** repo → Settings → Pages → Branch: `main` → Save. Your site will be live at `https://YOUR-USERNAME.github.io/REPO-NAME/`.

**Vercel / Netlify:** import the repo, then hit Deploy. No settings needed.

## More free sites
New templates every week on Instagram & TikTok: **[@sicscod.drops](https://www.instagram.com/sicscod.drops/)**

## License
MIT: use it for anything, credit appreciated ⭐

← [All drops](https://sicscod.github.io/drops/)
