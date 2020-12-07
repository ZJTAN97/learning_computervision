# CHAPTER 6 - JOINING IMAGES
import cv2
import numpy as np
img = cv2.imread('lena.png')

# Basic Horizontal Stack
imgHor = np.hstack((img,img))
cv2.imshow('Horizontal', imgHor)

# Basic Vertical Stack
imgVer = np.vstack((img,img))
cv2.imshow('Vertical', imgVer)

from utils import stackImages
# stack 2 x 3 normal image
imgStack = stackImages(0.5, ([img,img,img], [img,img,img]))
cv2.imshow('ImageStack', imgStack)

# stack with greyscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack2 = stackImages(0.5, ([img, imgGray,img], [img,imgGray,img]))
cv2.imshow('ImageStack2', imgStack2)
cv2.waitKey(0)