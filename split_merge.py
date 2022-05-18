import cv2 as cv
import numpy as np


img = cv.imread('./images/img_7.jpg')
cv.imshow('Image I', img)

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


cv.waitKey(0)
