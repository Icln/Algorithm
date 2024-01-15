import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
lis = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            lis[i] = max(lis[i], lis[j] + 1)

print(n - (max(lis) + 1))