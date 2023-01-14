import sys

import cv2

cap = cv2.VideoCapture('Blossoms.mp4')

if not cap.isOpened():
    print('동영상을 열수 없습니다')
    sys.exit()

print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS:', fps)

delay = round(1000 / fps)
print('delay:', delay)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()