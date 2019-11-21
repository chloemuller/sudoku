from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

P=1./50 #portion de l'image totale pour calculer la moyenne locale

def pngToGrey (fichier) : #à partir du nom de fichier renvoie un tableau de nuance de gris
    imgpil = Image.open(fichier)
    img = np.array(imgpil)
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





























from digit_recognition import *
import cv2
from pylab import imread, imshow, show
from copy import deepcopy
from numpy import *


#pip install digit-recognition

def bitmap_to_usable(nom_image):
    #fonctionne seulement pour une image en bitmap (donc ça c'est juste une fonction pour tester)
    imor = imread(nom_image)
    print(imor)
    im = [[0 for i in range(len(imor))] for j in range(len(imor[0]))]
    im = array(im)
    for i in range(len(imor)):
        for j in range(len(imor)):
            if imor[i][j][0] == 255 :
                im[i][j] = 0
            else :
                im[i][j] = 1
    return im






def decoupage(nom_image):
    grey = pngToGrey(nom_image)
    im = greyToBin(grey)
    # imshow(im)
    # show()
    #on va découper la grille en 81 cases
    size = len(im)
    cell_size = size//9 #in pixels
    cells = []
    # print("cell size", cell_size)
    # print("image", im)
    # print("image", len(im[0]))
    for row in range(9):
        for column in range(9):
            cells.append(extract_cell(row, column, im, cell_size))
    # for cell in cells :
    #     imshow(cell)
    #     show()
    return cells

def extract_cell(row, column, image, cell_size):
    left_boundary = row*cell_size
    right_boundary = (row+1)*cell_size
    up_boundary = column*cell_size
    down_boundary = (column+1)*cell_size
    cell = array([[0 for i in range(cell_size)] for j in range(cell_size)])
    for i in range(left_boundary, right_boundary):
        for j in range(up_boundary, down_boundary):
            iprime = i-left_boundary    #les indices primes representent les indices de la cellule
            jprime = j-up_boundary
            cell[iprime][jprime] = image[i][j]
    return cell


def extract_amas(cell):
    size_cell = len(cell)
    carte = [[-1 for i in range(size_cell)] for j in range(size_cell)]
    milieu = size_cell//2
    front = [(milieu, milieu)]
    carte[milieu][milieu] = 1
    while not noir_in_front(front, cell)[0]:
        front, carte = front_superieure(front, carte, cell)
    pixels_noirs = noir_in_front(front, cell)[1]
    amas = pixels_noirs
    amas = grossir_amas(cell, amas, carte)
    return amas


def grossir_amas(cell, amas, carte):
    amas_a_grossi = True 
    while amas_a_grossi :
        amas_a_grossi = False
        for pixel in amas :
            for voisin in pixels_voisins(pixel):
                i, j = voisin
                if i < len(cell) and j < len(cell) :
                    if carte[i][j] == -1 :
                        if cell[i][j] == 0:
                            amas.append((i,j))
                            amas_a_grossi = True
                            carte[i][j] = 0
                        else :
                            carte[i][j] = 1
    return amas


def noir_in_front(front, cell):
    pixels_noirs = []
    for pixel in front :
        i, j = pixel
        if cell[i][j] == 0 :
            pixels_noirs.append(pixel)
    if pixels_noirs != [] :
        return True, pixels_noirs
    else :
        return False, []


def front_superieure(front, carte, cell):
    nouvelle_front = []
    for pixel in front :
        for voisin in pixels_voisins(pixel):
            i, j = voisin
            if carte[i][j] == -1 :
                nouvelle_front.append(voisin)
                if cell[i][j] == 1 :
                    carte[i][j] = 1
                else :
                    carte[i][j] = 0
    return nouvelle_front, carte



def pixels_voisins(pixel):
    i, j = pixel
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]

def amas_to_28pixels(amas):
    #On centre d'abord le nombre extrait dans le premier 
    hauteur = max([pixel[0] for pixel in amas]) - min([pixel[0] for pixel in amas])
    largeur = max([pixel[1] for pixel in amas]) - min([pixel[1] for pixel in amas])
    espace_vide_gauche = min([pixel[0] for pixel in amas])
    espace_vide_haut = min([pixel[1] for pixel in amas])
    surplus = abs(hauteur-largeur)//2
    border = int(max(hauteur, largeur)*0.2)
    if hauteur > largeur :
        number_size = hauteur  #la taille du nombre dans un carré
        decallage_horizontal = espace_vide_gauche - border//2
        decallage_vertical = espace_vide_haut - surplus - border//2
    else :
        number_size = largeur
        decallage_horizontal = espace_vide_gauche - surplus - border//2
        decallage_vertical = espace_vide_haut - border//2
    cell_size = number_size + border
    image = array([[0 for i in range(cell_size)] for j in range(cell_size)])
    for i in range(cell_size):
        for j in range(cell_size):
            if (i + decallage_horizontal, j + decallage_vertical) in amas :
                image[i][j] = 1
    cv2_image = convert_bitmap_to_cv2(image)
    cv2_resized_image = cv2.resize(cv2_image, (28,28))
    resized_image = convert_cv2_to_bitmap(cv2_resized_image)
    return resized_image

def convert_bitmap_to_cv2(bitmap_image):
    cv2_image = zeros(list(bitmap_image.shape) + [3])
    for i in range(bitmap_image.shape[0]):
        for j in range(bitmap_image.shape[1]):
            if bitmap_image[i][j] == 0 :
                for c in range(3):
                    cv2_image[i][j][c] = 0
            else :
                for c in range(3):
                    cv2_image[i][j][c] = 255
    return cv2_image

def convert_cv2_to_bitmap(cv2_image):
    bitmap_image = zeros(list(cv2_image.shape[:2]))
    for i in range(cv2_image.shape[0]):
        for j in range(cv2_image.shape[1]):
            if cv2_image[i][j][0] == 255 :
                bitmap_image[i][j] = 1
            else :
                bitmap_image[i][j] = 0
    return bitmap_image

            
def interpret(output):
    maximum = max(output)
    return list(output).index(maximum)

def predict(image):
    weights = np.load("my_network.npy", allow_pickle = True)
    neural_network = NeuralNetwork([784,200,100,10], weights = weights, bias=True)
    print(neural_network.run(image))
    print(max(neural_network.run(image)))
    return interpret(neural_network.run(image))

# train_images, train_labels, test_images, test_labels = pre_processing()
# weights = np.load("my_network.npy", allow_pickle = True)
# neural_network = NeuralNetwork([784,200,100,10], weights = weights, bias=True)
# neural_network.evaluate(test_images, test_labels)

# for nom_image in ["un.bmp", "deux.bmp", "trois.bmp", "quatre.bmp", "cinq.bmp", "six.bmp", "sept.bmp", "huit.bmp", "neuf.bmp"]:
#     image = bitmap_to_usable(nom_image)
#     print(nom_image, interpret(neural_network.run(image)))



cells = decoupage("sudoku_moche.png")
im = amas_to_28pixels(extract_amas(cells[0]))
print(list(im))
# for i in range(81):
#     amas = extract_amas(cells[i])
#     im = amas_to_28pixels(amas)
#     print(predict(im))
#     imshow(im)
#     show()

    


# test = cv2.imread("sudoku_moche.png")
# print(test)
# resized_image = cv2.resize(test, (28,28))
# print(type(resized_image))
# print(len(resized_image))
# print(len(resized_image[0]))
# cv2.imshow("test", resized_image)
