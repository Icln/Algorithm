import sys
input = sys.stdin.readline

w = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
dp = [False for i in range(15001)]
dp[0] = True

for weight in weights:
    tmp = set()
    for i in range(15001 - weight):
        if dp[i]:
            tmp.add(i + weight)
            tmp.add(abs(i - weight))
    for j in tmp:
        dp[j] = True
    
for i in marbles:
    if i > 15000:
        print('N', end=' ')
    elif dp[i]:
        print('Y', end=' ')
    else:
        print('N', end=' ')