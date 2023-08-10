import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
    visitedD[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if not visitedD[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visitedB[start] = True
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for i in graph[node]:
            if not visitedB[i]:
                queue.append(i)
                visitedB[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitedB = [False] * (n + 1)
visitedD = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v)
print()
bfs(v)