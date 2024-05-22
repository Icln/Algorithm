from collections import deque
import sys
input = sys.stdin.readline

def move():
    q = deque([(7, 0)])
    visited = [[0] * 8 for _ in range(8)]
    visited[7][0] = 1
    while q:
        x, y = q.popleft()
        if arr[x][y] == '#':
            continue
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and arr[nx][ny] != '#':
                if nx == 0:
                    return 1
                if not visited[nx - 1][ny]:
                    visited[nx - 1][ny] = 1
                    q.append((nx - 1, ny))

    return 0

if __name__ == "__main__":
    arr = [list(map(str, input().rstrip())) for _ in range(8)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, 0)]
    print(move())