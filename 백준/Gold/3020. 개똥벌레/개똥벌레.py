import sys
input = sys.stdin.readline


def check(tmp, cur):
    s, e = 0, len(tmp) - 1
    while s <= e:
        mid = (s + e) // 2
        if tmp[mid] <= cur:
            s = mid + 1
        else:
            e = mid - 1

    return s


if __name__ == "__main__":
    n, h = map(int, input().split())
    up = []
    down = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            up.append(int(input()))
        else:
            down.append(int(input()))

    up.sort()
    down.sort()

    m, r = 1e9, 0
    for i in range(1, h + 1):
        u = len(up) - check(up, h - i)
        d = len(down) - check(down, i - 1)

        if m == u + d:
            r += 1
        elif u + d < m:
            r = 1
            m = u + d

    print(m, r)