from collections import deque
import sys
input = sys.stdin.readline
def check(sx,sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        tmp = 0
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if not arr[nx][ny]:
                    tmp += 1
        cnt[x][y] = tmp
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    while True:
        visited = [[0] * m for _ in range(n)]
        cnt = [[0] * m for _ in range(n)]
        num = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if arr[i][j] and not visited[i][j]:
                    check(i, j)
                    num += 1

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                tmp = arr[i][j] - cnt[i][j]
                if tmp <= 0:
                    arr[i][j] = 0
                else:
                    arr[i][j] = tmp
        
        if num >= 2:
            print(result)
            break
        result += 1
        
        flag = True
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if arr[i][j]:
                    flag = False
                    break
        
        if flag:
            print(0)
            break
                   