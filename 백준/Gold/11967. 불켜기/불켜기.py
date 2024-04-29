from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(1, 1)])
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    visited[1][1] = 1
    room = [[0] * (n + 1) for _ in range(n + 1)]
    room[1][1] = 1
    cnt = 1
    while queue:
        tx, ty = queue.popleft()

        for ax, by in buttons[(tx, ty)]:
            if not room[ax][by]:
                room[ax][by] = 1
                cnt += 1
                for dx, dy in d:
                    nx, ny = ax + dx, by + dy
                    if 0 < nx <= n and 0 < ny <= n and visited[nx][ny]:
                        queue.append((nx, ny))

        for dx, dy in d:
            nx, ny = tx + dx, ty + dy
            if 0 < nx <= n and 0 < ny <= n and room[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    buttons = defaultdict(list)

    for _ in range(m):
        x, y, a, b = map(int, input().split())
        buttons[(x, y)].append((a, b))

    print(bfs())