from tkinter import *
from tkinter.filedialog import *
import numpy as np
from cv2 import cv2
import time
import pygame
boucle=True

image="test"

def recherche_fichiers():
    global image #important
    image = askopenfilename(filetypes=[("PNG","*.png")], title="Choisissez votre fichier")


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

    window=Tk()
    label=Label(text="Appuyez sur entrer pour prendre la photo")
    label.pack()

    while(True):
        while boucle :
            window.bind("<Return>", change_boucle)
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
    window.mainloop()
    cap.release()
    time.sleep(0.1)
    cv2.destroyAllWindows()



def tk_interface():
    window=Tk()
    window.title("Sudoku Resolver")
    label = Label(window, text="Rentrez ici votre image de sudoku à résoudre :")
    label.pack()

    bouton_choix1 = Button(window, text="Je souhaite télécharger ma photo", activebackground="grey", command=recherche_fichiers)
    bouton_choix2 = Button(window, text="Je souhaite prendre une photo avec la webcam", command=window.quit)
    bouton_choix1.pack()
    bouton_choix2.pack()

    window.mainloop()

prendre_photo()