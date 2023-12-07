import sys
from collections import deque
input = sys.stdin.readline

def check(a, b, t):
    for i in times:
        if a == i[0] and b == i[1]:
            return False
        if i[2] > t:
            continue
        if abs(i[2] - t) >= abs(i[0] - a) + abs(i[1] - b):
            return False
    return True

def bfs(a, b):
    visited = [[True] * (n + 1)] + [[True] + [False] * n for _ in range(m)]
    q = deque([[a, b, 0]])
    visited[a][b] = True
    result = []
    while q:
        nx, ny, time = q.popleft()
        if check(nx, ny, time):
            result.append([arr[nx][ny], time])
        else:
            continue
        for i in range(4):
            if 1 <= nx + dx[i] <= m and 1 <= ny + dy[i] <= n and not visited[nx + dx[i]][ny + dy[i]]:
                q.append([nx + dx[i], ny + dy[i], time + 1])
                visited[nx + dx[i]][ny + dy[i]] = True
    return result

m, n, v = map(int, input().split())
x, y = map(int, input().split())
arr = [[]] + [[0] + list(map(int, input().split())) for _ in range(m)]
times = [list(map(int, input().split())) for _ in range(v)]
times.sort(key=lambda x: x[2])
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
answer = bfs(x, y)
answer.sort(key=lambda x:x[0], reverse= True)
print(answer[0][0], answer[0][1])