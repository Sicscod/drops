#!/usr/bin/env python3
"""
Beating heart made of a name — right in your terminal.
Usage:  python3 heart.py Delly
        python3 heart.py            (asks for a name)
Stop:   Ctrl + C

Free code by @sicscod.drops  (Instagram / TikTok)
No libraries needed. Works on macOS, Linux and Windows 10+.
"""
import math
import os
import random
import shutil
import sys
import time

# ---------- settings you can change ----------
MESSAGE = "I love you, {name}"   # line under the heart
BPM = 72                          # heartbeat speed
TOP = (255, 45, 95)               # color at the top of the heart
BOTTOM = (255, 140, 190)          # color at the bottom
# ---------------------------------------------

ESC = "\x1b["
HIDE, SHOW, HOME, CLEAR, RESET = ESC + "?25l", ESC + "?25h", ESC + "H", ESC + "2J", ESC + "0m"


def rgb(c):
    return f"{ESC}38;2;{c[0]};{c[1]};{c[2]}m"


def mix(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def beat(t):
    """Scale of the heart over time: a 'lub-dub' double pulse."""
    p = (t * BPM / 60.0) % 1.0
    return 1.0 + 0.10 * math.exp(-((p - 0.08) ** 2) / 0.0025) + 0.06 * math.exp(-((p - 0.28) ** 2) / 0.0025)


def inside(x, y):
    """Classic heart curve: (x² + y² − 1)³ − x²·y³ ≤ 0"""
    a = x * x + y * y - 1
    return a * a * a - x * x * y * y * y <= 0


def type_out(text, color=(255, 255, 255), delay=0.06):
    for ch in text:
        sys.stdout.write(rgb(color) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def frame(name, t, cols, rows, sparkles):
    h = max(12, min(rows - 5, 34))
    w = min(cols - 2, h * 2 + 10)
    s = beat(t)
    shift = int(t * 8)
    out = []
    pad = " " * max(0, (cols - w) // 2)
    for r in range(h):
        y = (1.38 - r * 2.74 / h) / s
        line = [pad]
        for c in range(w):
            x = ((c - w / 2) / (w / 2)) * 1.45 / s
            if inside(x, y):
                ch = name[(c - shift + r) % len(name)]
                glow = 0.25 * math.sin(t * 6 + c * 0.3 + r * 0.2)
                col = mix(TOP, BOTTOM, r / h + glow)
                line.append(rgb(col) + ch)
            elif (r, c) in sparkles:
                twinkle = mix((120, 40, 70), (255, 220, 235), (math.sin(t * 5 + r + c) + 1) / 2)
                line.append(rgb(twinkle) + sparkles[(r, c)])
            else:
                line.append(" ")
        out.append("".join(line) + RESET)
    return out, w, h


def main():
    if os.name == "nt":
        os.system("")  # enables colors on Windows terminals
    name = " ".join(sys.argv[1:]).strip()
    if not name:
        name = input("Who is this heart for? ").strip() or "you"
    letters = name.replace(" ", "") or "love"

    sys.stdout.write(CLEAR + HOME)
    type_out(f"compiling feelings for {name}...", (160, 160, 180), 0.04)
    time.sleep(0.4)
    type_out("done. ", (120, 220, 150), 0.04)
    time.sleep(0.6)

    message = MESSAGE.format(name=name) + " ❤"
    start = time.time()
    sparkles = {}
    sys.stdout.write(HIDE + CLEAR)
    try:
        while True:
            t = time.time() - start
            cols, rows = shutil.get_terminal_size((80, 30))
            # sparkles appear and fade around the heart
            if random.random() < 0.6:
                sparkles[(random.randrange(0, 34), random.randrange(0, 90))] = random.choice("·✦*+.")
            if len(sparkles) > 40:
                sparkles.pop(next(iter(sparkles)))
            lines, w, h = frame(letters, t, cols, rows, sparkles)
            shown = message[: int(max(0, t - 1.2) * 14)]  # types itself after a moment
            caption = " " * max(0, (cols - len(message)) // 2) + rgb((255, 255, 255)) + shown + RESET
            sys.stdout.write(HOME + "\n" + "\n".join(lines) + "\n\n" + caption + ESC + "K\n")
            sys.stdout.flush()
            time.sleep(1 / 30)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(RESET + SHOW + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
