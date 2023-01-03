 # ----------------------------- 230103 답안 ------------------------------------
s = input()
char_list =[]
num_sum = 0 

for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        char_list.append(s[i])
    else:
        num_sum += int(s[i])

char_list.sort()
print("".join(char_list),num_sum,sep='')

# ----------------------------- 예시 답안 ------------------------------------
data = input()
result = []
value = 0 

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value!=0:
    result.append(str(value))
    
print("".join(result))