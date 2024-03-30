import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    prefixSum = [0] * (n + 1)
    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + int(input())

    dp = [[0] + [-1e9] * m for _ in range(n + 1)]
    dp[1][1] = prefixSum[1]

    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if j == 1:
                dp[i][j] = max(dp[i][j], prefixSum[i])

            for k in range(i - 1):
                s = prefixSum[i] - prefixSum[k + 1]
                dp[i][j] = max(dp[i][j], dp[k][j - 1] + s)

    print(dp[n][m])