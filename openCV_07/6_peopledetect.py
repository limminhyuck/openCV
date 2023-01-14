import random
import cv2

cap = cv2.VideoCapture('vtest.avi')

# 보행자 검출을 위한 HOG 기술자 설정
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 매 프레임마다 보행자를 검출출 (_ : 신뢰도)
    detectd, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detectd:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y, w, h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()