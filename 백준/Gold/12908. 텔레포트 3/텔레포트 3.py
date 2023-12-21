import sys
input = sys.stdin.readline

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
pos = [(xs, ys), (xe, ye)]
time = [[sys.maxsize] * 8 for _ in range(8)]

for i in range(1, 4):
    x1, y1, x2, y2 = map(int, input().split())
    pos.append((x1, y1))
    pos.append((x2, y2))
    time[2 * i][2 * i + 1], time[2 * i + 1][2 * i] = 10, 10

for i in range(8):
    time[i][i] = 0

for i in range(8):
    for j in range(8):
        if i != j:
            time[i][j] = min(time[i][j], abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]))
            time[j][i] = min(time[j][i], abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]))

for k in range(8):
    for i in range(8):
        for j in range(8):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])

print(time[0][1])