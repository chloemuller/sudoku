import cv2
import copy
from transform import *

image = cv2.imread('sudokutest.jpg',0)
original = copy.copy(image)

# passage de l'image en blanc sur noir pour qu'elle puisse ête lue par findcontours
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blur = cv2.medianBlur(gray, 3)
#thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,3)

# utilisation de la fonction findcontours
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_, cnts, hierarchy = cnts
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)


drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
for i in range(len(cnts)):
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    cv2.drawContours(drawing, cnts, i, color, 2, cv.LINE_8, hierarchy, 0)

cv2.namedWindow('Contours')
cv2.imshow('Contours', drawing)
cv2.waitKey()