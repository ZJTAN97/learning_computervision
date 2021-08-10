import cv2 as cv 

img = cv.imread('Resources/Photos/park.jpg')

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# Blur -- to reduce noise
# increase kernel size to blur more
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


# Edge Cascade (find the edges in the image)
canny = cv.Canny(img, 125, 175)
canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)
cv.imshow('Reduce edges with blur', canny_blur)


# Dilating the image (make edges line thicker)
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)


# Eroding the image (make edges line thinner)
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)


# Resize
# cv.INTER_CUBIC -> slowest but highest quality
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)