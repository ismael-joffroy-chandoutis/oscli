#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
oscli : oscilloscope CLI headless.

osci-render n'a pas de mode ligne de commande : oscli comble ce manque.
Il convertit un vecteur (SVG, OBJ, ou forme integree) en WAV stereo XY
(gauche = X, droite = Y), rejouable dans un vrai oscilloscope, et en rend
un apercu PNG (glow phosphore). Entierement scriptable et automatisable
(Blender -> SVG/OBJ -> oscli -> WAV -> chaine).

Exemples :
  python3 oscli.py --input forme.svg --out-wav f.wav --out-png f.png
  python3 oscli.py --input builtin:lissajous --out-wav l.wav --out-png l.png
  python3 oscli.py --input modele.obj --out-wav o.wav --out-png o.png --freq 80

Dependances : numpy, Pillow, ffmpeg (uniquement pour --out-mp4).
Limites SVG : commandes M L H V C Q Z (+ relatives), polyline, polygon.
S, T, A ignorees (best effort). Pas un parseur SVG complet, mais reel et teste.
"""
import argparse, os, re, math, wave, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

NUM = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?')


# ---------- flattening des courbes de Bezier ----------
def flatten_cubic(p0, p1, p2, p3, n=24):
    t = np.linspace(0, 1, n); mt = 1 - t
    x = (mt**3)*p0[0] + 3*(mt**2)*t*p1[0] + 3*mt*(t**2)*p2[0] + (t**3)*p3[0]
    y = (mt**3)*p0[1] + 3*(mt**2)*t*p1[1] + 3*mt*(t**2)*p2[1] + (t**3)*p3[1]
    return list(zip(x, y))


def flatten_quad(p0, p1, p2, n=18):
    t = np.linspace(0, 1, n); mt = 1 - t
    x = (mt**2)*p0[0] + 2*mt*t*p1[0] + (t**2)*p2[0]
    y = (mt**2)*p0[1] + 2*mt*t*p1[1] + (t**2)*p2[1]
    return list(zip(x, y))


# ---------- parseurs ----------
def parse_svg_path(d):
    pts = []; cur = (0.0, 0.0); start = (0.0, 0.0)
    for cmd, argstr in re.findall(r'([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)', d):
        a = [float(v) for v in NUM.findall(argstr)]
        rel = cmd.islower(); C = cmd.upper()
        if C == 'M':
            for k in range(0, len(a) - 1, 2):
                x, y = a[k], a[k+1]
                if rel: x += cur[0]; y += cur[1]
                cur = (x, y)
                if k == 0: start = cur
                pts.append(cur)
        elif C == 'L':
            for k in range(0, len(a) - 1, 2):
                x, y = a[k], a[k+1]
                if rel: x += cur[0]; y += cur[1]
                cur = (x, y); pts.append(cur)
        elif C == 'H':
            for x in a:
                if rel: x += cur[0]
                cur = (x, cur[1]); pts.append(cur)
        elif C == 'V':
            for y in a:
                if rel: y += cur[1]
                cur = (cur[0], y); pts.append(cur)
        elif C == 'C':
            for k in range(0, len(a) - 5, 6):
                c1 = (a[k], a[k+1]); c2 = (a[k+2], a[k+3]); e = (a[k+4], a[k+5])
                if rel:
                    c1 = (c1[0]+cur[0], c1[1]+cur[1]); c2 = (c2[0]+cur[0], c2[1]+cur[1]); e = (e[0]+cur[0], e[1]+cur[1])
                pts += flatten_cubic(cur, c1, c2, e)[1:]; cur = e
        elif C == 'Q':
            for k in range(0, len(a) - 3, 4):
                c = (a[k], a[k+1]); e = (a[k+2], a[k+3])
                if rel:
                    c = (c[0]+cur[0], c[1]+cur[1]); e = (e[0]+cur[0], e[1]+cur[1])
                pts += flatten_quad(cur, c, e)[1:]; cur = e
        elif C == 'Z':
            pts.append(start); cur = start
        # S, T, A non gerees (best effort)
    return pts


def load_svg(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    pts = []
    for d in re.findall(r'<path[^>]*\sd="([^"]*)"', txt):
        pts += parse_svg_path(d)
    for pl in re.findall(r'<(?:polyline|polygon)[^>]*\spoints="([^"]*)"', txt):
        nums = [float(v) for v in NUM.findall(pl)]
        pts += [(nums[i], nums[i+1]) for i in range(0, len(nums) - 1, 2)]
    return pts


def load_obj(path):
    V = []; L = []
    for line in open(path, encoding="utf-8", errors="replace"):
        if line.startswith('v '):
            p = line.split(); V.append((float(p[1]), float(p[2])))
        elif line.startswith('l '):
            L.append([int(i.split('/')[0]) for i in line.split()[1:]])
    if not V:
        return []
    if L:
        pts = []
        for poly in L:
            for i in poly:
                pts.append(V[i - 1])
        return pts
    return V


def builtin(name):
    t = np.linspace(0, 2*math.pi, 2048, endpoint=False)
    if name == "circle":
        return list(zip(np.cos(t), np.sin(t)))
    if name == "lissajous":
        return list(zip(np.sin(3*t + math.pi/2), np.sin(2*t)))
    if name == "eclair":
        seg = np.array([[0,1],[-.25,.35],[.12,.30],[-.18,-.25],[.20,-.30],[-.05,-1],
                        [.05,-1],[-.15,-.25],[.22,-.20],[-.10,.32],[.28,.38],[.04,1]])
        d = np.sqrt((np.diff(seg, axis=0)**2).sum(1)); u = np.concatenate([[0], np.cumsum(d)])
        uu = np.linspace(0, u[-1], 2048)
        return list(zip(np.interp(uu, u, seg[:,0]), np.interp(uu, u, seg[:,1])))
    raise SystemExit("forme integree inconnue: " + name)


# ---------- traitement ----------
def resample(pts, n):
    P = np.array(pts, dtype=float)
    if len(P) < 2:
        raise SystemExit("trace insuffisant (moins de 2 points)")
    d = np.sqrt((np.diff(P, axis=0)**2).sum(1)); u = np.concatenate([[0], np.cumsum(d)])
    if u[-1] == 0:
        raise SystemExit("trace degenere")
    uu = np.linspace(0, u[-1], n)
    return np.interp(uu, u, P[:,0]), np.interp(uu, u, P[:,1])


def normalize(x, y, flip_y=False):
    if flip_y: y = -y
    x = x - (x.max() + x.min())/2; y = y - (y.max() + y.min())/2
    m = max(np.abs(x).max(), np.abs(y).max()) or 1.0
    return x/m*0.95, y/m*0.95


def write_wav(path, X, Y, sr):
    inter = np.empty(X.size*2, dtype=np.float32)
    inter[0::2] = np.clip(X, -1, 1); inter[1::2] = np.clip(Y, -1, 1)
    pcm = (inter*32767.0).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


def render_xy(x, y, size=1080, width=2):
    sc = size*0.40; c = size/2.0
    pts = list(zip((c + x*sc).tolist(), (c - y*sc).tolist()))
    core = Image.new("L", (size, size), 0)
    ImageDraw.Draw(core).line(pts, fill=255, width=width, joint="curve")
    acc = np.asarray(core, dtype=np.float32).copy()
    for r, w in ((3, .7), (9, .5), (24, .35)):
        acc += np.asarray(core.filter(ImageFilter.GaussianBlur(r)), dtype=np.float32)*w
    acc = np.clip(acc/acc.max()*1.6, 0, 1)
    R = np.clip(acc*0.25 + acc**4*0.9, 0, 1)
    G = np.clip(acc*1.00, 0, 1)
    B = np.clip(acc*0.30 + acc**4*0.8, 0, 1)
    return Image.fromarray((np.dstack([R, G, B])*255).astype(np.uint8), "RGB")


def main():
    ap = argparse.ArgumentParser(description="oscilloscope CLI : vecteur -> WAV XY + PNG")
    ap.add_argument("--input", required=True, help="fichier .svg | .obj | builtin:circle|lissajous|eclair")
    ap.add_argument("--out-wav"); ap.add_argument("--out-png"); ap.add_argument("--out-mp4")
    ap.add_argument("--sr", type=int, default=96000, help="taux d'echantillonnage (defaut 96000)")
    ap.add_argument("--freq", type=float, default=50.0, help="frequence de la boucle en Hz (defaut 50)")
    ap.add_argument("--dur", type=float, default=2.0, help="duree du WAV en secondes")
    ap.add_argument("--size", type=int, default=1080)
    ap.add_argument("--no-flip-y", action="store_true", help="ne pas inverser Y (SVG est Y vers le bas)")
    a = ap.parse_args()

    inp = a.input
    if inp.startswith("builtin:"):
        pts = builtin(inp.split(":", 1)[1]); flip = False
    elif inp.lower().endswith(".svg"):
        pts = load_svg(inp); flip = not a.no_flip_y
    elif inp.lower().endswith(".obj"):
        pts = load_obj(inp); flip = False
    else:
        raise SystemExit("entree inconnue (attendu .svg, .obj ou builtin:NAME)")
    if not pts:
        raise SystemExit("aucun point extrait de l'entree")

    M = max(64, int(a.sr / a.freq))
    x, y = resample(pts, M)
    x, y = normalize(x, y, flip)

    if a.out_wav:
        total = int(a.sr * a.dur); reps = int(np.ceil(total / M))
        X = np.tile(x, reps)[:total]; Y = np.tile(y, reps)[:total]
        write_wav(a.out_wav, X, Y, a.sr)
    if a.out_png:
        render_xy(x, y, a.size).save(a.out_png)
    if a.out_mp4:
        framedir = a.out_mp4 + "_frames"; os.makedirs(framedir, exist_ok=True)
        N = 90
        for i in range(N):
            ang = 2*math.pi*i/N
            rx = x*math.cos(ang) - y*math.sin(ang); ry = x*math.sin(ang) + y*math.cos(ang)
            render_xy(rx, ry, a.size).save(os.path.join(framedir, "f%03d.png" % i))
        subprocess.run(["ffmpeg", "-y", "-framerate", "30", "-i", os.path.join(framedir, "f%03d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", a.out_mp4],
                       capture_output=True)

    print("oscli OK | points/boucle=%d | freq=%gHz | input=%s" % (M, a.freq, os.path.basename(inp)))
    for f in (a.out_wav, a.out_png, a.out_mp4):
        if f:
            print("  ->", f, "(%d o)" % (os.path.getsize(f) if os.path.exists(f) else 0))


if __name__ == "__main__":
    main()
