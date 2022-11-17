N,M = map(int,input().split())
ddok = list(map(int,input().split()))

ddok.sort(reverse=True)
H = ddok[0]
customer = 0 

while True:
    if customer >= M:
        print(H)
        break
    H = H - 1 
    result =list(map(lambda x:x-H,ddok))
    result = list(map(lambda x:0 if x<=0 else x,result))
    customer = sum(result)
    