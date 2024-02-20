import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split()) 

graph = [[INF] * (v + 1) for _ in range(v + 1)]   
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):   
        for j in range(1, v + 1):   
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = INF
for i in range(1, v + 1):
    result = min(result, graph[i][i])

if result == INF:
    print(-1)
else:
    print(result)