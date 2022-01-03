# _Compte Rendu de Guillaume Lochon_

## Le Jeu de la Vie


Le projet portait sur la réalisation d'un jeu de la vie sur Python

###Utilistion du programme :

On lancera simplement main.py, et on utilisera des arguments de la manière suivante :
```sh 
python main.py -t 
```  
pour rendre le jeu dans le terminal.
```sh 
python main.py -g 
```  
pour rendre en fenêtre graphique avec pygame,
```sh 
python main.py -t -f save.txt 
```  
Pour utiliser un fichier de sauvegarde dont on spécifiera le nom à la place de save.txt. On fournira un fichier d'exemple  
En l'absence de l'argument TEXTFILE avec -f, une erreur sera renvoyée. On peut retrouver dans TEXTFILE un fichier texte brut avec des 0 et des 1 séparés par des espaces et disposés ligne par ligne
Pour ce faire, on a utilisé plusieurs packages avec chacun une utilisation précise et différente :

- __pygame__ -> Utilisé pour l'affichage graphique

- __numpy__ -> Le jeu étant représenté sous forme d'array numpy, son utilisation est évidente

- __optparse__ -> Pour l'utilisation d'arguments au lancement du programme, afin de préciser si on veut lancer le jeu dans sa version terminal ou graphique, et si l'on veut faire usage d'un fichier de sauvergarde à importer pour accéder à un jeu au choix avec certains patterns précis par exemple

- __os__ -> Utilisé pour la gestion du terminal, spécifiquement pour le clear à chaque nouveau jour du jeu

- __time__ -> Pour faire des pauses dans chaque tour de jour afin de bien voir le changement de chaque génération


Le jeu s'arrête soit au bon d'un certain nombre de jours, que l'on peut choisir dans la fonction __main__ du jeu ligne 156. Ou bien lorsqu’aucun changement n’est détecté entre 2 jours d’affilées. On peut choisir de régler la vitesse du jeu dans la fonction __terminal_render()__, en modifiant la ligne __time.sleep()__, et indiquant dans les parenthèses la durée choisie en secondes entre chaque jour.


###Ce qu'on a appris :
L'utilisation des parsers avec optparse, afin de pouvoir utiliser des arguments au lancement du jeu et personnaliser l'expérience globale avec des fichiers de sauvegarde. On à également vu l'I/O. Nous avons aussi découvert succinctement comment fonctionnait pygame.

Concernant Vigenère, j'ai appris comment fonctionnaient les erreurs et comment les lever, l'existence des fonctions pour passer un texte en minuscule et majuscule, et enfin les possibilités de récupérer le cardinal de chaque caractère pour le convertir de texte à ASCII

### Difficultés :
Pygame est assez dur à prendre en main, et beaucoup de questions techniques se posent avec son utilisation :  
Étant donné qu'on choisit d'afficher une grille sur des pixels,  
ilfaut qu'on arrive à faire une fonction aussi polyvalente pour afficher une grille de 7x7 qu'une de 500x500.  
Nous n'avons pas réussi à trouver comment avoir une fonction fonctionnelle dans tous les cas de figure. Nous avons laissé l'ébauche de cette fonction
Pygame est quand même appelable avec l'argument -g, et on peut quitter la fenêtre en appuyant sur Q. C'est dommage que nous n’ayons pas réussi à aller plus loin avec, car cela permet de très  
nombreuses fonctionnalités, avec le jeu qui peut réellement avoir une incidence sur une partie en cours.

On peut également alléger le code en évitant de unpad le frame à chaque fin de jour

## Chiffrement de Vigenère

Programme simple, à lancer de la manière suivante pour encrypter:
```sh 
python main.py -e  
``` 
Ou pour décrypter :
```sh 
python main.py -d 
``` 

Une fenêtre apparait alors pour demander le texte, puis la clef. Le programme fonctionne aussi bien pour les textes en minuscules qu'en majuscule, et renverras toujours un texte en majuscule pour une question de lisibilité. 