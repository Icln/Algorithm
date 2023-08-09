import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(u):
    global cnt
    visited[u] = cnt
    for i in graph[u]:
        if visited[i] == 0:
            cnt +=1 
            dfs(i) 

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

dfs(r)
for i in range(1, n + 1):
    print(visited[i])