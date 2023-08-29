answer = 0
tmp = []
def dfs(depth, op, numbers, target):
    global answer
    
    if depth == len(numbers):
        if sum(tmp) == target:
            answer += 1
        return
    if op == '+':
        tmp.append(numbers[depth])
    else:
        tmp.append(-numbers[depth])  
    dfs(depth + 1, '+', numbers, target)
    dfs(depth + 1, '-', numbers, target)
    tmp.pop()
    return 
    
def solution(numbers, target):    
    dfs(0, '+', numbers, target)
    tmp = []
    dfs(0, '-', numbers, target)
    tmp = []
    return answer // 2