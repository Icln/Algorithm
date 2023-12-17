import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[i for i in arr[0]]] + [[1e9] * m for _ in range(n - 1)]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + arr[i][j])

print(min(dp[-1]))