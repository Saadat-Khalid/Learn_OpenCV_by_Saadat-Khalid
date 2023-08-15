# Chapter: 17
## How to see the image side by side
### Image Stacking * Horizontal Stacking * Vertical Stacking

import cv2 as cv
import numpy as np

def resizing_img(img, img1):
    # Resize the second image to have the same height as the first image
    height, width = img.shape[:2]
    img1_resized = cv.resize(img1, (width, height))
    return img1_resized

img = cv.imread("FILE PATH")
img1 = cv.imread("FILE PATH")

img1_resized = resizing_img(img, img1)

# 1: Horizontal Stacking
hor_img = np.hstack((img, img1_resized))

# 2: Vertical Stacking
ver_img = np.vstack((img, img1_resized))

# Display
cv.imshow("Horizontal", hor_img)
cv.imshow("Vertical", ver_img)

cv.waitKey(0)
cv.destroyAllWindows()
