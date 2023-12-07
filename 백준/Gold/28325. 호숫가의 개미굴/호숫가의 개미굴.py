from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
add = list(map(int, input().split()))
room = deque([1 for i in range(n)])

for i, j in enumerate(add):
    if j >= 1:
        room[i] = 0

result = 0
for i in range(n):
    tmp, cnt = 0, 0
    if 1 not in room:
        break
    while cnt < n:
        if room[cnt] == 1:
            if cnt == n - 1 and room[0] == 1:
                break
            tmp += 1
            cnt += 2
            continue
        cnt += 1
    result = max(result, tmp)
    room.rotate(1)

print(result + sum(add))