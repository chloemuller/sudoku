from PIL import Image
import numpy as np
from pylab import *
import matplotlib.pyplot as pl

fichier="Capture d’écran 2019-11-18 à 10.23.08.png"
photo=Image.open(fichier)
image=np.array(photo)

def transform_to_grey (image):
    longueur=len(image)
    largeur=len(image[0])
    image_gris=[[[0,0,0] for j in range (largeur)]for i in range (longueur)]
    for i in range(longueur):
        for j in range (largeur):
            moy=(image[i][j][0]+image[i][j][1]+image[i][j][2])//3
            image_gris[i][j][0]=moy
            image_gris[i][j][1]=moy
            image_gris[i][j][2]=moy
    return image_gris

#image_gris=transform_to_grey(image)
#imshow(image_gris)
#pl.show()

carre=100

def moyenne_gris_image(image_gris,x,y):
    moyenne=0
    longueur=len(image)
    largeur=len(image[0])
    for i in range(x-carre,x+carre):
        for j in range (y-carre,y+carre):
            moyenne+=image_gris[i][j][0]
    return moyenne//(4*carre^2)

def transform_to_bw (image_gris):
    #moyenne=moyenne_gris_image(image_gris)
    longueur=len(image)
    largeur=len(image[0])
    for i in range(carre,longueur-carre):
        for j in range (carre,largeur-carre):
            moyenne=moyenne_gris_image(image_gris,i,j)
            if moyenne>=image_gris[i][j][0]:
                image_gris[i][j][0]=255
                image_gris[i][j][1]=255
                image_gris[i][j][2]=255
            else:
                image_gris[i][j][0]=0
                image_gris[i][j][1]=0
                image_gris[i][j][2]=0
    return image_gris

image_bw=transform_to_bw(image)
imshow(image_bw)
pl.show()