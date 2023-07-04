import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        stack.pop()
    else :
        stack.append(n)
print(sum(stack))