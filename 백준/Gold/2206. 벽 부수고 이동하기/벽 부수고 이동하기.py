import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][z]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and z == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    queue.append([nx, ny, 1])
                elif arr[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())