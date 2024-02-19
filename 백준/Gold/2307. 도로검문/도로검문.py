import sys
import heapq
input = sys.stdin.readline

def dijkstra(s, e):
    time = [1e9] * (n + 1)
    time[1] = 0
    q = [(1, 0)]
    while q:
        cur, t = heapq.heappop(q)
        if time[cur] < t:
            continue
        for next in graph[cur]:
            if (s == cur and e == next[0]) or (s == next[0] and e == cur):
                continue
            if next[1] + t < time[next[0]]:
                time[next[0]] = next[1] + t
                path[next[0]] = cur
                heapq.heappush(q, (next[0], next[1] + t))
    return time[n]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
path = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

shortest = dijkstra(-1, -1)
result, end = 0, n
fast = path[::]

while end != 1:
    prev = fast[end]
    cost = dijkstra(prev, end)
    if cost == 1e9:
        print(-1)
        sys.exit()

    result = max(result, cost - shortest)
    end = prev
print(result)