#--------------------------------------#
# ENSEMBLES DE TEST ET D'APPRENTISSAGE #
#--------------------------------------#

# Chargement des donnees
produit <- read.csv("Data Produit.csv", header = TRUE, sep = ",", dec = ".", stringsAsFactors = T)
str(produit)
View(produit)
table(produit$Produit)

# Construction des ensembles d'apprentissage et de test
produit_EA <- produit[1:400,]
produit_ET <- produit[401:600,]

# Suppression de la variable ID
produit_EA <- subset(produit_EA, select = -ID) 
# Autre solution par reference au numero de colonne : produit_EA <- produit_EA[,-1]

# Affichages des ensembles et des distributions de valeurs des variables
View(produit_EA)
View(produit_ET)
summary(produit_EA)
summary(produit_ET)

#--------------------------------#
# APPRENTISSAGE DE L'ARBRE RPART #
#--------------------------------#

# Installation et activation de la librairie requise
install.packages("rpart")
library(rpart)

# Construction de l'arbre de decision 'tree1'
tree1 <- rpart(Produit~., produit_EA)

# Affichage de l'arbre par 'tree1' par plot.rpart() et text.rpart() 
plot(tree1)
text(tree1, pretty=0)

# Affichage textuel de l'arbre de decision
print(tree1)

#---------------------------------------#
# AFFICHAGE PAR LA LIBRAIRIE RPART.PLOT #
#---------------------------------------#

# Installation et activation de la librairie requise
install.packages("rpart.plot")
library(rpart.plot)

# Affichage par d�faut d'un arbre rpart par la fonction prp()
prp(tree1)

# Valeurs sur les arcs, classe en couleur et proportion de la classe majoritaire dans chaque noeud
prp(tree1, type=4, extra=8, box.col=c("tomato", "darkturquoise")[tree1$frame$yval])

# Valeurs sur les arcs, classe en couleur et effectifs de chaque classe dans chaque noeud
prp(tree1, type=4, extra=1, box.col=c("tomato", "darkturquoise")[tree1$frame$yval])

# Choix atomatique des couleurs et intensit� proportionnelle � la proportion de la classe majoritaire 
prp(tree1, type=4, extra=8, box.palette = "auto")
prp(tree1, type=4, extra=1, box.palette = "auto")

#-------------------------------------------#
# GENERATION DES PROBABILITES DE PREDICTION #
#-------------------------------------------#

# Generation de la classe pr�dite pour chaque exemple de test pour l'arbre 'tree1'
test_tree1 <- predict(tree1, produit_ET, type="class")

# Generation des probabilites pour chaque exemple de test pour l'arbre 'tree1'
prob_tree1 <- predict(tree1, produit_ET, type="prob")

# Affichage des deux vecteurs de probabilites generes
print(prob_tree1)

# Affichage du vecteur de probabilites de prediction 'Oui'
prob_tree1[,2]

# Affichage du vecteur de probabilites de prediction 'Non'
prob_tree1[,1]

# Construction d'un data frame contenant classe reelle, prediction et probabilit�s des predictions
df_result1 <- data.frame(produit_ET$Produit, test_tree1, prob_tree1[,2], prob_tree1[,1])
View(df_result1)

# Rennomage des colonnes afin d'en faciliter la lecture et les manipulations
colnames(df_result1) = list("Classe","Prediction", "P(Oui)", "P(Non)")
View(df_result1)

# Quartiles et moyenne des probabilites des predictions 'Oui' pour l'arbre 'tree1'
summary(df_result1[df_result1$Prediction=="Oui", "P(Oui)"])

# Quartiles et moyenne des probabilites des predictions 'Non' pour l'arbre 'tree1'
summary(df_result1[df_result1$Prediction=="Non", "P(Non)"])
