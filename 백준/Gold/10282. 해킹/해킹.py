import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    q = []
    distance[c] = 0
    heapq.heappush(q, (c, 0))
    while q:
        cur, time = heapq.heappop(q)
        if distance[cur] < time:
            continue
        for next in graph[cur]:
            if time + next[1] < distance[next[0]]:
                distance[next[0]] = time + next[1]
                heapq.heappush(q, (next[0], time + next[1]))

    result = 0
    for i in range(1, n + 1):
        if distance[i] != 1e9:
            result = max(result, distance[i])
    print((n + 1) - distance.count(1e9), result)