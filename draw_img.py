

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

# drawing a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# draw line
cv.line(blank, (100, 250), (300, 400), (0, 255, 0), thickness=3)
cv.imshow('Line', blank)
cv.waitKey(0)
