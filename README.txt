Jeu du Pendu
=========================

Description
--------------
Ce programme est un jeu du pendu, où le joueur doit deviner un mot aléatoire tiré d'un fichier texte (`mots_pendu.txt`).
Le joueur a 6 vies pour deviner toutes les lettres du mot. Une fonction d'indice est disponible lorsque le joueur est sur le point de perdre.

Il a été choisi de rédifer les noms des variables et noms des fonctions en anglais pour des raisons d'apprentissage, puisque la majorité du code est régdigé en anglais.
Les commentaires sont tous de même écris en français.


Fonctionnalités
------------------
- Sélection aléatoire d’un mot depuis un fichier texte.
- Suppression des accents dans les mots.
- Interaction via la console.
- Système de vies (6 tentatives).
- Option d’indice disponible à 1 tentatives restantes.
- Possibilité de rejouer à la fin de chaque partie.

Fichier requis
-----------------
- "mots_pendu.txt" : contient une liste de mots (un mot par ligne).
Vous pouvez utiliser un autre fichier texte, à conditions de le spécifier dans les paramètres lors de l'appel du programme main en utilisant la syntaxe suivante :à
main(file = "fichier_texte.txt")


Structure du programme
-------------------------
Idéation :
Puisque plusieurs variables traversent plusieurs fonctions, une approche de variables globales a été utilisé.
Ces variables sont partagées et modifiés au travers des différentes fonctions du programme, et elles permettes d'éviter avoir à prendre plusieurs entrée / sortie par fonction.
Il reste que certaines fonctions utilisent les variables globales pour démontrer leurs utilités et ma compréhension de leurs utilisations.

Autrement, un programme principal {main()} est une boucle qui s'arrête lorsque l'utilisateur choisis de ne pas rejoeur. Dans cette boucle, on choisit un mot, puis
on initialise le jeu. On boucle ensuite tant que l'utilisateur à plus que 0 vie ou tant que l'utilisateur n'a pas trouvé toutes les lettres du mot. Si l'utilisateur
à une tentatives restantes, une fonction s'initie pour lui permmetre de choisir s'il veut s'accorder un indice.

Lorsque la boucle interne se termine (soit parce que les tentaives égales à 0 , soit parce que l'utilisateur a trouvé toutes les lettres), un affichage dans la console
lui montre s'il a gagner ou perdu. Il a alors l'option de rejouer ou de terminer, ce qui relance la première boucle ou met fin au programme.


Variables globales :
- "life": nombre de vies restantes.
- "answer": mot sélectionné.
- "answer_hidden": liste contenant les lettres devinées ou des soulignés ("_").
- "clue": booléen indiquant si un indice a été donné.


Fonctions principales :
- main(file="mots_pendu.txt"): Boucle principale du jeu
- word_selection(file): choisit un mot aléatoire depuis le fichier.
- delete_accent(word): remplace les lettres accentuées par leur équivalent sans accent.
- game_initialisation(word): affiche le message d’introduction.
- guess_letter(letter_list): permet au joueur de proposer une lettre et affiche les résultats.
- lose_life(): enlève une vie.
- check_for_underscore(): vérifie si toutes les lettres ont été trouvées.
- print_win() / print_lose(): affiche un message de victoire ou défaite.
- give_clue() : donne un indice (révèle une lettre).
- replay() : demande au joueur s’il souhaite rejouer.


Exécution
------------
Pour exécuter le jeu, il suffit de lancer le programme main.
Assurez-vous que le fichier "mots_pendu.txt", ou que le fichier texte de mots voulant être jouer se trouve dans le même dossier.

Le fichier texte qui contient les mots doit être dans le même format que celui par défault, soit en utf-8 avec un mot par ligne.


Auteur
---------
Projet de jeu du pendu écrit en Python par Antoine Gingras, le 21 mai 2025.
