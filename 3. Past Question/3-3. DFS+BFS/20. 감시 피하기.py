 # ----------------------------- 230106 답안 ------------------------------------


# ----------------------------- 예시 답안 ------------------------------------
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j]=='X':
            spaces.append((i,j))

def watch(x,y,direction):
    if direction == 0: # 왼쪽 방향 감시 
        while y>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y -= 1
    if direction == 1: # 오른쪽 방향 감시
        while y<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False 
            y += 1
    if direction ==2: # 위쪽 방향 감시 
        while x>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x -= 1 
    if direction==3: # 아래쪽 방향 감시 
        while x<n:
            if board[x][y]=='S':
                return True 
            if board[x][y]=='O':
                return True 
            x += 1
    return False

def process(): # 모든 선생님에 대해서 학생들이 감시되는지 검사 
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
        return False 

find = False
for data in combinations(spaces,3): # 모든 빈공간에 대해 3가지를 선택하는 조합
    for x,y in data: # 장애물 설치
        board[x][y]=='O'
    if not process(): # 모든 선생님들에 대해서 학생들이 감지되지 않는다면 
        find = True
        break

    for x,y in data: # 장애물 되돌리기 
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')