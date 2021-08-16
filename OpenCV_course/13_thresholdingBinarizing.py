import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
"""
if above 150, set to 1, if not set to 0
"""
cv.imshow('Simple Threshold', thresh)


# Inverse Thresholding
threshold, inv_thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholding', inv_thresh)


# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)



cv.waitKey(0)