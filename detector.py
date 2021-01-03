import cv2
import csv
from deepface import DeepFace
import datetime
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np






# print the current timestamp




faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Can not open webcam")

with open('emotions.csv', 'w', newline='') as csvfile:
    emotionwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


    while True:
        ret, frame = cap.read()
        # ts stores the time in seconds
        ts = dt.datetime.now()
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        print(result["dominant_emotion"])

        # converting emotions into numbers
        if result["dominant_emotion"] == "happy":
            no = 1
        elif result["dominant_emotion"] == "sad":
            no = 2
        elif result["dominant_emotion"] == "angry":
            no = 3
        else:
            no = 4
        emotionwriter.writerow([ts,no])
        print(no)





        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, result["dominant_emotion"], (0,50), font,1,
                            (0,255,0), 2, cv2.LINE_4);



        cv2.imshow('Original Video', frame)





        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()