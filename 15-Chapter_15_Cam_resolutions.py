# Chapter: 15
## working with cameras resolutions

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def sd_resolutions():
    cap.set(3, 1280)
    cap.set(4, 720)

def hd_resolutions():
    cap.set(3, 640)
    cap.set(4, 480)

def fhd_resolutions():
    cap.set(3, 1920)
    cap.set(4, 1080)


def set_frame_rate():
    cap.set(cv.CAP_PROP_FPS, 30)

# sd_resolutions()
# hd_resolutions()
fhd_resolutions()
set_frame_rate()

while(True):
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv.imshow("Cam", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()