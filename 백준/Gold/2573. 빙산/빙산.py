from collections import deque
import sys
input = sys.stdin.readline
def bfs(sx,sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    cnt = []
    while q:
        x, y = q.popleft()
        tmp = 0

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if not arr[nx][ny]:
                    tmp += 1
        if tmp > 0:
            cnt.append((x, y, tmp))

    for x, y, z in cnt:
        arr[x][y] = max(0, arr[x][y] - z)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    while True:
        visited = [[0] * m for _ in range(n)]
        num = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if arr[i][j] and not visited[i][j]:
                    bfs(i, j)
                    num += 1

        result += 1
        if not num:
            print(0)
            exit()

        if num >= 2:
            print(result - 1)
            break