from collections import deque
import sys
input = sys.stdin.readline

def bfs(u):
    global cnt
    visited[u] = cnt
    queue = deque([u])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                cnt +=1 
                visited[i]= cnt
             

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse = True)

bfs(r)
for i in range(1, n + 1):
    print(visited[i])