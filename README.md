# 사과게임 치터 만들어보기

얼마 전 사과게임을 해보다가 사과게임 치터를 만들어보면 어떨까..라는 생각이 들었다.  

1인게임으로만 즐길 수 있는 게임이기 때문에 가볍게 만들어보면서 공부해볼 예정이다.  
<br>
## 실행 방법
### 설치해야할 패키지
```bash
pip install selenium opencv-python numpy pytesseract
```
selenium을 실행하려면 chrome driver 먼저 다운받고 같은 파일에 넣어두자.  
https://googlechromelabs.github.io/chrome-for-testing/
<br><br><br>
## 실행 결과
제작중 
## 코드 소개
### 사과게임 룰
제작중
## 시행착오
### 첫번째 방법
```python
def break_right(array_apple, current_row, current_col):
    rows = 10
    cols = 17

    apple_now = array_apple[current_row][current_col]

    # 1. 오른쪽 n칸 판단
    apple_hap = apple_now
    n = 16 - current_col

    for i in range(n):
        plus_col = current_col + 1 + i
        apple_hap += array_apple[current_row][plus_col] 

        if apple_hap == 10:
            array_apple[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

        if apple_hap > 10:
            break

    # 2. 아래 n칸 판단
    apple_hap = apple_now
    n = 9 - current_row
    for i in range(n):
        plus_row = current_row + 1 + i
        apple_hap += array_apple[plus_row][current_col]

        if apple_hap == 10:
            for i in range(current_row, plus_row + 1):
                array_apple[i][current_col] = 0
            return
        if apple_hap > 10:
            break
```
가장 왼쪽부터 한 칸씩 움직여 가며 오른쪽으로 n칸 합이 10인 경우에 0으로 바꾸고,
10이 되는 경우의 수가 없다면 아래로 n칸 합이 10인 경우에 0으로 바뀌도록 해봤다.  

유튜브에서 사과점수 170점을 얻으신 분의 사과 숫자를 소스로 써서 내 방법이 몇 점까지 올릴 수 있는지 판단할 것이다.  
<br>
#### 초기 사과
```python
[2, 9, 1, 2, 2, 8, 4, 1, 1, 4, 2, 3, 3, 4, 3, 8, 8]
[7, 7, 2, 8, 3, 4, 9, 1, 9, 3, 5, 4, 7, 2, 4, 2, 3]
[7, 9, 4, 2, 5, 6, 1, 2, 4, 7, 9, 5, 1, 4, 3, 7, 6]
[2, 8, 6, 9, 3, 1, 2, 4, 5, 6, 3, 8, 9, 5, 5, 4, 1]
[3, 4, 1, 3, 4, 4, 6, 7, 6, 9, 1, 7, 3, 1, 8, 5, 7]
[3, 9, 6, 9, 5, 7, 9, 8, 3, 2, 8, 8, 8, 1, 4, 1, 4]
[1, 2, 6, 7, 5, 8, 4, 6, 1, 3, 5, 1, 5, 3, 2, 3, 5]
[7, 5, 5, 1, 6, 3, 7, 1, 5, 5, 2, 9, 5, 5, 4, 7, 1]
[5, 1, 8, 5, 9, 4, 6, 2, 5, 4, 7, 8, 1, 3, 6, 7, 8]
[5, 1, 8, 4, 1, 1, 2, 9, 9, 3, 2, 5, 5, 5, 2, 1, 1]
```
#### 이후 사과
```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 7, 0, 0, 0, 0, 0, 0, 9, 0, 5, 4, 7, 2, 0, 0, 0]
[0, 9, 0, 2, 5, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 7, 0]
[0, 0, 0, 9, 0, 0, 0, 0, 5, 6, 3, 8, 9, 0, 5, 0, 0]
[0, 4, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
[0, 9, 6, 9, 0, 7, 9, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0]
[0, 2, 6, 7, 0, 8, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 7, 0, 0, 5, 2, 0, 0, 5, 0, 0, 0]
[0, 1, 8, 5, 0, 0, 0, 2, 0, 4, 7, 8, 0, 0, 0, 7, 8]
[0, 1, 8, 4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 115점
```
0으로 바꾼 개수 만큼이 최종 점수가 되므로 이 방법으로는 115점밖에 얻지 못한다.  
다른 방법을 고민해보면서 고득점을 얻을 수 있는 조건을 생각해보았다.  
<br> 
- #### 사각형 모양을 처리할 수 있어야한다. 
- #### 숫자 9나 8과 같은 처리하기 힘든 숫자부터 먼저 처리해보자.
- #### 각 숫자의 개수를 먼저 세어보고 중요한 경로를 먼저 짜보자.
실제 나올 수 있는 숫자를 세어보니, 숫자 9가 1보다 많거나 어떠한 방법으로도 사과를 다 없애지 못하는 경우가 대부분이었다.
나올 수 있는 숫자의 개수가 존재하긴하나, 디테일한 조건은 따로 없는 것 같다. (사과의 총합은 항상 10으로 나누어 떨어진다.)

또한 각 숫자의 개수를 세어보고, 높은 숫자가 많으면 리셋을 시키는게 고득점을 얻기에 유리하다고 판단했다.  
<br>
| 숫자 | 개수 |
|------|------|
| 1    | 26   |
| 2    | 19   |
| 3    | 20   |
| 4    | 21   |
| 5    | 25   |
| 6    | 12   |
| 7    | 16   |
| 8    | 16   |
| 9    | 15   |

170점이 가능한 사과 숫자의 소스를 정리해보았다.  
6,7,8,9가 각각 1,2,3,4보다 적게 나오는 상황에만 코드를 실행하도록 만들어야겠다.   
<br>
### 두번째 방법
```python
def highnum_first(array_apple, current_row, current_col):
    rows = 10
    cols = 17

    apple_now = array_apple[current_row][current_col]

    apple_hap = apple_now

    plus_col = current_col + 1
    apple_hap += array_apple[current_row][plus_col] 

    if apple_now in [1,2,8,9]:
        if apple_hap == 10:
            array_apple[current_row][current_col:plus_col + 1] = [0] * (plus_col - current_col + 1)
            return

    apple_hap = apple_now
    
    plus_row = current_row + 1
    apple_hap += array_apple[plus_row][current_col]
    
    if apple_now in [1,2,8,9]:
        if apple_hap == 10:
            for i in range(current_row, plus_row + 1):
                array_apple[i][current_col] = 0
            return
``` 
높은 숫자인 9와 8을 먼저 없애보았다.  
<br>  
#### 이후 사과
```python
[0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
[0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 9, 0, 0, 0, 0, 0, 0, 4, 0, 9, 5, 0, 0, 0, 0, 0]
[0, 0, 0, 9, 0, 0, 0, 0, 5, 6, 0, 8, 0, 0, 5, 0, 0]
[0, 4, 1, 3, 4, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 7]
[0, 9, 6, 9, 0, 7, 9, 8, 0, 0, 0, 8, 8, 1, 0, 0, 0]
[0, 2, 6, 7, 0, 8, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 8, 5, 0, 0, 0, 2, 0, 4, 7, 8, 0, 0, 0, 7, 8]
[0, 1, 8, 4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 120점
```
숫자 9는 1 외에는 10을 만들 수 있는 숫자가 없기 때문에 먼저 없애면 점수가 크게 높아질 줄 알았으나    
120점으로 유의미한 변화는 없었다.  
<br>
### 세번째 방법
```python
    apple_hap = 0
    target_row = current_row + 1
    target_col = current_col + 1

    while True:
        if target_col >= 17:
            break
        if target_row >= 10:
            break

        for i in range(current_row, target_row):
            for j in range(current_col, target_col):
                apple_hap += array_apple[i][j]

        if apple_hap == 10:
            for i in range(current_row, target_row):
                for j in range(current_col, target_col):
                    array_apple[i][j] = 0
            return
        
        if apple_hap > 10:
            break

        target_col += 1
        if target_col >= 16:
            target_row += 1
            target_col = current_col + 1
``` 
더 많은 사과를 없애기 위해서 멀리 대각선 방향으로 떨어진 사과도 처리해야겠다.
2*2 이상의 사각형도 처리해주는 코드를 짜보았다.  
<br>  
#### 이후 사과
```python
[0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
[0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 9, 0, 2, 0, 0, 0, 2, 4, 0, 9, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 9, 0, 0, 0, 0, 5, 6, 0, 8, 0, 0, 0, 0, 0]
[0, 4, 1, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 7]
[0, 0, 6, 9, 0, 7, 0, 8, 0, 0, 0, 8, 8, 0, 0, 0, 0]
[1, 0, 0, 7, 0, 8, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
[7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 0, 0, 0, 7, 8]
[0, 0, 8, 4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# 132점
```
멀리 있는 사각형을 처리할 수 있으니, 132점으로 전에 비해 훨씬 높은 점수를 받을 수 있었다.  
이제 사과를 처리하는 기본적인 방법은 모두 준비가 되었다.   
<br>  
### 네번째 방법  
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
def check_break_apple(copy_array):
    prev_copy_array = copy.deepcopy(apple_array)

    while is_array_change(copy_array, prev_copy_array):
        prev_copy_array = copy.deepcopy(copy_array)
        for i in range(ROW):
            for j in range(COL):
                break_apple_right(copy_array, i, j) 

                break_apple_under(copy_array, i, j)

                break_apple_square(copy_array, i, j)

    cnt = 0
    for i in range(0,ROW):
        for j in range(0,COL):
            if copy_array[i][j] == 0:
                cnt += 1

    return cnt
```
0으로 바꿀 수 있는 경우가 몇 가지 남았는지 체크하는 코드를 짜주고  
<br>
```python
def is_break_apple_where(where, current_row, current_col, max_cnt):
    copy_array = copy.deepcopy(apple_array)
    now_cnt = None

    match where:
        case 1:
            if break_apple_right(copy_array, current_row, current_col):
                now_cnt= check_break_apple(copy_array)
        case 2:
            if break_apple_under(copy_array, current_row, current_col):
                now_cnt = check_break_apple(copy_array)
        case 3:
            if break_apple_square(copy_array, current_row, current_col):
                now_cnt = check_break_apple(copy_array)
    
    if now_cnt is None:
        return False, max_cnt  

    if now_cnt > max_cnt:
        max_cnt = now_cnt
        return True, max_cnt
    
    else:
        return False, max_cnt


def simulate_break(apple_array):
    current_row, current_col = 0, 0   
    target_row, target_col = 0, 0 

    while True:
        max_cnt = 0
        how_break = 0
        for i in range(1, 4):
            change_target, max_cnt = is_break_apple_where(i, current_row, current_col, max_cnt)

            if change_target:
                target_row, target_col = current_row, current_col
                how_break = i
        
        
        if how_break == 1:
            break_apple_right(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        elif how_break == 2:
            break_apple_under(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        elif how_break == 3:
            break_apple_square(apple_array, target_row, target_col)
            for row in apple_array:
                print(row)
            print("-----------------------------------")
        else:
            pass


        if current_col < COL - 1:
            current_col += 1
        elif current_col == COL - 1 and current_row < ROW - 1:
            current_col = 0
            current_row += 1
        else:
            is_finish = copy.deepcopy(apple_array)
            for i in range(ROW):    
                for j in range(COL):
                    break_apple(is_finish, i, j)
            if not is_array_change(apple_array, is_finish):
                print("finish")
                break
            else:
                current_row, current_col = 0, 0   
                target_row, target_col = 0, 0 

```
이렇게 코드를 짜보았다.  
먼저 시작점 (0,0)에서 오른쪽, 왼쪽, 사각형 중 합을 10으로 만들수 있는 경우의 수를 구한다.  
10으로 만들 수 있는 한 상황에서 0으로 변화 후, 내가 0으로 바꿀 수 개수를 구한다.  
그렇게 각각의 경우에서 최종 결과가 가장 나을 때 해당 공간을 0으로 바꾼다.   
<br>
```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 7, 2, 0, 3, 0, 0, 0, 9, 0, 5, 4, 7, 0, 0, 0, 0]
[0, 9, 0, 0, 0, 0, 0, 0, 4, 0, 9, 0, 0, 0, 0, 7, 0]
[0, 0, 0, 9, 0, 0, 0, 0, 5, 6, 3, 8, 9, 0, 0, 0, 0]
[0, 4, 1, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7]
[0, 9, 6, 9, 0, 7, 9, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0]
[0, 2, 6, 7, 0, 8, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 7, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0]
[0, 1, 8, 5, 0, 0, 0, 0, 0, 4, 7, 8, 0, 0, 0, 7, 8]
[0, 1, 8, 4, 0, 1, 2, 9, 9, 0, 0, 0, 0, 0, 2, 1, 1]
# 113점
```


