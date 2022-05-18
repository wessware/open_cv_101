
import cv2 as cv


img = cv.imread('./images/img_1.jpg')

cv.imshow('Image One', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale IM1', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny IM1', canny)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours identified!')


cv.waitKey(0)
