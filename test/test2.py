import copy
import time

ROW = 5
COL = 5

apple_array = [
    [1,6,2,3,5],
    [2,1,2,3,7],
    [2,2,8,3,5],
    [4,1,5,3,9],
    [1,7,4,1,3]
]
apple_array = [
    [3,1,4,7,1],
    [9,3,6,1,4],
    [5,3,8,2,2],
    [7,3,2,1,2],
    [5,3,1,6,1]
]

def is_array_change(first_array, second_array):
    one = copy.deepcopy(first_array)
    two = copy.deepcopy(second_array)

    if one == two:
        return False
    else:
        return True
    
def break_apple_square(apple_array, current_row, current_col):
    hap_apple = 0

    target_row = current_row
    target_col = current_col

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

def search_best_path(copy_array, trace_path, index, judge):
    i , j = 0, 0
    while i < ROW - 1:
        while j < COL - 1:
            cnt = 0
            cnt = Q_break_apple_right(copy_array, i, j)
            cnt += Q_break_under(copy_array, i, j)
            cnt += Q_break_apple_square(copy_array, i, j)
            
            judge = cnt

            if i == 0 and j== 0:
                pass
            """ 
            print(n, "에서",index, "인데",i, j,"에서",cnt, "번 겹친다")
            if judge > 1:
                pass
                """

            if [i, j, 1, index] not in trace_path:
                if break_apple_right(copy_array, i, j):
                    trace_path.append([i, j, 1, index])
                    index += 1
                    search_best_path(copy_array, trace_path, index, judge) 
                    
            if [i, j, 2, index] not in trace_path:
                if break_apple_under(copy_array, i, j):
                    trace_path.append([i, j, 2, index])
                    index += 1
                    search_best_path(copy_array, trace_path, index, judge)

            if [i, j, 3, index] not in trace_path:
                if break_apple_square(copy_array, i, j):
                    trace_path.append([i, j, 3, index])
                    index += 1
                    search_best_path(copy_array, trace_path, index, judge)
            
            j += 1
        i += 1
        j = 0

def all_search_best_path(apple_array):
    max_score = 0
    trace_path = []
    
    n = 1
    for i in range(10):
        copy_array = copy.deepcopy(apple_array)
        index, judge = 0, 0
        search_best_path(copy_array, trace_path, index, judge)

        now_score = count_score(copy_array)

        n += 1
        print_array(copy_array)
        print(trace_path)
        if now_score > max_score:
            max_score = now_score
            
            if now_score == ROW*COL:
                break_apple(apple_array, trace_path)
                break
        
        if judge > 1:
            pass


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


    all_search_best_path(apple_array)
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if apple_array[i][j] == 0:
                cnt += 1

    print(cnt)

