import cv2 as cv


img = cv.imread('./images/img_2.jpg')
cv.imshow('Image 3', img)

# converting image to gratscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image 3', gray)
cv.waitKey(0)
