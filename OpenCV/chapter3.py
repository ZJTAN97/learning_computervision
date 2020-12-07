# CHAPTER 3 CROP & RESIZE
import cv2
import numpy as np

# Resize Image
img = cv2.imread('lambo.png')
print(img.shape) # (height, width, RGB)
cv2.imshow('Image', img)

imgResize = cv2.resize(img, (300,200)) #(width, height)
print(imgResize.shape)
cv2.imshow('Image Resize', imgResize)

# Cropping Image
imgCropped = img[0:200, 200:500] # height, width
cv2.imshow('Image Cropped', imgCropped)

cv2.waitKey(0)