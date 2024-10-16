from collections import defaultdict
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    q = [(0, start)]
    dist = [INF] * (n + 1)
    path = [0] * (n + 1)
    path[start], dist[start] = start, 0

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for next in arr[cur]:
            if next[1] + cost < dist[next[0]]:
                dist[next[0]] = next[1] + cost
                heapq.heappush(q, (next[1] + cost, next[0]))
                path[next[0]] = cur

    return path, dist

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    arr = [[] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            c = c * 2 - 1
        else:
            c *= 2
        arr[a].append((b, c))
        arr[b].append((a, c))
    path, dist = dijkstra(s)

    result = []
    for _ in range(t):
        cand = int(input())
        tmp = cand
        cnt = defaultdict(int)
        cnt[g], cnt[h] = 1, 1
        while path[tmp] != tmp:
            cnt[tmp] -= 1
            tmp = path[tmp]
        if s == g:
            cnt[g] -= 1
        if s == h:
            cnt[h] -= 1
        if cnt[g] == 0 and cnt[h] == 0:
            result.append(cand)

    result.sort()
    print(*result)
