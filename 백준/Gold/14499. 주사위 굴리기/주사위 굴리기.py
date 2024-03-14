import sys
input = sys.stdin.readline
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0] * 6

for i in command:
    nx, ny = x + dr[i], y + dc[i]
    if not 0 <= nx < n or not 0 <= ny < m:      
        continue

    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if i == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif i == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif i == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif i == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    if not arr[nx][ny]:
        arr[nx][ny] = dice[5]
    else:
        dice[5] = arr[nx][ny]
        arr[nx][ny] = 0
    x, y = nx, ny
    print(dice[4])