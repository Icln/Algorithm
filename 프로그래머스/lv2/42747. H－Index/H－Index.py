def solution(citations):
    citations.sort()
    cnt = len(citations)
    h = max(citations)
    answer = 0
    for i in range(h):
        tmp = 0
        for j in range(cnt):
            if i <= citations[j]:
                tmp += 1
        if tmp >= i:
            answer = i
    return answer