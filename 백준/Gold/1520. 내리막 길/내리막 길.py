import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == row - 1 and y == col - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0 
    for i in range(4):
        tempX = x + newX[i]
        tempY = y + newY[i]
        if tempX < 0 or tempX > row - 1 or tempY < 0 or tempY > col - 1:
            continue
        if map[x][y] > map[tempX][tempY]:
            dp[x][y] += dfs(tempX, tempY)
    
    return dp[x][y] 

row, col = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(row)]
dp = [[-1] * col for _ in range(row)]
newX = [1, -1, 0, 0]
newY = [0, 0, 1, -1]

print(dfs(0, 0))
