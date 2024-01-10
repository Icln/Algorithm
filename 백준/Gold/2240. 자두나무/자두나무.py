import sys
input = sys.stdin.readline

t, w = map(int, input().split())
dp = [[[0 for _ in range(3)] for _ in range(w + 2)] for _ in range(t + 1)]
nums = [int(input()) for _ in range(t)]

if nums[0] == 1: dp[1][0][1] = 1
else: dp[1][1][2] = 1

for i in range(2, t + 1):    
    for j in range(w + 1):
        if nums[i - 1] == 1:  
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][2]) + 1
            dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][1])
        else:  
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][2])
            dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][1]) + 1

result = 0
for i in range(w + 1):
    result = max(result, max(dp[t][i][1], dp[t][i][2]))
print(result) 