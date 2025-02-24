from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import cv2
import numpy as np
import pytesseract

options = Options()
options.add_argument("--headless")  # UI 없이 실행 (광고가 보이지 않음)
options.add_argument("--disable-gpu")  # GPU 비활성화 (가끔 필요)
options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화 (리소스 절약)
options.add_argument("--disable-dev-shm-usage")  # /dev/shm 사용 안 함 (리소스 절약)

driver = webdriver.Chrome(options=options)

# 880 570 << 기본화면 

# 100 550 << 리셋버튼
# 250 320 << 시작버튼

# 41*41 << 사과 하나 공간

example_img = cv2.imread('./example.png')

array_apple = [
    [6, 3, 5, 5, 1, 9, 4, 7, 1, 2, 7, 5, 1, 8, 7, 5, 9],
    [6, 5, 1, 5, 4, 2, 9, 2, 3, 2, 7, 1, 9, 5, 8, 7, 8],
    [7, 4, 2, 5, 8, 5, 9, 8, 7, 6, 3, 1, 8, 7, 9, 1, 8],
    [7, 1, 4, 3, 3, 7, 6, 1, 7, 8, 4, 5, 4, 7, 5, 4, 7],
    [1, 1, 4, 5, 2, 9, 1, 4, 5, 3, 7, 9, 9, 1, 5, 9, 5],
    [2, 6, 6, 3, 7, 7, 6, 1, 2, 7, 6, 3, 1, 7, 4, 3, 6],
    [5, 8, 1, 4, 1, 9, 7, 3, 3, 8, 5, 9, 6, 1, 4, 9, 4],
    [4, 7, 3, 5, 8, 3, 3, 5, 3, 7, 1, 2, 3, 5, 9, 5, 9],
    [6, 7, 4, 2, 4, 8, 8, 1, 8, 4, 4, 8, 4, 2, 8, 6, 9],
    [7, 9, 7, 2, 6, 5, 7, 3, 8, 6, 4, 8, 5, 6, 9, 7, 2]
]
# 1. 오른쪽 한칸 판단
# 2. 아래 한칸 판단
# 3. 가능한 사각형 판단

# 오른쪽 두칸판단
# 아래 두칸판단
# 가능한 사각형 판단

# 사각형은 1 -> 3 -> 5-> 7 순으로 늘어남 *최대 17개 

def break_right(array_apple, current_row, current_col):
    rows = 10
    cols = 17

    apple_now = array_apple[current_row][current_col]

    # 1. 오른쪽 n칸 판단
    apple_hap = apple_now
    n = 16 - current_col

    for i in range(n):
        plus_col = current_col + 1 + i
        apple_hap += array_apple[current_row][plus_col] 

        if apple_hap == 10:
            array_apple[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

        if apple_hap > 10:
            break

    
    # 2. 아래 n칸 판단
    apple_hap = apple_now
    n = 9 - current_row
    for i in range(n):
        plus_row = current_row + 1 + i
        apple_hap += array_apple[plus_row][current_col]

        if apple_hap == 10:
            for i in range(current_row, plus_row + 1):
                array_apple[i][current_col] = 0
            return
        if apple_hap > 10:
            break

    print("고민 끝")

"""    # 3. 사각형 판단
    apple_hap = apple_now
    for i in range(n):
        pass

    if apple_hap == 10:
        array_apple[current_row][current_col] = 0
        array_apple[plus_row][current_col] = 0
        return
"""



T = 100
while T:
    for i in range(0,10):
        for j in range(0,16):
            break_right(array_apple, i, j)

    for row in array_apple:
        print(row)
    print("-----------------------------------")
    T -= 1

cnt = 0

for i in range(0,10):
    for j in range(0,16):
        if array_apple[i][j] == 0:
            cnt += 1

print(cnt)
