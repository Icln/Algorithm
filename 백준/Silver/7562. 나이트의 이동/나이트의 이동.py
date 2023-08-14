import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([startX, startY])
    while queue:
        x, y = queue.popleft()
        if x == endX and y == endY:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < l and 0 <= ny < l and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])
    return arr[endX][endY]

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(int(input())):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    print(bfs())
