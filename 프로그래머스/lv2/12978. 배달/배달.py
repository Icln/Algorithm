import sys
from collections import deque

def bfs(g, graph, K, N):
    queue = deque([g])
    arr = [sys.maxsize] * (N + 1)
    arr[1] = 0
    
    while queue:
        tmp = queue.popleft()
        start = tmp[0]
        cost = tmp[1]

        for i in graph[start]:
            end, new_cost = i[0], i[1]
            if cost + new_cost <= K and cost + new_cost < arr[end]:
                arr[end] = cost + new_cost
                queue.append([end, cost + new_cost])
    return arr

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for i, j, cost in road:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    lst = bfs([1, 0], graph, K, N)
    for i in lst:
        if i != sys.maxsize:
            answer += 1
            
    return answer