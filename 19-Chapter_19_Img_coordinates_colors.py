# Chapter: 19
## Coordinates of an image
### BGR color codes from an image

import cv2 as cv
import numpy as np

def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, '', y)
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (28,64,40), thickness=2)
        cv.imshow("Image", img)
    
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '', y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255,0,0), 2)
        cv.imshow("Image", img)

if __name__=="__main__":
    img = cv.imread("File Path",1)
    cv.imshow("image", img)
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
