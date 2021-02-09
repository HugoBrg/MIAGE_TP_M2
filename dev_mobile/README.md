# MVP
J'ai réalisé toutes les US sauf la #6 (Filtrer sur la liste des vêtements).
Je suis pas sûre que j'ai compris le critèes d'acceptance numéro #2 de la US #5 par rapport au champ password. Ici mon champ password sert de confirmation pour changer les autres champs.

# User
Il y a un utilisateur test vierge : 
- login: hugo
- password: 1234

Et un utilisateur test avec un panier deja rempli et des informations deja rempli : 
- login: test
- password: test

# Commentaire
J'ai réaliser une fois que le projet était bien avancé que j'aurais gerer plus interactivement les données au sein de l'application, c'est à dire, créer dynamiquement les widgets et les renvoyer une fois qu'ils sont prêts au lieu d'utiliser des List<>.

Il y a une AppBar mais elle est pas nécessaire à la navigation. Je l'ai surtout mis car la bar de notifcation de l'émulateur m'empechait de cliquer certain bouton.