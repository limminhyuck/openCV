import sys
import cv2
import numpy as np

src = cv2.imread('cat.bmp')

'''
    x' = x + a
    y' = y + b
    
           x
    1 0 a  y
    0 1 b  1
'''

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()