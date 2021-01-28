# TP 13-(14-15): Conception et implémentation d’un algorithme de recherche d’informations 

## TP effectué en solo

# Fichiers
* Les textes se trouve dans le dossier /texts
* Les résultats se trouve au même emplacements que le programme (output.txt)

# Programme 
## Etape 1 : Etape 2 - Tâche 1
* Recuperation des fichiers
* Tokenisation des documents par documents

## Etape 2 - Tâche 2
* Suppression des stop words
* Supression de la ponctuation

## Etape 2 - Tâche 3
* Utilisation du lemmatizer de Porter sur les tokens

## Etape 2 - Tâche 4
* Création d'un dictionnaire contenant le nombre d'occurence de chaque mot

## Etape 2 - Tâche 5
* Création d'un dictionnaire contenant les ids des documents ou les mots sont présents

## Etape 3
* Création d'un dictionnaire contenant le nombre d'occurence de chaque mot par document

## Etape 4 - Tâche intermediaire
* Définition d'une méthode arrondissent les resultats pour ameliorer la lisibilité
* Utilisation des dictionnaires crées précédemment pour caclculer le document le plus pertinent pour un mot donné
* Utilisation de 2 méthode de calcul possible : 
    * 1 - Renvoie le nombre d'occurences du mot par document (en commentaire)
    * 2 - Renvoie le nombre d'occurences du mot par document divisé par le nombre de mot total de chaque document (en utilisation)

## Etape 4 - Tâche 1
* Définition d'un méthode permettant de supprimer des éléments d'un dictionnaire (utilisé plus tard)
* Définition de la méthode 'boolean_request' permettant de traiter les requêtes contenant :
    * AND
    * OR
    * NOT
* Les parenthèses ne sont pas traitées
* Les requêtes en langage naturel sont traités comme des AND
* Les resultats sont ensuite trier puis exploiter (calcul de TF * IDF (2 versions disponibles))
* Les requêtes avec des mots non connus sont attrapée
* Les résultats sont arrondis pour plus de lisibilité et affichés

# Tests
* Les requêtes du TP sont toute testée
* Les requêtes contenant des parenthèses ont probablement des résultats érronés
* La requête contenant "hugo" est le test d'un mot n'étant pas présent dans les documents
* Les deux requête suivante test un mot seul et sa negation (l'ordre de pertinence des documents s'inverse)
* La requête suivante test le AND
* La requête suivante test le OR (dans ce cas précis censé être la moitié du AND)

# Installation
Décommenter ligne 7 si besoin pour télécharger les stopwords
```
git clone https://github.com/HugoBrg/MIAGE_TP_M2/
cd /MIAGE_TP_M2/traitement_du_langage_naturel/TD5_information_retrieval
python TD5_information_retrieval
```