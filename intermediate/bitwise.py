import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND
bitwise_AND = cv.bitwise_and(rectangle, circle)
#v.imshow('Bitwise AND', bitwise_AND)

# bitwise OR
bitwise_OR = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_OR)

cv.waitKey(0)
