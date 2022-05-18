import cv2 as cv


img = cv.imread('./images/img_7.jpg')
cv.imshow('Image 7', img)


# BLuRRING
# i. Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average BLur', average)

# Gaussian BLur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussain Blur', gauss)

cv.waitKey(0)
