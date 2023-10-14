import heapq
def solution(n, k, enemy):
    if len(enemy) < k:
        return len(enemy)
    
    q = []
    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            tmp = heapq.heappop(q)
            if tmp > n:
                return i
            n -= tmp
    
    return len(enemy)