import sys
input = sys.stdin.readline

n = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(100)]
MOD = 1000000000

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j + 1][k]) % MOD
            elif j == 9:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k]) % MOD
            else:
                dp[i][j][k | (1 << j)] = (dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]) % MOD

result = 0
for i in range(10):
    result = (result + dp[n - 1][i][1023]) % MOD
print(result)