import numpy as np
import cv2

src = cv2.imread('nemo.jpg')

# 사각형 지정을 통한 초기 분할
# 초기 위치를 지정하고 모서리 좌표 4개를 튜플값으로 리턴
rc = cv2.selectROI(src)

# 검정색으로 채움. 입력 영상과 동일한 크기
mask = np.zeros(src.shape[:2], np.uint8)

# 결과를 계속 업데이트 하고 싶으면 bgd, fgd 입력
cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# where 조건에 맞는 인덱스의 위치를 찾아주는 함수(np 내장함수)
# grabcut 자료에서 0, 2는 배경 또는 배경으로 추축되는 값
# 1, 3은 전경 또는 전경으로 추측되는 오브젝트
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis]

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()