import copy
# 880 570 << 기본화면 dsd

# 100 550 << 리셋버튼
# 250 320 << 시작버튼

# 41*41 << 사과 하나 공간
ROW = 10
COL = 10

apple_array = [
    [4, 6, 3, 7, 5, 5, 2, 8, 2, 0],
    [5, 5, 4, 6, 3, 3, 4, 1, 9, 1],
    [3, 7, 3, 3, 4, 6, 2, 8, 5, 5],
    [2, 8, 6, 4, 4, 6, 2, 5, 5, 2],
    [3, 3, 4, 0, 3, 5, 5, 5, 0, 8],
    [5, 5, 2, 8, 4, 5, 3, 3, 4, 1],
    [9, 1, 3, 7, 3, 3, 4, 6, 2, 8],
    [5, 5, 2, 8, 0, 4, 4, 6, 2, 5],
    [5, 2, 3, 3, 4, 6, 3, 7, 5, 5],
    [2, 8, 4, 6, 3, 3, 4, 1, 9, 1],
]

def is_break_apple_right(array, row, col): # currnet row, current col
    start_point = [row, col]
    now = array[row][col]
    if now == 0:
        return []
    
    for i in range(col + 1, COL):
        last_value = array[row][i]
        if last_value == 0:
            continue
        else:
            if now + last_value == 10:
                last_point = [row, i]
                return [start_point, last_point, now, last_value]
            else:
                return []
    return [] 

def is_break_apple_under(array, row, col): # currnet row, current col
    start_point = [row, col]
    now = array[row][col]
    if now == 0:
        return []

    for i in range(row + 1, ROW):
        last_value = array[i][col]
        if last_value == 0:
            continue
        else:
            if now + last_value == 10:
                last_point = [i, col]
                return [start_point, last_point, now, last_value]  
            else:
                return []
    return []

def is_break_apple_square(array, row, col, direction = 'down'): # currnet row, current col
    start_point = [row, col]
    now = array[row][col]

    if direction == 'up':
        range_row = next((r for r in range(row - 1, -1, -1) if array[r][col] != 0), -1)
        range_col = next((c for c, value in enumerate(array[row][col + 1:], start=col + 1) if value != 0), COL)
        step = -1

    else: # direction == 'down'
        range_row = next((r for r, _ in enumerate(array[row + 1:], start=row + 1) if array[r][col] != 0), ROW)
        range_col = next((c for c, value in enumerate(array[row][col + 1:], start=col + 1) if value != 0), COL)
        step = 1

    for i in range(row + step, range_row, step):
        for j in range(col + 1, range_col):
            last_value = array[i][j]

            if last_value == 0:
                continue
            else:
                if now + last_value == 10:
                    last_point = [i, j]
                    return [start_point, last_point, now, last_value]  
                else:
                    break
    return []

def break_apple(array, range_coords):
    start_point, last_point, _, _ = range_coords
    array[start_point[0]][start_point[1]] = 0
    array[last_point[0]][last_point[1]] = 0

def recover_apple(array, range_coords):
    start_point, last_point, first, last = range_coords
    array[start_point[0]][start_point[1]] = first
    array[last_point[0]][last_point[1]] = last

def print_array(array):
    print("-----------------------------------")
    for row in array:
            print(row)
    print("-----------------------------------")

def count_score(array):
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if array[i][j] == 0:
                cnt += 1
    return cnt

def expected_destroyed_apple(array, range_coords):
    break_apple(array, range_coords)
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            
            if is_break_apple_right(array,i,j):
                cnt += 1
            if is_break_apple_under(array,i,j):
                cnt += 1
            if is_break_apple_square(array,i,j):
                cnt += 1
            if is_break_apple_square(array,i,j, 'up'):
                cnt += 1
    recover_apple(array, range_coords)
    return cnt

def get_pruning_value_map(array):
    value_map = {} 
    idx = 0
    for i in range(ROW):
        for j in range(COL):

            range_coords = {
                'right': is_break_apple_right(array, i, j),
                'under': is_break_apple_under(array, i, j),
                'square': is_break_apple_square(array, i, j),
                'square up' : is_break_apple_square(array, i, j, 'up')
            }

            count_range_coords = {
                key:expected_destroyed_apple(array, coords)
                for key, coords in range_coords.items() if coords
            }

            if count_range_coords:
                max_value = max(count_range_coords, key = count_range_coords.get)
                value_map.update({(idx, max_value, count_range_coords[max_value]): range_coords[max_value]})
                idx += 1 # Prevents key duplication / It's just an index
    
    return value_map

def pruning(array):
    value_map = get_pruning_value_map(array)

    if value_map:
        target_apple = max(x[2] for x in value_map)
        max_items = {key: value for key, value in value_map.items() if key[2] == target_apple}

        print(next(iter(max_items.values())))

        if len(max_items) == 0:
            return
        else:
            first_value = next(iter(max_items.values()))
            break_apple(array, first_value)
            s = sum(sum(row) for row in array)
            print(s)
            print_array(array)
            pruning(array)
            
    else:
        return

    """
        if len(max_items) == 1:
            break_apple(array, *max_items.values())
        else:
            for value in max_items.values():
                print(expected_destroyed_apple(array, value))
                """
    

if __name__:
    trace_path = []
    pruning(apple_array)
    print_array(apple_array)
    print(count_score(apple_array))