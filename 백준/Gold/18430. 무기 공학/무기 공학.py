import sys
input = sys.stdin.readline

def dfs(x, y, tmp):
    global answer
    if y == m:
        x, y = x + 1, 0

    if x == n:
        answer = max(answer, tmp)
        return

    if not visited[x][y]:
        for i in range(4):
            nx1, ny1, nx2, ny2 = x + d[i][0], y + d[i][1], x + d[i][2], y + d[i][3]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if not visited[nx1][ny1] and not visited[nx2][ny2]:
                    visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = True
                    dfs(x, y + 1, tmp + arr[x][y] * 2 + arr[nx1][ny1] + arr[nx2][ny2])
                    visited[x][y] = visited[nx1][ny1] = visited[nx2][ny2] = False
    dfs(x, y + 1, tmp)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0, 0, 1), (0, -1, 1, 0), (-1, 0, 0, 1), (0, -1, -1, 0)]
visited = [[False] * m for _ in range(n)]
answer = 0

if n == 1 or m == 1:
    print(answer)
else:
    dfs(0, 0, 0)
    print(answer)
