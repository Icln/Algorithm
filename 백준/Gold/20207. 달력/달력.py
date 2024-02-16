import sys
input = sys.stdin.readline

n = int(input())
days = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        days[i] += 1

result, row, col = 0, 0, 0 
for day in days:
    if day: 
        col = max(col, day)
        row += 1
    else:
        result += row * col
        row, col = 0, 0

result += row * col 
print(result)