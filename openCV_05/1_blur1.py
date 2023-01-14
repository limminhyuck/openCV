import sys
import numpy as np
import cv2

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽을 수 없습니다')
    sys.exit()

# kernel = np.array([[1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9]])

# kernel = np.ones((3, 3), dtype=np.float64) /9.
#
# dst = cv2.filter2D(src, -1, kernel)

dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# noinspection PyUnresolvedReferences
cv2.destroyAllWindows()
