### Importation
import numpy as np
import random
from copy import deepcopy


### première solution :

def estcontradictoire(liste):
    chiffres = set(liste) - {0}
    for c in chiffres:
        if liste.count(c) != 1:
            return True
    return False

def grille_verification(grille):
    for i in range(n):
        lig=[]
        for j in range(n):
            lig.append(grille[i][j])
        if estcontradictoire(lig):
            return False
    for i in range(n):
        col=[]
        for j in range(n):
            col.append(grille[j][i])
        if estcontradictoire(col):
            return False
    for l in range(3):
        for c in range(3):
            cellule = []
            for i in range(3):
                cellule = cellule + sudoku[l * 3 + i][c * 3:(c + 1) * 3]
            if estcontradictoire(cellule):
                return False
    return True

def casepos(case,sudoku):
    chiffres = set(sudoku[case[0]])
    chiffres |= {sudoku[i][case[1]] for i in range(9)}
    cellule = case[0] // 3 , case[1] // 3
    for i in range(3):
        chiffres |= set(sudoku[cellule[0] * 3 + i][cellule[1] * 3:(cellule[1] + 1) * 3])
    return list(set(range(1,10)) - chiffres)

def resolution(grille):
    possibles = [[] for i in trous]
    casearemplir = 0
    while casearemplir < len(trous):
        possibles[casearemplir] = casepos(trous[casearemplir],sudoku)
        try:
            while not possibles[casearemplir]:
                sudoku[trous[casearemplir][0]][trous[casearemplir][1]] = 0
                casearemplir -= 1
        except IndexError:
            print("Le sudoku n’a pas de solution.")

        exit(1)
        sudoku[trous[casearemplir][0]][trous[casearemplir][1]] = possibles[casearemplir].pop()
        casearemplir += 1




















