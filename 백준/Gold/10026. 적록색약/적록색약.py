from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, type):
    q = deque([(start[0], start[1])])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if type == "RGB" and not RGB[nx][ny]:
                    if arr[x][y] == arr[nx][ny]:
                        q.append((nx, ny))
                        RGB[nx][ny] = 1
                elif type == "RB" and not RB[nx][ny]:
                    if (arr[x][y] == "R" or arr[x][y] == "G") and (arr[nx][ny] == "R" or arr[nx][ny] == "G"):
                        q.append((nx, ny))
                        RB[nx][ny] = 1
                    if arr[x][y] == "B" and arr[nx][ny] == "B":
                        q.append((nx, ny))
                        RB[nx][ny] = 1

n = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(n)]
RGB = [[0] * n for _ in range(n)]
RB = [[0] * n for _ in range(n)]
res1, res2 = 0, 0

for i in range(n):
    for j in range(n):
        if not RGB[i][j]:
            bfs((i, j), "RGB")
            res1 += 1
        if not RB[i][j]:
            bfs((i, j), "RB")
            res2 += 1

print(res1, res2)