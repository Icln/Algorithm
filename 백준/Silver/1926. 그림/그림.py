from collections import deque
import sys
input = sys.stdin.readline
def bfs(sx, sy):
    global size
    q = deque([(sx, sy)])
    arr[sx][sy] = 0
    tmp = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                arr[nx][ny] = 0
                q.append((nx, ny))
                tmp += 1

    size = max(size, tmp)

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    size, cnt = 0, 0

    for i in range(n):
        for j in range(m):
            if arr[i][j]:
               cnt += 1
               bfs(i, j)

    print(cnt)
    print(size)