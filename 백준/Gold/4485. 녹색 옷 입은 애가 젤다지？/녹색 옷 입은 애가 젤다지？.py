import sys
import heapq
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 1

while True:
    n = int(input())
    if not n:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[1e9] * n for _ in range(n)]
    q, dist[0][0] = [], arr[0][0]
    heapq.heappush(q, (0, 0, arr[0][0]))

    while q:
        x, y, w = heapq.heappop(q)
        if dist[x][y] < w:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] + w < dist[nx][ny]:
                    dist[nx][ny] = arr[nx][ny] + w
                    heapq.heappush(q, (nx, ny, dist[nx][ny]))

    print(f'Problem {cnt}: {dist[-1][-1]}')
    cnt += 1