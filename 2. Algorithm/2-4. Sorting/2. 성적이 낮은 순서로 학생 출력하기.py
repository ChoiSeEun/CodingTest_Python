N = int(input())
array = []

for i in range(N):
    name , score = input().split()
    array.append((name,int(score)))

def setting(data):
    return data[1]
def print_name(data):
    return data[0]

result = sorted(array,key=setting)

for i in result:
    print(print_name(i),end=' ')