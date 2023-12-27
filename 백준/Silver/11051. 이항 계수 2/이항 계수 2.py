import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[1] * n for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n - 1][k - 1] % 10007)