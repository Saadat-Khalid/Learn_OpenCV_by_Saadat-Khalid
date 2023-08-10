# Chapter: 4 
## Converintg into black and white

import cv2 as cv

img = cv.imread("FILE PATH") # Reading the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converting into gray scale

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # convering into Black&White

#Display
cv.imshow("Original Color", img)
cv.imshow("Gray", gray)
cv.imshow("Black & White", binary)

cv.waitKey(0)
cv.destroyAllWindows()