# CHAPTER 9 - FACE DETECTION
import cv2
import os
import zipfile
import shutil
from os import getcwd

path = f'{getcwd()}/haarcascades.zip'
local_zip = path
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

faceCascade = cv2.CascadeClassifier('/tmp/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)