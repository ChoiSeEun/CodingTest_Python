# ----------------------------- 230102 답안 ------------------------------------
n = int(input())
people = list(map(int,input().split()))
people.sort()
people.reverse()

group = 0
for x in people:
    if n<0 or n<x:
        break
    n = n -3
    group += 1 
print(group)

# ----------------------------- 예시 답안 ------------------------------------
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0 

for i in data:
    count +=i
    if count>=i:
        result += 1
        count = 0 

print(result)

