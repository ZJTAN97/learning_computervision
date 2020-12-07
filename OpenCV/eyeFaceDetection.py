import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in image
img = cv2.imread('Images/eye_face.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Classifiers
faceClassifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eyeClassifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')


# Function to detect both eyes and faces
def detect_faceAndEyes(img):
    # detectMultiScale(img, scaleFactor, minNeighbors)
    face_rects = faceClassifier.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in face_rects:
        # (img, (start_point), (end_point), color, thickness)
        cv2.rectangle(img, (x,y), (x+w, y+h),
                      (255,255,255), 10)

        eye_rects = eyeClassifier.detectMultiScale(img)
        for (ix,iy,iw,ih) in eye_rects:
            cv2.rectangle(img, (ix,iy), (ix+iw, iy+ih),
                         (0,0,255), 20)

    plt.figure(figsize=(12,10))
    
    return plt.imshow(img)


detect_faceAndEyes(img)
plt.show()