import cv2
import numpy as np

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.2, minSize=(100, 100), maxSize=(400, 400))

    for (x, y, w, h) in faces:
        pass