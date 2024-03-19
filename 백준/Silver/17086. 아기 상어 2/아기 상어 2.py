from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
n, m = map(int, input().split())
arr = []
q = deque()
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j]:
            q.append((i, j))
    arr.append(tmp)

bfs()
result = 0
for i in range(n):
    for j in range(m):
        result = max(result, arr[i][j])

print(result - 1)