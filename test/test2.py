import copy

ROW = 5
COL = 5

apple_array = [
    [1,6,1,3,5],
    [2,1,2,3,7],
    [2,2,8,3,5],
    [4,1,6,3,9],
    [1,7,4,1,3]
]
apple_array = [
    [1,6,1,6,0],
    [1,1,1,0,0],
    [1,0,0,0,2],
    [0,3,3,1,0],
    [0,0,4,1,0]
]


def break_apple_right(array, row, col): # currnet row, current col

    for i in range(col + 1, COL):
        partial_array = array[row][col:i + 1]
        hap = sum(partial_array)

        if hap > 10:
            return []
        if hap == 10:
            array[row][col:i + 1] = [0] * (i - col + 1)
            return tuple(partial_array) # Used for restoration
    return []

def break_apple_under(array, row, col): # currnet row, current col
    now = array[row][col]
    hap = now

    partial_array = [now] # Used for restoration

    for i in range(row + 1, ROW):
        a = array[i][col]
        partial_array.append(a) 
        hap += a

        if hap > 10:
            return []
        if hap == 10:
            for j in range(row, i + 1):
                array[j][col] = 0
            return tuple(partial_array)
    return []

def break_apple_square(array, row, col): # currnet row, current col
    
    i = row + 1
    while i <= ROW:
        j = col + 1
        while j <= COL:
            partial_array = [array[k][col:j + 1] for k in range(row, i + 1)]
            hap = sum(sum(partial_array, []))

            if hap > 10:
                j = col + 1
                i += 1
                continue

            if hap == 10:
                for l in range(row, i + 1):
                    array[l][col:j + 1] = [0] * (j - col + 1)
                return tuple(partial_array)
            j += 1
        i += 1
    return []
print(break_apple_under(apple_array, 0,0))

print(break_apple_square(apple_array, 0,0))

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
    
    for i in range(ROW):
        for j in range(COL):
            step = break_apple_right(array, i, j)
            if not step:
                pass
            else:
                trace_path.append(step)


def break_apple(apple_array, trace_path):
    final_path = []

    for list in trace_path:
        if list[-1] == 0:
            final_path.clear()
            final_path.append(list)
        else:
            final_path.append(list)


# 실험코드
if __name__:

    cnt = 0

