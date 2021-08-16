import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

# histogram for grayscale images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.bitwise_and(gray, gray, mask=circle)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
cv.imshow('mask', mask)


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# histogram for colored images
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
colors = ('b', 'g' ,'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)