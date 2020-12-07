import cv2
import numpy as np

bodyClassifier = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')
cap = cv2.VideoCapture('Videos/People_Walking.mp4')

while cap.isOpened():
    # Read the capture
    ret, frame = cap.read()

    # Pass the Frame to the Classifier
    bodies = bodyClassifier.detectMultiScale(frame, 1.2, 3)

    if ret == True:
        # Bound boxes to Identified Bodies
        for (x,y,w,h) in bodies:
            cv2.rectangle(frame, (x,y), (x+w, y+h),
                          (25,125,225), 10)
            cv2.imshow('Pedestrians', frame)
        
        # Exit with Esc Button
        if cv2.waitKey(1) == 27:
            break
    else:
        break

# Release the Capture & Destroy all windows
cap.release()
cv2.destroyAllWindows()