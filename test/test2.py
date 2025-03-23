import copy
import time
ROW = 10
COL = 10

depth = 0
max_depth = 5

apple_array = [
    [1,6,4,3,5],
    [2,1,2,3,7],
    [2,2,8,3,5],
    [4,1,6,3,1],
    [1,7,3,1,9]
]
apple_array = [
    [7,2,8,2,3],
    [7,2,5,8,3],
    [7,2,5,2,3],
    [7,2,8,8,2],
    [7,2,2,3,3]
]
apple_array = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 3, 3, 4, 0, 0, 1],
    [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [3, 3, 4, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 3, 0, 4, 1],
    [0, 0, 3, 0, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [5, 0, 3, 3, 4, 0, 3, 0, 5, 0],
    [2, 0, 0, 0, 3, 3, 4, 0, 0, 1]
]

# 41*41 << 사과 하나 공간


def break_apple_right(array, row, col): # currnet row, current col

    for i in range(col + 1, COL):
        partial_array = array[row][col:i + 1]
        hap = sum(partial_array)

        if hap > 10:
            return []
        if hap == 10:
            array[row][col:i + 1] = [0] * (i - col + 1)
            return (row, col, tuple(partial_array)) # (row, col, (value to recover))

def break_apple_under(array, row, col): # currnet row, current col
    now = array[row][col]
    hap = now

    partial_array = [now]

    for i in range(row + 1, ROW):
        a = array[i][col]
        partial_array.append(a) 
        hap += a

        if hap > 10:
            return []
        if hap == 10:
            for j in range(row, i + 1):
                array[j][col] = 0
            return (row, col, tuple(partial_array)) # (row, col, (value to recover))
    return []

def break_apple_square(array, row, col): # currnet row, current col
    
    while all(x == 0 for x in array[row][col:COL]):
        row += 1
        if row > ROW-1:
            break

    while all(array[r][col] == 0 for r in range(row, ROW)):
        if col > COL:
            break
        col += 1

        
    i = row + 1
    while i < ROW:
        j = col + 1
        while j < COL:
            if i >= ROW:
                break

            partial_array = [array[k][col:j + 1] for k in range(row, i + 1)]
            hap = sum(sum(partial_array, []))

            if hap > 10:
                j = col + 1
                i += 1
                continue

            if hap == 10:
                for l in range(row, i + 1):
                    array[l][col:j + 1] = [0] * (j - col + 1)
                return (row, col, tuple(partial_array)) # (row, col, (value to recover))
            j += 1
        i += 1
        
    return []


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

def can_add_path(step):
    if not step:
        return False
    else:
        return True

def search_best_path(array, trace_path):
    
    if count_score(array) == ROW*COL:
        print("finish")
        return True
    
    for i in range(ROW):
        for j in range(COL):
            step_right = break_apple_right(array, i, j)
            if step_right:
                print(count_score(array))
                trace_path.append(step_right)
                if search_best_path(array, trace_path):
                    return True
                row, col, value = trace_path[-1]

                for v in value: # recover array
                    array[row][col] = v
                    col += 1    
                
                trace_path.pop()

            step_under = break_apple_under(array, i, j)
            if step_under:
                print(count_score(array))
                trace_path.append(step_under)
                if search_best_path(array, trace_path):
                    return True
                row, col, value = trace_path[-1]

                for v in value:
                    array[row][col] = v
                    row += 1
                trace_path.pop()

            step_square = break_apple_square(array, i, j)
            if step_square:
                print(count_score(array))
                trace_path.append(step_square)
                if search_best_path(array, trace_path):
                    return True
                
                row, col, value = trace_path[-1]
                for element in value:
                    c = col
                    for v in element:
                        array[row][c] = v
                        c += 1
                    row += 1    
                trace_path.pop()
    if not trace_path:
        print("cant")
        return False
    # recover array (backtracking!!!)
    # The function was integrated to reduce overhead since it is frequently called during the backtracking process.
    

if __name__:
    trace_path = []
    search_best_path(apple_array, trace_path)

    print("result path: ",trace_path)
    print_array(apple_array)
