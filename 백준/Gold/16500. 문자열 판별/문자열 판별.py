import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
a = [input().rstrip() for _ in range(n)]
dp = [1] + [0] * (len(s))

for i in range(len(s) + 1):
    for w in a:
        if i >= len(w) and dp[i - len(w)] == 1 and s[i - len(w) : i] == w:
            dp[i] = 1
            
print(1) if dp[-1] else print(0)