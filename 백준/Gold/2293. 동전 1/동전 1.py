import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1] + [0 for _ in range(k)]

for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j- i]
print(dp[k])