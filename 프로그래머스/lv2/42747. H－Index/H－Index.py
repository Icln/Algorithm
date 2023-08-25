def solution(citations):
    citations.sort()
    cnt = len(citations)
    
    for i in range(cnt):
        if cnt - i <= citations[i]:
            return cnt - i
    return 0