# 880 570 << 기본화면 dsd

# 100 550 << 리셋버튼
# 250 320 << 시작버튼

# 41*41 << 사과 하나 공간


array_apple = [
    [2, 9, 1, 2, 2, 8, 4, 1, 1, 4, 2, 3, 3, 4, 3, 8, 8],
    [7, 7, 2, 8, 3, 4, 9, 1, 9, 3, 5, 4, 7, 2, 4, 2, 3],
    [7, 9, 4, 2, 5, 6, 1, 2, 4, 7, 9, 5, 1, 4, 3, 7, 6],
    [2, 8, 6, 9, 3, 1, 2, 4, 5, 6, 3, 8, 9, 5, 5, 4, 1],
    [3, 4, 1, 3, 4, 4, 6, 7, 6, 9, 1, 7, 3, 1, 8, 5, 7],
    [3, 9, 6, 9, 5, 7, 9, 8, 3, 2, 8, 8, 8, 1, 4, 1, 4],
    [1, 2, 6, 7, 5, 8, 4, 6, 1, 3, 5, 1, 5, 3, 2, 3, 5],
    [7, 5, 5, 1, 6, 3, 7, 1, 5, 5, 2, 9, 5, 5, 4, 7, 1],
    [5, 1, 8, 5, 9, 4, 6, 2, 5, 4, 7, 8, 1, 3, 6, 7, 8],
    [5, 1, 8, 4, 1, 1, 2, 9, 9, 3, 2, 5, 5, 5, 2, 1, 1]
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


# 실험코드
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
