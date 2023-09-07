def solution(n):
    answer = ""
    
    while n > 0:
        remainder = n % 3
        n = n // 3
        
        if remainder == 0:
            remainder = 4
            n -= 1  
        
        answer = str(remainder) + answer
    return answer