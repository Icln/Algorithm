def solution(sequence, k):
    n = len(sequence)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + sequence[i]
    
    idx = {0: -1}
    answer = []
    
    for i in range(n):
        cur = prefix[i + 1]
        if cur - k in idx:
            start, end = idx[cur - k] + 1, i
            answer.append([start, end])
    
        if cur not in idx:
            idx[cur] = i
        
    answer.sort(key = lambda x: (x[1] - x[0], x[0]))
    return answer[0]
