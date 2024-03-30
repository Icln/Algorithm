import sys, math
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    c = [[0] + [-1e9] * m for _ in range(n + 1)]
    nc = [[0] + [-1e9] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        num = int(input())
        for j in range(1, min(m, math.ceil(i / 2)) + 1):
            c[i][j] = max(c[i - 1][j], nc[i - 1][j - 1]) + num
            nc[i][j] = max(nc[i - 1][j], c[i - 1][j])

    print(max(c[n][m], nc[n][m]))