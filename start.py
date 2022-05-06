from tkinter import Frame
import cv2 as cv


#img = cv.imread('./images/img_1.jpg')


#cv.imshow('Image_One', img)
capture = cv.VideoCapture('./videos/vid_1.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
