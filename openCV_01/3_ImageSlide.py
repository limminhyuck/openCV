import sys
import cv2
import glob

imgFiles = glob.glob('images\\*.jpg')
# print(imgFiles)

if not imgFiles:
    print('영상을 불러올 수 없습니다')
    sys.exit()

idx = 0

while True:
    img = cv2.imread(imgFiles[idx])

    if img is None:
        print('영상을 불러올 수 없습니다')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    if idx >= len(imgFiles):
        idx = 0

cv2.destroyAllWindows()
