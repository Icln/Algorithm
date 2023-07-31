import sys
input = sys.stdin.readline
def dp():
    n, file = int(input()), list(map(int, input().split()))
    arr = [[0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = sys.maxsize
            for k in range(j - i):
                small = min(small, arr[i][i + k] + arr[i + k + 1][j])
            arr[i][j] = small + sum(file[i : j + 1])

    print(arr[0][n - 1])

for _ in range(int(input())):
    dp()
    