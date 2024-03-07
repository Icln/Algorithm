import sys
input = sys.stdin.readline

def solve(x, a, b):
    if x == cnt:
        return 0
    cur = order[x]
    dp[x][a][b] = min(abs(cur - a) + solve(x + 1, cur, b), abs(cur - b) + solve(x + 1, a, cur))
    return dp[x][a][b]

n = int(input())
a, b = map(int, input().split())
cnt = int(input())
order = [int(input()) for _ in range(cnt)]
dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(cnt)]
print(solve(0, a, b))