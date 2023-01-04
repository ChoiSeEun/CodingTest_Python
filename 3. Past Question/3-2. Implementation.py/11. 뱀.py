 # ----------------------------- 230104 답안 ------------------------------------
from collections import deque
n = int(input()) # 보드의 크기 
k = int(input()) # 사과의 개수 

# 보드 초기화
board =  [[0]*(n+1) for _ in range(n+1)]

# 사과 위치 입력 
for _ in range(k):
    x,y = map(int,input().split())
    board[x][y] = 1 

l = int(input()) # 방향변환횟수

queue = deque()
# 방향 변환 정보 입력
for _ in range(l):
    time,dir = input().split()
    time = int(time)
    queue.append((time,dir))

total_count = 0 
snake = (1,1)
moving = [(1,0),(-1,0),(0,1),(1,0)]
current_dir = 0

while(snake[0]!=n and snake[1]!=n):
    total_count += 1
    

# ----------------------------- 예시 답안 ------------------------------------

n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c=="L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction 

def simulate():
    x,y = 1,1 # 뱀의 머리 위치 
    data[x][y] = 2 # 뱀이 존재하는 위치 
    direction = 0  # 방향
    time = 0 # 시작한 뒤의 초
    index = 0  # 다음 회전 정보 
    q = [(x,y)] # 뱀이 차지하고 있는 위치 

    while True:
        # 이동 후
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 범위 내 위치 and 뱀의 몸통도 없는 경우 
        if 1<=nx and nx<=x and 1<=y and ny<=n and data[nx][ny]!=2:
            if data[nx][ny]==0: # 사과가 없는 경우 꼬리 뺴기 
                data[nx][ny]=2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0 
            
            if data[nx][ny]==1: # 사과가 있는 경우 꼬리 냅두기
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        x,y = nx,ny 
        time += 1 
        if index < l and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index += 1
        return time
print(simulate())