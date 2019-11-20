import cv2
import copy
from transform import *

image = cv2.imread('test.png',0)
original = copy.copy(image)

# passage de l'image en blanc sur noir pour qu'elle puisse ête lue par findcontours
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blur = cv2.medianBlur(gray, 3)
#thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,3)

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
peri = cv2.arcLength(cadre, True)
approx = cv2.approxPolyDP(cadre, 0.015 * peri, True)

# la liste des coins est mise au bon format

corners=[]

for c in approx:
    corners.append(list(c[0]))    


warped=four_point_transform(image,corners)

cv2.namedWindow('Contours')
cv2.imshow('Contours', warped)
cv2.waitKey()