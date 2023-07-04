import sys
input = sys.stdin.readline

for _ in range(int(input())):
    stack = []
    n = list(input().rstrip())
    for i in n:
        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(')')
        elif i == '(':
            stack.append(i)
    if len(stack) != 0:
        print('NO')
    else :
        print('YES')