import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start, end = 0, 0
    cur = 2000000001
    while end < n:
        tmp = arr[end] - arr[start]
        if tmp < m:
            end += 1
        elif tmp > m:
            cur = min(cur, tmp)
            start += 1
        else:
            cur = m
            break
    print(cur)