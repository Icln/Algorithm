import sys
input = sys.stdin.readline

def bfs(x, y):
    cur = arr[x][y]
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        cnt = 1
        while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == cur:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and arr[x - dx[k]][y - dy[k]] == cur:
                    break
                if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and arr[nx + dx[k]][ny + dy[k]] == cur:
                    break

                print(cur)
                print(x + 1, y + 1)
                exit(0)

            nx += dx[k]
            ny += dy[k]

arr = [list(map(int, input().split())) for _ in range(19)]

dx, dy = [0, 1, 1, -1], [1, 0, 1, 1]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            bfs(i, j)

print(0)