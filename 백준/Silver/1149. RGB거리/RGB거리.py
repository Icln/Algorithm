import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split()))for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i][j] + dp[i - 1][j + 1], dp[i][j] +  dp[i - 1][j + 2])
        elif j == 1:
            dp[i][j] = min(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j + 1])
        elif j == 2:
            dp[i][j] = min(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j - 2])
            
print(min(dp[n-1]))