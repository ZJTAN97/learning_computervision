"""
contours and edges are 2 different things
"""

import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blurred', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, type=cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
"""
contours --> a python list of all the coordinates of all the contours
RETR_LIST --> returns all the contours that is found in the image
CHAIN_APPROX_NONE --> return all contours
"""
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)