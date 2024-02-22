import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
s = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

q = [(0, 0)]
dist = [INF] * n
dist[0] = 0

while q:
    cost, cur = heapq.heappop(q)
    if dist[cur] < cost:
        continue
    for next in graph[cur]:
        if not s[next[0]] or next[0] == (n - 1):
            if next[1] + cost < dist[next[0]]:
                dist[next[0]] = next[1] + cost
                heapq.heappush(q, (next[1] + cost, next[0]))

print(dist[n - 1]) if dist[n - 1] != INF else print(-1)