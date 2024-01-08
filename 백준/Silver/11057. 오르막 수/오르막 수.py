import sys
input = sys.stdin.readline

n = int(input())
arr = [[], [1 for _ in range(10)]] + [[0] * 10 for _ in range(n - 1)]
dp = [[], 10] + [0] * (n - 1)

for i in range(2, n + 1):    
    arr[i][0] = dp[i - 1]
    for j in range(1, 10):
        arr[i][j] = arr[i][j - 1] - arr[i - 1][j - 1] 
    dp[i] = sum(arr[i])

print(dp[n] % 10007)