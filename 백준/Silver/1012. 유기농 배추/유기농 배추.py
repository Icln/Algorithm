import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

for _  in range(int(input())):
    m, n, k = map(int, input().split()) 
    farm = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        farm[x][y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1
    print(cnt)