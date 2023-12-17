import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1):
    for j in range(m):
        tmp = min(arr[i][:j] + arr[i][j + 1:])
        arr[i + 1][j] += tmp

print(min(arr[-1]))