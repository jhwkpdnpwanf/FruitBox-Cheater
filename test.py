# 880 570 << 기본화면 dsd

# 100 550 << 리셋버튼
# 250 320 << 시작버튼

# 41*41 << 사과 하나 공간

import copy
import time

ROW = 3
COL = 5


apple_array = [
    [9, 1, 6, 1, 2],
    [3, 1, 7, 5, 3],
    [1, 8, 4, 5, 4]
]
"""
apple_array = [
    [6, 1, 2, 2, 1],
    [2, 1, 7, 5, 3],
    [2, 8, 4, 5, 4]
]
"""
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

def count_score(array):
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if array[i][j] == 0:
                cnt += 1
    return cnt

def print_array(array):
    print("-----------------------------------")
    for row in array:
            print(row)
    print("-----------------------------------")

def search_best_path(copy_array, trace_path, explored_index):
    for i in range(ROW):
        for j in range(COL):
            if [i, j, 1, explored_index] not in trace_path:
                if break_apple_right(copy_array, i, j):
                    trace_path.append([i, j, 1, explored_index])
                    explored_index = 1
                    search_best_path(copy_array, trace_path, explored_index) 

            if [i, j, 2, explored_index] not in trace_path:
                if break_apple_under(copy_array, i, j):
                    trace_path.append([i, j, 2, explored_index])
                    explored_index = 1
                    search_best_path(copy_array, trace_path, explored_index)
                
            if [i, j, 3, explored_index] not in trace_path:
                if break_apple_square(copy_array, i, j):
                    trace_path.append([i, j, 3, explored_index])
                    explored_index = 1
                    search_best_path(copy_array, trace_path, explored_index)
                    


def all_search_best_path(apple_array):
    max_score = 0
    trace_path = []
    is_return = 0

    i, j = 0, 0
    while i < ROW:
        while j < COL:
            copy_array = copy.deepcopy(apple_array)
            explored_index = 0

            search_best_path(copy_array, trace_path, explored_index)
            now_score = count_score(copy_array)

            
            if now_score > max_score:
                max_score = now_score
                
                if now_score == ROW*COL:
                    break_apple(apple_array, trace_path)
                    i = ROW
                    j = COL
            j += 1
        i += 1
        j = 0
    print(max_score)

                    


def break_apple(apple_array, trace_path):
    final_path = []

    for list in trace_path:
        if list[-1] == 0:
            final_path.clear()
            final_path.append(list)
        else:
            final_path.append(list)

    print("final: ", final_path)

    for list in final_path:
        if list[2] == 1:
            break_apple_right(apple_array, list[0], list[1])
            print_array(apple_array)
        elif list[2] == 2:
            break_apple_under(apple_array, list[0], list[1])
            print_array(apple_array)
        elif list[2] == 3:
            break_apple_square(apple_array, list[0], list[1])
            print_array(apple_array)
        else:
            pass

    print("its break!!!!!!!!")

# 실험코드
if __name__:
    """
    break_apple_square(apple_array, 0, 0)

    for row in apple_array:
        print(row)
    print("-----------------------------------")
"""


    all_search_best_path(apple_array)
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if apple_array[i][j] == 0:
                cnt += 1

    print(cnt)

    """
break_apple(apple_array, 0,0)
for row in apple_array:
    print(row)
print("-----------------------------------")
"""