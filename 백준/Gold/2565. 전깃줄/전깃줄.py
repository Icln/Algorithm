import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
numbers.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if numbers[j][1] < numbers[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))