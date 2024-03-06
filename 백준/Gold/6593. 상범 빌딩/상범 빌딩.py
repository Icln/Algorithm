from collections import deque
import sys
input = sys.stdin.readline
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
def bfs():
    q = deque([(sz, sy, sx, 0)])
    while q:
        z, y, x, cnt = q.popleft()
        if x == ex and y == ey and z == ez:
            return f"Escaped in {cnt} minute(s)."
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and visited[nz][ny][nx] == 0:
                if arr[nz][ny][nx] == '.' or arr[nz][ny][nx] == 'E':
                    q.append((nz, ny, nx, cnt + 1))
                    visited[nz][ny][nx] = 1

    return "Trapped!"

while True:
    l, r, c = map(int, input().split())
    if not l and not r and not c:
        break

    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    arr = [[] * r for _ in range(l)]

    for i in range(l):
        for j in range(r):
            arr[i].append(list(map(str, input().rstrip())))
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    sz, sy, sx = i, j, k
                    continue
                if arr[i][j][k] == 'E':
                    ez, ey, ex = i, j, k

    print(bfs())