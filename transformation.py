import cv2 as cv
import numpy as np


img = cv.imread('./images/img_1.jpg')

cv.imshow('Image One', img)


# Image translation
def translate(img, x, y):

    transMat = np.float32([[1, 0, x], [0, 1, y]])

    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# (-x) ====> left
# (-y) ====> up
# (x) =====> right
# (y) =====> down


translated = translate(img, -100, 100)
cv.imshow('Translated Image', translated)

# image rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# positive angles for anticlockwise, negative angles for clockwise
rotated = rotate(img, 45)
cv.imshow('Rotated Image', rotated)


cv.waitKey(0)
