import heapq
def solution(scoville, K):
    if K == 0:
        return 0
    
    scoville.sort()
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)    
        if second == 0 and K != 0:
            return -1
        
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    
    return answer

    