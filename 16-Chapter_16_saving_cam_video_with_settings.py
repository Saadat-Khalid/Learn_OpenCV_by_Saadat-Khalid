# Chapter: 16
## Saving and working with cameras resolutions

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

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cv.get(4))

out = cv.VideoWriter("cam_video.mp4", cv.VideoWriter_fourcc('M', 'j', 'P', 'G'), 30, (frame_width, frame_height))

while(True):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        # Display the resulting frame
        cv.imshow("Cam", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()