def solution(number, k):
    answer = ''
    A = len(number) - k 
    
    start = 0
    end = k + 1

    while len(answer) != A:
        if end - start == 1:
            answer += number[start: ]
            break
        
        tmp = -1
        for i in range(start, end):
            if int(number[i]) == 9:
                idx = i
                break
            
            if int(number[i]) > tmp:
                tmp = int(number[i])
                idx = i
        
        answer += number[idx]
        start = idx + 1
        end += 1  
        
    return answer