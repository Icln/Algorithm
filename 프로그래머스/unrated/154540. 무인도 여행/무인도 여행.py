import sys
sys.setrecursionlimit(10 ** 9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(x, y, maps):
    global cnt
    if x < 0 or y < 0 or x > len(maps) - 1 or y > len(maps[0]) - 1:
        return False 
    if maps[x][y] == 'X':
        return False
    
    cnt += int(maps[x][y])
    maps[x][y] = 'X'
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, maps)        
    return True

def solution(maps):
    global cnt
    answer = []
    maps = list(map(list, maps))
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):  
            cnt = 0 
            if dfs(i, j, maps):
                answer.append(cnt)
        
    return sorted(answer) if answer else [-1]