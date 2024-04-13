import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(sx, sy, cx, cy, cnt):
    if (sx, sy) == (cx, cy) and cnt >= 4:
        print('Yes')
        exit()

    for dx, dy in d:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if arr[sx][sy] == arr[nx][ny]:
                visited[nx][ny] = 1
                dfs(sx, sy, nx, ny, cnt + 1)
                visited[nx][ny] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(str, input().rstrip()))for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j, i, j, 0)

    print('No')