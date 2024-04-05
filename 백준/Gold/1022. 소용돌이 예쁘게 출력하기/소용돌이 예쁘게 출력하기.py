import sys
input = sys.stdin.readline

if __name__ == "__main__":
    r1, c1, r2, c2 = map(int, input().split())
    arr = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
    d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    cnt = (c2 - c1 + 1) * (r2 - r1 + 1)

    repeat = 1
    x, y = 0, 0
    cur = 1
    num = 0
    i = 0

    while cnt > 0:
        for _ in range(2):
            for _ in range(repeat):
                if r1 <= x <= r2 and c1 <= y <= c2:
                    arr[x - r1][y - c1] = cur
                    cnt -= 1
                    num = cur
                cur += 1
                x, y = x + d[i % 4][0], y + d[i % 4][1]
            i += 1
        repeat += 1

    length = len(str(num))
    for i in arr:
        for j in i:
            sub = length - len(str(j))
            if sub > 0:
                print(' ' * sub, end='')
            print(j, end=' ')
        print('')