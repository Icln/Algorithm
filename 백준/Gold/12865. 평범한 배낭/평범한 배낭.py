import sys
input = sys.stdin.readline

n, k = map(int, input().split())
value = [0] * (n + 1)
weight  = [0] * (n + 1) 
for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])