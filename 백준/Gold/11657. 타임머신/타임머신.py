import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
arr = []
for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

dist = [INF] * (n + 1)
dist[1], isTimeMachine = 0, False
for i in range(n):
    for start, end, cost in arr:
        if dist[start] != INF and dist[start] + cost < dist[end]:
            dist[end] = dist[start] + cost
            if i == n - 1:
                isTimeMachine = True

if isTimeMachine:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])