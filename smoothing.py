import cv2 as cv


img = cv.imread('./images/img_7.jpg')
cv.imshow('Image 7', img)


# BLuRRING

# i. Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average BLur', average)

# Gaussian BLur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussain Blur', gauss)


# Median BLur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
cv.waitKey(0)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 35, 15)
cv.imshow('Bilateral', bilateral)
