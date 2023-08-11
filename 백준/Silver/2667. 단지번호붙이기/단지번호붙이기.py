import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
map = [list(map(int, input().rstrip())) for _ in range(n)]
result = []
home = 0

def dfs(row, col):
    global home
    if row < 0 or row >= n or col < 0 or col >= n:
        return False
    if map[row][col] == 1:
        home += 1
        map[row][col] = 0
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        return True
    return False
             
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(home)
            home = 0  

result.sort()
print(len(result))
for i in result:
    print(i)
