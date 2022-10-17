N = int(input())
count = []
coins = [500,100,50,10]

for coin in coins:
    count.append(N//coin)
    N = N % coin
print(count)