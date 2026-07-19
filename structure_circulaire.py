#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
structure_circulaire : animatique en boucle pour oscilloscope. Morph :
cercle calme -> eclair -> Lissajous -> spirale -> cercle. La boucle est
fermee (circulaire). Blanc sur noir, et c'est un vrai signal (le WAV le
dessine).
Sortie : samples/structure_circulaire.gif / .mp4 / .wav
"""
import os, math, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SR = 96000
N = 1600
W = 720
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")


def resample(P, n):
    P = np.asarray(P, float)
    d = np.sqrt((np.diff(P, axis=0) ** 2).sum(1)); u = np.concatenate([[0], np.cumsum(d)])
    uu = np.linspace(0, u[-1], n)
    return np.interp(uu, u, P[:, 0]), np.interp(uu, u, P[:, 1])


def norm(x, y):
    x = x - (x.max() + x.min()) / 2; y = y - (y.max() + y.min()) / 2
    m = max(np.abs(x).max(), np.abs(y).max()) or 1.0
    return x / m * 0.9, y / m * 0.9


def shape(name):
    t = np.linspace(0, 2 * math.pi, N, endpoint=False)
    if name == "circle":
        return norm(np.cos(t), np.sin(t))
    if name == "lissajous":
        return norm(np.sin(3 * t + math.pi / 2), np.sin(2 * t))
    if name == "spiral":
        r = np.linspace(0.05, 1.0, N)
        a = t * 4
        return norm(r * np.cos(a), r * np.sin(a))
    if name == "eclair":
        seg = [(0,1),(-.25,.35),(.12,.30),(-.18,-.25),(.20,-.30),(-.05,-1),
               (.05,-1),(-.15,-.25),(.22,-.20),(-.10,.32),(.28,.38),(.04,1)]
        x, y = resample(seg, N); return norm(x, y)


def render(x, y, size=W):
    sc = size * 0.42; c = size / 2.0
    pts = list(zip((c + x * sc).tolist(), (c - y * sc).tolist()))
    core = Image.new("L", (size, size), 0)
    ImageDraw.Draw(core).line(pts, fill=255, width=2, joint="curve")
    acc = np.asarray(core, np.float32).copy()
    for r, w in ((2, .7), (7, .5), (18, .35)):
        acc += np.asarray(core.filter(ImageFilter.GaussianBlur(r)), np.float32) * w
    acc = np.clip(acc / acc.max() * 1.7, 0, 1)
    return Image.fromarray((np.dstack([acc, acc, acc]) * 255).astype(np.uint8), "RGB")


def main():
    keys = ["circle", "eclair", "lissajous", "spiral", "circle"]
    S = [shape(k) for k in keys]
    framedir = os.path.join(OUT, "_struct_frames"); os.makedirs(framedir, exist_ok=True)
    PER, HOLD = 34, 10
    allx, ally = [], []
    idx = 0
    for i in range(len(S) - 1):
        ax, ay = S[i]; bx, by = S[i + 1]
        for h in range(HOLD):
            allx.append(ax); ally.append(ay)
            render(ax, ay).save(os.path.join(framedir, "f%04d.png" % idx)); idx += 1
        for f in range(PER):
            k = 0.5 - 0.5 * math.cos(math.pi * f / PER)
            mx, my = ax * (1 - k) + bx * k, ay * (1 - k) + by * k
            allx.append(mx); ally.append(my)
            render(mx, my).save(os.path.join(framedir, "f%04d.png" % idx)); idx += 1
    X = np.concatenate(allx); Y = np.concatenate(ally)
    inter = np.empty(X.size * 2, dtype=np.float32); inter[0::2] = X; inter[1::2] = Y
    pcm = (np.clip(inter, -1, 1) * 32767).astype("<i2")
    with wave.open(os.path.join(OUT, "structure_circulaire.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    gif = os.path.join(OUT, "structure_circulaire.gif")
    subprocess.run(["ffmpeg", "-y", "-framerate", "25", "-i", os.path.join(framedir, "f%04d.png"),
                    "-vf", "scale=460:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse",
                    "-loop", "0", gif], capture_output=True)
    mp4 = os.path.join(OUT, "structure_circulaire.mp4")
    subprocess.run(["ffmpeg", "-y", "-framerate", "25", "-i", os.path.join(framedir, "f%04d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", mp4], capture_output=True)
    print("structure OK | frames=%d | gif+mp4+wav" % idx)


if __name__ == "__main__":
    main()
