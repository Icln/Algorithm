from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        tmp = dict()
        cnt = 0
        for j in orders:
            for k in combinations(j, i):
                k = list(map(str, k))
                k.sort()
                s = ''.join(k)
                
                if s not in tmp:
                    tmp[s] = 1
                else:
                    tmp[s] += 1
                cnt = max(cnt, tmp[s])
    
        for key, val in tmp.items():
            if val == cnt and cnt > 1:
                answer.append(key)
        answer.sort()
    return answer