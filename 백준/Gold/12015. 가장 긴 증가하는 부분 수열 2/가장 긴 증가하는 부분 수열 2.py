import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = [0]

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        start = 0
        end = len(stack)
        while(start < end):
            mid = (start + end) // 2

            if stack[mid] < a:
                start = mid + 1
            else:
                end = mid
        stack[end] = a
print(len(stack) - 1)