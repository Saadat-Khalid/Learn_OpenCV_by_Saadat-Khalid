# Chapter: 6
## Reading Video

import cv2 as cv

cap = cv.VideoCapture("FILE")

# Indicators
if (cap.isOpened() == False):
    print("error in reading video")

# Reading & Playing

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()