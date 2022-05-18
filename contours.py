
import cv2 as cv
import numpy as np


img = cv.imread('./images/img_1.jpg')

#cv.imshow('Image One', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale IM1', gray)

#blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny IM1', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh IM1', thresh)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours identified!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)
