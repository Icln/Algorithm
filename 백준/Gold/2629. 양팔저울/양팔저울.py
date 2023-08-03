import sys
input = sys.stdin.readline

w = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
dp = [False for i in range(40001)]
dp[0] = True

for weight in weights:
    tmp = set()
    for i in range(40001):
        if dp[i]:
            tmp.add(i + weight)
            tmp.add(abs(i - weight))
    for j in tmp:
        dp[j] = True
    
for i in marbles:
    if dp[i]:
        print('Y', end=' ')
    else:
        print('N', end=' ')