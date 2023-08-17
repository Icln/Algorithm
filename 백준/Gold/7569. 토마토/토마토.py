import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    depth = 0
    for i, j, k, d in q:
        queue.append([i, j, k, d])
    
    while queue:
        tz, tx, ty, td = queue.popleft()
        depth = td
        for i in range(6):
            nz, nx, ny = tz + dz[i], tx + dx[i], ty + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0: 
                arr[nz][nx][ny] = 1
                queue.append([nz, nx, ny, td + 1]) 
    
    flag = True
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    flag = False
                    break
    if flag:
        print(depth)
    else:
        print(-1)
    return 

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)] 
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0 ,0, 0, 0, 1, -1]
q = []

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k, 0])

bfs()