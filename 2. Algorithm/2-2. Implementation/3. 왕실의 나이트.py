position = input()
row = int(position[1]) # 행 위치 저장 
column = ord(position[0])-ord('a')+1 # 열 위치 저장 
count = 0
# print(row,column)
# 왼쪽
if column>2:
    if row != 1:
        count += 1
    if row != 8:
        count += 1 
# 오른쪽
if column<7:
    if row!=1:
        count += 1
    if row!=8:
        count += 1
# 위쪽
if row >2:
    if column != 1:
        count += 1
    
    if column != 8:
        count += 1

# 아래쪽
if row <7:
    if column != 1:
        count += 1
    if column != 8:
        count += 1 
print(count)

