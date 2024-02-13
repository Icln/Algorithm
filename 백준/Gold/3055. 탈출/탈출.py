from collections import deque
import sys
input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    while q:
        r, c = q.popleft()
        if endR == r and endC == c:
            return dis[r][c]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if (arr[nr][nc] == '.' or arr[nr][nc] == 'D') and arr[r][c] == 'S':
                    arr[nr][nc] = 'S'
                    dis[nr][nc] = dis[r][c] + 1
                    q.append((nr, nc))
                elif (arr[nr][nc] == '.' or arr[nr][nc] == 'S') and arr[r][c] == '*':
                    arr[nr][nc] = '*'
                    q.append((nr, nc))
    return "KAKTUS"


R, C = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(R)]
dis = [[0] * C for _ in range(R)]
q = deque()
endR, endC = 0, 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            q.append((i, j))
        elif arr[i][j] == 'D':
            endR, endC = i, j

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            q.append((i, j))


print(bfs())