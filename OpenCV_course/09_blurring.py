import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats' , img)


# Averaging Blur
"""
higher kernel size --> more blur
"""
average = cv.blur(img, (7,7))
cv.imshow('Averaged Blur', average)



# Gaussian Blur
"""
more natural than average blur
"""
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussianed Blur', gaussian)



# Median Blur
"""
more effective in reducing noise
not meant for high kernel size.
"""
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)



# Bilateral Blur
"""
most effective, applies blurring and return edges in the image
"""
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)




cv.waitKey(0)