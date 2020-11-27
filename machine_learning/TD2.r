#------------------------------------#
# DONNEES DE TEST ET D'APPRENTISSAGE #
#------------------------------------#

# Chargement des donnees
produit <- read.csv("Data Produit.csv", header = TRUE, sep = ",", dec = ".")
str(produit)
View(produit)
table(produit$Produit)

# Construction des ensembles d'apprentissage et de test
produit_EA <- produit[1:400,]
produit_ET <- produit[401:600,]

# Suppression variable ID
produit_EA <- subset(produit_EA, select = -ID) 

# Autre solution par reference au numero de colonne : produit_EA <- produit_EA[,-1]

# Affichages
View(produit_EA)
View(produit_ET)
summary(produit_EA)
summary(produit_ET)

#--------------------------------#
# APPRENTISSAGE DE L'ARBRE RPART #
#--------------------------------#

# Installation des packages requis
install.packages("rpart")
library(rpart)

# Construction de l'arbre de decision
tree1 <- rpart(Produit~., produit_EA)

# Affichage de l'arbre par les fonctions de base de R
plot(tree1)
text(tree1, pretty=0)

#-----------------------#
# TEST DE L'ARBRE RPART #
#-----------------------#

# Application de l'arbre de decision a l'ensemble de test 'produit_ET'
test_tree1 <- predict(tree1, produit_ET, type="class")

# Affichage du vecteur de predictions de la classe des exemples de test
test_tree1

# Affichage du nombre de predictions pour chacune des classes
table(test_tree1)

# Ajout des predictions comme une nouvelle colonne 'Prediction' dans le data frame 'produit_ET'
produit_ET$Prediction <- test_tree1
View(produit_ET)

# Affichage de liste des exemples de test correctement predits
View(produit_ET[produit_ET$Produit==produit_ET$Prediction, ])

# Calcul du nombre de succes : nombre d'exemples avec classe reelle et prediction identiques
nbr_succes <- length(produit_ET[produit_ET$Produit==produit_ET$Prediction,"ID"])
nbr_succes

# Calcul du taux de succes : nombre de succes sur nombre d'exemples de test
taux_succes <- nbr_succes/nrow(produit_ET)
taux_succes

# Calcul du nombre d'echecs : nombre d'exemples avec classe reelle et prediction differentes
nbr_echecs <- length(produit_ET[produit_ET$Produit!=produit_ET$Prediction,"ID"])
nbr_echecs

# Calcul du taux d'echecs : nombre d'echecs sur nombre d'exemples de test
taux_echecs <- nbr_echecs/nrow(produit_ET)
taux_echecs

#-------------------------------#
# PREDICTIONS PAR L'ARBRE RPART #
#-------------------------------#

# Chargement des exemples prospects dans un data frame 'produit_pro'
produit_pro <- read.csv("Data Produit Prospects.csv", header = TRUE, sep = ",", dec = ".")

# Application de l'arbre de decision aux prospects dans 'produit_pro' : classe predite
pred_tree1 <- predict(tree1, produit_pro, type="class")

# Affichage des r�sultats (predictions)
pred_tree1

# Affichage du nombre de predictions pour chaque classe
table(pred_tree1)

# Ajout dans le data frame produit_pro d'une colonne Predition contenant la classe predite 
produit_pro$Prediction <- pred_tree1

# Creation d'un data frame contenant les predictions 'Oui'
produit_pro_oui <- produit_pro[produit_pro$Prediction=="Oui",]
produit_pro_oui

# Creation d'un data frame contenant les predictions 'Non'
produit_pro_non <- produit_pro[produit_pro$Prediction=="Non",]
produit_pro_non