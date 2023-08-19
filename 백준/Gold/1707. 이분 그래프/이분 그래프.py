import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(start, group):
    global error 
    if error:
        return 
    
    visit[start] = group
    for i in graph[start]:
        if not visit[i]:
            dfs(i, -group)
        elif visit[start] == visit[i]:
            error = True
            return

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visit = [0] * (v + 1)
    error = False
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(1, v + 1):
        if not visit[i]:
            dfs(i, 1)
            if error:
                print('NO')
                break
    
    if not error:
        print('YES')
