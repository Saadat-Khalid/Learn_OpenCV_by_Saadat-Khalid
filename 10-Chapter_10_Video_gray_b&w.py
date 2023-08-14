# Chapter: 10
## Video in Gray and Black&White

from tkinter import Frame 
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

if (cap.isOpened() == False):
    print("There's some error.")

while(True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY) # convering into Black&White

    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("Black&WhiteCam", binary)

    #to quit with q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release or close window

cap.release()
cv.destroyAllWindows()