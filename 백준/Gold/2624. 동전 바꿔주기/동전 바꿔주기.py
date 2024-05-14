import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    k = int(input())
    dp = [[0] * (t + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    
    for i in range(1, k + 1):
        a, b = map(int, input().split())
        for j in range(t + 1):
            dp[i][j] = dp[i - 1][j]
            for z in range(1, b + 1):
                if j - a * z >= 0:
                    dp[i][j] += dp[i - 1][j - a * z]
                else:
                    break

    print(dp[k][t])