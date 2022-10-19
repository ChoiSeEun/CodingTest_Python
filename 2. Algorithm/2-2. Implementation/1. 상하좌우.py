N = int(input())
plans = list(input().split())
x,y = 1,1

for i in range(len(plans)):
    if plans[i]=='L': # 왼쪽
        if (y-1)<1:
            pass
        else:
            y -= 1
    elif plans[i]=='R': # 오른쪽
        if (y+1)>N:
            pass
        else:
            y += 1
    elif plans[i]=='U': # 위
        if (x-1)<1:
            pass
        else:
            x -= 1
    else: # 아래
        if (x+1)>N:
            pass
        else:
            x += 1 
print(x,y)