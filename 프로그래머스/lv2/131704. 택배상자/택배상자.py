def solution(order):
    stack = []
    idx = 0
    
    for num in range(1, len(order) + 1):
        stack.append(num)
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
            
    return idx