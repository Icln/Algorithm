from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    arr[x][y] = 1 
    size = 1    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                q.append((ny, nx))
                size += 1
    return size

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

result = []
for i in range(m):
    for j in range(n):
        if not arr[i][j]:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))