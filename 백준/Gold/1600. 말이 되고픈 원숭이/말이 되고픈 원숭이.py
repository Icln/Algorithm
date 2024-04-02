from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    q = deque([(0, 0, k)])
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny]:
                if not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))

        if z:
            for dx, dy in horse:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny]:
                    if not visited[nx][ny][z - 1]:
                        visited[nx][ny][z - 1] = visited[x][y][z] + 1
                        q.append((nx, ny, z - 1))
    return -1


if __name__ == "__main__":
    k = int(input())
    w, h = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(h)]
    horse = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    print(bfs())