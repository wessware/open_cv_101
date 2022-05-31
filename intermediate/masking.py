import cv2 as cv


img = cv.imread('../images/img_1.jpg')
cv.imshow('Image One', img)

cv.waitKey(0)
