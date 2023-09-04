def solution(topping):
    kind = set(topping)
    Front = [1] * len(topping)
    Back = [0] * len(topping)
    answer = 0
    cnt = 0
    
    for i in range(len(topping)):
        if topping[i] in kind:
            cnt += 1
            kind.remove(topping[i])
        Front[i] = cnt

    for i in range(len(topping) - 1, -1, -1):
        Back[i] = len(kind)
        kind.add(topping.pop())
        
    for i in range(len(Front)):
        if Front[i] == Back[i]:
            answer += 1
            
    return answer
