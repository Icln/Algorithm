from collections import defaultdict        
def solution(edges):
    start, end = defaultdict(int), defaultdict(int)
    for edge in edges:
        start[edge[0]] += 1
        end[edge[1]] += 1
    
    v, d, s, e = 0, 0, 0, 0
    last = max(max(start), max(end)) + 1
    for i in range(1, last):
        if start[i] == 0:
            s += 1
            continue
        if start[i] >= 2 and end[i] >= 2:
            e += 1
            continue
        if start[i] >= 2 and end[i] == 0:
            v = i
            continue
    
    d = start[v] - (s + e)
    return [v, d, s, e]