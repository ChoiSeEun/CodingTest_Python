 # ----------------------------- 230105 답안 ------------------------------------
n,k = map(int,input().split())
data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

s,x,y =  map(int,input().split())
t = 0 
dx = [-1,0,1,0]
dy = [0,1,0,-1]
virus = 1 # 1부터 시작 
temp = data.copy() # 매 시점의 변화 기록

while(t<s):
    while (virus<=k): # 1부터 k번째 바이러스까지 확인 
        for i in range(0,n):
            for j in range(0,n):
                if data[i][j]==virus: # 해당하는 바이러스를 찾으면
                    for m in range(4): # 상하좌우로 확장 
                        nx = i + dx[m]
                        ny = j + dy
                        # 확장이 가능하면 
                        if nx>=0 and nx<n and ny>=0 and ny<n and data[nx][ny]==0:
                            temp[nx][ny] = virus # 번식 후 
                            data[nx][ny] = -1  # 번식 불가한 자리 표시
        
        virus += 1 
    t += 1
    data = temp.copy()
    virus = 1

print(data[x-1][y-1])    



# ----------------------------- 예시 답안 ------------------------------------
from collections import deque

n,k = map(int,input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))

data.sort()
q = deque(data)

target_s,target_x,target_y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus,s,x,y = q.popleft()
    if s==target_s:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<-nx and nx<n and 0<=ny and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
print(graph[target_x-1][target_y-1])