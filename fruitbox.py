import copy
# 880 570 << 기본화면 dsd

# 100 550 << 리셋버튼
# 250 320 << 시작버튼

# 41*41 << 사과 하나 공간
ROW = 10
COL = 17

apple_array = [
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

def is_array_change(first_array, second_array):
    one = copy.deepcopy(first_array)
    two = copy.deepcopy(second_array)

    if one == two:
        return False
    else:
        return True 

def highnum_first(apple_array, current_row, current_col):
    now_apple = apple_array[current_row][current_col]
    hap_apple = now_apple

    plus_col = current_col + 1
    hap_apple += apple_array[current_row][plus_col] 

    if now_apple in [1,2,8,9]:
        if hap_apple == 10:
            apple_array[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

    hap_apple = now_apple
    
    plus_row = current_row + 1
    hap_apple += apple_array[plus_row][current_col]
    
    if now_apple in [1,2,8,9]:
        if hap_apple == 10:
            for i in range(current_row, plus_row + 1):
                apple_array[i][current_col] = 0
            return

def break_apple_right(apple_array, current_row, current_col):
    now_apple = apple_array[current_row][current_col]
    hap_apple = now_apple

    rc = COL - current_col - 1

    for i in range(rc):
        plus_col = current_col + 1 + i
        hap_apple += apple_array[current_row][plus_col] 

        if hap_apple == 10:
            apple_array[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return 1

        if hap_apple > 10:
            return 0
    return 0

def break_apple_under(apple_array, current_row, current_col):
    now_apple = apple_array[current_row][current_col]
    hap_apple = now_apple

    rr = ROW - current_row - 1
    
    for i in range(rr):
        plus_row = current_row + 1 + i
        hap_apple += apple_array[plus_row][current_col]

        if hap_apple == 10:
            for i in range(current_row, plus_row + 1):
                apple_array[i][current_col] = 0
            return 1
        if hap_apple > 10:
            return 0
    return 0
        
def break_apple_square(apple_array, current_row, current_col):

    # c = 현재위치
    # 2*2 >> 1개 >> [c+1][c+1] 
    # 3*3 >> 3개 >> [c+2][c+1] [c+2][c+2] [c+1][c+2]
    # 4*4 >> 5개 >> [c+3][c+1] [c+3][c+2] [c+3][c+3] [c+2][c+3] [c+1][c+3]
    # 5*5 >> 7개 >> [c+4][c+1] [c+4][c+2] [c+4][c+3] [c+4][c+4] [c+3][c+4] [c+2][c+4] [c+1][c+4]

    hap_apple = 0

    target_row = current_row + 1
    target_col = current_col + 1

    while True:
        hap_apple = 0
        if target_row > ROW:
            return 0

        for i in range(current_row, target_row):
            for j in range(current_col, target_col):
                hap_apple += apple_array[i][j]

        if hap_apple == 10:
            for i in range(current_row, target_row):
                for j in range(current_col, target_col):
                    apple_array[i][j] = 0
            return 1
        
        if hap_apple > 10:
            return 0

        target_col += 1
        if target_col > COL:
            target_row += 1
            target_col = current_col + 1
    
def break_apple(apple_array, current_row, current_col):

    # 1. 오른쪽 n칸 판단
    break_apple_right(apple_array, current_row, current_col)
    
    # 2. 아래 n칸 판단
    break_apple_under(apple_array, current_row, current_col)

    # 3. 사각형 판단
    break_apple_square(apple_array, current_row, current_col)



def check_break_apple(copy_array):
    prev_copy_array = copy.deepcopy(apple_array)

    while is_array_change(copy_array, prev_copy_array):
        prev_copy_array = copy.deepcopy(copy_array)
        for i in range(ROW):
            for j in range(COL):
                break_apple_right(copy_array, i, j) 

                break_apple_under(copy_array, i, j)

                break_apple_square(copy_array, i, j)

    cnt = 0
    for i in range(0,ROW):
        for j in range(0,COL):
            if copy_array[i][j] == 0:
                cnt += 1

    return cnt

def is_break_apple_where(where, current_row, current_col, max_cnt):
    copy_array = copy.deepcopy(apple_array)
    now_cnt = None

    match where:
        case 1:
            if break_apple_right(copy_array, current_row, current_col):
                now_cnt= check_break_apple(copy_array)
        case 2:
            if break_apple_under(copy_array, current_row, current_col):
                now_cnt = check_break_apple(copy_array)
        case 3:
            if break_apple_square(copy_array, current_row, current_col):
                now_cnt = check_break_apple(copy_array)
    
    if now_cnt is None:
        return False, max_cnt  

    if now_cnt > max_cnt:
        max_cnt = now_cnt
        return True, max_cnt
    
    else:
        return False, max_cnt


def simulate_break(apple_array):
    current_row, current_col = 0, 0   
    target_row, target_col = 0, 0 

    while True:
        max_cnt = 0
        how_break = 0
        for i in range(1, 4):
            change_target, max_cnt = is_break_apple_where(i, current_row, current_col, max_cnt)

            if change_target:
                target_row, target_col = current_row, current_col
                how_break = i
        
        
        if how_break == 1:
            break_apple_right(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        elif how_break == 2:
            break_apple_under(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        elif how_break == 3:
            break_apple_square(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        else:
            pass


        if current_col < COL - 1:
            current_col += 1
        elif current_col == COL - 1 and current_row < ROW - 1:
            current_col = 0
            current_row += 1
        else:
            is_finish = copy.deepcopy(apple_array)
            for i in range(ROW):    
                for j in range(COL):
                    break_apple(is_finish, i, j)
            if not is_array_change(apple_array, is_finish):
                print("finish")
                break
            else:
                current_row, current_col = 0, 0   
                target_row, target_col = 0, 0 



    
# 실험코드
if __name__:
    """
    break_apple_square(apple_array, 0, 0)

    for row in apple_array:
        print(row)
    print("-----------------------------------")
"""
    simulate_break(apple_array)
    cnt = 0
    for i in range(0,ROW):
        for j in range(0,COL):
            if apple_array[i][j] == 0:
                cnt += 1
    for row in apple_array:
            print(row)
    print("-----------------------------------")
    print(cnt)

    """
break_apple(apple_array, 0,0)
for row in apple_array:
    print(row)
print("-----------------------------------")
"""