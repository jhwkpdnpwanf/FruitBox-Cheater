import copy
import time

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


def print_array(array, delay=0.1):
    print("-----------------------------------")
    for row in array:
            print(row)
    print("-----------------------------------")

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

def count_score(array):
    cnt = 0
    for i in range(ROW):
        for j in range(COL):
            if array[i][j] == 0:
                cnt += 1
    return cnt

def expected_destroyed_apple(array, direction, coords, max_depth = 5, exp_value = 0, temp_break_list = None):
    if temp_break_list is None:
        temp_break_list = []
    if max_depth < 0:
        return exp_value
    
    break_apple(array, coords)
    temp_break_list.append(coords) # to recover

    I = coords[1][0]
    J = coords[1][1]
    if direction == "square up":
        I = coords[0][0]
        J = coords[1][1]

    for i in range(I):
        for j in range(J):
                right = is_break_apple_right(array, i, j)
                if right:
                    temp_break_list.append(right)
                    max_depth -= 1
                    exp_value += 1
                    expected_destroyed_apple(array, "right", right, max_depth, exp_value)
                    recover_apple(array, temp_break_list.pop())
                    
        

                under = is_break_apple_under(array, i, j)
                square = is_break_apple_square(array, i, j)
                square2 = is_break_apple_square(array, i, j, 'up')


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
            """for k, v in range_coords.items():
                if v:
                    print(range_coords)"""
            count_range_coords = {
                direction:expected_destroyed_apple(array, direction, coords)
                for direction, coords in range_coords.items() if coords
            }


            if count_range_coords:
                max_value = max(count_range_coords, key = count_range_coords.get)
                value_map.update({(idx, max_value, count_range_coords[max_value]): range_coords[max_value]})
                idx += 1 # Prevents key duplication / It's just an index
                print(value_map)
            
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