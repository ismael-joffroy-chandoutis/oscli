[English](README.md) · **Français**

# oscli — boîte à outils oscilloscope (XY) headless

Transforme des formes vectorielles (SVG, OBJ, formes intégrées) en **audio stéréo XY**, plus des images à lueur phosphorescente, entièrement headless et scriptable. `oscli` comble un vide dans l'écosystème de la musique d'oscilloscope : un outil en ligne de commande, là où osci-render et OsciStudio sont des applications graphiques.

> Le son EST l'image. Le son EST l'image. (Mode XY d'oscilloscope : le canal gauche pilote X, le canal droit pilote Y.)

## Contenu
- **oscli.py** — vecteur (SVG / OBJ / intégré) vers WAV stéréo XY plus PNG (et un MP4 rotatif). L'outil central.
- **structure_circulaire.py / logo_loop.py** — animations de morphing (forme à forme) rendues en GIF/MP4 plus un vrai WAV (jouable sur un oscilloscope).
- **blender_to_osc.py** — Blender (headless) vers OBJ vers oscilloscope. Se lance avec `blender -b -P blender_to_osc.py -- out.obj`.
- **viz_fiche.py / viz_schemas.py** — fiches synoptiques et schémas techniques basés sur graphviz (outillage compagnon).

## Installation
Python 3, plus `numpy` et `pillow`. `ffmpeg` pour l'export GIF/MP4. `graphviz` (le binaire `dot`) pour les scripts viz.
```
pip install numpy pillow
```

## Usage
```
python3 oscli.py --input shape.svg     --out-wav out.wav --out-png out.png --freq 50
python3 oscli.py --input model.obj      --out-wav o.wav   --out-png o.png
python3 oscli.py --input builtin:lissajous --out-png liss.png
```
Support SVG : `<path>` (M L H V C Q Z, absolus et relatifs) plus `<polyline>` / `<polygon>`. OBJ : sommets plus arêtes de lignes. Le WAV est un vrai signal : joue-le dans un oscilloscope analogique en mode XY (ou dans osci-render) et il redessine l'image.

## Exemples
Voir `examples/` : une figure de Lissajous, un « éclair » dentelé, Suzanne de Blender dessinée par le son, et un morphing circulaire (cercle calme à éclair à Lissajous à spirale, en boucle). Chaque fixe et boucle est rendu à partir d'audio.

## Écosystème
[ECOSYSTEME.md](ECOSYSTEME.md) est un catalogue sourcé de la scène open-source de l'oscilloscope / vecteur / Vectrex / laser (dépôts vérifiés, scène contemporaine, festivals).

## Méthode
[METHODE.md](METHODE.md) : comment faire du cinéma d'oscilloscope avec des outils libres et orchestrés, et pourquoi (CC BY-SA).

## Filiation et crédits
Construit dans la filiation d'[osci-render](https://github.com/jameshball/osci-render) (James Ball) et de [vectorsynthesis](https://github.com/macumbista/vectorsynthesis) (Derek Holzer). `oscli` est le compagnon headless en ligne de commande qu'ils ne fournissent pas. Merci à la communauté de la musique d'oscilloscope.

## Licence
Code : MIT (voir LICENSE). Textes (METHODE.md, ECOSYSTEME.md) : CC BY-SA 4.0.
Auteur : Ismaël Joffroy Chandoutis.

Par [Ismaël Joffroy Chandoutis](https://ismaeljoffroychandoutis.com).
