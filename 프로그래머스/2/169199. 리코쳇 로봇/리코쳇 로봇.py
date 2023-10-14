from collections import deque
def solution(board):
    def move(d, x, y):
        while True:
            x += d[0]
            y += d[1]
            if x < 0 or y < 0 or x >= hei or y >= wid: break
            if board[x][y] == 'D': break
        return x - d[0], y - d[1]

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque()
    hei = len(board)
    wid = len(board[0])
    end = []
    visit = [[-1 for _ in range(wid)] for _ in range(hei)]
    
    for i in range(hei):
        for j in range(wid):
            if board[i][j] == 'R':
                q.append([i, j])
                visit[i][j] = 0
            if board[i][j] == 'G':
                end= [i, j] 

    while q:
        x, y = q.popleft()
        for d in dir:
            nx, ny = move(d, x, y)
            if visit[nx][ny] == -1:
                q.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1

    return visit[end[0]][end[1]]