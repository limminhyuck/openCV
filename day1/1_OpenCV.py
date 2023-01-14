import cv2
import sys

print('OpenCV 버전 : ', cv2.__version__)

img = cv2.imread('cat.bmp')

if img is None:
    print('영상을 불러올 수 없습니다')
    sys.exit() # 영상 파일 불러오기를 실패하면 에러 메세지를 출력하고 종료

cv2.namedWindow('image') # 새 창의 이름을 image라고 설정
cv2.imshow('image', img) # image창에 img 영상을 출력
cv2.waitKey() # 키보드 입력이 있을 때까지 대기
cv2.destroyWindow() # 모든 창을 닫음
