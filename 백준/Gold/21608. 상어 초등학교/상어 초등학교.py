from collections import defaultdict
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def seat(me, friend):
    tmp = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 0:
                cnt = 0
                space = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if arr[nx][ny] in friend:
                            cnt += 1
                        if arr[nx][ny] == 0:
                            space += 1
                tmp.append([i, j, cnt, space])

    tmp.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    arr[tmp[0][0]][tmp[0][1]] = me
    return


n = int(input())
friends = []
arr = [[0] * (n + 1) for _ in range(n + 1)]
idx = defaultdict(int)

for i in range(n ** 2):
    friends.append(list(map(int, input().split())))
    idx[friends[i][0]] = i
    seat(friends[i][0], friends[i][1:])


result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        around = friends[idx[arr[i][j]]][1:]
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 1 <= nx <= n and 1 <= ny <= n:
                if arr[nx][ny] in around:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)
