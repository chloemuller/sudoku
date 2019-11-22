# Sudoku

Description du projet : L'objectif de ce projet est de construire une application permettant de scanner un sudoku de reconstruire la grille associée et d'en proposer une résolution.

## authors

Muller Chloé, 
Dang-Nhu Barthélémy,
Basler Tristan,
Korchia Raphael,
Sasson Charlotte,
Carril Thomas.

## tâches
### MVP
#### coder un algorithme de résolution du sudoku lorsque celui est sous forme d'array et affichant le sudoku résolu

* via un algorithme de backtracking
* affichage via tkinter

#### coder un algorithme transformant une photo de sudoku en liste de liste 

* simplifier l'image (la mettre en noir et blanc)
* repérer le cadre du sudoku
* redresser le sudoku
* lire le quadrillage (les chiffres) et le transformer en array éxecutable par l'algorithme de backtracking

### autres fonctionnalités

* interface permettant de lancer l'appareil photo et de prendre en photo le sudoku ou de la sélectionner dans l'explorateur de fichiers
* interface permettant de modifier les chiffres scannés en cas d'erreur

## éxecution du programme

* pour éxecuter le programme éxecuter le fichier interface.py
* dans la fenêtre resolveur sudoku choisir son mode de chargement du sudoku (explorateur de fichier/ appareil photo/ remplissage manuel)
* attendre que le programme lise la grille
* verifier que la grille lue par le programme correspond bien au sudoku utilisé
* * si oui cliquer sur grille remplie et fermer la fenêtre resolveur sudoku
* * sinon cliquer sur corriger grille, modifier les cases à modifier en cliquant dessus et en utilisant les boutons sous la grille
puis cliquer sur grille remplie et fermer la fenetre sudoku resolve
* votre sudoku résolu s'affiche !

## modules necessaire

pour éxecuter ce programme il faut télécharger certain modules :

* opencv-python
* tensorflow
* tkinter 

si ce n'est pas suffisant installer les modules du fichier requirements.txt (il contient beaucoup de modules inutiles à ce programme)