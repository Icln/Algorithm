from collections import deque
def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        answer += check(s)
        
        s.rotate(-1) 
    return answer

def check(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
        if stack[-1] == '[' and s[i] == ']':
            stack.pop()
        elif stack[-1] == '{' and s[i] == '}':
            stack.pop()
        elif stack[-1] == '(' and s[i] == ')':
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return 1
    else:
        return 0
    
        