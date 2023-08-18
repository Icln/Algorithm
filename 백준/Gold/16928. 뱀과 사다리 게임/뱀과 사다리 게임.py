import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        cur = queue.popleft()
        for i in range(1, 7):
            next = cur + i
            if next <= 100 and visit[next] == 0:
                if next in ladder.keys():
                    next = ladder[next]
                if next in snake.keys():
                    next = snake[next]
                if visit[next] == 0:
                    queue.append(next)
                    visit[next] = visit[cur] + 1
    
n, m = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y
visit = [0] * 101    
bfs()
print(visit[100])