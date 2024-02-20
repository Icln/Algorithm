import sys
input = sys.stdin.readline

def bfs():
    q = set([(0, 0, arr[0][0])])
    cnt = 1
    while q:
        x, y, s = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in s:
                q.add((nx, ny, s + arr[nx][ny]))
                cnt = max(cnt, len(s) + 1)
    return cnt

r, c = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
print(bfs())

