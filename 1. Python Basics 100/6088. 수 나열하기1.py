a,d,n = input().split()
a = int(a)
d = int(d)
n = int(n)
cnt = 1
while cnt<n:
    a += d
    cnt += 1
print(a)