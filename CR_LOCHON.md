# Le Jeu de la Vie

## _Compte Rendu de Guillaume Lochon_

Le projet portait sur la réalisagtion d'un jeu de la vie sur Python

###Utilistion du programme :

On lancera simplement main.py, et on utilisera des arguments de la manière suivante : -t pour rendre en terminal, -g pour rendre en fenetre graphique avec pygame, -f TEXTFILE pour utiliser un fichier de sauvegarde dont on specierfiera le nom à la place de TEXTFILE. 
En l'absence de l'argument TEXTFILE avec -f, une erreur sera renvoyée. On peut rentrouver dans TEXTFILE un fichier texte brut avec des 0 et des 1 séparés par des espaces et disposés ligne par ligne
Pour ce faire, on a utilisé plusieurs packages avec chaucn une utilisation précise et différente :

- pygame -> Utilisé pour l'affichage graphique 

- numpy -> Le jeu étant représenté sous forme d'array numpy, son utilisation est évidente

- optparse -> Pour l'utilisation d'arguments au lancement du programme, afin de préciser si on veut lancer le jeu dans sa version terminal ou graphique, et si l'ont veut faire usage d'un fichier de sauvergarde à importer pour accéder à un jeu au choix avec certains patterns précis par exemple

- os -> Utilisé pour la gestion du terminal, spécifiquement pour le clear à chaque nouveau jour du jeu

- time -> Pour faire des pauses dans chaque tour de jour afin de bien voir le changement de chaque génération


###Ce qu'on a appris : 
L'utilisation des parsers avec optparse, afin de pouvoir utiliser des arguments au lancement du jeu et personnaliser l'expérience globale avec des fichiers de sauvegarde. On à également vu l'I/O. Nous avons aussi découvert succintement comment fonctionnait pygame. 

Concernant Vigenere, j'ai appris comment fonctionnaient les erreurs et comment les lever, l'existence des fonctions pour passer un text en minuscule et majuscule, et enfin les possibilités de récuperer le cardinal de chaque caractères pour le convertir de texte à ASCII

### Difficultés : 
Pygame est assez dur à prendre en main, et beaucoup de questions techniques se posent avec son utilisation : 
étant donner qu'on choisi d'afficher une grille sur des pixels, 
il faut qu'on arrive à faire une fonction aussi polyvalente pour afficher une grille de 7x7 qu'une de 500x500. 
On a pas réussi à trouver comment avoir une fonction fonctionnelle dans tous les cas de figure. Nous avons laissé l'ébauche de cette fonction
Pygame est quand meme appelable avec l'argument -g, et on peut quitter la fenetre en appuyant sur Q. C'est dommage qu'on ai pas réussi à aller plus loin avec, car cela permet de très 
nombreuses fonctionnalités, avec le jeu qui peut réelement avoir une incidence sur une partie en cours.

On peut egalement alleger le code en évitant de unpad le jeu à chaque fin de jour