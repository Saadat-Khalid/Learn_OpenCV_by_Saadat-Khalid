# Chapter: 13
## CV functions for manipulation of Image

import cv2 as cv
import numpy as np

img = cv.imread("Image Path")

# Resize
resized_img = cv.resize(img, (350, 250))

# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurred Image
gaussian_img = cv.GaussianBlur(img, (23, 23), 0)
# median_img = cv.medianBlur(img, (23, 23), 0)
blur_img = cv.blur(img, (23, 23), 0)

# Edge Detection
canny_img = cv.Canny(img, 53, 53)

# Thickness of lines
mat_kernel = np.ones((3,3), np.uint8)
dialated_img = cv.dilate(canny_img, (mat_kernel), iterations=1)

# Make thinner outline
ero_img = cv.erode(dialated_img, mat_kernel, iterations=1)

# Cropping we will use numpy library not open cv
croped_image = img[0:476:, 0:400]

cv.imshow("Orginal", img)
cv.imshow("Resized", resized_img)
cv.imshow("Gray", gray_img)
cv.imshow("Blur", blur_img)
cv.imshow("Gaussian", gaussian_img)
# cv.imshow("Median", median_img)
cv.imshow("Edge Detection", canny_img)
cv.imshow("Dilated", dialated_img)
cv.imshow("Cropped", croped_image)

cv.waitKey(0)
cv.destroyAllWindows()