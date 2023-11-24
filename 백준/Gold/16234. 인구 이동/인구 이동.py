from collections import deque
n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, visited):
    queue = deque()
    queue.append((i, j))
    tmp = a[i][j]
    cnt = 1
    pos = []
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        pos.append((x, y))
        for k in range(4):
            if 0 <= x + d[k][0] <= n - 1 and 0 <= y + d[k][1] <= n - 1 and not visited[x + d[k][0]][y + d[k][1]]:
                if l <= abs(a[x][y] - a[x + d[k][0]][y + d[k][1]]) <= r:
                    visited[x + d[k][0]][y + d[k][1]] = True
                    tmp += a[x + d[k][0]][y + d[k][1]]
                    queue.append((x + d[k][0], y + d[k][1]))
                    cnt += 1

    for x, y in pos:
        a[x][y] = tmp // cnt
    return False if cnt == 1 else True

result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    flag = True

    if not flag:
        print(result)
        break
    result += 1
