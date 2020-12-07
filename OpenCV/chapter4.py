# CHAPTER 4 - SHAPES & TEXT
import cv2
import numpy as np

# blank image
img = np.zeros((512,512,3))
print(img.shape)
#img[:] = 255,0,0
#color whole image blue

# Green line (Diagonal all the way)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)

# Rectangle
cv2.rectangle(img, (0,0), (250,350), (0,0,255), cv2.FILLED)

# Circle
cv2.circle(img, (400,50), 30, (255,255,0), 5)

# Text
cv2.putText(img, 'OPENCV', (300,200), cv2.FONT_ITALIC, 1.3, (0,150,0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)