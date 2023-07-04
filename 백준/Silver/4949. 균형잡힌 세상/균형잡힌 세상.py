import sys
input = sys.stdin.readline

while True:
    stack = []
    n = input()
    if n[0] == '.':
        break
    for i in n:
        if i == '(' or i =='[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(')')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else :
                stack.append(']')
                break    
    if len(stack) != 0:
        print('no')
    else :
        print('yes')