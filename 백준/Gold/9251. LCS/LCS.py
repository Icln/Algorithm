import sys
input = sys.stdin.readline

LCS = [list(map(str, input().rstrip())) for _ in range(2)]
dp = [[0 for _ in range(len(LCS[1]) + 1)] for _ in range(len(LCS[0]) + 1)]
result = []

for i in range(len(LCS[0])):
    for j in range(len(LCS[1])):
        if LCS[0][i] == LCS[1][j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) 

print(max(dp[len(LCS[0])]))