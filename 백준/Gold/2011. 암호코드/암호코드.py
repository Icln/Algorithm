import sys
input = sys.stdin.readline

if __name__ == "__main__":
    pwd = list(map(int, input().rstrip()))
    l = len(pwd)
    if pwd[0] == 0:
        print(0)
        sys.exit(0)

    pwd = [0] + pwd
    dp = [0] * (l + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, l + 1):
        if pwd[i] > 0:
            dp[i] += dp[i - 1]
        tmp = pwd[i - 1] * 10 + pwd[i]
        if 10 <= tmp <= 26:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)
