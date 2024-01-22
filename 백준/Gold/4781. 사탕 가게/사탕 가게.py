import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n, m = int(n), int(m * 100 + 0.5)
    if not n and not m:
        break

    dp = [0] * (m + 1)
    for i in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
        for j in range(p, m + 1):
            dp[j] = max(dp[j], dp[j - p] + c)

    print(dp[m])