import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    x = input().split()
    if x[0] == 'push':
        stack.append(int(x[1]))
    elif x[0] == 'top':
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'pop':
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif x[0] == 'empty':
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    
    