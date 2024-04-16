import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        time, cnt, *arr = map(int, input().split())
        dp[i] = time
        for j in arr:
            dp[i] = max(dp[i], dp[j] + time)

    print(max(dp))