# Questions réponses TLN - Hugo BERANGER - MIAGE IA2
## Description
Ce programme analyse des questions en langage naturel et tente de les transformer en requêtes SQL pour interroger la base de donnée DBPEDIA

## Problèmes recontrés
* Difficultée à faire une requête SPARQL (j'ai tester mes requêtes en lignes)
* Compréhension du début de la requête (resources, ontology, ect..)
* Type de réponse (uri, string, date, ect..)
* Utilisation de wordnet (abandonnée)

## Principale librairies utilisées
* nltk
* SPARQLWrapper
* difflib

## Résultats
3 requêtes sur 26 sont fonctionnelles. Le reste des requêtes a un ou plusieurs défauts. Voir les resultats avec les différences mis en valeurs

## Lancement
```
git clone https://github.com/HugoBrg/MIAGE_TP_M2/tree/master/traitement_du_langage_naturel
cd /MIAGE_TP_M2/traitement_du_langage_naturel
python TD3_questions_answers_system.py
```

Il se peut que vous ayez à télécharger des data nltk - voir début du fichier