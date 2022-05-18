import cv2 as cv


img = cv.imread('./images/img_7.jpg')
cv.imshow('Image 7', img)


# BLuRRING
# i. Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average BLur', average)

cv.waitKey(0)
