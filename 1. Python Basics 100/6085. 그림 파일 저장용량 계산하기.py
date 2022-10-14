r,g,b = input().split()
r = int(r)
g = int(g)
b = int(b)

result = r*g*b/8/1024/1024
# result = round(result,2)
print("{:.2f} MB".format(result))
# print(result,"MB")