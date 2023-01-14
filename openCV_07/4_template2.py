import numpy as np
import cv2

def load_digits():
    img_digits = []
    for i in range(10):
        filename = './digits/digit{}.bmp'.format(i)
        img_digits.append(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))
        if img_digits[i] is None:
            return None
    return img_digits

def find_digit(img, img_digits):
    max_idx = -1
    max_cceoff = -1

    for i in range(10):
        img = cv2.resize(img, (100, 150))
        res = cv2.matchTemplate(img, img_digits[i], cv2.TM_CCOEFF_NORMED)

        if res[0, 0] > max_cceoff:
            max_idx = i
            max_cceoff = res[0, 0]
    return max_idx


def main():
    src = cv2.imread('digits_print.bmp')

    img_digits = load_digits()

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 반전된 결과를 리턴, 이진화(이미지에 대한 히스토그램에서 임계값을 자동으로 계산)
    _, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 객체 정보를 함께 반환(레이블링 함수)
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src_bin)

    print(cnt)
    print(stats)

    dst = src.copy()
    for i in range(1, cnt):
        (x, y, w, h, s) = stats[i]

        if s < 1000:
            continue

        digit = find_digit(src_gray[y:y+h, x:x+w], img_digits)
        cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))
        cv2.putText(dst, str(digit), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 가장 먼저 실행되는 부분
if __name__ == '__main__':
    main()
