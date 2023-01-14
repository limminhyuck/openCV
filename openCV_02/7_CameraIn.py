import sys

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit()

print('가로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    # ret :read() 결과, 성공하면 True, 실패하면 False
    # frame : 현재 프레임(영상), numpy.ndarray
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # ESC키
        break

cap.release()
cv2.destroyAllWindows()
