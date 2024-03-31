import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    l, r = 0, max(arr) * m
    result = max(arr) * m
    while l <= r:
        mid = (l + r) // 2
        cnt = 0
        for i in range(n):
            cnt += mid // arr[i]

        if cnt >= m:
            r = mid - 1
        else:
            l = mid + 1

    print(r + 1)