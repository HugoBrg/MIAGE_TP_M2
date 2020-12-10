# Travaux pratiques 

## Installation

## Disclaimer 
Afin de comprendre les amélioration et différence de comportements entre les robots j'ai fait les choix de faire apparaître les nouvelles caratéristiques en **gras** et de faire apparare les caratéristiques qui ont due disparaitre en ~~barré~~.

## Agents réflexes simples
- Initialisation : Genère 2 couloirs qui sont sectionner en plusieurs partie pouvant avoir 2 etats : sale (1) ou propre (0).
- Comportement : Visite toutes les partie des couloirs et les nettoie si besoin.
- Amélioration : S'arrête quand toutes les salles sont propres, il commence dans une salle aléatoirement.

## Agents réflexes fondés sur des modèles (ou avec état interne)
- Initialisation : Genère 2 couloirs qui sont sectionner en plusieurs partie pouvant avoir 2 etats : sale (1) ou propre (0).
- Comportement : Visite toutes les partie des couloirs et les nettoie si besoin, **le robot enregistre son etat interne dans un tableau "log", son etat interne est consultable à n'importe quel moment grâce à la fonction "etatActuel()"**.
- Amélioration : S'arrête quand toutes les salles sont propres, il commence dans une salle aléatoirement, l'etat du robot à son départ est inconnue, le robot se dirige en partie en fonction de son etat interne et de l'etat de la salle voisine.

## Agents fondés sur des buts
- Initialisation : Genère 2 couloirs qui sont sectionner en plusieurs partie pouvant avoir 2 etats : sale (1) ou propre (0).
- Comportement : Visite toutes les partie des couloirs et les nettoie si besoin, le robot enregistre son etat interne dans un tableau "log", son etat interne est consultable à n'importe quel moment grâce à la fonction "etatActuel()", **le robot cherche à nettoyer un case spéciale qui est définie à l'initialisartion comme son but**.
- Amélioration : ~~S'arrête quand toutes les salles sont propres~~, il commence dans une salle aléatoirement, l'etat du robot à son départ est inconnue, ~~le robot se dirige en partie en fonction de son etat interne et de l'etat de la salle voisine~~, **le robot nettoie tout de même les salle sur son passage**.

## Agents fondés sur l'utilité
- Initialisation : Genère 2 couloirs qui sont sectionner en plusieurs partie pouvant avoir 2 etats : sale (1) ou propre (0).
- Comportement : Visite toutes les partie des couloirs et les nettoie si besoin, le robot enregistre son etat interne dans un tableau "log", son etat interne est consultable à n'importe quel moment grâce à la fonction "etatActuel()", le robot cherche à nettoyer un case spéciale qui est définie à l'initialisartion comme son but, **le robot s'interroge pour savoir si il est quel salle est la plus sale afin  de la nettoyer jusqu'à son objectif**.
- Amélioration : ~~S'arrête quand toutes les salles sont propres~~, ~~il commence dans une salle aléatoirement~~, l'etat du robot à son départ est inconnue, le robot se dirige en partie en fonction de son etat interne et de l'etat de la salle voisine, le robot nettoie tout de même les salle sur son passage, **le robot commence dans la salle la plus sale afin de pouvoir la nettoyer sur son passage**.

## ELIZA
- Comportement : Reformule la plupart des affirmations de l'utilisateur
- Amélioration : Etant un psychothérapeute ELIZA possède un degré d'attention ! Si son patient commence à parler de sujet concernant (suicide, meurtre, solitudes, ect..) plus de 2 fois elle va lui donner des réponses appropriées (ex: vous me faite peur, es-ce que ca va ?, ect..). Si le patient recommence à parler normalement ELIZA reprend la conversation classique.

## PARRY
- Comportement : Le chatbot possède des émotions
- Amélioration : Chaque phrase est analysé grâce à la base de données SentiWord, si un mot a une consonnance positive ou négative cela affecte les réponses et l'humeur de PARRY.

## Agent de resetvations de billets d'avions


## Au cas ou il vous est impossible de tester les codes des screenshots des résultats se trouve dans le dossier /results