from collections import Counter
def solution(weights):
    cnt, answer = Counter(weights), 0
    
    for i in cnt:
        if cnt[i] > 1:
            answer += (cnt[i] * (cnt[i] - 1)) / 2
        if i * 2 in cnt:
            answer += cnt[i] * cnt[i * 2]
        if i * 2 / 3 in cnt:
            answer += cnt[i] * cnt[i * 2 / 3]
        if i * 3 / 4 in cnt:
            answer += cnt[i] * cnt[i * 3 / 4]

    return answer