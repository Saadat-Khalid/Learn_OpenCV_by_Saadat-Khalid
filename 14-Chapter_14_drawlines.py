# Chapter: 14
## How to draw shapes, and lines in Python

import cv2 as cv
import numpy as np

# Draw a Canvas "0 is for black" "1 is for whites"
black = np.zeros((600,600))
white = np.ones((600,600))

# Additing Colors to Canvas
colored_img = np.zeros((600,600, 3), np.uint8) # 1: color channel addition
colored_img[:] = 225,170,235 #complete colored image
colored_img[150:230, 100:500] = 140,110,150

# adding line
cv.line(colored_img, (0,0), (300,300), (255,0,0), 3)
cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]), (215,100,0), 3)

# adding rectangles
cv.rectangle(colored_img, (50,90), (300,400), (255,0,0), 3)
cv.rectangle(colored_img, (100,110), (500,550), (255,55,100), cv.FILLED)

# adiing circle
cv.circle(colored_img, (30, 60), 50, (255,60,88), cv.FILLED)

# adding text 
cv.putText(colored_img, "Learning OpenCV - Saadat Khalid", (130,300), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,180,190), 1)


# cv.imshow("Black", black)
# cv.imshow("White", white)
# cv.imshow("Colored Image", colored_img)
cv.imshow("Colored Image", colored_img)

cv.waitKey(0)
cv.destroyAllWindows()