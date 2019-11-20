from PIL import Image
import cv2
import pytesseract
import numpy as np
from pylab import *
import matplotlib.pyplot as pl

fichier="Images/Capture d’écran 2019-11-18 à 11.09.40.png"
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

#image_gris=transform_to_grey(image)
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
    print(Moy)

    for i in range(1+carre,longueur-carre+1):
        #calcul de la moyenne
        moyenne=Moy[i-carre-1][0]
        for k in range(2*carre+1):
            moyenne-=image_gris[i-carre][k][0]//((2*carre+1)**2)
            moyenne+=image_gris[i+carre][k][0]//((2*carre+1)**2)
        Moy+=[[moyenne]]

        for j in range (1+carre,largeur-carre+1):
            #calcul de la moyenne
            moyenne=Moy[i-carre][j-carre]
            for k in range (i-carre,i+carre):
                moyenne-=image_gris[k][j-carre][0]//((2*carre+1)**2)
                moyenne+=image_gris[k][j+carre][0]//((2*carre+1)**2)
            Moy[i-carre]+=[moyenne]
            del(Moy[i-carre-1])

            if moyenne>image_gris[i][j][0]:
                image_gris[i][j][0]=255
                image_gris[i][j][1]=255
                image_gris[i][j][2]=255
            else:
                image_gris[i][j][0]=0
                image_gris[i][j][1]=0
                image_gris[i][j][2]=0
    return image_gris

#imshow(transform_to_bw(image))
#pl.show()



def greyToBin (t) : #tableau de nuance de gris -> tableau de 0/1

    X=len(t)
    Y=len(t[0])
        #On cherche S un tableau de triplet (s,x,y) avec
            #s la somme des nuances de gris dans un rectangle 2PX/2PY autour du pixel
            #x la largeur de la zone (différente vers les bords)
            #y la hauteur de la zone (différente vers les bords)
    s=0
    for i in range (int(P*X)) :
        for j in range (int (P*Y)) :
            s+=int(t[i][j])

    S=[]
    for x in range (X) :
        S.append ([[]]*Y)

    S[0][0]=[s,int(P*X),int (P*Y)]

    for y in range(1,Y) :
        S[0][y]=S[0][y-1][:]
        if (y-1)-(int(P*Y)-1)>=0 :
            for x in range (int(P*X)) :
                S[0][y][0]-=t[x][y-int(P*Y)]
            S[0][y][2]-=1
        if y+int(P*Y)-1<Y :
            for x in range (int(P*X)) :
                S[0][y][0]+=t[x][y+int(P*Y)-1]
            S[0][y][2]+=1

    for y in range (Y) :
        for x in range (1,X) :
            S[x][y]=S[x-1][y][:]
            if (x-1)-(int(P*X)-1)>=0 :
                for j in range (max(0,y-int(P*Y)),min(Y,y+int(P*Y))) :
                    S[x][y][0]-=t[x-int(P*X)][j]
                S[x][y][1]-=1
            if x+int(P*X)-1<X :
                for j in range (max(0,y-int(P*Y)),min(Y,y+int(P*Y))) :
                    S[x][y][0]+=t[x+int(P*X)-1][j]
                S[x][y][1]+=1

        #On en déduit M le tableau des moyennes locales de gris

    M=[]
    for x in S :
        M.append ([])
        for y in x :
            M[-1].append(y[0]//(y[1]*y[2]))

        #On en déduit tbis le tableau binaire gris>moyenne locale

    tbis=[]
    for x in range (X) :
        tbis.append([])
        for y in range (Y) :

            if t[x][y]<M[x][y] :
                tbis[-1].append(0)
            else :
                tbis[-1].append(1)

    return tbis

def showBin (t) : #afficher talbeau de 0/1
    tbis=[]

    for x in t :
        tbis.append ([])
        for y in x :
            if y==0 :
                tbis[-1].append ([255,255,255])
            else :
                tbis[-1].append ([0,0,0])
    plt.imshow(tbis)
    plt.show()


def image_grey (image):
    gray = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#image_grey("Images/sudo.jpg")

Avg=[200,215,220]

def image_bw (image,avg):
    img=cv2.imread(image)
    grey=cv2.imread(image,cv2.IMREAD_GRAYSCALE)
    moyenne = avg
    maxValue = 255
    ok, thr = cv2.threshold(grey, moyenne, maxValue, cv2.THRESH_BINARY)
    cv2.imshow("BW Image", thr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

