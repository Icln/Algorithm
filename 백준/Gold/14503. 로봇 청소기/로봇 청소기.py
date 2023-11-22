n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
while True:
    if arr[x][y] == 0:
        result += 1
        arr[x][y] = 2
    flag = False

    for i in range(4):
        if 0 <= x + dir[i][0] <= n - 1 and 0 <= y + dir[i][1] <= m - 1:
            if arr[x + dir[i][0]][y + dir[i][1]] == 0:
                flag = True
                break

    if flag:
        d -= 1
        if d == -5:
            d = 3
        if arr[x + dir[d][0]][y + dir[d][1]] == 0:
           x += dir[d][0]
           y += dir[d][1]
    else:
        if arr[x - dir[d][0]][y - dir[d][1]] == 1:
            break
        else:
            x -= dir[d][0]
            y -= dir[d][1]

print(result)