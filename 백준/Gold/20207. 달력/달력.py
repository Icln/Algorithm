from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
nums = []
tmp = defaultdict(int)
MAX, MIN = 0, 1e9

for i in range(n):
    a, b = map(int, input().split())
    MAX, MIN = max(MAX, a, b), min(MIN, a, b)
    for j in range(a, b + 1):
        tmp[j] += 1
    nums.append([a, b])

nums.sort(key=lambda x: (x[0], -x[1]))
cnt = max(tmp.values())
day = [[0] * (MAX + 1) for _ in range(cnt + 1)]

for num in nums:
    flag = False
    for i in range(1, cnt + 1):
        for j in range(num[0], num[1] + 1):
            if day[i][j] != 0:
                break
            if j == num[1]:
                flag = True
            day[i][j] = 1
        if flag:
            break

result, size, point = 0, 0, MIN - 1
for i in range(MIN, MAX + 1):
    size = max(size, tmp[i])
    for j in range(1, cnt + 1):
        if day[j][i] == 1 and i != MAX:
            break
        if j == cnt:
            if i != MAX:
                result += ((i - 1 - point) * size)
                point = i
                size = 0
            if i == MAX:
                result += ((i - point) * size)
print(result)