import sys
input = sys.stdin.readline
n = int(input())
dp = [1, 2, 3] + [0] * n

for i in range(3, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1] % 10007)