N,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B,reverse=True)

# print(A)
# print(B)

for i in range(K):
    A[i],B[i] = B[i],A[i]

# print(A)
# print(B)
print(sum(A))