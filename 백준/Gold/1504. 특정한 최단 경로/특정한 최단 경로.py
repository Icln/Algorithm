import sys
import heapq
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])
    graph[y].append([x, z])

def dijkstra(start):
    dis = [sys.maxsize] * (n + 1)
    dis[start] = 0
    queue = []
    heapq.heappush(queue, [start, 0])
    
    while queue:
        pos, cur = heapq.heappop(queue)
        if dis[pos] < cur:
            continue
        for i in graph[pos]:
            if dis[i[0]] > cur + i[1]:
                dis[i[0]] = cur + i[1]
                heapq.heappush(queue, [i[0], cur + i[1]])

    return dis
v1, v2 = map(int, input().split())

dis0 = dijkstra(1)
dis1 = dijkstra(v1)
dis2 = dijkstra(v2)

p1 = dis0[v1] + dis1[v2] + dis2[n]
p2 = dis0[v2] + dis2[v1] + dis1[n]

result = min(p1, p2)
print(result if result < sys.maxsize else -1)