def solution(n):
    answer = 0
    for i in range(1, (n // 2) + 1):
        plus = 1
        tmp = i
        while tmp <= n:
            if tmp == n:
                answer += 1
                break
            tmp += (i + plus) 
            plus += 1
    return answer + 1