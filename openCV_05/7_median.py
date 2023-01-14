import cv2
import numpy as np

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()