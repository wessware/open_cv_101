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


cv.waitKey(0)
