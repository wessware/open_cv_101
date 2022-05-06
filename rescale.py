import cv2 as cv

# image displaying


"""
img = cv.imread('./images/img_1.jpg')


cv.imshow('Image_One', img)
"""


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# video displaying

capture = cv.VideoCapture('./videos/vid_1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
