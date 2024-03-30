import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(k):
        a, b, c = map(int, input().split())
        if a < b:
            arr[a][b] = max(arr[a][b], c)

    for i in range(2, n + 1):
        dp[i][2] = arr[1][i]
    
    for i in range(2, n + 1):
        for j in range(3, m + 1):
            for z in range(1, i):
                if arr[z][i] and dp[z][j - 1]:
                    dp[i][j] = max(dp[i][j], dp[z][j - 1] + arr[z][i])
    
    print(max(dp[n]))