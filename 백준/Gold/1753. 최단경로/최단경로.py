import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

graph = [[] for v in range(V + 1)]
m = sys.maxsize
d = [m] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra():
    heap = []
    d[k] = 0
    heapq.heappush(heap, (0, k))
    while heap:
        w, v = heapq.heappop(heap)
        for ew, ev in graph[v]:
            if  d[ev] > w + ew:
                d[ev] = w + ew
                heapq.heappush(heap, (d[ev], ev))

dijkstra()
for i in range(1, V+1):
    print('INF') if d[i] == m else print(d[i])