import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp, coins = [1e9] * (k + 1), []
for i in range(n):
    coin = int(input())
    coins.append(coin)
    if coin <= k:
        dp[coins[-1]] = 1
coins.sort()

for i in range(1, k + 1):
    for j in coins:
        if j >= i:
            break
        if i % j == 0:
            dp[i] = min(dp[i], dp[j] * (i // j)) 
        if dp[i - j] != 1e9:
            dp[i] = min(dp[i], dp[j] + dp[i - j])

if dp[k] == 1e9: print(-1)
else: print(dp[k])