from collections import deque
def solution(maps):
    def bfs(start, end):
        visit = [[10001] * len(maps[0]) for _ in range(len(maps))]
        visit[start[0]][start[1]] = 1
        queue = deque([start])        
        while queue:
            cur = queue.popleft()
            if cur == end:
                return visit[cur[0]][cur[1]] - 1
            for i in range(4):
                nx, ny = cur[0] + dx[i], cur[1] + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and visit[cur[0]][cur[1]] + 1 < visit[nx][ny]:  
                    visit[nx][ny] = visit[cur[0]][cur[1]] + 1
                    queue.append([nx, ny])
        return -1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S': s = [i, j]
            elif maps[i][j] == 'L': l = [i, j]
            elif maps[i][j] == 'E': e = [i, j]
    
    first = bfs(s, l)
    if first == -1: return -1
    second = bfs(l, e)
    if second == -1: return -1
    
    return first + second