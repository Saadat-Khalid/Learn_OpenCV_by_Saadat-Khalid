# Chapter: 9
## How to capture a webcam inside python

# Step: 1 Import Libraries
import cv2 as cv
import numpy as np

# Step: 2 Read the Frames from Camera

cap = cv.VideoCapture(0) #webcam no.1 (1 for webcame no.2)

if (cap.isOpened() == False):
    print("There's some error.")

#  Step: 3 Display the cam frame by frame

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #to display frame
        cv.imshow("Frame", frame)
        
        #to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release or close window

cap.release()
cv.destroyAllWindows()