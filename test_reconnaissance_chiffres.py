# Reconnaissance des chiffres :

liste_nom_donnees={"1.png":1, "2.png":2, "3.png":3, "4.png":4, "5.png":5, "6.png":6, "7.png":7, "8.png":8, "9.png":9, "1.jpg":1, "2.jpg":2, "3.jpg":3,"4.jpg":4, "5.jpg":5, "6.jpg":6, "8.jpg":8, "9.jpg":9}

import matplotlib.image as mpimg
import numpy as np
import os
from PIL import Image
from copy import deepcopy

def comparaison(mat1,mat2):
    n=len(mat1)
    c=0
    for i in range (n):
        for j in range(n):
            m1=deepcopy(mat1[i][j])
            m2=deepcopy(mat2[i][j])
            print(m1)
            for k in range (3):
                if m1[k]!=m2[k]:
                    c=c+1
            """x0=mat1[i][j][0]
            x1=mat1[i][j][1]
            x2=mat1[i][j][2]
            y0=mat2[i][j][0]
            y1=mat2[i][j][1]
            y2=mat2[i][j][2]
            if x0!=y0:
                    c=c+1
            if x1!=y1:
                    c=c+1
            if x2!=y2:
                    c=c+1"""
    c=(c/(n**2))
    return c

def imag_to_string(nom_image):
    #gerer l'os*
    imgpil =Image.open(nom_image)
    imgpil=imgpil.resize((50,50),Image.ANTIALIAS)
    img=np.array(imgpil)
    donnees=liste_nom_donnees.keys()
    n=len(donnees)
    tab_compa=np.zeros(n)
    i=0
    for x in donnees :
        #x=str(donnees[i])
        imgpil2 = Image.open(x)
        imgpil2=imgpil2.resize((50,50),Image.ANTIALIAS)
        img2=np.array(imgpil2)
        comp=comparaison(img,img2)
        tab_compa[i]=comp
        i=i+1
    ind_max=indice_max(tab_compa)
    return liste_nom_donnees[donnees[ind_max]]

def indice_max(tab):
    n=len(tab)
    i=0
    for j in range (1,n):
        if tab[j]>tab[i]:
            i=j
    return i
