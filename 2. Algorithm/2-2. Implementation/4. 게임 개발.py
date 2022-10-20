n,m = map(int,input().split())

# 맵 초기화
d = [[0] * m for _ in range(n)]
x,y,direction = map(int,input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맴 정보 
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction == 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left = 0
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] ==0 and array[nx][ny] ==0: # 정면에 가보지 않은 칸
        d[nx][ny] = 1
        x = nx 
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 가보지 않은 칸이 없거나 바다
        turn_time = 1
    
    if turn_time ==4:  # 네 방향 모두 이동 불가
        nx = x-dx[direction]
        ny = y-dx[direction]
        
        if array[nx][ny] == 0: # 뒤로 갈 수 있는 경우
            x = nx
            y = ny
        else:
            break
        turn = 0 
print(count)
