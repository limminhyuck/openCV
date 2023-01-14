import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# 선그리기
# img : 그림을 그릴 영상
# (50,50), (200, 50) : 직선의 시작점과 끝점, 튜플
# (0, 0, 255) : 색상 또는 밝기, BGR 튜플
# 5 : 선 두께
cv2.line(img, (50,50), (200, 50), (0, 0, 255), 5)

# 사각형 그리기
# (50, 200, 150, 100) : 사각형 위치정보 (x, y, w, h) 튜플
# (0, 0, 255) : 색상 또는 밝기, BGR 튜플
# 2 : 두께, -1을 설정하면 내부를 채움
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220, 100, 200), (0, 255, 0), -1)

# 원그리기
# (300, 100) : 원의 중심 좌표 (x, y) 튜플
# 30 : 원의 반지름
# (0, 0, 255) : 색상 또는 밝기, BGR 튜플
# -1 : 선 두께, -1을 설정하면 내부를 채움
# cv2.LINE_AA : 선타입, cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)

text = 'Hello, Python'
# 문자열 출력
# (50, 350) : 영상에서 문자열을 출력할 위치의 좌표 하단 좌표
# cv2.FONT_HERSHEY_SIMPLEX : 폰트 종류
# 0.8 : 폰트 크기 확대/축소 비율
# (0, 0, 255) : 색상 또는 밝기, BGR 튜플
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

