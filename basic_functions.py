import cv2 as cv


img = cv.imread('./images/img_2.jpg')
cv.imshow('Image 3', img)


"""
# converting image to gratscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image 3', gray)
"""
# image blur
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blur', img)


cv.waitKey(0)
