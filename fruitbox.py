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
# 최악의 경우에 숫자 하나에 수백번 연산이 들어가짐

def highnum_first(array_apple, current_row, current_col):
    rows = 10
    cols = 17

    apple_now = array_apple[current_row][current_col]

    apple_hap = apple_now

    plus_col = current_col + 1
    apple_hap += array_apple[current_row][plus_col] 

    if apple_now in [1,2,8,9]:
        if apple_hap == 10:
            array_apple[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

    apple_hap = apple_now
    
    plus_row = current_row + 1
    apple_hap += array_apple[plus_row][current_col]
    
    if apple_now in [1,2,8,9]:
        if apple_hap == 10:
            for i in range(current_row, plus_row + 1):
                array_apple[i][current_col] = 0
            return




def break_right(array_apple, current_row, current_col):
    rows = 10
    cols = 17

    apple_now = array_apple[current_row][current_col]

    # 1. 오른쪽 n칸 판단
    apple_hap = apple_now
    rc = 16 - current_col

    for i in range(rc):
        plus_col = current_col + 1 + i
        apple_hap += array_apple[current_row][plus_col] 

        if apple_hap == 10:
            array_apple[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

        if apple_hap > 10:
            break

    
    # 2. 아래 n칸 판단
    apple_hap = apple_now
    rr = 9 - current_row
    for i in range(rr):
        plus_row = current_row + 1 + i
        apple_hap += array_apple[plus_row][current_col]

        if apple_hap == 10:
            for i in range(current_row, plus_row + 1):
                array_apple[i][current_col] = 0
            return
        if apple_hap > 10:
            break

    print("고민 끝")

    # 3. 사각형 판단
    rc = 16 - current_col
    rr = 9 - current_row

    # c = 현재위치
    # 2*2 >> 1개 >> [c+1][c+1] 
    # 3*3 >> 3개 >> [c+2][c+1] [c+2][c+2] [c+1][c+2]
    # 4*4 >> 5개 >> [c+3][c+1] [c+3][c+2] [c+3][c+3] [c+2][c+3] [c+1][c+3]
    # 5*5 >> 7개 >> [c+4][c+1] [c+4][c+2] [c+4][c+3] [c+4][c+4] [c+3][c+4] [c+2][c+4] [c+1][c+4]

    apple_hap = 0

    target_row = current_row + 1
    target_col = current_col + 1

    while True:
        if target_col >= 17:
            break
        if target_row >= 10:
            break

        for i in range(current_row, target_row):
            for j in range(current_col, target_col):
                apple_hap += array_apple[i][j]

        if apple_hap == 10:
            for i in range(current_row, target_row):
                for j in range(current_col, target_col):
                    array_apple[i][j] = 0
            return
        
        if apple_hap > 10:
            break

        target_col += 1
        if target_col >= 16:
            target_row += 1
            target_col = current_col + 1

# 숫자 개수
li = [0,0,0,0,0,0,0,0,0,0] 
for i in range(0,10):
    for j in range(0,17):
        li[array_apple[i][j]] += 1
print(li)

t = 0
for i in range(0,10):
    t += i * li[i]
print(t)

t=0
for i in range(0,10):
    for j in range(0,17):
        t += array_apple[i][j]
print(t)

# 실험코드

T = 5
while T:
    for i in range(0,9):
        for j in range(0,16):
            highnum_first(array_apple, i, j)

    for row in array_apple:
        print(row)
    print("-----------------------------------")
    T -= 1

T = 100
while T:
    for i in range(0,10):
        for j in range(0,17):
            break_right(array_apple, i, j)

    for row in array_apple:
        print(row)
    print("-----------------------------------")
    T -= 1

cnt = 0

for i in range(0,10):
    for j in range(0,17):
        if array_apple[i][j] == 0:
            cnt += 1

print(cnt)
