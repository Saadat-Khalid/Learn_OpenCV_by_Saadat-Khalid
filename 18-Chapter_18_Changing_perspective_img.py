# Chapter: 18
# Changing the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread("")

print(img.shape)

# Defining Points

point1 = np.float32([[233,196], [82,471], [522,169], [715,482]])
width, height = 800,900
point2 = np.float32([[0,0], [width,0], [0,height], [width,height]])

matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Original", img)
cv.imshow("Transformed", out_img)
cv.imwrite("wrap_perspective.png", out_img)
cv.waitKey(0)
cv.destroyAllWindows()
