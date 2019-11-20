import cv2
import copy
from transform import *


def corners_sudoku(image):
    # utilisation de la fonction findcontours
    cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)==2:
        cnts=cnts[0]
    else :
        cnts=cnts[1] 
    # le mode CHAIN_APPROX_SIMPLE sort une liste de points permettant de tracer le contour on veut le contour le plus grand
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    cadre=cnts[0]
    # on ne cheche que les quatres coins on fai donc des approximations pour les trouver ( négligeant les courbures)
    approx=cadre
    while len(approx)>4:
        peri = cv2.arcLength(cadre, True)   #calcul du périmètre du cadre trouvé
        approx = cv2.approxPolyDP(approx, 0.015 * peri, True) #approximation du polygone(le cadre du sudoku) avec un autre polygone plus simple (moins de côtés) avec un epsilon de 0.015*perimètre jusqu'à ce qu'il y ait de quatre côtés.
    # la liste des coins est mise au bon format
    corners=[]
    for c in approx:
        corners.append(list(c[0]))    
    return corners

def get_clean_grid(image):
    warped=four_point_transform(image,corners_sudoku(image))
    return warped
