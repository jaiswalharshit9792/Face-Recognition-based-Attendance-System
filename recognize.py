import cv2
import numpy as np
import pandas as pd
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

names = ['None', 'Harshit', 'Student2']

cam = cv2.VideoCapture(0)

attendance = []

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for(x,y,w,h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if confidence < 70:
            name = names[id]
            time = datetime.now().strftime('%H:%M:%S')

            attendance.append([name, time])
        else:
            name = "Unknown"

        cv2.putText(img, str(name), (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow('camera', img)

    if cv2.waitKey(1) == 27:
        break

df = pd.DataFrame(attendance, columns=["Name","Time"])
df.to_csv("attendance.csv", index=False)

cam.release()
cv2.destroyAllWindows()
