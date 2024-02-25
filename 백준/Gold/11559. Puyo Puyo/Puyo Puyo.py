from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = 1
    path = [(a, b)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny]:
                if arr[a][b] == arr[nx][ny]:
                    path.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    if len(path) >= 4:
        path.sort(key=lambda x: (x[1], x[0]))
        for x, y in path:
            arr[x][y] = '_'
            tmp.append((x, y))
        
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = [list(map(str, input().rstrip())) for _ in range(12)]

result = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    tmp = []
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and arr[i][j] != '_' and not visited[i][j]:
                bfs(i, j)
                
    if not tmp:
        print(result)
        break

    for i in tmp:
        for j in range(i[0], 0, -1):
            arr[j][i[1]] = arr[j - 1][i[1]]
        arr[0][i[1]] = '.'

    result += 1

