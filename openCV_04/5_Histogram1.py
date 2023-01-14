import sys

import cv2
import matplotlib.pyplot as plt

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()

src = cv2.imread('cat.bmp')

if src is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

# print(bgr_planes)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()

cv2.destroyAllWindows()