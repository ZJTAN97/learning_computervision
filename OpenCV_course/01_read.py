import cv2 as cv

# Reading Image
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0) # waits until a keyboard key is pressed

# Reading Video
# to use your own webcam
# capture = cv.VideoCapture(0) 

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()