# Chapter: 1 
## Reading an image and displaying it

# Library Import

import cv2 as cv
# OpenCV library for image processing.

img = cv.imread("FILE PATH")
#Read the Image from file path or URL.

cv.imshow("WINDOWS TEXT", img)
#Displays an image in a window.
cv.waitKey(0)
#Wait until any key is pressed, then return value is given by parameter.
