# Chapter: 12
# Settings of Camera or Video

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10, 30) # 10 is the key used for brightness
cap.set(3, 640) # 3 is the key used for width
cap.set(3, 480) # 4 is the key used for height

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()