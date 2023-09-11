def setUV(p):  
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]  

def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False


def solution(p):
    if not p:  
        return p

    u, v = setUV(p)  

    if check(u):  
        return u + solution(v)  
    else:  
        answer = '('  
        answer += solution(v)  
        answer += ')' 

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer