## 두번째 방법  
170점을 세우기 위해서는 사과의 위치를 고려하는 것 보다 다음에 처리할 사과까지 고려해야 한다는 것을 깨달았다.  
<br>
예를 들어 아래와 같은 3*3 크기의 사과가 있다고 생각해보자.
<table>
    <tr><td>1</td><td>2</td><td>8</td></tr>
    <tr><td>3</td><td>8</td><td>7</td></tr>
    <tr><td>1</td><td>5</td><td>5</td></tr>
</table>   

- #### 방법 1
<table>  
  <tr>
    <td>
      <table border="1">
        <tr><td>1</td><td><b>2</b></td><td><b>8</b></td></tr>
        <tr><td>3</td><td>8</td><td>7</td></tr>
        <tr><td>1</td><td>5</td><td>5</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>1</td><td> </td><td> </td></tr>
        <tr><td>3</td><td>8</td><td>7</td></tr>
        <tr><td>1</td><td><b>5</b></td><td><b>5</b></td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>1</td><td> </td><td> </td></tr>
        <tr><td>3</td><td>8</td><td>7</td></tr>
        <tr><td>1</td><td> </td><td> </td></tr>
      </table>
    </td>
  </tr>
</table>  
가로로 놓인 숫자 2와 8을 먼저 처리하면 숫자를 4개밖에 없애지 못한다.  

- #### 방법 2
<table>  
  <tr>
    <td>
      <table border="1">
        <tr><td>1</td><td><b>2</b></td><td>8</td></tr>
        <tr><td>3</td><td><b>8</b></td><td>7</td></tr>
        <tr><td>1</td><td>5</td><td>5</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>1</td><td> </td><td>8</td></tr>
        <tr><td>3</td><td> </td><td>7</td></tr>
        <tr><td>1</td><td>5</td><td>5</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>1</td><td> </td><td>8</td></tr>
        <tr><td><b>3</b></td><td> </td><td><b>7</b></td></tr>
        <tr><td>1</td><td><b>5</b></td><td><b>5</b></td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td><b>1</b></td><td> </td><td><b>8</b></td></tr>
        <tr><td> </td><td>&nbsp;&nbsp;</td><td> </td></tr>
        <tr><td><b>1</b></td><td> </td><td> </td></tr>
      </table>
    </td>
  </tr>
</table>  
같은 숫자 2와 8을 처리하는 순서만 바꾸었을 뿐인데 점수가 두배 가량 늘었다.    
이와 같이 숫자를 단순히 처리하는 경우를 넘어서 다음 수까지 읽을 수 있어야 만점을 받을 수 있다는 것을 알았다.  
<br><br>
그렇다면 어떻게 순서를 판단해야할까?  
<br><br>  
아래의 예시를 보며 방법을 찾아보자.  
<br>
<table>
  <tr><td>9</td><td>1</td><td>6</td><td>1</td><td>2</td></tr>
  <tr><td>3</td><td>1</td><td>7</td><td>5</td><td>3</td></tr>
  <tr><td>1</td><td>8</td><td>4</td><td>5</td><td>4</td></tr>
</table>

- #### 풀이
<table>  
  <tr>
    <td>
      <table border="1">
        <tr><td>9</td><td><b>1</b></td><td>6</td><td>1</td><td>2</td></tr>
        <tr><td>3</td><td><b>1</b></td><td>7</td><td>5</td><td>3</td></tr>
        <tr><td>1</td><td><b>8</b></td><td>4</td><td>5</td><td>4</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>9</td><td>&nbsp;&nbsp;</td><td>6</td><td>1</td><td>2</td></tr>
        <tr><td>3</td><td>&nbsp;&nbsp;</td><td>7</td><td><b>5</b></td><td>3</td></tr>
        <tr><td>1</td><td>&nbsp;&nbsp;</td><td>4</td><td><b>5</b></td><td>4</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>9</td><td>&nbsp;&nbsp;</td><td>6</td><td>1</td><td>2</td></tr>
        <tr><td><b>3</b></td><td>&nbsp;&nbsp;</td><td><b>7</b></td><td>&nbsp;&nbsp;</td><td>3</td></tr>
        <tr><td>1</td><td>&nbsp;&nbsp;</td><td>4</td><td>&nbsp;&nbsp;</td><td>4</td></tr>
      </table>
    </td>
  </tr>
</table> 
<table>  
  <tr>
    <td>
      <table border="1">
        <tr><td>9</td><td>&nbsp;&nbsp;</td><td>6</td><td>1</td><td>2</td></tr>
        <tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>3</td></tr>
        <tr><td>1</td><td>&nbsp;&nbsp;</td><td>4</td><td>&nbsp;&nbsp;</td><td>4</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td>9</td><td>&nbsp;&nbsp;</td><td><b>6</b></td><td>1</td><td>2</td></tr>
        <tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>3</td></tr>
        <tr><td>1</td><td>&nbsp;&nbsp;</td><td><b>4</b></td><td>&nbsp;&nbsp;</td><td>4</td></tr>
      </table>
    </td>
    <td>
      <table border="1">
        <tr><td><b>9</b></td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>1</td><td>2</td></tr>
        <tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>3</td></tr>
        <tr><td><b>1</b></td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;</td><td>4</td></tr>
      </table>
    </td>
  </tr>
</table>   
만약 가장 높은 숫자를 먼저 처리하려 했다면 위 상황에서 높은 점수를 얻지 못한다.  <br>
오히려 8,1,1을 먼저 없애야 다음 단계로 넘어갈 수 있다.  <br><br>


그래서 생각해낸 방법이 처리하기 위한 숫자가 없어졌을 때 **처리할 수 있는 다음 숫자의 수 기억하기**이다.     
<br>

  <table border="1">
    <tr><td>9</td><td>&nbsp;&nbsp;</td><td>6</td><td>1</td><td>2</td></tr>
    <tr><td>3</td><td>&nbsp;&nbsp;</td><td>7</td><td>&nbsp;&nbsp;</td><td>3</td></tr>
    <tr><td>1</td><td>&nbsp;&nbsp;</td><td>4</td><td>&nbsp;&nbsp;</td><td>4</td></tr>
  </table>
이러한 경우에 합이 10을 만들 수 있는 방법은 3-7, 7-3, 1-2-3-4 총 세가지이다.  
그리고 각각 없어졌을 때 내가 처리할 수 있는 경우의 수가 더 많아질 때를 찾는다.  

| 방법 | 연결 수 | 예시 |
|--------|----------|---------------|
| 3-7  | 3개    | 9-1,  6-4,  1-2-3-4 |
| 7-3  | 1개    | 6-4 |
| 1-2-3-4 | 1개  | 6-4 |

3-7 방법일 때 주변에 연결 가능한 사과 수가 가장 많아지니 3-7 방법을 사용한다.  
실제 코드에서는 주변이 아닌 전체에서 가능한 연결 수로 판단하게 만드는 것이 확실하게 처리할 수 있을 것 같다.    
<br>
```python
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
```
작은 배열로 테스트를 해보기 위해서 기존의 코드를 함수로 객체지향으로 바꾸어줬다.  
ROW와 COL을 전역변수로 할당하고 가독성을 높이기 위해 일부 변수명도 바꾸어줬다.  
<br>
```python
def is_array_change(first_array, second_array):
    one = copy.deepcopy(first_array)
    two = copy.deepcopy(second_array)

    if one == two:
        return False
    else:
        return True
```
배열의 변화를 감지하는 반복문을 만들어주고    
<br>

```python
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
```

디버깅을 위한 점수세기, 배열프린트 함수도 만들어줬다.  
<br>
```python
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
```
재귀함수를 활용해서 최적의 전략을 찾아보겠다.  
내가 이전에 갔던 경로인지 확인해야 하기 때문에 trace_path로 경로를 저장하고, explored_index를 통해 첫 시작점을 판단한다 (첫 시작일 때는 0 이후엔 1).   
<br>
```python
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
```  
깊은 복사를 통해 독립적인 배열을 만들어주고 모든 경우의 수를 탐색한다.   
그리고 모든 블럭을 0으로 만들 수 있으면 i와 j를 각각 ROW와 COL로 변환시켜 반복문을 탈출한다.  
<br>
```python
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
```
trace_path에서 경로를 가져오고  
final_path에 최종경로를 저장하고 부수기를 실행한다.  
<br>
기존 사과가 너무 커서 ROW = 3, COL = 5인 위 예시를 활용했을때  
```python
-----------------------------------
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
-----------------------------------
its break!!!!!!!!
```
모두 부술 수 있었다.   
<br>
#### 이후 사과
```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
[0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0]
[0, 9, 0, 2, 5, 0, 0, 0, 4, 0, 9, 5, 0, 0, 0, 7, 6]
[0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
[0, 9, 6, 9, 0, 7, 9, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0]
[1, 2, 6, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 5, 0, 0, 8, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0]
# 136점
```
그래서 기존 코드에도 적용해보았는데,  결과는 136점으로 전부 점수에 큰 변화가 없었다.  
아마 한 좌표에서 여러 방법이 가능한 경우 경로처리가 잘 안 되어서 그런 것 같다.  
<br>
