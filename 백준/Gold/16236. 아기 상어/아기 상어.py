from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, cur):
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 1
    tmp = []
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] <= cur:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    if arr[nx][ny] < cur and arr[nx][ny]:
                        tmp.append((nx, ny, dist[nx][ny]))

    tmp.sort(key=lambda x: (-x[2], -x[0], -x[1]))
    return tmp


d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n = int(input())
size, cnt, startX, startY, result = 2, 0, 0, 0, 0
arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 9:
            startX, startY = i, j
    arr.append(tmp)

while True:
    fish = bfs(startX, startY, size)
    if not fish:
        print(result)
        break

    endX, endY, time = fish.pop()
    result += time
    arr[startX][startY], arr[endX][endY] = 0, 0
    startX, startY = endX, endY

    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
