import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    q, dist = [], [1e9] * (n + 1)
    dist[s] = 0
    heapq.heappush(q, (s, 0))
    while q:
        cur, cost = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for next in graph[cur]:
            if next[1] + cost < dist[next[0]]:
                dist[next[0]] = next[1] + cost
                heapq.heappush(q, (next[0], dist[next[0]]))
    return dist

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

party = dijkstra(x)
party[0] = 0
for i in range(1, n + 1):
    if i != x:
        start = dijkstra(i)
        party[i] += start[x]

print(max(party))
