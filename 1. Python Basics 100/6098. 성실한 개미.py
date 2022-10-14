board = []
x = 1
y = 1

for i in range(10):
    temp = list(map(int,input().split()))
    board.append(temp)
    
while True:
    if board[x][y] == 2: 
        board[x][y] = 9
        break
    elif board[x+1][y] == 1 and board[x][y+1] == 1:
        board[x][y] = 9
        break
    board[x][y] = 9
    if board[x][y+1] == 1: 
        x += 1
    elif board[x+1][y] == 1: 
        y += 1
    else: y += 1 

for a in board:
    for b in a:
        print(b,end=' ')
    print()