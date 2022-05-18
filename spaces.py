import cv2 as cv


img = cv.imread('./images/img_1.jpg')
cv.imshow('Image I', img)

"""
# BGR tp Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)
"""
# BGR to HSV (Hue Saturation Value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


cv.waitKey(0)
