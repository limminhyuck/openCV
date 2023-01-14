import sys

import cv2

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

print('src.shape:', src.shape)
print('src.dtype:', src.dtype)

b_plane, g_plane, r_plane = cv2.split(src)

print(b_plane)
print(g_plane)
print(r_plane)

cv2.imshow('src', src)
cv2.imshow('b_plane', b_plane)
cv2.imshow('g_plane', g_plane)
cv2.imshow('r_plane', r_plane)
cv2.waitKey()
cv2.destroyAllWindows()