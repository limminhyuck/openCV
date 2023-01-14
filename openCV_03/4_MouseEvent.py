import cv2
import numpy as np

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy # 전역변수를 사용할 수 있도록 설정

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼이 눌렸다면
        oldx, oldy = x, y
        print('왼쪽 버튼 클릭: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼이 땠다면
        print('왼쪽 버튼 땜: %d %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
