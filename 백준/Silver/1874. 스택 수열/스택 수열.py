import sys
input = sys.stdin.readline

result = []
stack = []
num = 1
for i in range(int(input())):
    target = int(input())
    while num <= target:
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == target:
        stack.pop()
        result.append('-')    
    else :
        print('NO')
        break

if len(stack) == 0:
    for i in result:
        print(i)