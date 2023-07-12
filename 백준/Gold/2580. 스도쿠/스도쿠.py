import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blank = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]
num = [i for i in range(1,10)]

def dfs(n):
    global board
    if n == len(blank):
        for i in board:
            print(*i)
        exit()    
    
    x,y = blank[n]
    a,b = x//3, y//3
    numbers = num[:]
    
    for i in range(9):
        if board[x][i] in numbers:
            numbers.remove(board[x][i])
        if board[i][y] in numbers:
            numbers.remove(board[i][y])

    for i in range(a * 3, (a + 1) * 3):
        for j in range(b * 3, (b + 1) * 3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    
    for i in numbers:
       board[x][y] = i
       dfs(n + 1)
       board[x][y] = 0    
    
dfs(0)
