import sys;
input = sys.stdin.readline

N , M = map(int , input().split())
num = [[0] * (N + 1)]
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    num.append([0] + list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1] + num[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1]+ arr[x1 - 1][y1 - 1])