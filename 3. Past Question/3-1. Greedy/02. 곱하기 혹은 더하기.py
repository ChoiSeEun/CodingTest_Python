# ----------------------------- 230102 답안 ------------------------------------
data = input()
result = 0

one = int(data[0])
two = int(data[1])

if one==0 or two ==0:
    result += (one+two)
else:
    result += (one*two)

for i in range(2,len(data)):
    now = int(data[i])
    if now == 0:
        result += now
    else:
        result *= now

print(result)

# ----------------------------- 예시 답안 ------------------------------------
data = input()
result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num
print(result)