

import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow('Blank', blank)

#img = cv.imread('./images/img_2.jpg')
#cv.imshow('Img', img)

#blank[200:300, 300:400] = 255, 255, 0
#cv.imshow('Green', blank)

# drawing a rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
