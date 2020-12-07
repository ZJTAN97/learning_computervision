import cv2
import numpy as np
import matplotlib.pyplot as plt

carPlateClassifier = cv2.CascadeClassifier('Haarcascades/haarcascade_plate_number.xml')

img = cv2.imread('Images/car_plate.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def detect_carPlate(img):

    plate_img = img.copy()
    plate_rects = carPlateClassifier.detectMultiScale(img, 1.1, 1)
    for (x,y,w,h) in plate_rects:
        cv2.rectangle(plate_img, (x,y), (x+w, y+h),
                      (255,255,255), 10)

    return plate_img

img = detect_carPlate(img)
cv2.imshow('Car Plate Detected', img)
cv2.waitKey(0)