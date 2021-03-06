import cv2 as cv


img = cv.imread('./images/img_7.jpg')
cv.imshow('Image 3', img)


"""
# converting image to gratscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image 3', gray)
"""
# image blur
"""
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
#

# Edge cascade
cany = cv.Canny(img, 125, 175)
cv.imshow('Canny', cany)
# 

# image dilation
dilated = cv.dilate(cany, (7, 7), iterations=3)
cv.imshow('Dilated Image', dilated)

# image eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded Image', eroded)

# image resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized Image 6', resized)
"""
# image cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)
