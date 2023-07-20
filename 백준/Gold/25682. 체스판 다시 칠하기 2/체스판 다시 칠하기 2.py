import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[0] * (m + 1)] + [[0] + list(input().rstrip()) for _ in range(n)]

prefixSumB = [[0] * (m + 1) for _ in range(n + 1)]
prefixSumW = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i + j) % 2 == 0:
            prefixSumB[i][j] = int(board[i][j] != 'B') + prefixSumB[i-1][j] + prefixSumB[i][j-1] - prefixSumB[i-1][j-1]
            prefixSumW[i][j] = int(board[i][j] != 'W') + prefixSumW[i-1][j] + prefixSumW[i][j-1] - prefixSumW[i-1][j-1]
        else:
            prefixSumB[i][j] = int(board[i][j] != 'W') + prefixSumB[i-1][j] + prefixSumB[i][j-1] - prefixSumB[i-1][j-1]
            prefixSumW[i][j] = int(board[i][j] != 'B') + prefixSumW[i-1][j] + prefixSumW[i][j-1] - prefixSumW[i-1][j-1]
        
result = sys.maxsize
for i in range(1, n - k + 2):
    for j in range(1, m - k + 2):
        cntB = prefixSumB[i + k - 1][j + k - 1] - prefixSumB[i - 1][j + k - 1] - prefixSumB[i + k - 1][j - 1] + prefixSumB[i - 1][j - 1]
        cntW = prefixSumW[i + k - 1][j + k - 1] - prefixSumW[i - 1][j + k - 1] - prefixSumW[i + k - 1][j - 1] + prefixSumW[i - 1][j - 1]
        result = min(result, cntB, cntW)

print(result)