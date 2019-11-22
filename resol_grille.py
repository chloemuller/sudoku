import numpy as np


def est_dans_carre(i,j,x,grille):
    indi=i//3
    indj=j//3
    res=False
    for k in range(3*indi,3*indi+3):
        for l in range(3*indj,3*indj+3):
            if grille[k,l]==x:
                res=True
    return res

def est_dans_ligne(i,x,grille):
    return x in list(grille[i,:])

def est_dans_colonne(j,x,grille):
    return x in list(grille[:,j])

def est_possible(i,j,x,grille):
    return not(est_dans_carre(i,j,x,grille))and not(est_dans_ligne(i,x,grille)) and not(est_dans_colonne(j,x,grille))
    

def listecase(grille):
    l=[]
    for i in range(9):
        l2=[]
        for j in range(9):
            l3=[]
            for k in range(1,10):
                if grille[i,j]==0 and est_possible(i,j,k,grille):
                    l3.append(k)
            l2.append(l3)
        l.append(l2)
    return l

def maj_listecase(grille,listecase):
    for i in range(9):
        for j in range(9):
            for k in listecase[i][j]:
                if grille[i,j]==0 and not(est_possible(i,j,k,grille)):
                    listecase[i][j].remove(k)
                    
                    
                    
def maj_grille(grille,listecase):
    grille2=np.copy(grille)
    for i in range(9):
        for j in range(9):
            if grille[i,j]==0 and len(listecase[i][j])==1:
                grille2[i,j]=listecase[i][j][0]
    return grille2

def simplifie_grille(grille):
    listcase=listecase(grille)
    grille2=maj_grille(grille,listcase)
    while grille.all()!=grille2.all():
        maj_listecase(grille,listcase)
        grille,grille2=grille2,maj_grille(grille2,listcase)
    return grille2

def backtrac(grille,pos):
    if pos==81:
        return True
    i,j=pos//9,pos%9
    if grille[i,j]!=0:
        return backtrac(grille,pos+1)
    for k in range(1,10):
        if est_possible(i,j,k,grille):
            grille[i][j]=k
            if backtrac(grille,pos+1):
                return True
    grille[i][j]=0
    return False
            
def resol(grille):
    grille2=np.copy(grille)
    grille2=simplifie_grille(grille2)
    backtrac(grille2,0)
    return grille2
    
     
    
    
    
    
    
            
