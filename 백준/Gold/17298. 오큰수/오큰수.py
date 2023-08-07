import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
stack = []
result = [-1] * n

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
