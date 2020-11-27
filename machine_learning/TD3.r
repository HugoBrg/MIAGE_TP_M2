#-------------------------#
# PREPARATION DES DONNEES #
#-------------------------#

# Chargement des donnees
produit <- read.csv("Data Produit.csv", header = TRUE, sep = ",", dec = ".", stringsAsFactors = T)
str(produit)

# Creation des ensembles d'apprentissage et de test
produit_EA <- produit[1:400,]
produit_ET <- produit[401:600,]

# Suppression de la variable ID de l'ensemble d'apprentissage
produit_EA <- subset(produit_EA, select=-ID)

# Installation/m-a-j des librairies
install.packages("rpart")
install.packages("C50")
install.packages("tree")

# Activation des librairies
library(rpart)
library(C50)
library(tree)

#-----------------------------------------#
# APPRENTISSAGE ARBRE DE DECISION 'rpart' #
#-----------------------------------------#

# Apprentissage arbre
tree1 <- rpart(Produit~., produit_EA)

# Affichage graphique : tracage des arcs par la fonction plot.rpart() 
plot(tree1)
# Ajout du texte au graphique par la fonction text.rpart()
text(tree1, pretty = 0)

#----------------------------------------#
# APPRENTISSAGE ARBRE DE DECISION 'C5.0' #
#----------------------------------------#

# Apprentissage arbre
tree2 <- C5.0(Produit~., produit_EA)

# Affichage graphique (arcs et texte) par la fonction plot.C5.0()
plot(tree2, type="simple")

#----------------------------------------#
# APPRENTISSAGE ARBRE DE DECISION 'tree' #
#----------------------------------------#

# Apprentissage arbre
tree3 <- tree(Produit~., data=produit_EA)

# Affichage graphique : tracage des arcs par la fonction plot.tree() 
plot(tree3)
# Ajout du texte au graphique par la fonction text.tree()
text(tree3, pretty=0)

#------------------------------------------------------------------#
# TEST DES ARBRES DE DECISION PAR APPLICATION A L'ENSEMBLE DE TEST #
#------------------------------------------------------------------#

# Application de l'arbre 'tree1' a l'ensemble de test 'produit_ET' 
test_tree1 <- predict(tree1, produit_ET, type="class")
# Application de l'arbre 'tree2' a l'ensemble de test 'produit_ET' 
test_tree2 <- predict(tree2, produit_ET, type="class")
# Application de l'arbre 'tree3' a l'ensemble de test 'produit_ET' 
test_tree3 <- predict(tree3, produit_ET, type="class")

# Comparaison des repartitions des predictions
table(test_tree1)
table(test_tree2)
table(test_tree3)

#---------------------------#
# CALCUL DES TAUX DE SUCCES #
#---------------------------#

# Ajout des predictions de 'tree1' comme  nouvelle colonne 'Tree1' dans 'produit_ET'
produit_ET$Tree1 <- test_tree1
# Ajout des predictions de 'tree2' comme  nouvelle colonne 'Tree2' dans 'produit_ET'
produit_ET$Tree2 <- test_tree2
# Ajout des predictions de 'tree3' comme  nouvelle colonne 'Tree3' dans 'produit_ET'
produit_ET$Tree3 <- test_tree3

# Affichage de la classe reelle et des classes predites 
View(produit_ET[,c("Produit", "Tree1", "Tree2", "Tree3")])
                
# Calcul du taux de succes : nombre de succes sur nombre d'exemples de test
taux_succes1 <- length(produit_ET[produit_ET$Produit==produit_ET$Tree1,"ID"])/nrow(produit_ET)
taux_succes1
taux_succes2 <- length(produit_ET[produit_ET$Produit==produit_ET$Tree2,"ID"])/nrow(produit_ET)
taux_succes2
taux_succes3 <- length(produit_ET[produit_ET$Produit==produit_ET$Tree3,"ID"])/nrow(produit_ET)
taux_succes3

#----------------------------------------#
# PREDICTIONS DU CLASSIFIEUR SELECTIONNE #
#----------------------------------------#

# Chargement des donnees a predire dans un data frame 'produit_PR'
produit_PR <- read.csv("Data Produit Prospects.csv", sep=",", dec=".", header=T)

# Application de l'arbre 'tree2' a l'ensemble de prospects 'produit_PR' 
class_tree2 <- predict(tree2, produit_PR, type="class")
class_tree2
table(class_tree2)

#---------------------------------#
# ENREGISTREMENT DES PREDICTIONS  #
#---------------------------------#

# Ajout des resultat dans une colonne Prediction au data frame produit_PR
produit_PR$Prediction <- class_tree2
View(produit_PR)

# Enregistrement du fichier de resultats au format csv
write.table(produit_PR, file='resultats.csv', sep="\t", dec=".", row.names = F)