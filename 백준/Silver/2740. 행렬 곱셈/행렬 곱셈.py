import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

result = [[0 for _ in range(k)]for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            result[i][j] += a[i][x] * b[x][j]

for i in result:
    print(*i)