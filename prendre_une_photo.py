import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    while  not(prendre_photo()) :
        ret,im = cap.read()
        cv2.imshow('video test',im)
        key = cv2.waitKey(10)
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        cv2.imwrite('images/c1.png',frame)
        cv2.destroyAllWindows()
        break
    if cv2.getWindowProperty("frame", 1) == -1:
        break

cap.release()
time.sleep(0.1)
cap.close()
cv2.destroyAllWindows()


