def solution(clothes):
    kind = dict()
    for i in clothes:
        if kind.get(i[1]) == None:
            kind[i[1]] = 1
        else:
            kind[i[1]] += 1 
    
    answer = 1
    for i in kind.values():
        answer *= (i + 1)
    return answer - 1