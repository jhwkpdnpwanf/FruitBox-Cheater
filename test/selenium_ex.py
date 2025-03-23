import os
import time
import pyautogui
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ROW = 10
COL = 17

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

pyautogui.FAILSAFE = False

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1135, 890)

url = "https://www.gamesaien.com/game/fruit_box_a/"
driver.get(url)

time.sleep(8)

current_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(current_dir, "..", "img")

# image path
start_page_img = os.path.join(img_dir, "start_page.png")
btn_play_img = os.path.join(img_dir, "btn_play.png")
btn_reset_img = os.path.join(img_dir, "btn_reset.png")
digits_img_paths = {
    i: os.path.join(img_dir, f"digit{i}.png") for i in range(1, 10)
}

def click_btn(img_path, confidence=0.7):
    screenshot = pyautogui.screenshot()
    screen_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    template = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("[클릭버튼오류]")
        return False

    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        t_h, t_w = template.shape[:2]
        center_x = max_loc[0] + t_w // 2
        center_y = max_loc[1] + t_h // 2

        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
        return True
    else:
        print(f"최대 유사도={max_val:.2f} , 최대 유사도 수정해야함")
        return False

click_btn(btn_play_img)
pyautogui.moveTo(1,1)
time.sleep(2)


def extract_digit_positions(digits_img_paths, threshold=0.7):
    results = []
    screenshot = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    for digit, img_path in digits_img_paths.items():
        template_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if template_gray is None:
            print("[숫자 찾기 오류]")
            continue

        match_result = cv2.matchTemplate(screen, template_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(match_result >= threshold)

        t_h, t_w = template_gray.shape[:2]

        for pt in zip(*loc[::-1]):
            x_center = pt[0] + t_w // 2
            y_center = pt[1] + t_h // 2

            if not any(abs(x_center - x) < 10 and abs(y_center - y) < 10 for (_, x, y) in results):
                results.append([digit, x_center, y_center])

    return results


apples = extract_digit_positions(digits_img_paths, threshold=0.92)

def change_digits_to_array(datas, eps=3):
    data = [(int(digit), int(x), int(y)) for digit, x, y in datas]
    
    xs = [x for _, x, _ in data]
    ys = [y for _, _, y in data]
    
    def cluster_values(values, eps):
        clusters = []
        for v in sorted(values):
            if not clusters or v - clusters[-1][-1] > eps:
                clusters.append([v])
            else:
                clusters[-1].append(v)
        reps = [sum(cluster) / len(cluster) for cluster in clusters]
        return reps
    
    def find_cluster(value, reps):
        diffs = [abs(value - r) for r in reps]
        return diffs.index(min(diffs))
    
    x_reps = cluster_values(xs, eps)
    y_reps = cluster_values(ys, eps)
    
    rows = len(y_reps)
    cols = len(x_reps)
    grid = [[None for _ in range(cols)] for _ in range(rows)]
    
    for digit, x, y in data:
        col = find_cluster(x, x_reps)
        row = find_cluster(y, y_reps)
        grid[row][col] = digit

    coord_array = [[(x_reps[c], y_reps[r]) for c in range(cols)] for r in range(rows)]
    
    return grid, coord_array, x_reps, y_reps


grid, coord_array, x_reps, y_reps = change_digits_to_array(apples, eps=3)

print("x 대표값(열):", x_reps)
print("y 대표값(행):", y_reps)
print("2차원 배열:")
for row in grid:
    print(row)

for row in coord_array:
    print(row)

# ----- ----- ----- 

apple_array = grid


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

def pruning(array, trace_path):
    value_map = get_pruning_value_map(array)

    if value_map:
        target_apple = max(x[2] for x in value_map)
        max_items = {key: value for key, value in value_map.items() if key[2] == target_apple}

        if len(max_items) == 0:
            return
        else:
            first_value = next(iter(max_items.values()))
            trace_path.append(first_value)
            break_apple(array, first_value)
            print_array(array)
            pruning(array, trace_path)
            
    else:
        return
    
def break_with_drag(coord_array, trace_path):

    sx, sy = coord_array[0][0]
    ex, ey = coord_array[ROW-1][COL-1]

    plus_x = (ex - sx) / (COL - 1) / 2
    plus_y = (sy - ey) / (ROW - 1) / 2

    for rr, rc, _, _ in trace_path:
        start_row, start_col = rr
        end_row, end_col = rc

        center_start_coord = coord_array[start_row][start_col]
        center_end_coord = coord_array[end_row][end_col]

        drag_start_coord = (center_start_coord[0] - plus_x, center_start_coord[1] + plus_y)
        drag_end_coord = (center_end_coord[0] + plus_x, center_end_coord[1] - plus_y)

        if start_row > end_row:
            drag_start_coord = (drag_start_coord[0] + plus_x, drag_start_coord[1] - plus_y)
            drag_end_coord = (drag_end_coord[0] - plus_x, drag_end_coord[1] + plus_y)
        
        pyautogui.moveTo(drag_start_coord, duration=0.01)
        time.sleep(0.05)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(drag_end_coord, duration=0.1)
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')

if __name__:
    trace_path = []
    pruning(apple_array, trace_path)
    break_with_drag(coord_array, trace_path)
    print_array(apple_array)
    print(count_score(apple_array))
    print(trace_path)