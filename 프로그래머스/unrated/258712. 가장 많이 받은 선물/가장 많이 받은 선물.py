from collections import defaultdict
from itertools import combinations
def solution(friends, gifts):
    arr = defaultdict(int)
    idx = defaultdict(int)
    result = defaultdict(int)
    
    for gift in gifts:    
        a, b = gift.split()
        arr[(a, b)] += 1
        idx[a] += 1
        idx[b] -= 1
    
    for f in combinations(friends, 2):
        if arr[(f[0], f[1])] != arr[(f[1], f[0])]: 
            if arr[(f[0], f[1])] > arr[(f[1], f[0])]:
                result[f[0]] += 1 
            else:
                result[f[1]] += 1
        else:
            if idx[f[0]] != idx[f[1]]:
                if idx[f[0]] > idx[f[1]]:
                    result[f[0]] += 1
                else:
                    result[f[1]] += 1
    
    return max(result.values()) if result else 0