from PIL import Image
import numpy as np
from pylab import *
import matplotlib.pyplot as pl

fichier="Images/sudo.jpg"
photo=Image.open(fichier)
image=np.array(photo)

def transform_to_grey (image):
    longueur=len(image)
    largeur=len(image[0])
    image_gris=[[[0,0,0] for j in range (largeur)]for i in range (longueur)]
    for i in range(longueur):
        for j in range (largeur):
            moy=(int(image[i][j][0])+int(image[i][j][1])+int(image[i][j][2]))//3
            print(moy)
            image_gris[i][j][0]=moy
            image_gris[i][j][1]=moy
            image_gris[i][j][2]=moy
    return image_gris

image_gris=transform_to_grey(image)
#imshow(image_gris)
#pl.show()

carre=10

def moyenne_gris_image(image_gris,x,y):
    moyenne=0
    for i in range(x-carre,x+carre+1):
        for j in range (y-carre,y+carre+1):
            moyenne+=image_gris[i][j][0]
    return moyenne//((2*carre+1)**2)



def transform_to_bw (image_gris):
    (longueur,largeur,x)=np.shape(image_gris)
    moyenne=0
    Moy=[[]]

    for j in range (1+carre,largeur-carre+1):
        for k in range(2*carre+1):
            for l in range (j-carre, j+carre):
                moyenne+=image_gris[k][l][0]//((2*carre+1)**2)
                Moy[0]+=[moyenne]

    for i in range(1+carre,longueur-carre+1):
        #calcul de la moyenne
        moyenne=Moy[i-carre-1][0]
        for k in range(2*carre+1):
            moyenne-=image_gris[i-carre][k][0]//((2*carre+1)**2)
            moyenne+=image_gris[i+carre][k][0]//((2*carre+1)**2)
        Moy+=[[moyenne]]
        print(Moy)

        for j in range (1+carre,largeur-carre+1):
            #calcul de la moyenne
            print(i,j)
            moyenne=Moy[i-carre][j-carre-1]
            for k in range (i-carre,i+carre):
                moyenne-=image_gris[k][j-carre][0]//((2*carre+1)**2)
                moyenne+=image_gris[k][j+carre][0]//((2*carre+1)**2)
            Moy[i-carre]+=[moyenne]
            print(Moy)
            del(Moy[i-carre-1])
            print(Moy)

            if moyenne>image_gris[i][j][0]:
                image_gris[i][j][0]=255
                image_gris[i][j][1]=255
                image_gris[i][j][2]=255
            else:
                image_gris[i][j][0]=0
                image_gris[i][j][1]=0
                image_gris[i][j][2]=0
    return image_gris

imshow(transform_to_bw(image_gris))
pl.show()
