import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    depth = 0
    for i, j, k in q:
        queue.append([i, j, k])
    
    while queue:
        tx, ty, td = queue.popleft()
        depth = td
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]
            if  0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0: 
                arr[nx][ny] = 1
                queue.append([nx, ny, td + 1]) 
    
    flag = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                flag = False
                break
    if flag:
        print(depth)
    else:
        print(-1)
    return 

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = []
for i in range (n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, 0])

bfs()