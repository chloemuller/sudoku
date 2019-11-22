import cv2
import copy
from transform import *


# img=cv2.imread('sudoku-paper-puzzle2.jpg')

def png_to_bin(image):
    im_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    (thresh, im_bw) = cv2.threshold(im_bw, 100, 255, 0)
    return im_bw


def corners_sudoku(image):
    # utilisation de la fonction findcontours
    original=image.copy()
    cnts = cv2.findContours(cv2.bitwise_not(png_to_bin(image)), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)==2:
        cnts=cnts[0]
    else :
        cnts=cnts[1] 
    # le mode CHAIN_APPROX_SIMPLE sort une liste de points permettant de tracer le contour on veut le contour le plus grand
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    cadre=cnts[0]
    # on ne cheche que les quatres coins on fai donc des approximations pour les trouver ( négligeant les courbures)
    approx=cadre
    peri = cv2.arcLength(cadre, True)   #calcul du périmètre du cadre trouvé
    approx = cv2.approxPolyDP(approx, 0.015 * peri, True) #approximation du polygone(le cadre du sudoku) avec un autre polygone plus simple (moins de côtés) avec un epsilon de 0.015*perimètre jusqu'à ce qu'il y ait de quatre côtés.
    # la liste des coins est mise au bon format
    corners=[]
    for c in approx:
        corners.append(list(c[0]))   
    return original, corners

def get_clean_grid(image):
    original, corners=corners_sudoku(image)
    warped=four_point_transform(original,corners)
    return warped


# cv2.namedWindow('noir et blanc')
# cv2.imshow('noir et blanc', cv2.bitwise_not(png_to_bin(img)))
# cv2.namedWindow('l')
# cv2.imshow('l',png_to_bin(img))
# cv2.namedWindow('grille redressée')
# cv2.imshow('grille redressée', get_clean_grid(img))
# cv2.waitKey()