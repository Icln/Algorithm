from itertools import combinations
def solution(relation):
    idx = [i for i in range(len(relation[0]))]
    visit = [False] * len(relation[0])
    key = []
    for i in range(1, len(relation) + 1):
        for j in combinations(idx, i):
            tmp = [tuple(relation[i][k] for k in j) for i in range(len(relation))]
            if len(relation) == len(set(tmp)):
                flag = True
                for k in key:
                    if set(k).issubset(set(j)):
                        flag = False
                        break
                if flag:
                    key.append(j)   
    return len(key)

from itertools import combinations

