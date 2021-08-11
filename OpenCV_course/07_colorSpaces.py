import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg') # BGR IMAGE
cv.imshow('Boston', img)

# plt.imshow(img) # matplotlib displays RGB image, OpenCV by default display BGR Image
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR TO L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()


cv.waitKey(0)

"""
OpenCV allows you to convert BGR to the above following and reverse.
However it is not possible to convert GRAY2HSV .. etc.. you have to convert back to BGR first.
"""