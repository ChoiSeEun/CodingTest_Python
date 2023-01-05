 # ----------------------------- 230105 답안 ------------------------------------
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

def dfs(graph,v,visited):
    result = []
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True       
            dfs(graph,i,visited)

distance = 0
result = []
visited = [False]*(n+1)
visited[x] = True 

for i in graph[x]:
    distance += 1
    while(distance<k):
        if len(graph[i])==0:
            break
        else:
            distance += 1

# ----------------------------- 예시 답안 ------------------------------------

from collections import deque

n,m,k.x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0 

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            q.append(next_node)

check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True 
if check == False:
    print(-1)