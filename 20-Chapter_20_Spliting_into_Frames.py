# Chapter: 20
## Split your video into frames/image sequence

import cv2 as cv

cap = cv.VideoCapture("File Path")

frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"file path/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+2

cap.release()