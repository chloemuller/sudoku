from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

P=1./50 #portion de l'image totale pour calculer la moyenne locale

def pngToGrey (img) : #à partir du nom de fichier renvoie un tableau de nuance de gris
    t=[]
    for x in img :
        t.append ([])
        for y in x :
            s=int(y[0])+int(y[1])+int(y[2])
            t[-1].append (s/3)
    return t

def showGrey (t) : #afficher un tableau de nuance de gris
    tbis=[]
    for x in t :
        tbis.append ([])
        for y in x :
            tbis[-1].append ([y,y,y])
    plt.imshow(tbis)
    plt.show()

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