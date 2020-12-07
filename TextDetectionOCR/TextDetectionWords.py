import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

img = cv2.imread('2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

heightImg, widthImg, _ = img.shape
config_digits = r'--oem 1 --psm 6 outputbased digits'
config_words = r'--oem 1 --psm 6'
boxes = pytesseract.image_to_data(img, config=config_words)
#print(boxes)


for x,b in enumerate(boxes.splitlines()):

    if x!=0:

        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            # Placing Bounding Boxes for the Characters Identified
            cv2.rectangle(img, (x, y), (w+x, h+y), (0,0,255), 3)
            # Placing the corresponding characters below the boxes
            cv2.putText(img, b[11], (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,200,0), 2)
    


cv2.imshow('Result', img)
cv2.waitKey(0)