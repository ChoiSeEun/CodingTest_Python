 # ----------------------------- 230103 답안 ------------------------------------
n = input()

mid = int(len(n)/2)
left = n[:mid]
right = n[mid:]

left = list(map(int,left))
right = list(map(int,right))

if sum(left)==sum(right):
    print("LUCKY")
else:
    print("READY")

# ----------------------------- 예시 답안 ------------------------------------
n = input()
length = len(n)
summary = 0 

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2,length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")