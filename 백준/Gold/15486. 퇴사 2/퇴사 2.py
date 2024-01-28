import sys
input = sys.stdin.readline
n = int(input())
T, P = [0], [0]
dp = [0] * (n + 1)

for _ in range(n):
    i, j = map(int, input().split())
    T.append(i)
    P.append(j)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    cur = i + T[i] - 1
    if cur <= n:
        dp[cur] = max(dp[cur], dp[i - 1] + P[i])
print(max(dp))