from collections import deque
def solution(maps): 
    return bfs(maps)

def bfs(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    row = len(maps) - 1
    col = len(maps[0]) - 1
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        if x == row and y == col:
            return maps[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > row or ny < 0 or ny > col:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1 
                queue.append([nx, ny])
    return -1