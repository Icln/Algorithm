import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n, m = int(n), int(m * 100 + 0.5)
    if not n and not m:
        break

    arr = []
    for _ in range(n):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
        arr.append([c, p])

    arr.sort(key=lambda x:x[1])
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        for j in range(n):
            if i < arr[j][1]:
                break
            dp[i] = max(dp[i], dp[i - arr[j][1]] + arr[j][0])

    print(dp[m])