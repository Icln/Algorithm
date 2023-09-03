def solution(m, n, board):
    board = list(map(list, board))   
    cnt = 0
    
    while True:
        hit_box = set()
        for i in range(m - 1):
            for j in range(n - 1):
                lt, ld, rt, rd = board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]
                if lt == ld == rt == rd and lt != 0:
                    hit_box.add((i, j))
                    hit_box.add((i + 1, j))
                    hit_box.add((i, j + 1))
                    hit_box.add((i + 1, j + 1))
        if not hit_box: break
        cnt += len(hit_box)
        
        for hit in hit_box:
            hit_i, hit_j = hit
            board[hit_i][hit_j] = 0
        
        for j in range(n):
            for i in range(m):
                for ii in range(1, m - i):
                    if board[ii][j] == 0:
                        board[ii - 1][j], board[ii][j] = board[ii][j], board[ii - 1][j]
    return cnt
