# CHAPTER 1 READ IMAGES VIDEO WEBCAM
import cv2

# ----- Import Images -----#
img = cv2.imread('lena.png')
cv2.imshow('Ouptut', img)
cv2.waitKey(1000)  # 1second delay

# ----- Import Videos -----#
cap = cv2.VideoCapture('test_video.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    # adds a delay and if you press 'q' it stops.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ----- Using Webcam -----#
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 is idNumber for width
cap.set(4, 380)  # 4 is idNumber for height
cap.set(10, 100)  # 10 is idNumber for brightness

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    # adds a delay and if you press 'q' it stops.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break