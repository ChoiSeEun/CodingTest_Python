a,m,d,n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
cnt = 1
while cnt<n:
    a = a*m+d
    cnt += 1
print(a)