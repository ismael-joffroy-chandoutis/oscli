# Méthode : un cinéma d'oscilloscope, outils libres, orchestré

> Texte de méthode, CC BY-SA 4.0. Comment fabriquer des images dont le son est la matière, avec des outils libres et une chaîne que l'on tient de bout en bout.

## Le principe
Sur un oscilloscope en mode XY, le canal gauche pilote l'axe horizontal, le canal droit l'axe vertical. Le son ne décrit pas l'image, il la trace. Ce que l'on voit et ce que l'on entend sont une seule chose. Tout part de là.

## La chaîne
1. Concevoir des formes comme des tracés continus : à la main (SVG), en 3D (Blender, projeté en 2D), ou par des fonctions paramétriques.
2. Les convertir en signal stéréo XY : c'est le rôle d'`oscli` (headless, scriptable) ou d'osci-render / OsciStudio (interfaces graphiques) pour les scènes riches.
3. Donner le signal à voir : un affichage logiciel pour une captation maîtrisée, ou une interface audio à couplage continu vers un oscilloscope à tube pour la matière authentique.
4. Assembler, étalonner, masteriser avec des outils standard.

Le point technique qui commande tout : le couplage continu (DC). Sans lui, les formes asymétriques dérivent et se recentrent. Le taux d'échantillonnage commande la netteté des angles.

## L'éthique
Rendre la chaîne cachée visible. Le courant, le signal, le procédé : on ne les masque pas, on les donne à voir comme sujet. L'outil est au service du geste, jamais à sa place. Quand des processus génératifs ou algorithmiques entrent dans la chaîne, c'est comme un instrument que l'on accorde, dans la tradition de l'artiste qui programme son propre synthétiseur. On code et on partage ses outils : c'est pourquoi `oscli` est libre.

## Orchestration
La chaîne est assez légère pour être tenue par une personne seule, outillée. Chaque étape est scriptable, donc reproductible et automatisable : générer une forme, la convertir, la rendre, l'assembler. Le calcul lourd, quand il y en a, se déporte sur une machine GPU ; le cœur vectoriel, lui, tourne partout.

## Contexte
Cette méthode est née de la fabrication d'un film en cours, DÉCHARGE. Le film reste inédit ; ce qui est partagé ici, ce sont les outils et la méthode, pas l'œuvre.

## Lignée
Ben Laposky, John Whitney, Nam June Paik, les Vasulka, Mary Ellen Bute et ses films à l'oscilloscope, le son dessiné de Norman McLaren, puis la scène contemporaine de l'oscilloscope music (Jerobeam Fenderson, Hansi Raber, Derek Holzer, Robert Henke, le festival VectorHack). `oscli` se place dans cette lignée, du côté de l'outil libre.
