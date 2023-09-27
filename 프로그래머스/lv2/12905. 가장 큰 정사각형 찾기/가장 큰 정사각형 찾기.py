def solution(board):
    size = 0
    row, col = len(board), len(board[0])
    
    dp = [[0] * (col + 1) for _ in range(row + 1)]

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if board[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                size = max(size, dp[i][j])

    return size ** 2
