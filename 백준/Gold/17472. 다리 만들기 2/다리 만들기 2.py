from collections import deque
import sys

input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    x, y = find(a), find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def check(x, y):
    #상
    if x - 1 >= 0 and arr[x - 1][y] == 0:
        isRoad, d = False, 0
        for i in range(x - 1, -1, -1):
            if arr[i][y] != 0:
                isRoad = True
                break
            d += 1
        if isRoad and d >= 2:
            if arr[x][y] < arr[x - d - 1][y]:
                paths.add((arr[x][y] - 1, arr[x - d - 1][y] - 1, d))
            else:
                paths.add((arr[x - d - 1][y] - 1, arr[x][y] - 1, d))
    # 하
    if x + 1 < n and arr[x + 1][y] == 0:
        isRoad, d = False, 0
        for i in range(x + 1, n):
            if arr[i][y] != 0:
                isRoad = True
                break
            d += 1
        if isRoad and d >= 2:
            if arr[x][y] < arr[x + d + 1][y]:
                paths.add((arr[x][y] - 1, arr[x + d + 1][y] - 1, d))
            else:
                paths.add((arr[x + d + 1][y] - 1, arr[x][y] - 1, d))

    # 좌
    if y - 1 >= 0 and arr[x][y - 1] == 0:
        isRoad, d = False, 0
        for i in range(y - 1, -1, -1):
            if arr[x][i] != 0:
                isRoad = True
                break
            d += 1
        if isRoad and d >= 2:
            if arr[x][y] < arr[x][y - d - 1]:
                paths.add((arr[x][y] - 1, arr[x][y - d - 1] - 1, d))
            else:
                paths.add((arr[x][y - d - 1] - 1, arr[x][y] - 1, d))

    # 우
    if y + 1 < m and arr[x][y + 1] == 0:
        isRoad, d = False, 0
        for i in range(y + 1, m):
            if arr[x][i] != 0:
                isRoad = True
                break
            d += 1
        if isRoad and d >= 2:
            if arr[x][y] < arr[x][y + d + 1]:
                paths.add((arr[x][y] - 1, arr[x][y + d + 1] - 1, d))
            else:
                paths.add((arr[x][y + d + 1] - 1, arr[x][y] - 1, d))

def bfs(a, b):
    q = deque([(a, b)])
    arr[a][b] = node
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = node
                q.append((nx, ny))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
node = 2
paths = set()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)
            node += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            check(i, j)

paths = sorted(paths, key=lambda x:(x[2]))


parent = [i for i in range(node - 1)]
result = 0
for a, b, cost in paths:
    if find(a) != find(b):
        union(a, b)
        result += cost

for i in range(1, node - 1):
    parent[i] = find(i)

if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(result)
