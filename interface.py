import tkinter as tk
from tkinter.filedialog import *
import numpy as np
from cv2 import cv2
import time
import time
import numpy
from copy import deepcopy
from image_to_bin import *
from image_to_grid import *
from contours import *
from affichage_grille import *
from remplir_grille1 import *
from resol_grille import *
from resolution_backtracking import *
from transform import *

image="test"

def recherche_fichiers():
    image = askopenfilename(filetypes=[("PNG","*.png"),("JPG","*.jpg")], title="Choisissez votre fichier")
    grille=picture_to_grid(image)
    grid=traiter_grille(grille)
    grid_reso=resol(grid)
    affich_2(grid_reso,grid)



def photo_prise():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RETURN:
            return True



###PRENDRE PHOTO
def prendre_photo():
    pygame.init()
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`

    while(True):
        while  not photo_prise():
            ret,im = cap.read()
            cv2.imshow('video test',im)
            key = cv2.waitKey(10)
            cv2.imshow('img1',frame) #display the captured image
            if cv2.waitKey(1) :
                cv2.imwrite('C:/Users/trisr/sudoku/grille.png',frame) #changer le chemin
                cv2.destroyAllWindows()
                break
            if cv2.getWindowProperty("frame", 1) == -1:
                break

    cap.release()
    time.sleep(0.1)
    cv2.destroyAllWindows()


def change_boucle():
    global boucle
    boucle=False

def prendre_photo2():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # video capture source camera (Here webcam of laptop)
    ret,frame = cap.read() # return a single frame in variable `frame`
    a=time.time()
    b=a
    while(True):
        while b-a<10 :
            ret,im = cap.read()
            cv2.imshow('video test',im)
            key = cv2.waitKey(10)
            b=time.time()
        ret,im1= cap.read()
        cv2.imshow('video test',im1)
        key = cv2.waitKey(10)
        ret,frame = cap.read()
        cv2.imshow('img1',frame) #display the captured image
        if cv2.waitKey(1) :
            cv2.imwrite('C:/Users/trisr/sudoku/grille.png',frame) #changer le chemin
            cv2.destroyAllWindows()
            break
        if cv2.getWindowProperty("frame", 1) == -1:
                break
    cap.release()
    time.sleep(0.1)
    cv2.destroyAllWindows()
    return ('C:/Users/trisr/sudoku/grille.png')


def tk_interface():
    window=Tk()
    window.title("Sudoku Resolver")
    label = Label(window, text="Rentrez ici votre image de sudoku à résoudre :")
    label.pack()

    bouton_choix1 = Button(window, text="Je souhaite télécharger ma photo", activebackground="grey", command=recherche_fichiers)
    bouton_choix2 = Button(window, text="Je souhaite prendre une photo avec la webcam", command=prendre_scan) #lancer le scan de la grille
    bouton_choix3 = Button(window, text="Je souhaite remplir la grille", command=remplir_la_grille) # lancer le remplissage manuscrit de la grille
    bouton_choix1.pack()
    bouton_choix2.pack()
    bouton_choix3.pack()
    window.mainloop()


def prendre_scan():
    nom=prendre_photo2()
    image=cv2.imread(nom)
    grille=picture_to_grid(image)
    grille,grille_reso=traiter_grille(grille)
    affich_2(grille_reso,grille)


def remplir_la_grille():
    mat = numpy.zeros((9,9))
    grille=remplir_grille(mat,0)
    grille_reso=resol(grille)
    affich_2(grille_reso,grille)

tk_interface()