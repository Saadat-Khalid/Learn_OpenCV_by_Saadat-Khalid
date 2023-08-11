# Chapter: 7
## Converting it into B&W and Gray

import cv2 as cv

cap = cv.VideoCapture("F:\\video.m4v")

# Indicators
if (cap.isOpened() == False):
    print("error in reading video")

# Reading & Playing

while(True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY) # convering into Black&White

    #to show in player
    if ret == True:
        cv.imshow("Video", frame) # COlORED
        cv.imshow("Video", grayframe) #GRAY
        cv.imshow("Video", binary) #BLACK&WHITE

        # to quit with q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()