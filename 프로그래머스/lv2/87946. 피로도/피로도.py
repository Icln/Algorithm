from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons, len(dungeons)):
        sum = k
        tmp = 0
        for j in i:
            if sum >= j[0]:
                sum -= j[1]
                tmp += 1
        answer = max(answer, tmp)
    
    return answer