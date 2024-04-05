import sys
input = sys.stdin.readline


def move(x, y, z, k):
    global cur, curX, curY, num
    for i in range(1, z + 1):
        cur += 1
        nx, ny = x + d[k][0] * i, y + d[k][1] * i
        if r1 <= nx - n <= r2 and c1 <= ny - n <= c2:
            num = str(cur)
            arr[nx - n - r1][ny - n - c1] = cur

    curX, curY = x + d[k][0] * z, y + d[k][1] * z

if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, input().split())
    n = max(abs(r1), abs(c1), abs(r2), abs(c2))
    d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    num = ''

    arr = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
    cnt, cur = 0, 1
    curX, curY = n, n
    if r1 <= curX - n <= r2 and c1 <= curY - n <= c2:
        arr[curX - n - r1][curY - n - c1] = cur

    for i in range((2 * n) * 2 + 1):
        if i % 2 == 0:
            cnt += 1
        move(curX, curY, cnt, i % 4)

    for i in arr:
        for j in i:
            sub = len(num) - len(str(j))
            if sub > 0:
                print(' ' * sub, end='')
            print(j, end=' ')
        print('')
