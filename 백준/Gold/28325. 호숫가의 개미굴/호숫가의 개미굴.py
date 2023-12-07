import sys
input = sys.stdin.readline

def solve():
    tmp, cnt = 0, 0
    while cnt < n:
        if room[cnt] == 1:
            if cnt == n - 1 and room[0] == 1:
                break
            tmp += 1
            cnt += 2
            continue
        cnt += 1
    return tmp


n = int(input())
add = list(map(int, input().split()))
room = [1 for i in range(n)]

for i, j in enumerate(add):
    if j >= 1:
        room[i] = 0

result = 0
if room[0] == 0:
    result = max(result, solve())
else:
    result = max(result, solve())
    room[0] = 0
    result = max(result, solve())

print(result + sum(add))
