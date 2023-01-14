import cv2

src = cv2.imread('cat.bmp')

cp = (src.shape[1] / 2, src.shape[0] / 2)  #[1] 가로 [0] 세로
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()