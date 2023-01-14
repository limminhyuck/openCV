import sys

import cv2

# 그레이스케일 영상
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

dst = cv2.add(src, 100)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상
src = cv2.imread('cat.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()