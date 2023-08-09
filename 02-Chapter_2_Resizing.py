# Chapter: 2
# Resizing the Image

import cv2 as cv

#Reading
img = cv.imread("FILE PATH")
img2 = cv.imread("FILE PATH")

#Resizing
img = cv.resize(img, (800,600))

#Display
cv.imshow('WINDOWS TEXT', img)
cv.imshow('WINDOWS TEXT', img2)

cv.waitKey(0)
cv.destroyAllWindows()


