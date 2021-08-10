import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston Park', img)


# Translation (shifting between x and y axis)
def translate(img, x, y):
    """
    negative x value --> moves left
    negative y value --> moves up
    positive x vlaue --> moves right
    positive y value --> moves down
    """
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # width x height
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    """
    positive value --> anti-clockwise
    negative value --> clockwise
    """
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2) # take middle
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flipping
"""
0 -> flip vertically
1 -> flip horizontally
-1 -> flipping vertically & horizontally
"""
flipped = cv.flip(img, 1)
cv.imshow('Flip', flipped)


# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)