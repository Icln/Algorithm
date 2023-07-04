import sys
input = sys.stdin.readline

while True:
    stack = []
    n = list(input().rstrip())
    if n[0] == '.':
        break
    for i in n:
        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(')')
        elif i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else :
                stack.append(']')    
    if len(stack) != 0:
        print('no')
    else :
        print('yes')