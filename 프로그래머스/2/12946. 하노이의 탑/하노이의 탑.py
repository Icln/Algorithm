def solution(n):
    def hanoi(n, start, end, mid):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n - 1, start, mid, end)
        answer.append([start, end])
        hanoi(n - 1, mid, end, start) 
        
    answer = []
    hanoi(n, 1, 3, 2)
    return answer
