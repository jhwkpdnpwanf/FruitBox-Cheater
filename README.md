﻿# 사과게임 치터 만들어보기

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
<br><br>

## 사과게임 규칙
- **격자 크기**: 10x17 (가로x세로)
- **제한 시간**: 2분
- **세부 규칙**:
  - 합이 10이 되는 사과들을 제거할 수 있음
  - 제거된 사과의 개수만큼 점수 획득
  - 사각형 크기로만 드래그 가능  
<br><br>
## 최종 목표
- 제한 시간 내에 170점 달성 알고리즘 만들기  
- 실제 사과게임 창에서 170점을 달성해주는 봇 만들기
<br><br>

## 코드소개
제작중 ..<>
<br><br>

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

### 다섯번째 방법  

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
DFS(깊이 우선 탐색) 알고리즘과 백트래킹 알고리즘을 이용하여 배열이 갈 수 있는 모든 경우의 수를 다 가본 뒤, 만점이 되면 반환하는 함수를 만들어봤다.  
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






