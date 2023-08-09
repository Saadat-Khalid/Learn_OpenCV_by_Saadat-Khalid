# Chapter: 3 
## Converintg into grayscale

# Library Import

import cv2 as cv
from cv2 import cvtColor #color conversion

img = cv.imread("FILE PATH")

## Conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

#Displays an image in a window.
cv.imshow("WINDOWS TEXT", img)
cv.imshow("GrayScale Image", gray_img)


cv.waitKey(0)
cv.destroyAllWindows()