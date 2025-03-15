## 세번째 방법  
사과를 전부 부수기 위해서 모든 경로를 탐색해볼 예정이다.   
<br>
한 경로를 탐색해보고 정답이 아니라면 배열을 복원해 다른 경로를 가볼 수 있는   
DFS(깊이우선탐색)과 백트래킹 알고리즘을 활용할 것이다.  
```python
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
```
재귀함수로 DFS(깊이우선탐색)을 제대로 구현하기 위해 기존 로직들을 전부 수정해줬다. (부순 정보를 리턴해줌)  
속도를 조금이라도 높이기 위해 튜플로 (row, col, value to recover)를 리턴한다.  
break_apple_square 같은 경우엔 0이 많을수록 시간이 오래 걸리기때문에 자신보다 오른쪽 혹은 아래가 전부 0일때 연산을 뛰어넘는 조건도 추가해줬다.  
<br>
```python
def search_best_path(array, trace_path):

    if count_score(array) == ROW*COL:
        print("finish")
        return True
    
    for i in range(ROW):
        for j in range(COL):
            step_right = break_apple_right(array, i, j)
            if step_right:
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
```
배열이 갈 수 있는 모든 경우의 수를 다 가본 뒤, 만점이 되면 반환하는 함수를 만들어봤다.  
이 함수는 **판단 및 변화 → 기록 → 재귀 → 복원**의 흐름으로 만들었다.  
#### 1. 판단 및 변화
> `step_right = break_apple_right(array, i, j)`  

#### 2. 기록
> `trace_path.append(step_right)`

#### 3. 재귀 호출
> `if search_best_path(array, trace_path):`

#### 4. 복원
> `array[row][col] = v`

#### 초기사과
```python
apple_array = [
    [7,2,8,2,3],
    [7,2,5,8,3],
    [7,2,5,2,3],
    [7,2,8,8,2],
    [7,2,2,3,3]
]
```
#### 이후사과
```python
result path:  [(0, 1, (2, 8)), (0, 2, (0, 5, 5)), (0, 2, ([0, 2], [0, 8])), (0, 3, (0, 0, 2, 8)), (3, 2, (8, 0, 2)), (0, 1, ([0, 0], [2, 0], [2, 0], [0, 0, 0, 3)), (2, 0, (7, 0, 0, 0, 3)), (4, 0, (7, 0, 0, 3)), (3, 0, ([7, 0, 0, 0, 0], [0, 0, 0, 0, 3]))]
-----------------------------------
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
-----------------------------------
```
경로와 사과가 잘 부서졌다.   
그래서 기존 코드에도 넣어봤더니  
<br>
5분 동안 돌려도 끝나질 않았다.  
search_best_path 함수 속에 점수를 보는 코드를 넣어 점수를 확인해보면   
```python
139
141
139
139
139
138
141
... 계속
```
138점부터 141점 제각각인 점수들이 나온다.  
무한루프는 아니고 DFS + Backtracking + Brute Force 방식이라 경로탐색에 무수히 많은 시간이 소요되는 것 같다.  

### 개선할 점
#### 1. DLS (Depth-Limited Search, 깊이 제한 탐색) 사용
- 잘못된 경로를 깊게 탐색했던 DFS를 개선

#### 2. Backtracking (백트래킹) 개선
- 효율적인 백트래킹을 위해 가지치기가 필수

#### 3. Greedy Algorithm (그리디 알고리즘) 사용
- 전체 경로에서 길을 찾으려니 비효율적이였음
- 현재단계 ~ +10번째 단계 내에서 가장 효율적인 경로를 우선 탐색


