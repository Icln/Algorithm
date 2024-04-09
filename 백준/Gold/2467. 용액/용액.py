import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    s, e = 0, n - 1
    m = 1e10
    x, y = 0, 0
    while s < e:
        cur = arr[s] + arr[e]
        if cur == 0:
            print(arr[s], arr[e])
            break
        elif cur > 0:
            if m > abs(cur):
                m = abs(cur)
                x, y = arr[s], arr[e]
            e -= 1
        else:
            if m > abs(cur):
                m = abs(cur)
                x, y = arr[s], arr[e]
            s += 1
    else:
        print(x, y)