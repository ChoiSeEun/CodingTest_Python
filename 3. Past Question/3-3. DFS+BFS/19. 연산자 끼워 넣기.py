 # ----------------------------- 230106 답안 ------------------------------------
n = int(input())
data = list(map(int,input().split()))
oper = list(map(int,input().split()))

def oper_cal(a,b,oper):
    if oper == 0:
        return a+b
    elif oper ==1:
        return a-b
    elif oper ==2:
        return a*b
    else:
        if a<0:
            a = abs(a)
            temp = a//b 
            return temp*(-1)
        else:
            return a//b

min_result = 0
max_result = 0
current_result = 0 

# from itertools import 

# ----------------------------- 예시 답안 ------------------------------------
n = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i,now):
    global min_value,max_value,add,sub,mul,div
    if i ==n:
        min_value = min(min_value,now)
        max_value = max(max_value,now)
    else:
        if add>0:
            add -= 1
            dfs(i+1,now+data[i])
            add += 1
        if sub>0:
            sum -= 1
            dfs(i+1,now-data[i])
            sub += 1
        if mul>0:
            mul -= 1
            dfs(i+1,now*data[i])
            mul += 1
        if div>0:
            div -= 1
            dfs(i+1,int(now/data[i]))
            div += 1
dfs(1,data[0])

print(min_value)
print(max_value)