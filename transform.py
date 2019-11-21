#for this file you'll need to install opencv with the command pip install opencv-python
import numpy as np
import cv2


#points order: top-left,top-right, bottom-right, bottom-left
#corners come from the transformed black and white image
def order_points(corners):
    pts=[]
    leftest=corners[0]
    for k in range(1,4):
        if leftest[0]>corners[k][0]:
            leftest=corners[k]
    pts.append(leftest)
    remaining_pts=corners.copy()
    remaining_pts.remove(leftest)
    scd_leftest= remaining_pts[0]
    for k in range(1,3):
        if scd_leftest[0]>remaining_pts[k][0]:
            scd_leftest=remaining_pts[k]
    pts.append(scd_leftest)
    remaining_pts.remove(scd_leftest)
    pts.append(remaining_pts[0])
    pts.append(remaining_pts[1])
    top_left=pts[0]
    bottom_left=pts[1]
    top_right=pts[2]
    bottom_right=pts[3]
    if pts[1][1]>top_left[1]:
        top_left=pts[1]
        bottom_left=pts[0]
    if pts[3][1]>top_right[1]:
        top_right=pts[3]
        bottom_right=pts[2]
    return [ list(bottom_left), list(bottom_right), list(top_right), list(top_left)]

#the transform should be applied on the original image with the corners

def four_point_transform(img, corners):
    rect = order_points(corners)
    rect=np.array(rect, dtype= "float32")
    (bl, br, tr, tl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    grid_size=max(int(widthA), int(widthB), int(heightA), int(heightB))
    dst = np.array([ [0, 0], [grid_size-1, 0],	[grid_size-1, grid_size-1], [0, grid_size-1]], dtype = "float32")
    matrix = cv2.getPerspectiveTransform( rect, dst)
    warped_img = cv2.warpPerspective(img, matrix ,(grid_size, grid_size))
    return warped_img

