import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(C) + 1)] for _ in range(n + 1)]
result = sum(C)

for i in range(1, n + 1):
    for j in range(1, sum(C) + 1):
        if j >= C[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - C[i]] + A[i])
            if dp[i][j] >= m:
                result = min(result, j)
        else:
            dp[i][j] = dp[i - 1][j] 
print(result)