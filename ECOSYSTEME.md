# Écosystème open-source de l'oscilloscope music et de la synthèse vectorielle

> Catalogue sourcé : dépôts open-source (oscilloscope XY, Pure Data, Vectrex, DAC laser), scène élargie (laser, synthèse vidéo analogique, VJing) et festivals. Tous les dépôts ont été vérifiés sur leurs pages GitHub et les sites officiels. Niveaux de confiance entre parenthèses (élevé / moyen / faible). Ressource communautaire, maintenue avec l'outil [oscli](README.md). CC BY-SA 4.0.

---

## Pôle 1 : oscilloscope XY — rendu logiciel

| Dépôt | Rôle | Langage | Activité | Étoiles | URL |
|-------|------|---------|----------|---------|-----|
| jameshball/osci-render | Outil pivot : .obj, .svg, Blender, texte → audio XY stéréo. Plugin VST/AU. Scripting Lua. Gratuit avec version premium (offline render, live video — périmètre exact du premium non documenté publiquement, confiance moyenne sur ce point). | C++ (89 %) | Actif, v2.8.9.18, avril 2026 (élevé) | 704 | https://github.com/jameshball/osci-render |
| jameshball/sosci | Oscilloscope logiciel compagnon pour monitoring signal XY live, outil de prévisualisation du workflow osci-render. | Java | Maintenu, date exacte du dernier commit non affichée (élevé) | 3 | https://github.com/jameshball/sosci |
| kritzikratzi/Oscilloscope | Émulateur oscilloscope CRT vintage (OpenFrameworks), simulation de l'esthétique phosphore sur fichiers audio. Par Hansi Raber, co-créateur d'OsciStudio. OsciStudio lui-même est propriétaire et non open-source. | C++ (93,6 %) | Dernier commit jan. 2022, non maintenu (élevé) | 624 | https://github.com/kritzikratzi/Oscilloscope |
| m1el/woscope | Émulateur oscilloscope WebGL dans le navigateur. Transforme l'audio en affichage XY via shaders GPU. Démo live disponible. | JS (84 %) | Inactif, pas de commits récents (élevé) | 253 | https://github.com/m1el/woscope |
| alemidev/scope-tui | Oscilloscope, vectorscope et spectroscope dans le terminal. Mode vectorscope = affichage XY stéréo en ASCII/braille. Outil de monitoring, pas de génération de signal. | Rust (100 %) | Très actif, fév. 2026 (élevé) | 648 | https://github.com/alemidev/scope-tui |
| corrscope/corrscope | Rendu vidéo d'oscilloscope à partir de WAV avec algorithme de corrélation. Export MP4 via FFmpeg. Conçu pour chiptune — usage DECHARGE : export renders vidéo du signal, pas génération. | Python (99,9 %) | Semi-actif, 0.11.0 mai 2025 (élevé) | 726 | https://github.com/corrscope/corrscope |

**Note sur OsciStudio :** logiciel propriétaire Windows de Jerobeam Fenderson et Hansi Raber. Pas abandonné, utilisé par Fenderson dans ses performances actuelles. Le code source n'est pas disponible. osci-render est la continuation open-source la plus proche, pas un remplacement direct.

---

## Pôle 2 : Pure Data

| Dépôt | Rôle | Langage | Activité | Étoiles | URL |
|-------|------|---------|----------|---------|-----|
| macumbista/vectorsynthesis | Bibliothèque Pure Data par Derek Holzer. Formes 2D/3D, Lissajous, scan-processing vidéo via signaux audio envoyés à oscilloscope, Vectrex modifié, laser ILDA ou émulateur logiciel. Fondement théorique de l'écosystème XY artistique. Note : GitHub détecte Python (100 %) à cause d'un script utilitaire — le contenu réel est des patches .pd. | Python déclaré, patches .pd réels | Dernier commit mai 2022, non maintenu activement (élevé) | 311 | https://github.com/macumbista/vectorsynthesis |
| Eric-Lennartson/pd-osci | 70 externals Pure Data : primitives 2D/3D, équations paramétriques, transformations, effets. Complément pratique à vectorsynthesis pour la composition. | C (89 %) | Maintenu, date exacte non vérifiée (élevé) | 14 | https://github.com/Eric-Lennartson/pd-osci |
| timredfern/pd_helios | External Pure Data pour piloter le Helios Laser DAC directement depuis un patch Pd. Pont entre vectorsynthesis/pd-osci et le hardware laser. | C (40,6 %) | Maintenu (élevé) | 15 | https://github.com/timredfern/pd_helios |

---

## Pôle 3 : rendu en code (Processing, p5.js, convertisseurs)

| Dépôt | Rôle | Langage | Activité | Étoiles | URL |
|-------|------|---------|----------|---------|-----|
| ffd8/xyscope | Bibliothèque Processing/Java : primitives graphiques → audio XY pour oscilloscopes, Vectrex modifié ou laser RGB. Supporte la correction ratio Vectrex. Par Ted Davis. | Java (46 %) | v3.0.0, mars 2023 (élevé) | 168 | https://github.com/ffd8/xyscope |
| ffd8/xyscopejs | Port p5.js de XYscope. Live-coding oscilloscope depuis le navigateur, compatible P5LIVE. | JS (93 %) | Actif, v0.4.7 déc. 2025 (élevé) | 22 | https://github.com/ffd8/xyscopejs |
| ffd8/leesuhzhoo | Interface slider 2D pour explorer les ratios de fréquences Lissajous sur oscilloscope physique ou logiciel. Outil de composition. Créé pour des recherches sur les cinéastes expérimentaux oscilloscope. | Processing (100 %) | Dernier commit fév. 2018, inactif (élevé) | 8 | https://github.com/ffd8/leesuhzhoo |
| ffd8/dac_ilda | Schémas hardware DIY pour construire un adaptateur audio DAC multicanal → ILDA laser. Passerelle entre la sortie audio d'un XYscope et un vrai laser. | Documentation | v0.1.2, 2018 (élevé) | 66 | https://github.com/ffd8/dac_ilda |
| ferluht/XYRender | Addon Blender → audio XY oscilloscope. Supporte Grease Pencil. Intégration VCV Rack. Absent de la recherche initiale, découvert via github.com/topics/oscilloscope-music. | Python (100 %) | Activité à vérifier (moyen) | 10 | https://github.com/ferluht/XYRender |
| PotatoKingTheVII/Video-to-Lissajous-Oscilloscope | Convertit une vidéo monochrome en WAV stéréo (L=X, R=Y). Deux modes : vectoriel (potrace/SVG, style Vectrex) et pseudo-rasterisation. | Python (100 %) | Maintenu (élevé) | 6 | https://github.com/PotatoKingTheVII/Video-to-Lissajous-Oscilloscope |
| simonyiszk/scopelogo | Script minimaliste SVG → audio oscilloscope via soundcard (aplay, Linux). | Python (97,6 %) | Inactif (élevé) | 3 | https://github.com/simonyiszk/scopelogo |
| zippy731/vamp | Addon Blender (Vector Art Motion Processor) : supprime les arêtes cachées, génère silhouettes et line drawings Freestyle. Construit pour OsciStudio, complémentaire de l'addon osci-render. | Python (100 %) | Maintenu (élevé) | 42 | https://github.com/zippy731/vamp |

---

## Pôle 4 : DAC laser (hardware ILDA)

| Dépôt | Matériel | Activité | URL |
|-------|----------|----------|-----|
| Grix/helios_dac | Helios DAC USB open-source. 12 bit XY (4095x4095), 8 bit RGBI, 65,5 kpps max. Prix : ~99 €/114 $ (élevé). SDK C++, Python, C#/.NET, firmware KiCAD. SDK v11.0 jan. 2025 : support IDN réseau, compatible StageMate ISP et adaptateurs OpenIDN. | Actif, jan. 2025 (élevé) | https://github.com/Grix/helios_dac |
| j4cbo/j4cDAC | Firmware open-source de l'Ether Dream DAC (Ethernet). Implémentation de référence du protocole EtherDream, standard dans l'écosystème. | Dernier commit pré-2020, inactif (élevé) | https://github.com/j4cbo/j4cDAC |
| brendan-w/lzr | Framework C++ laser show avec bibliothèques ILDA, interpolation, drivers EtherDream. Abandonné. Utile comme référence ILDA. | Abandonné déc. 2020 (élevé) | https://github.com/brendan-w/lzr |
| Volst/laser-dac | Outils Node.js/TypeScript multi-DAC (Helios, EtherDream, LaserDock) + simulateur web. Marqué legacy. Le README recommande de migrer vers un successeur Rust non encore nommé publiquement. | Legacy, non maintenu (élevé) | https://github.com/Volst/laser-dac |
| marcan/openlase | Framework C pour graphiques laser temps réel : SVG, 3D, lecture/écriture ILDA. Référence historique. | Abandonné sept. 2020 (élevé) | https://github.com/marcan/openlase |

**Scan rate minimal :** 30 kpps pour figures simples, 65+ kpps pour scènes Lissajous 3D fluides. Le Helios atteint 65,5 kpps (élevé).

---

## Pôle 5 : Vectrex

| Dépôt | Rôle | URL |
|-------|------|-----|
| malbanGit/Vide | IDE Vectrex complet : assembleur 6809, émulateur, éditeur vectoriel, éditeur musique/images. Principal outil pour le homebrew Vectrex. Java, 61 étoiles. | https://github.com/malbanGit/Vide |
| jhawthorn/vecx | Émulateur Vectrex SDL en C. Base de nombreux forks (vecxl, libretro-vecx, jsvecx). | https://github.com/jhawthorn/vecx |
| pmaciel/vecxl | vecx + Helios DAC : exécute des ROMs/jeux Vectrex et sort les vecteurs vers un laser via USB. Démontre le pipeline Vectrex → laser directement. C++, 3 étoiles. | https://github.com/pmaciel/vecxl |
| gtoal/pitrex | PiTrex : Raspberry Pi Zero WH pilotant l'affichage vectoriel Vectrex hardware. Permet de lancer MAME, Asteroids, Battlezone sur le moniteur Vectrex. C, 37 étoiles. Distinct de pelrun/piTrex (5 étoiles, 'Raspberry Pi to Vectrex bridge') — deux projets connexes non interchangeables. | https://github.com/gtoal/pitrex |
| MiSTer-devel/Vectrex_MiSTer | Core Vectrex FPGA pour plateforme MiSTer. VHDL, 21 étoiles. | https://github.com/MiSTer-devel/Vectrex_MiSTer |
| obsidian-dot-dev/openFPGA-Vectrex | Core Vectrex pour Analogue Pocket (openFPGA). Rendu 540x720, beam persistence réglable. v0.9.4, avril 2024. VHDL, 19 étoiles. | https://github.com/obsidian-dot-dev/openFPGA-Vectrex |
| libretro/libretro-vecx | Core Vectrex pour RetroArch/libretro, rendu OpenGL ou software. | https://github.com/libretro/libretro-vecx |

---

## Scène élargie : laser et art du signal

**Robert Henke — Lumière III.** La série Lumière (2013 en cours) est la référence formelle la plus directement pertinente pour DECHARGE. Lumière I utilisait trois lasers blancs ; Lumière II a introduit quatre lasers couleur. Pour Lumière III, la description officielle ne précise pas un nombre différent de lasers (moyen sur ce point). Le son n'est pas causalement produit par les lasers : un moteur sonore parallèle est développé de Lumière II à III, les signaux audio et laser sont produits simultanément mais séparément. Finale au Mapping Festival Genève, mai 2025. https://www.roberthenke.com/concerts/lumiere.html

**Derek Holzer — Vector Synthesis.** Ateliers en Europe, bibliothèque open-source (macumbista/vectorsynthesis). Outils : Benjolin (deux VCO + circuit Rungler), soundcard DC-coupled (MOTU), Pure Data. Généalogie citée par Holzer lui-même : Bute, Whitney, Paik, Laposky, Vasulka. http://macumbista.net/?page_id=4869

**Robin Fox — Triptych.** Première à Unsound Cracovie, fin 2022. Tournée : Berlin Atonal, Barbican, Lincoln Center. Isao Tomita Special Prize, Ars Electronica 2023. Dates NFSA oct. 2024 = tournée, pas création récente. Intérêt pour DECHARGE : la causation inversée (lumière qui génère du son) comme dispositif dramaturgique. https://disquiet.com/2024/12/17/robin-foxs-lasers/

**Cracked Ray Tube (James Connolly + Kyle Evans).** Tutoriels DIY pour transformer un TV CRT en oscillographe. Article dans Leonardo Music Journal (2014). Filiation avec la communauté Vector Circuits. https://crackedraytube.com/textstutorials.html

**BUS ERROR Collective — Primer.** Gagnant de la Wild compo (catégorie fourre-tout de la demoscene, pas une catégorie oscilloscope dédiée) et Crowd Favorite à Revision 2025, la plus grande demoparty mondiale. Outils confirmés : osci-render + Ableton 11. Logic Pro/Alchemy est cité dans certains rapports mais non sourcé dans l'article Hackaday original (faible). Proof-of-concept que l'oscilloscope music est compétitive en demoscene en 2025. https://hackaday.com/2025/04/26/amazing-oscilloscope-demo-scores-the-win-at-revision-2025/

---

## Scène élargie : synthèse vidéo analogique

**Rutt/Etra Video Synthesizer (1971-1972).** Steve Rutt + Bill Etra. Manipulation du raster vidéo par déflexion XY d'un CRT, rescané par caméra. Utilisé par Paik, Vasulka, Etra. Plugin logiciel v002 disponible (macOS/Quartz Composer, 2012) — compatibilité avec les macOS récents à vérifier avant usage (moyen). https://en.wikipedia.org/wiki/Rutt/Etra_Video_Synthesizer

**LZX Industries.** Modules Eurorack pour synthèse vidéo analogique. Visual Cortex (keying, animation 2D), Vidiot (instrument standalone). Chromagnon : FPGA, générateurs de waveform quad, entrée/sortie vidéo — en développement actif en 2025 avec refonte hardware, non livré aux utilisateurs finaux. Affirmer que son firmware est mis à jour et disponible est inexact (faible sur ce point). Production artisanale, délais 6-12 mois. https://lzxindustries.net/

**Généalogie historique.** Ben Laposky (1950-53, Oscillons, 200 venues en tournée). Mary Ellen Bute (1952, Abstronic, oscilloscope comme "crayon de lumière", Bell Labs). John Whitney Sr (IBM 7094). Nam June Paik + Shuya Abe (synthétiseur vidéo 1969-72). Dan Sandin, Image Processor (1974, distribution libre "Distribution Religion", 20+ copies construites). Sources : https://spalterdigital.com/artists/ben-laposky/ et https://www.centerforvisualmusic.org/ButeRetrospective.htm

---

## Scène élargie : VJing et outils temps réel

**Hydra (Olivia Jack).** Live coding visuel WebGL dans le navigateur. Syntaxe inspirée de la synthèse modulaire. Partage de flux via WebRTC entre fenêtres. Le repo officiel maintenu est hydra-synth/hydra (organisation GitHub), pas le compte personnel ojack/hydra — les deux existent, les deux renvoient vers le même projet. Plugin Hydra 2 TD pour TouchDesigner. https://hydra.ojack.xyz/

**TouchDesigner.** CHOP Helios DAC intégré nativement dans la documentation officielle (canaux X/Y + RGB). Point Operators (POPs) introduits en 2024 pour manipulation GPU de données 3D. Pertinent pour le pipeline performance DECHARGE : génératif audio-réactif → laser en temps réel. https://docs.derivative.ca/Helios_DAC_CHOP

**MadMapper MadLaser.** Extension MadMapper 5+ (macOS 11+/Windows 10+). Multi-protocole : ILDA (EtherDream/Helios USB), Shownet, FB4. Vectorisation temps réel de contenu vidéo, shaders laser programmables, import SVG. Vectoriser des animations type Émile Cohl en projection laser est faisable nativement. https://madmapper.com/extensions/madlaser

**vvvv gamma 6.0.** Sorti le 5 avril 2024, version actuelle 6.7. VL.Fuse : bibliothèque GPU open-source. Alternative à TouchDesigner pour installations interactives en paradigme dataflow/.NET. https://vvvv.org/

**Pangolin BEYOND.** Leader mondial du logiciel laser show commercial (concerts, événements). DAC FB3QS/FB4, PangoScript. Sa place dans une production d'art contemporain est marginale — Helios DAC + TouchDesigner ou MadLaser couvrent les besoins de DECHARGE sans ce budget. https://pangolin.com/pages/beyond

---

## Festivals

| Festival | Lieu | Période | Pertinence DECHARGE |
|----------|------|---------|---------------------|
| Mapping Festival | Genève | Mai (Lumière III, mai 2025) | Référence mondiale art audiovisuel, programmation oscilloscope/laser documentée |
| Scopitone / Stereolux | Nantes | Sept. (23e éd. 17-21 sept. 2025) | Lien institutionnel existant d'Ismaël, 25 000-50 000 festivaliers, cible co-production |
| Ars Electronica | Linz | Septembre | Robin Fox, Isao Tomita Special Prize, catégories art numérique |
| MUTEK | Montréal / international | Variable | Performances audiovisuelles live, art numérique |
| Revision | En ligne + Allemagne | Pâques | Demoscene, Wild compo, BUS ERROR Collective 2025 |
| Piksel | Bergen, Norvège | Novembre | DIY, open-source, hardware libre (moyen : édition 2024 vérifiée, suite incertaine) |
| Annecy MIFA | Annecy | Juin | Animation expérimentale — voir chapitre 12 |

Signal Culture (résidence toolmaker, équipement synthétiseurs vidéo uniques) : en transition entre Loveland CO et Binghamton NY en juin 2026. Statut du programme de résidence à confirmer avant candidature. https://signalculture.org/

---

## Usages typiques (par chaîne)

**Film d'animation :** pipeline Blender + osci-render (Blender addon distribué dans les releases jameshball/osci-render) + zippy731/vamp (suppression arêtes cachées) + corrscope (export render vidéo). Alternative légère : ffd8/xyscope (Processing) ou ferluht/XYRender (Grease Pencil Blender).

**Performance live :** Helios DAC (99 €) + TouchDesigner (gratuit non-commercial) ou MadLaser (extension MadMapper). Pipeline Pure Data possible avec macumbista/vectorsynthesis + pd-osci + timredfern/pd_helios. Budget minimal pour une salle : 500-800 € pour le laser ILDA d'occasion + 99 € pour le DAC. Réglementation laser UE classe 3B/4 : évaluation de risques requise avant toute performance publique. En France, contacter la DGCCRF/DGS ; formation Laser Safety Officer disponible via ILDA (https://www.ilda.com/safety-basics.htm).

**Jeu vidéo :** malbanGit/Vide pour le homebrew Vectrex (assembleur 6809), pmaciel/vecxl pour sortir les vecteurs vers un laser depuis un émulateur, gtoal/pitrex pour piloter du hardware Vectrex réel depuis un Raspberry Pi Zero WH.

**Monitoring sans matériel :** alemidev/scope-tui (terminal Rust, vectorscope XY, actif fév. 2026), m1el/woscope (navigateur WebGL), kritzikratzi/Oscilloscope (macOS/Windows, OpenFrameworks).

---

## À vérifier / pistes ouvertes

- Compatibilité de ferluht/XYRender (Grease Pencil) avec votre version de Blender.
- Périmètre exact de la version premium d'osci-render (offline MP4, live video) : à documenter depuis le changelog GitHub, pas depuis la page officielle qui ne le détaille pas.
- Fonctionnement du Helios DAC SDK v11.0 en configuration multi-points (IDN réseau) pour une installation immersive.
- Compatibilité du plugin v002 Rutt-Etra avec macOS 14+.
- Statut exact du programme de résidence Signal Culture (Colorado vs Binghamton NY, juin 2026).
- Scan processing vidéo via macumbista/vectorsynthesis : tester sur une version fixe de Pure Data + Gem pour contourner les problèmes de dépendances (dernier commit mai 2022).
- Vectrex32 (vectrex32.com) : plateforme hardware distincte référencée par jaymzjulian/vectrex32_tools, dont le dépôt principal n'a pas été retrouvé sur GitHub — à vérifier directement sur le site.

---

## Sources

- https://github.com/jameshball/osci-render
- https://github.com/jameshball/sosci
- https://github.com/macumbista/vectorsynthesis
- https://github.com/Eric-Lennartson/pd-osci
- https://github.com/ffd8/xyscope
- https://github.com/ffd8/xyscopejs
- https://github.com/ffd8/dac_ilda
- https://github.com/ffd8/leesuhzhoo
- https://github.com/corrscope/corrscope
- https://github.com/kritzikratzi/Oscilloscope
- https://github.com/zippy731/vamp
- https://github.com/Grix/helios_dac
- https://github.com/timredfern/pd_helios
- https://github.com/j4cbo/j4cDAC
- https://github.com/brendan-w/lzr
- https://github.com/Volst/laser-dac
- https://github.com/marcan/openlase
- https://github.com/alemidev/scope-tui
- https://github.com/m1el/woscope
- https://github.com/PotatoKingTheVII/Video-to-Lissajous-Oscilloscope
- https://github.com/ferluht/XYRender
- https://github.com/malbanGit/Vide
- https://github.com/jhawthorn/vecx
- https://github.com/pmaciel/vecxl
- https://github.com/gtoal/pitrex
- https://github.com/MiSTer-devel/Vectrex_MiSTer
- https://github.com/obsidian-dot-dev/openFPGA-Vectrex
- https://www.roberthenke.com/concerts/lumiere.html
- http://macumbista.net/?page_id=4869
- https://crackedraytube.com/textstutorials.html
- https://disquiet.com/2024/12/17/robin-foxs-lasers/
- https://hackaday.com/2025/04/26/amazing-oscilloscope-demo-scores-the-win-at-revision-2025/
- https://osci-render.com/
- https://lzxindustries.net/
- https://bitlasers.com/helios-laser-dac/
- https://madmapper.com/extensions/madlaser
- https://hydra.ojack.xyz/
- https://docs.derivative.ca/Helios_DAC_CHOP
- https://vvvv.org/
- https://pangolin.com/pages/beyond
- https://mappingfestival.com/
- https://stereolux.org/scopitone
- https://piksel.no/
- https://signalculture.org/
- https://www.ilda.com/safety-basics.htm
- https://spalterdigital.com/artists/ben-laposky/
- https://www.centerforvisualmusic.org/ButeRetrospective.htm
- https://en.wikipedia.org/wiki/Rutt/Etra_Video_Synthesizer
- https://en.wikipedia.org/wiki/Sandin_Image_Processor
