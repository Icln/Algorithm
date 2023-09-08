from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        tmp = Counter()
        for j in orders:
            for k in combinations(j, i):
                tmp[''.join(sorted(k))] += 1
                
        cnt = tmp.most_common(1)
        if cnt and cnt[0][1] < 2:
            continue
        for key, val in tmp.items():
            if val == cnt[0][1]:
                answer.append(key)
    
    return sorted(answer)