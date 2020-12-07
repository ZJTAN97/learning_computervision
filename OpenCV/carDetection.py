import cv2
import numpy as np

carClassifier = cv2.CascadeClassifier('Haarcascades/haarcascade_car.xml')
cap = cv2.VideoCapture('Videos/Vehicles.mp4')

while cap.isOpened():
    # Read the capture
    ret, frame = cap.read()

    # Pass the Frame to the Classifier
    cars = carClassifier.detectMultiScale(frame, 1.4, 2)

    if ret == True:
        # Bound boxes to Identified Bodies
        for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x,y), (x+w, y+h),
                          (25,125,225), 5)
            cv2.imshow('Cars', frame)
        
        # Exit with Esc Button
        if cv2.waitKey(1) == 27:
            break
    else:
        break

# Release the Capture & Destroy all windows
cap.release()
cv2.destroyAllWindows()