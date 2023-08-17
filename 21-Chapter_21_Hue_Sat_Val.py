# Chapter: 21
## Hue, Saturation, Value

import cv2 as cv
import numpy as np

def slider():
    pass


path = "FILE PATH"

cv.namedWindow("Bars")
cv.resizeWindow("Bars", 640, 300)

cv.createTrackbar("Hue Min", "Bars", 0,179, slider)
cv.createTrackbar("Hue Max", "Bars", 179,179, slider)
cv.createTrackbar("Sat Min", "Bars", 0,255, slider)
cv.createTrackbar("Sat Max", "Bars", 255,255, slider)
cv.createTrackbar("Val Min", "Bars", 0,255, slider)
cv.createTrackbar("Val Max", "Bars", 255,255, slider)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min", "Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Bars")
    sat_min = cv.getTrackbarPos("Sat Min", "Bars")
    sat_max = cv.getTrackbarPos("Sat Max", "Bars")
    val_min = cv.getTrackbarPos("Val Min", "Bars")
    val_max = cv.getTrackbarPos("Val Max", "Bars")
    print(hue_max, hue_max, sat_min, sat_max, val_min, val_max)

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv.inRange(hsv_img, lower, upper) # masking the image with range of values
    out = cv.bitwise_and(img , img, mask=mask)

    cv.imshow("Mask", mask)
    cv.imshow("Final", out)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()