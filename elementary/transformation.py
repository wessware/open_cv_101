import cv2 as cv
import numpy as np


img = cv.imread('./images/img_1.jpg')

cv.imshow('Image One', img)

"""
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

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated Image', rotated_rotated)

# image resizing

resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image', resize)

# image flipping
# flip codes 0 => flip vertical,1 => flip horizontal,-1 => flip vertical & horizontal

# vertical
flip = cv.flip(img, 0)
cv.imshow('Flipped Vertical', flip)
# horizontal
flip = cv.flip(img, 1)
cv.imshow('Flipped Horizontal', flip)

flip = cv.flip(img, -1)
cv.imshow('Flipped Vertical Horizontal', flip)

"""
# image cropping
crop = img[200:400, 300:400]
cv.imshow('Cropped', crop)

cv.waitKey(0)
