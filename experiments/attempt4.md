## 네번째 방법

시간복잡도를 해결하기 위해서 우선 가치치기에 집중해 보았다.  

170개를 전부 부수는 영상을 계속 돌려보니  
50점이 넘어서야 첫번째 3개조합이 나왔고 100점이 넘어서야 두번째 3개조합이 나왔다.  

당연히 그럴 수 밖에 없는게 3개를 깨뜨리는 조합은 홀수 개를 깨뜨리는 조합이 한번 더 나와야지만(짝수번 맞춰주기) 170점을 기록할 수 있고  
3개이상의 조합은 낮은 자리 숫자를 여러개 써야하는 단점이 있기에 두개를 최우선으로 확인해주어야겠다.  
<br>

### 단계별 로직
1. **탐색 가능한 모든 쌍 찾기**  
   - 각 칸을 기준으로 합이 10이 되는 모든 짝을 찾는다(오른쪽, 아래쪽, 사각형).  
   - 가능한 후보들을 모으기.

2. **기댓값 계산**  
   - 만약 어떤 쌍을 제거했을 때, 추가로 제거될 가능성이 높은(즉, 기댓값이 큰) 쌍이 있다면, 그 쌍을 우선적으로 선택.  

3. **가장 유망한 쌍 제거**  
   - 기댓값이 최대인 쌍을 제거.

4. **재귀적 반복**  
   - 제거 후, 다시 가능한 쌍들을 찾기.  
   - 더 이상 제거할 쌍이 없을 때까지 과정을 반복.

5. **종료**  
   - 종료.
<br>

### 초기사과
```python
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
```

해결을 할 수 있는 10*10 배열을 하나 준비해주고  
기존에 사과를 부수는 로직을 사과를 부술 수 있는지 확인해주게 바꾸었다.  
<br>

```python
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
```
오직 두개일 때만 깨뜨리면 되므로 10이 아니면 바로 리턴 하도록 했다.  
그리고 본인이 0일 때는 바로 리턴해주어 중복을 줄여주었다.  
<br>

```python
def is_break_apple_square(array, row, col): # currnet row, current col
    start_point = [row, col]
    now = array[row][col]

    range_row = next((r for r, _ in enumerate(array[row + 1:], start=row + 1) if array[r][col] != 0), ROW)
    range_col = next((c for c, value in enumerate(array[row][col + 1:], start=col + 1) if value != 0), COL)

    for i in range(row + 1, range_row):
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
```
사각형을 부술 때도 같은 row나 col에 0이 일때까지만 반복되도록 range_row와 range_col을 따로 지정해줫다.  
미찬가지로 10이 되는지만 판단하고 맞으면 시작좌표(왼쪽상단), 끝좌표(오른쪽하단), 시작 값, 끝 값을 리스트로 반환한다.  
<br>

```python
def break_apple(array, range_coords):
    start_point, last_point, _, _ = range_coords
    array[start_point[0]][start_point[1]] = 0
    array[last_point[0]][last_point[1]] = 0

def recover_apple(array, range_coords):
    start_point, last_point, first, last = range_coords
    array[start_point[0]][start_point[1]] = first
    array[last_point[0]][last_point[1]] = last
```
사과를 부술 때는 break_apple로 사과를 부숴주고 (`is_break_apple_방향`의 반환값으로 부숨)  
사과를 복원할 때는 recover_apple로 사과를 복원한다 (`is_break_apple_방향`의 반환값으로 부숨)  

두개만 부수는 로직이기에 간단하게 작성해보았다.  

이제 돌아가면서 2개만 부수는 경우로 가지치기를 해줄 예정이다.  
만약 2개만 부술 수 있는 경우가 없다면 전에 만들어둔 백트래킹 `search_best_path` 함수를 사용해서 답을 찾아낼 것이다.  

<br>
```python
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
    recover_apple(array, range_coords)
    return cnt
```
기댓값을 계산하기 위해 expected 함수를 만들어줬다.  
<br>

```python
def get_pruning_value_map(array):
    value_map = {} 
    idx = 0
    for i in range(ROW):
        for j in range(COL):

            range_coords = {
                'right': is_break_apple_right(array, i, j),
                'under': is_break_apple_under(array, i, j),
                'square': is_break_apple_square(array, i, j)
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
```
각 기댓값을 기록하는 value_map을 만들기 위한 함수도 만들어주고,  
<br>

```python
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
```
마지막으로 가지치기를 실행할 pruning 함수까지 만들어주면 끝이다.   
시간복잡도가 그리 높지 않기때문에 딕셔너리를 사용하여 가독성을 챙겨주었다.  
value_map은 key값에 (중복방지용 idx, '방향', 기댓값)이 들어가고 value로 좌표와 해당값들이 기록된다.  
- 예시 : `(0, 'right', 28): [[0, 2], [0, 3], 3, 7]`

그렇게 가지치기를 해주면  
### 가지치기 이후 사과
```python
[0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
[0, 0, 0, 0, 3, 3, 4, 0, 0, 1]
[0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
[3, 3, 4, 0, 3, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 4, 0, 3, 0, 4, 1]
[0, 0, 3, 0, 3, 3, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
[5, 0, 3, 3, 4, 0, 3, 0, 5, 0]
[2, 0, 0, 0, 3, 3, 4, 0, 0, 1]
```
이런 배열이 나온다.  
이걸 이전에 만들어둔 `search_best_path` 함수에 넣어주면
<br>
### 이후사과
```python
finish
result path:  [(0, 0, (0, 0, 0, 0, 3, 0, 0, 0, 5, 2)), (0, 1, ([0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 4])), (0, 1, ([0, 0], [0, 0], [0, 3], [0, 0], [3, 4])), (0, 3, ([0, 0], [0, 0], [0, 0], [0, 0], [0, 3], [0, 4], [0, 3])), (0, 3, ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 3], [0, 0, 0], [3, 4, 0])), (0, 8, ([2, 0], [0, 1], [0, 0], [0, 0], [0, 0], [4, 1], [0, 0], [2, 0])), (4, 6, (0, 3, 0, 0, 3, 4)), (3, 5, ([0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 5], [3, 0, 0, 0])), (6, 2, ([3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0, 1]))]
-----------------------------------
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
-----------------------------------
```
이렇게 해결을 할 수 있었다.  

이제 원래 배열에 넣어보면
```python
146
143
146
146
146
146
146
.
.
.
```
으로 시간이 너무 오래 걸리고 바로 해결을 하지 못하게된다.  
2-7점 가량 높아지긴 했으나 여전히 만점까진 25점 정도 남았다.  

수정한 코드를 유심히 보다보니 한가지 오류를 발견했다.  
바로 정사각형 로직을 단순화 시키려다보니 왼쪽 하단 오른쪽 상단을 부숴야하는 상황을 부수지 못하였다.  
<br>
```python
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
```
이렇게 direction을 추가해서 up인 경우도 따로 적어줬다.  
expected_destroyed_apple 함수와 get_pruning_value_map 함수에도 up 방향을 전부 추가해준 뒤,  

원래 배열에 넣어보면   
```python
152
152
152
149
152
152
149
.
.
.
```
으로 아까보다 최대 9점이나 올랐다!  
이제 170점까지 18점만 더 해결하면 된다.  
