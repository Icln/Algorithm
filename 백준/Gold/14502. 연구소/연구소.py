from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline
def bfs():
    result = 0
    for c in combinations(empty, 3):
        tmp = copy.deepcopy(arr)
        for x, y in c:
            tmp[x][y] = 1

        virus = deque()
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    virus.append((i, j))
        while virus:
            x, y = virus.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not tmp[nx][ny]:
                    tmp[nx][ny] = 2
                    virus.append((nx, ny))

        cnt = 0
        for i in range(n):
            for j in range(m):
                if not tmp[i][j]:
                    cnt += 1
        result = max(result, cnt)
    return result


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
empty = []
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            empty.append((i, j))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(bfs())