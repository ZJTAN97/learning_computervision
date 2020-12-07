# This script is for detecting characters using Tesseract.

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Printing out the texts found in strings
print(pytesseract.image_to_string(img))

# Printing out the bounding boxes parameters
print(pytesseract.image_to_boxes(img))

heightImg, widthImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():

    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    # Placing Bounding Boxes for the Characters Identified
    cv2.rectangle(img, (x, heightImg-y), (w, heightImg-h), (0,0,255), 2)
    # Placing the corresponding characters below the boxes
    cv2.putText(img, b[0], (x,heightImg-y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,0), 2)



cv2.imshow('Result', img)
cv2.waitKey(0)

