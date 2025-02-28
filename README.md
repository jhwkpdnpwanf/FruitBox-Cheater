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
```
숫자 9는 1 외에는 10을 만들 수 있는 숫자가 없기 때문에 먼저 없애면 점수가 크게 높아질 줄 알았으나    
120점으로 유의미한 변화는 없었다.  
<br>

