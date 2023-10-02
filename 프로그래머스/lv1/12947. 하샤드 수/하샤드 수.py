def solution(x):
    arr = list(str(x))
    sum_ = 0
    
    for i in range(len(arr)):
        sum_ += int(arr[i])
        if x % sum_ == 0:
            answer = True
        else:
            answer = False    
    
    return answer