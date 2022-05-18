import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('./images/img_1.jpg')
cv.imshow('Image I', img)

"""
plt.imshow(img)
plt.show()


# BGR tp Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# BGR to LAB (L*A*B)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
"""

# BGR to HSV (Hue Saturation Value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# HSV - BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -- BGR', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
