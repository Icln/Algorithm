from collections import deque
import sys
input = sys.stdin.readline

def bfs(u):
    visited[u] = True
    queue = deque([u])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i) 
                visited[i]= True
             

n, pair = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(pair):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


bfs(1)
print(visited.count(True) - 1)
