import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)  

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

warning_count = 0
max_warnings = 5  
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:

            gaze_deviation_x = random.randint(ex, ex + ew)
            gaze_deviation_y = random.randint(ey, ey + eh)

            left_threshold = ex + ew // 4
            right_threshold = ex + ew * 3 // 4
            up_threshold = ey + eh // 4
            down_threshold = ey + eh * 3 // 4

            if gaze_deviation_x < left_threshold or gaze_deviation_x > right_threshold:

                warning_count += 1
                print(f"Warning: Gaze deviation detected! Warning count: {warning_count}")

                if warning_count >= max_warnings:
     
                    print("Maximum warnings reached. The exam is restricted.")
                    break

            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("Eye Tracking Simulation", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()