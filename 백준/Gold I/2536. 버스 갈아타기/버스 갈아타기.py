from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    visited = [0] * (k + 1)
    for i in start:
        q.append((i, 1))
        visited[i] = 1

    while q:
        cur, cnt = q.popleft()
        if cur in end:
            print(cnt)
            break
        for node in graph[cur]:
            if not visited[node]:
                q.append((node, cnt + 1))
                visited[node] = 1

m, n = map(int, input().split())
k = int(input())
bus = [[] for _ in range(k + 1)]
short = [0] * (k + 1)
graph = [[] for _ in range(k + 1)]
for i in range(k):
    a, b, c, d, e = map(int, input().split())
    bus[a] = (min(b, d), min(c, e), max(b, d), max(c, e))

sx, sy, ex, ey = map(int, input().split())
start = []
end = []

for i in range(1, k + 1):
    cur = bus[i]
    for j in range(1, k + 1):
        if i == j or short[j]:
            continue
        tmp = bus[j]
        if cur[0] == cur[2] == tmp[0] == tmp[2]:
            if cur[1] <= tmp[1] <= tmp[3] <= cur[3]:
                short[j] = 1
        elif cur[1] == cur[3] == tmp[1] == tmp[3]:
            if cur[0] <= tmp[0] <= tmp[2] <= cur[2]:
                short[j] = 1

for i in range(1, k + 1):
    if short[i]:
        continue
    cur = bus[i]
    for j in range(1, k + 1):
        if i == j or short[j]:
            continue
        tmp = bus[j]
        if cur[0] == cur[2]:
            if tmp[0] <= cur[0] <= tmp[2] and cur[1] <= tmp[1] <= cur[3]:
                graph[i].append(j)
                graph[j].append(i)

        elif cur[0] == cur[2] == tmp[0] == tmp[2]:
            if cur[1] <= tmp[1] <= cur[3]:
                graph[i].append(j)
                graph[j].append(i)

        elif cur[1] == cur[3] == tmp[1] == tmp[3]:
            if cur[0] <= tmp[0] <= cur[2]:
                graph[i].append(j)
                graph[j].append(i)

for i in range(1, k + 1):
    if short[i]:
        continue
    if bus[i][0] <= sx <= bus[i][2] and bus[i][1] <= sy <= bus[i][3]:
        start.append(i)
    if bus[i][0] <= ex <= bus[i][2] and bus[i][1] <= ey <= bus[i][3]:
        end.append(i)
        
bfs()