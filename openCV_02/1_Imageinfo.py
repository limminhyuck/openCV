import cv2

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

print('type(img1):', type(img1)) # <class 'numpy.ndarray'>
print('img1.shape:', img1.shape) # (480, 640)
print('img2.shape:', img2.shape) # (480, 640, 3)
print('img2.dtype:', img2.dtype) # uint8

h, w = img2.shape[:2] # h : 480, w : 640
print('img2 size: {} * {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1은 흑백 영상입니다')
elif len(img1.shape) == 3:
    print('img1은 컬러 영상입니다')

# for문으로 픽셀값을 변경하는 작업은 매우 느림
# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255
#         img2[y, x] = (0, 0, 255)

img1[:,:] = 255
img2[:,:] = (0 , 0, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()