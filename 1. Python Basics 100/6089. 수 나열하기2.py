a,r,n = input().split()
a = int(a)
r = int(r)
n = int(n)
cnt = 1
while cnt<n:
    a *= r 
    cnt += 1
print(a)