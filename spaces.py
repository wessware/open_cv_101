import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('./images/img_1.jpg')
cv.imshow('Image I', img)


plt.imshow(img)
plt.show()

"""
# BGR tp Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# BGR to HSV (Hue Saturation Value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR to LAB (L*A*B)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
"""
# cv.waitKey(0)
