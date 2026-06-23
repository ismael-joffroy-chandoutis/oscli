#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
viz_fiche — genere une FICHE-RESUME visuelle (carte synoptique) a partir
d'un digest de recherche verifie (recherche/<domaine>.md) de DECHARGE.

Systematise la demande "a chaque recherche, un resume en visuel".
Sortie : un PNG (et SVG) carte sur charte noir + vert phosphore, via graphviz.

Usage : python3 viz_fiche.py recherche/<domaine>.md bible/visuels/<domaine>.png
"""
import sys, re, os, html, subprocess

md = open(sys.argv[1], encoding="utf-8", errors="replace").read()
out_png = sys.argv[2]
out_svg = out_png.rsplit(".", 1)[0] + ".svg"


def esc(s, n=150):
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > n:
        s = s[:n - 1].rstrip() + "…"
    return html.escape(s)


def block(name):
    m = re.search(r'\*\*' + name + r'[^*]*\*\*(.*?)(\n\*\*[0-9A-Za-zÀ-ÿ][^*]*\*\*|\Z)', md, re.S)
    return m.group(1) if m else ""


m = re.search(r'^##\s+(.*?)\s*\(`([^`]+)`\)', md, re.M)
title = m.group(1).strip() if m else os.path.basename(sys.argv[1])
key = m.group(2) if m else ""
mv = re.search(r'\*\*Verif:\*\*\s*(\w+)', md)
verdict = mv.group(1) if mv else "?"

vcolor = {"solide": "#7fae3f", "corrections_mineures": "#c9a23f",
          "corrections_majeures": "#c95f3f"}.get(verdict, "#888888")

# resume : texte entre la ligne Verif et **Findings:**
ms = re.search(r'\*\*Verif:\*\*[^\n]*\n+(.*?)\n+\*\*Findings', md, re.S)
def wrap(s, n, width=70):
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > n:
        s = s[:n - 1].rstrip() + "…"
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return '<BR ALIGN="LEFT"/>'.join(html.escape(l) for l in lines)

summary = wrap(ms.group(1), 240) if ms else ""

findings = re.findall(r'^- \*\*(.+?)\*\*', md, re.M)[:6]
ent_names = re.findall(r'^- ([^:\n]+):', block("Entit"), re.M)[:7]
risks = [l.strip("- ").strip() for l in block("Risques").splitlines() if l.strip().startswith("- ")][:3]

ROW = '<TR><TD ALIGN="LEFT"><FONT COLOR="{c}" POINT-SIZE="{p}">{t}</FONT></TD></TR>'
rows = []
rows.append(ROW.format(c="#7fe6a8", p=18, t="<B>" + esc(title, 70) + "</B>"))
rows.append(ROW.format(c=vcolor, p=10, t="vérification : <B>" + verdict.replace("_", " ") + "</B>"))
if summary:
    rows.append('<TR><TD ALIGN="LEFT"><FONT COLOR="#cfeede" POINT-SIZE="10">' + summary + '</FONT></TD></TR>')
rows.append('<TR><TD HEIGHT="6"></TD></TR>')
if findings:
    rows.append(ROW.format(c="#46b67a", p=11, t="<B>POINTS CLÉS</B>"))
    bul = "<BR ALIGN=\"LEFT\"/>".join("• " + esc(f, 90) for f in findings)
    rows.append('<TR><TD ALIGN="LEFT"><FONT COLOR="#e9ffe9" POINT-SIZE="10">' + bul + '<BR ALIGN="LEFT"/></FONT></TD></TR>')
if ent_names:
    rows.append(ROW.format(c="#46b67a", p=11, t="<B>ACTEURS / OUTILS</B>"))
    rows.append('<TR><TD ALIGN="LEFT"><FONT COLOR="#9fe0bf" POINT-SIZE="10">' + wrap(" · ".join(ent_names), 220, 80) + '</FONT></TD></TR>')
if risks:
    rows.append(ROW.format(c="#c9a23f", p=11, t="<B>À ÉPROUVER / RISQUES</B>"))
    bul = "<BR ALIGN=\"LEFT\"/>".join("– " + esc(r, 90) for r in risks)
    rows.append('<TR><TD ALIGN="LEFT"><FONT COLOR="#e6cf9f" POINT-SIZE="9">' + bul + '<BR ALIGN="LEFT"/></FONT></TD></TR>')

label = ('<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="7" BGCOLOR="#0e2419">'
         + "".join(rows) + '</TABLE>>')

dot = ('digraph fiche {\n bgcolor="#080a09";\n node [shape=plaintext];\n'
       ' rankdir=TB;\n fiche [label=' + label + '];\n}\n')

dotpath = out_png.rsplit(".", 1)[0] + ".dot"
open(dotpath, "w", encoding="utf-8").write(dot)
subprocess.run(["dot", "-Tpng", dotpath, "-o", out_png], check=True)
subprocess.run(["dot", "-Tsvg", dotpath, "-o", out_svg], check=True)
print("fiche:", os.path.basename(out_png), "| verdict:", verdict, "| findings:", len(findings))
