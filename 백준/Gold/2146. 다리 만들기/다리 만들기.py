from collections import deque
import sys
input = sys.stdin.readline
def bfs(sx, sy):
    q = deque([(sx, sy)])
    arr[sx][sy] = tmp
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = tmp
                q.append((nx, ny))

def check(cur, sx, sy):
    q = deque([(sx, sy, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] != cur:
                if arr[nx][ny] != 0:
                    path.append(cnt)
                    break
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tmp = 2
    path = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
                tmp += 1

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                check(arr[i][j], i, j)


    path.sort()
    print(path[0])