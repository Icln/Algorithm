import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    global size
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if arr[x][y] == 1:
        return False

    arr[x][y] = 1
    size += 1

    for i in range(4):
        dfs(x + dx[i], y + dy[i])
    return True

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
size = 0

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

sizes = []
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            sizes.append(size)
            size = 0

sizes.sort()
print(len(sizes))
for size in sizes:
    print(size, end=' ')