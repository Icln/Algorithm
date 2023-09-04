def solution(topping):
    if len(topping) % 2 == 0:
        left, right = len(topping) // 2 - 1, len(topping) // 2 + 1     
    else: 
        left, right = len(topping) // 2, len(topping) // 2 + 2
    
    answer = 0
    
    while True:
        if len(set(topping[:left + 1])) == len(set(topping[left + 1:])):
            answer += 1
            left -= 1
        else:
            break
        
            
    while True:
        if len(set(topping[:right])) == len(set(topping[right:])):       
            answer += 1
            right += 1
        else:
            break
        
    
    return  answer
