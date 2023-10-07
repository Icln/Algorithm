import heapq
import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, cur = heapq.heappop(queue)
        if distance[cur] < dist:
            continue
        for i in graph[cur]: 
            city, cost = i[0], i[1]
            cost  = dist + cost
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(queue, [cost, city])


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append([y, z])

start, end = map(int,input().split())

distance = [sys.maxsize] * (n + 1)
dijkstra(start)
print(distance[end])