 # ----------------------------- 230104 답안 ------------------------------------

def cal_distance(r1,c1,r2,c2):
    return abs(r1-r2)+(c1+c2)    

# 각 집의 치킨 거리 계산 
def shortest_chicken(n,city,r1,c1):
    min_distance = 0
    for i in range(1,n):
        for j in range(1,n):
            if city[i][j] == 2:
                distance = cal_distance(r1,c1,i,j)
                min_distance = min(min_distance,distance)
    return min_distance

n,m = map(int,input().split())
city = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    city[i] = list(map(int,input().split()))

# ----------------------------- 예시 답안 ------------------------------------
from itertools import combinations

n,m = map(int,input().split())
chicken,house = [],[]

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c]==1:
            house.append((r,c))
        elif data[c]==2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m)) # 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 

# 치킨 거리의 합
def get_sum(candidate):
    result = 0 
    for hx,hy in house:
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))
        result += temp
    return result 

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result,get_sum(candidate))
print(result)

