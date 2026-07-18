#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
viz_schemas — schemas techniques / mises en situation DECHARGE, en graphviz.
Deterministe (donc exact, contrairement a une image generee). Charte noir + vert
phosphore, rouge pour les avertissements. Donnees issues des recherches verifiees.
Sortie : bible/visuels/schema_*.png (+ .svg)
"""
import os, subprocess

OUT = os.environ.get("OSCLI_VIZ_OUT", "./visuels")
os.makedirs(OUT, exist_ok=True)

HEAD = '''digraph {{
  bgcolor="#080a09"; rankdir={rk}; labelloc="t"; fontname="Helvetica";
  fontcolor="#7fe6a8"; fontsize=18; label="{title}";
  nodesep=0.35; ranksep=0.5;
  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11,
        fontcolor="#e9ffe9", color="#2f7d52", fillcolor="#0e2419", penwidth=1.5, margin="0.18,0.10"];
  edge [color="#46b67a", fontname="Helvetica", fontsize=9, fontcolor="#a9e6c4", penwidth=1.3, arrowsize=0.8];
'''

SCHEMAS = {
"live": ("Performance live — routage du signal", "LR", '''
  pc    [label="Ordinateur\\nosci-render / Pure Data / TouchDesigner", fillcolor="#123524"];
  link  [label="Ableton Link\\nsync tempo (<5 ms LAN)", shape=octagon, fillcolor="#231a10", color="#b6863f", fontcolor="#ffe9c0"];
  dc    [label="Interface DC-couplée\\nES-8 (±10 V, 96 kHz)"];
  scope [label="Oscilloscope CRT\\nou Vectrex moddée", fillcolor="#10291c"];
  pa    [label="Sono / PA\\n(même signal = son)"];
  cam   [label="Caméra"];
  proj  [label="Vidéoprojecteur\\n+ écran"];
  syph  [label="Syphon (macOS)\\nosci-render → TouchDesigner → OBS", shape=note, fillcolor="#142e20"];
  obs   [label="OBS\\nstream / captation"];
  pc -> dc;
  dc -> scope [label="X / Y / Z"];
  dc -> pa [label="audio"];
  scope -> cam -> proj;
  pc -> syph -> obs;
  link -> pc [style=dashed, color="#b6863f"];
'''),

"vectrex_mod": ("Mod Vectrex — entrée XY/Z externe (réversible)", "LR", '''
  dc    [label="Interface DC-couplée\\nsorties X / Y / Z (±10 V)", fillcolor="#123524"];
  att   [label="Atténuateurs\\n±10 V → ±9 / ±11 V"];
  conn  [label="Connecteur d'interception\\nCPU ↔ driver CRT (réversible)", shape=note, fillcolor="#142e20"];
  jx    [label="Jack X · fil orange · ±9 V"];
  jy    [label="Jack Y · fil bleu · ±11 V"];
  jz    [label="Jack Z · fil blanc · intensité"];
  crt   [label="Carte driver CRT\\n→ écran vectoriel", fillcolor="#10291c"];
  sk    [label="SPOT KILLER\\nswitch SPST 110 V\\nfermé = mode synthèse", color="#c95f3f", fillcolor="#2a1411", fontcolor="#ffd9cf"];
  hv    [label="⚠ HAUTE TENSION\\nphosphore fragile · risque de brûlure résiduelle\\nréf : PDF Andrew Duff 2014 + README Holzer", shape=box, color="#c95f3f", fillcolor="#180a08", fontcolor="#ffb3a3"];
  dc -> att -> conn;
  conn -> jx; conn -> jy; conn -> jz;
  jx -> crt; jy -> crt; jz -> crt;
  sk -> crt [style=dashed, color="#c95f3f", label="désactive la coupure"];
  hv -> crt [style=dotted, color="#c95f3f", arrowhead=none];
'''),

"capture": ("Captation de l'écran — deux voies", "TB", '''
  scope [label="Oscilloscope CRT / Vectrex\\n(phosphore, glow réel)", fillcolor="#10291c"];
  setup [label="Pièce noire · polarisant circulaire\\nfiltre diffusion (graisse / bas nylon)\\noptique macro · longue exposition", shape=note, fillcolor="#142e20"];
  cam   [label="Caméra"];
  soft  [label="Rendu logiciel\\nosci-render / sosci"];
  sc    [label="Screen capture\\n(zéro reflet)"];
  frames[label="Séquences PNG / vidéo"];
  ff    [label="ffmpeg → master\\n(grain, glow, étalonnage)"];
  scope -> setup -> cam -> frames;
  soft -> sc -> frames;
  frames -> ff;
'''),
}

for name, (title, rk, body) in SCHEMAS.items():
    dot = HEAD.format(rk=rk, title=title) + body + "}\n"
    base = os.path.join(OUT, "schema_" + name)
    open(base + ".dot", "w", encoding="utf-8").write(dot)
    subprocess.run(["dot", "-Tpng", base + ".dot", "-o", base + ".png"], check=True)
    subprocess.run(["dot", "-Tsvg", base + ".dot", "-o", base + ".svg"], check=True)
    print("schema:", name, "OK")
