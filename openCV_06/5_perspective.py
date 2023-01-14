import cv2
import numpy as np

src = cv2.imread('namecard.jpg')

w, h = 720, 400
srcQuad = np.array([[345, 287], [1123, 229], [1272, 657], [332, 768]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
# retvol : 3x3 투시 변환 행렬

dst = cv2.warpPerspective(src, pers, (w, h))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()