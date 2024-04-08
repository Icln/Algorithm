import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    t = input().rstrip()

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    result = 0
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])

    print(result)