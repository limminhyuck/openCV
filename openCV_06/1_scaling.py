import cv2

src = cv2.imread('cat.bmp')  # src.shape=(640, 480)

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (2560, 1920)) # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (2560, 1920), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (2560, 1920), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('dst1', dst1[500:1600, 1000:1800])
cv2.imshow('dst2', dst2[500:1600, 1000:1800])
cv2.imshow('dst3', dst3[500:1600, 1000:1800])
cv2.imshow('dst4', dst4[500:1600, 1000:1800])


cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()