
 # ----------------------------- 230103 답안 ------------------------------------
from collections import deque

def solution(food_times, k):
    queue = deque()
    for i in range(len(food_times)):
        queue.append((i+1,food_times[i]))
    
    for _ in range(k):
        id,cost = queue.popleft()
        #print(id,cost)
        cost -= 1 
        if cost>0:
            queue.append((id,cost))

    answer = 0
    if queue:
        id,cost = queue.popleft()
        answer = id
    else:
        answer = -1
    return answer

food_times = list(map(int,input().split()))
k = int(input())
print(solution(food_times,k))

# ----------------------------- 예시 답안 ------------------------------------
import heapq

def solution(food_times,k):
    if sum(food_times)<=k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value = 0 
    previous = 0 
    length = 0 

    while sum_value + ((q[0][0]-previous)+length)<=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now 
    
    result = sorted(q,key=lambda x:x[1])
    return result[(k-sum_value)%length][1]